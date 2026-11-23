"""Unit tests for LMS Accessibility Profile and its API endpoints."""

import json
from unittest.mock import patch

import frappe
from frappe.tests.utils import FrappeTestCase

from lms_neuro_a11y.api import (
	get_user_a11y_profile,
	save_calibration_results,
	update_a11y_setting,
)


class TestLMSAccessibilityProfile(FrappeTestCase):
	"""Verify profile auto-creation, validation, and calibration mapping."""

	def test_profile_defaults_and_update(self):
		"""Creating/fetching a profile returns defaults and validates updates."""
		test_user = "Administrator"
		frappe.set_user(test_user)

		profile = get_user_a11y_profile()
		self.assertEqual(profile["user"], test_user)
		self.assertIn(profile["preferred_modality"], {"Balanced", "Video_First", "Text_First", "Audio_Only"})

		updated = update_a11y_setting("bionic_reading", 1)
		self.assertEqual(updated["bionic_reading"], 1)

		updated = update_a11y_setting("preferred_modality", "Text_First")
		self.assertEqual(updated["preferred_modality"], "Text_First")

		with self.assertRaises(frappe.ValidationError):
			update_a11y_setting("unknown_field", 1)

		with self.assertRaises(frappe.ValidationError):
			update_a11y_setting("preferred_modality", "InvalidMode")

	def test_save_calibration_results(self):
		"""Calibration answers map deterministically to accessibility switches."""
		frappe.set_user("Administrator")
		answers = {
			"visual_density": "tunnel",
			"text_processing": "dyslexia_sepia",
			"info_consumption": "text_structured",
			"sensory_control": "manual_reduced",
		}
		res = save_calibration_results(json.dumps(answers))
		self.assertEqual(res["calibration_completed"], 1)
		self.assertEqual(res["focus_mode"], 1)
		self.assertEqual(res["dyslexia_font"], 1)
		self.assertEqual(res["reduced_motion"], 1)
		self.assertEqual(res["preferred_modality"], "Text_First")
