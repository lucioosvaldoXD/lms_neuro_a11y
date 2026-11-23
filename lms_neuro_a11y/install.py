"""Post-installation helpers for LogiSentinel LMS branding."""

import frappe


def after_install():
	"""Apply LogiSentinel default branding in Website Settings and LMS Settings if available."""
	_apply_website_branding()


def _apply_website_branding():
	"""Configure Website Settings with LogiSentinel name and icon without altering core code."""
	if not frappe.db.exists("DocType", "Website Settings"):
		return

	try:
		ws = frappe.get_single("Website Settings")
		if not ws.app_name or ws.app_name in ("Frappe", "Frappe Learning", "Learning"):
			ws.app_name = "LogiSentinel Academy"
		if not ws.app_logo:
			ws.app_logo = "/assets/lms_neuro_a11y/images/logisentinel-icon-transparent.png"
		if not ws.favicon:
			ws.favicon = "/assets/lms_neuro_a11y/images/logisentinel-icon-transparent.png"
		ws.save(ignore_permissions=True)
	except Exception:
		frappe.log_error(frappe.get_traceback(), "lms_neuro_a11y: Failed to apply Website Settings branding")
