/**
 * Classic loader for Frappe Desk (app_include_js) that mounts the ES module once.
 */
(function () {
	if (window.__lmsNeuroA11yLoaded) return;
	window.__lmsNeuroA11yLoaded = true;
	var script = document.createElement('script');
	script.type = 'module';
	script.src = '/assets/lms_neuro_a11y/js/a11y_main.js';
	document.head.appendChild(script);
})();
