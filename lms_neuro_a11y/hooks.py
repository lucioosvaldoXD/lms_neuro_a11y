app_name = "lms_neuro_a11y"
app_title = "LMS Neuro A11y"
app_publisher = "LogiSentinel"
app_description = "Neurodivergent-friendly accessibility and LogiSentinel branding for Frappe LMS"
app_email = "soporte@logisentinel.com"
app_license = "MIT"
required_apps = ["frappe", "lms"]

# Desk includes
app_include_css = "/assets/lms_neuro_a11y/css/a11y.css"
app_include_js = "/assets/lms_neuro_a11y/js/a11y_loader.js"

# Website / LMS SPA injection without touching apps/lms/ or apps/frappe/
after_request = ["lms_neuro_a11y.injection.inject_lms_a11y_assets"]

# Post-install LogiSentinel branding setup
after_install = "lms_neuro_a11y.install.after_install"

# Fixtures
fixtures = [
    {
        "dt": "Custom Field",
        "filters": [["name", "in", ["Course Lesson-tldr_summary"]]],
    }
]
