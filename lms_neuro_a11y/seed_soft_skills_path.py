"""Idempotent seeder for the LogiSentinel Executive Soft Skills Learning Path.

Run inside bench:
    bench --site <site> execute lms_neuro_a11y.seed_soft_skills_path.seed_learning_path
"""

import frappe

from lms_neuro_a11y.seed_data_c1_c2 import COURSES_1_AND_2
from lms_neuro_a11y.seed_data_c3_c4 import COURSES_3_AND_4

PROGRAM_TITLE = "Ruta Ejecutiva: Comunicación Estratégica, Ventas B2B y Oratoria para Líderes Técnicos"
DEFAULT_INSTRUCTOR = "Administrator"


def ensure_tldr_custom_field():
	"""Create Custom Field `tldr_summary` on `Course Lesson` if it does not exist."""
	if frappe.db.exists("Custom Field", {"dt": "Course Lesson", "fieldname": "tldr_summary"}):
		return

	cf = frappe.get_doc(
		{
			"doctype": "Custom Field",
			"dt": "Course Lesson",
			"fieldname": "tldr_summary",
			"fieldtype": "Small Text",
			"label": "Resumen Ejecutivo (TL;DR)",
			"description": "Resumen ejecutivo de 3 viñetas (Markdown) mostrado al inicio de la lección.",
			"insert_after": "title",
			"module": "LMS Neuro A11y",
		}
	)
	cf.insert(ignore_permissions=True)
	frappe.db.commit()


def _upsert_question(q_data: dict) -> str:
	"""Create or update an LMS Question by exact question text."""
	existing = frappe.db.get_value("LMS Question", {"question": q_data["question"]}, "name")
	doc = frappe.get_doc("LMS Question", existing) if existing else frappe.new_doc("LMS Question")

	doc.question = q_data["question"]
	doc.type = "Choices"
	doc.marks = 1

	for idx, (opt_text, is_correct, explanation) in enumerate(q_data["options"], start=1):
		setattr(doc, f"option_{idx}", opt_text)
		setattr(doc, f"is_correct_{idx}", is_correct)
		setattr(doc, f"explanation_{idx}", explanation)

	doc.save(ignore_permissions=True)
	return doc.name


def _upsert_quiz(quiz_data: dict, course_name: str) -> str:
	"""Create or update an LMS Quiz and its scenario-based LMS Questions."""
	existing = frappe.db.get_value("LMS Quiz", {"title": quiz_data["title"]}, "name")
	doc = frappe.get_doc("LMS Quiz", existing) if existing else frappe.new_doc("LMS Quiz")

	doc.title = quiz_data["title"]
	doc.passing_percentage = quiz_data.get("passing_percentage", 70)
	doc.show_answers = 1
	doc.show_submission_history = 1
	doc.course = course_name
	doc.set("questions", [])

	for q_data in quiz_data["questions"]:
		q_name = _upsert_question(q_data)
		doc.append("questions", {"question": q_name, "marks": 1})

	doc.save(ignore_permissions=True)
	return doc.name


def _upsert_lesson(lesson_data: dict, chapter_name: str, quiz_id: str | None = None) -> str:
	"""Create or update a Course Lesson inside a Course Chapter."""
	existing = frappe.db.get_value(
		"Course Lesson", {"title": lesson_data["title"], "chapter": chapter_name}, "name"
	)
	doc = frappe.get_doc("Course Lesson", existing) if existing else frappe.new_doc("Course Lesson")

	doc.title = lesson_data["title"]
	doc.chapter = chapter_name
	doc.body = lesson_data["body"]
	doc.tldr_summary = lesson_data["tldr_summary"]
	doc.include_in_preview = 1
	if quiz_id:
		doc.quiz_id = quiz_id

	doc.save(ignore_permissions=True)
	return doc.name


def _upsert_chapter(chapter_data: dict, course_name: str) -> str:
	"""Create or update a Course Chapter and its lessons/quiz."""
	existing = frappe.db.get_value(
		"Course Chapter", {"title": chapter_data["title"], "course": course_name}, "name"
	)
	doc = frappe.get_doc("Course Chapter", existing) if existing else frappe.new_doc("Course Chapter")

	doc.title = chapter_data["title"]
	doc.course = course_name
	doc.save(ignore_permissions=True)

	quiz_id = None
	if chapter_data.get("quiz"):
		quiz_id = _upsert_quiz(chapter_data["quiz"], course_name)

	lesson_names = []
	lessons = chapter_data["lessons"]
	for idx, lesson_data in enumerate(lessons):
		attach_quiz = quiz_id if (quiz_id and idx == len(lessons) - 1) else None
		lesson_names.append(_upsert_lesson(lesson_data, doc.name, quiz_id=attach_quiz))

	doc.reload()
	doc.set("lessons", [{"lesson": name} for name in lesson_names])
	doc.save(ignore_permissions=True)
	return doc.name


def _upsert_course(course_data: dict) -> str:
	"""Create or update an LMS Course and its chapters."""
	existing = frappe.db.get_value("LMS Course", {"title": course_data["title"]}, "name")
	doc = frappe.get_doc("LMS Course", existing) if existing else frappe.new_doc("LMS Course")

	doc.title = course_data["title"]
	doc.short_introduction = course_data["short_introduction"]
	doc.description = course_data["description"]
	doc.published = 1
	doc.enforce_lesson_completion = 1
	if not doc.instructors:
		doc.append("instructors", {"instructor": DEFAULT_INSTRUCTOR})

	doc.save(ignore_permissions=True)

	chapter_names = [_upsert_chapter(ch, doc.name) for ch in course_data["chapters"]]

	doc.reload()
	doc.set("chapters", [{"chapter": ch_name} for ch_name in chapter_names])
	doc.save(ignore_permissions=True)
	return doc.name


def _upsert_program(course_names: list[str]) -> str:
	"""Create or update the sequential LMS Program (Learning Path)."""
	existing = frappe.db.get_value("LMS Program", {"title": PROGRAM_TITLE}, "name")
	doc = frappe.get_doc("LMS Program", existing) if existing else frappe.new_doc("LMS Program")

	doc.title = PROGRAM_TITLE
	doc.published = 1
	doc.enforce_course_order = 1
	doc.set("program_courses", [{"course": c_name} for c_name in course_names])
	doc.save(ignore_permissions=True)
	return doc.name


def seed_learning_path() -> dict:
	"""Idempotently seed the complete 4-course Executive Soft Skills Learning Path."""
	ensure_tldr_custom_field()

	all_courses = COURSES_1_AND_2 + COURSES_3_AND_4
	course_names = [_upsert_course(c) for c in all_courses]
	program_name = _upsert_program(course_names)

	frappe.db.commit()
	return {
		"program": program_name,
		"courses": course_names,
		"status": "ok",
	}
