"""Controller for LMS Accessibility Profile DocType."""

import frappe
from frappe.model.document import Document

CACHE_KEY_PREFIX = "lms_neuro_a11y:profile:"
VALID_MODALITIES = {"Balanced", "Video_First", "Text_First", "Audio_Only"}


def get_profile_cache_key(user: str) -> str:
	"""Return the Redis cache key for a user's accessibility profile."""
	return f"{CACHE_KEY_PREFIX}{user}"


class LMSAccessibilityProfile(Document):
	"""1-to-1 user cognitive and reading accessibility settings."""

	def validate(self):
		"""Ensure preferred_modality is valid and normalize boolean check fields."""
		if not self.preferred_modality:
			self.preferred_modality = "Balanced"
		if self.preferred_modality not in VALID_MODALITIES:
			frappe.throw(
				f"Invalid preferred_modality '{self.preferred_modality}'. "
				f"Allowed: {', '.join(sorted(VALID_MODALITIES))}"
			)

	def on_update(self):
		"""Invalidate cached profile when saved."""
		if self.user:
			frappe.cache().delete_value(get_profile_cache_key(self.user))

	def on_trash(self):
		"""Invalidate cached profile when deleted."""
		if self.user:
			frappe.cache().delete_value(get_profile_cache_key(self.user))
