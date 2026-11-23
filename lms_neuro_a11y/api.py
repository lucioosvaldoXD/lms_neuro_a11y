"""Whitelisted RPC/REST API for LMS Neuro A11y."""

import json

import frappe
from frappe import _

from lms_neuro_a11y.lms_neuro_a11y.doctype.lms_accessibility_profile.lms_accessibility_profile import (
	VALID_MODALITIES,
	get_profile_cache_key,
)

BOOLEAN_FIELDS = {
	"calibration_completed",
	"focus_mode",
	"bionic_reading",
	"dyslexia_font",
	"reading_ruler",
	"reduced_motion",
	"tldr_first",
}

ALL_PROFILE_FIELDS = sorted(BOOLEAN_FIELDS | {"preferred_modality"})

DEFAULT_PROFILE = {
	"calibration_completed": 0,
	"focus_mode": 0,
	"bionic_reading": 0,
	"dyslexia_font": 0,
	"reading_ruler": 0,
	"reduced_motion": 0,
	"tldr_first": 1,
	"preferred_modality": "Balanced",
}


def _serialize_profile(doc) -> dict:
	"""Serialize an LMS Accessibility Profile document into a plain dict."""
	return {
		"user": doc.user,
		"calibration_completed": int(doc.calibration_completed or 0),
		"focus_mode": int(doc.focus_mode or 0),
		"bionic_reading": int(doc.bionic_reading or 0),
		"dyslexia_font": int(doc.dyslexia_font or 0),
		"reading_ruler": int(doc.reading_ruler or 0),
		"reduced_motion": int(doc.reduced_motion or 0),
		"tldr_first": int(doc.tldr_first if doc.tldr_first is not None else 1),
		"preferred_modality": doc.preferred_modality or "Balanced",
	}


def _get_or_create_profile_doc(user: str):
	"""Fetch the user's LMS Accessibility Profile or create one with defaults."""
	if frappe.db.exists("LMS Accessibility Profile", user):
		return frappe.get_doc("LMS Accessibility Profile", user)

	doc = frappe.get_doc(
		{
			"doctype": "LMS Accessibility Profile",
			"user": user,
			**DEFAULT_PROFILE,
		}
	)
	doc.insert(ignore_permissions=True)
	frappe.db.commit()
	return doc


def _coerce_bool_int(value) -> int:
	"""Convert truthy/falsy inputs strictly to 0 or 1."""
	if isinstance(value, bool):
		return 1 if value else 0
	if isinstance(value, int) and value in (0, 1):
		return value
	if isinstance(value, str) and value.strip().lower() in {"0", "1", "true", "false"}:
		return 1 if value.strip().lower() in {"1", "true"} else 0
	frappe.throw(_("Invalid boolean value: {0}").format(value), frappe.ValidationError)


@frappe.whitelist(allow_guest=True)
def get_user_a11y_profile() -> dict:
	"""Return the current user's accessibility profile, creating defaults if absent."""
	user = frappe.session.user
	if not user or user == "Guest":
		return {"user": "Guest", "is_guest": True, **DEFAULT_PROFILE}

	cache_key = get_profile_cache_key(user)
	cached = frappe.cache().get_value(cache_key)
	if isinstance(cached, dict):
		return cached

	doc = _get_or_create_profile_doc(user)
	data = _serialize_profile(doc)
	data["is_guest"] = False
	frappe.cache().set_value(cache_key, data, expires_in_sec=3600)
	return data


@frappe.whitelist()
def update_a11y_setting(field: str, value) -> dict:
	"""Update a single accessibility setting for the logged-in user with schema validation."""
	user = frappe.session.user
	if not user or user == "Guest":
		frappe.throw(_("Authentication required to save accessibility settings."), frappe.PermissionError)

	if field not in ALL_PROFILE_FIELDS:
		frappe.throw(_("Unsupported accessibility field: {0}").format(field), frappe.ValidationError)

	if field in BOOLEAN_FIELDS:
		normalized_value = _coerce_bool_int(value)
	else:
		if not isinstance(value, str) or value not in VALID_MODALITIES:
			frappe.throw(
				_("Invalid preferred_modality '{0}'. Allowed: {1}").format(
					value, ", ".join(sorted(VALID_MODALITIES))
				),
				frappe.ValidationError,
			)
		normalized_value = value

	doc = _get_or_create_profile_doc(user)
	setattr(doc, field, normalized_value)
	doc.save(ignore_permissions=True)
	frappe.db.commit()

	data = _serialize_profile(doc)
	data["is_guest"] = False
	frappe.cache().set_value(get_profile_cache_key(user), data, expires_in_sec=3600)
	return data


@frappe.whitelist()
def save_calibration_results(answers_dict) -> dict:
	"""Process the 4-step cognitive calibration answers and persist profile switches."""
	user = frappe.session.user
	if not user or user == "Guest":
		frappe.throw(_("Authentication required to save calibration."), frappe.PermissionError)

	if isinstance(answers_dict, str):
		try:
			answers = json.loads(answers_dict)
		except json.JSONDecodeError:
			frappe.throw(_("Invalid JSON payload for calibration answers."), frappe.ValidationError)
	elif isinstance(answers_dict, dict):
		answers = answers_dict
	else:
		frappe.throw(_("Calibration answers must be a dictionary or JSON object."), frappe.ValidationError)

	doc = _get_or_create_profile_doc(user)

	if not answers.get("skipped"):
		visual_density = answers.get("visual_density", "standard")
		text_processing = answers.get("text_processing", "standard")
		info_consumption = answers.get("info_consumption", "balanced")
		sensory_control = answers.get("sensory_control", "standard")

		doc.focus_mode = 1 if visual_density == "tunnel" else 0
		doc.dyslexia_font = 1 if text_processing == "dyslexia_sepia" else 0
		doc.bionic_reading = 1 if text_processing == "bionic" else 0
		doc.reduced_motion = 1 if sensory_control == "manual_reduced" else 0
		doc.tldr_first = 1

		modality_map = {
			"video_transcript": "Video_First",
			"text_structured": "Text_First",
			"audio_only": "Audio_Only",
			"balanced": "Balanced",
		}
		doc.preferred_modality = modality_map.get(info_consumption, "Balanced")

	doc.calibration_completed = 1
	doc.save(ignore_permissions=True)
	frappe.db.commit()

	data = _serialize_profile(doc)
	data["is_guest"] = False
	frappe.cache().set_value(get_profile_cache_key(user), data, expires_in_sec=3600)
	return data


@frappe.whitelist(allow_guest=True)
def get_lesson_tldr(lesson_name: str) -> dict:
	"""Return the TL;DR summary for a Course Lesson if the user has read permission."""
	if not lesson_name or not frappe.db.exists("Course Lesson", lesson_name):
		return {"lesson": lesson_name, "tldr_summary": ""}

	if not frappe.has_permission("Course Lesson", ptype="read", doc=lesson_name):
		frappe.throw(_("Not permitted to view this lesson."), frappe.PermissionError)

	tldr = frappe.db.get_value("Course Lesson", lesson_name, "tldr_summary") or ""
	return {"lesson": lesson_name, "tldr_summary": tldr}
