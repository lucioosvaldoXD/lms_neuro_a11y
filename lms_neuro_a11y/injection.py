"""HTML response injection for /lms SPA without modifying core frappe/lms templates."""

import frappe

BOOTSTRAP_HEAD_SNIPPET = """<!-- lms_neuro_a11y: FOUC-free bootstrap & LogiSentinel theme -->
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400;1,700&display=swap" />
<link rel="stylesheet" href="/assets/lms_neuro_a11y/css/a11y.css" />
<script>
(function(){
  try {
    var raw = localStorage.getItem('lms_neuro_a11y_profile');
    if (!raw) return;
    var p = JSON.parse(raw);
    var root = document.documentElement;
    var map = {
      focus_mode: 'data-a11y-focus',
      bionic_reading: 'data-a11y-bionic',
      beeline_reading: 'data-a11y-beeline',
      dyslexia_font: 'data-a11y-dyslexia',
      reading_ruler: 'data-a11y-ruler',
      reduced_motion: 'data-a11y-motion',
      tldr_first: 'data-a11y-tldr'
    };
    Object.keys(map).forEach(function(k){
      root.setAttribute(map[k], p[k] ? '1' : '0');
    });
    if (p.preferred_modality) {
      root.setAttribute('data-a11y-modality', String(p.preferred_modality));
    }
  } catch (e) {}
})();
</script>"""

BODY_END_SNIPPET = """<script type="module" src="/assets/lms_neuro_a11y/js/a11y_main.js"></script>"""


def _is_lms_html_response(response) -> bool:
	"""Return True when the current HTTP response is an HTML page under the LMS path."""
	if not response or not getattr(response, "mimetype", "") == "text/html":
		return False
	req = getattr(frappe.local, "request", None)
	if not req:
		return False
	path = (req.path or "").strip("/")
	lms_path = (frappe.conf.get("lms_path") or "lms").strip("/") if frappe.conf else "lms"
	return path == lms_path or path.startswith(f"{lms_path}/")


def inject_lms_a11y_assets(response=None, **kwargs):
	"""Inject anti-FOUC bootstrap, CSS, and modular JS into /lms HTML responses."""
	if not _is_lms_html_response(response):
		return response

	try:
		html = response.get_data(as_text=True)
		if not html or "lms_neuro_a11y: FOUC-free bootstrap" in html:
			return response

		if "</head>" in html:
			html = html.replace("</head>", f"{BOOTSTRAP_HEAD_SNIPPET}\n</head>", 1)
		if "</body>" in html:
			html = html.replace("</body>", f"{BODY_END_SNIPPET}\n</body>", 1)

		response.set_data(html)
	except Exception:
		frappe.log_error(frappe.get_traceback(), "lms_neuro_a11y: HTML injection failed")

	return response
