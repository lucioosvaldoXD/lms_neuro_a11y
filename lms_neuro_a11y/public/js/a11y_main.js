/**
 * Main orchestrator for LogiSentinel LMS Neuro-Accessibility.
 * Synchronizes localStorage (FOUC-free) with Frappe RPC API and DOM engines.
 */

import { applyBionicReading, revertBionicReading } from './a11y_bionic.js';
import { showCalibrationModal } from './a11y_calibration_modal.js';
import { mountA11yDrawer } from './a11y_drawer.js';
import { renderFocusWidgets } from './a11y_focus_pomodoro.js';
import { ensureReadingRuler } from './a11y_ruler.js';

const STORAGE_KEY = 'lms_neuro_a11y_profile';

const DEFAULT_PROFILE = {
	calibration_completed: 0,
	focus_mode: 0,
	bionic_reading: 0,
	dyslexia_font: 0,
	reading_ruler: 0,
	reduced_motion: 0,
	tldr_first: 1,
	preferred_modality: 'Balanced',
	is_guest: true,
};

let currentProfile = loadLocalProfile();
let observerTimer = null;

function loadLocalProfile() {
	try {
		const raw = localStorage.getItem(STORAGE_KEY);
		return raw ? { ...DEFAULT_PROFILE, ...JSON.parse(raw) } : { ...DEFAULT_PROFILE };
	} catch {
		return { ...DEFAULT_PROFILE };
	}
}

function saveLocalProfile(profile) {
	currentProfile = { ...DEFAULT_PROFILE, ...profile };
	try {
		localStorage.setItem(STORAGE_KEY, JSON.stringify(currentProfile));
	} catch {
		/* Ignore private-mode storage errors */
	}
}

function applyAttributes(profile) {
	const map = {
		focus_mode: 'data-a11y-focus',
		bionic_reading: 'data-a11y-bionic',
		dyslexia_font: 'data-a11y-dyslexia',
		reading_ruler: 'data-a11y-ruler',
		reduced_motion: 'data-a11y-motion',
		tldr_first: 'data-a11y-tldr',
	};

	[document.documentElement, document.body].forEach((el) => {
		if (!el) return;
		Object.entries(map).forEach(([field, attr]) => {
			el.setAttribute(attr, profile[field] ? '1' : '0');
		});
		el.setAttribute('data-a11y-modality', profile.preferred_modality || 'Balanced');
	});

	ensureReadingRuler(Boolean(profile.reading_ruler));

	if (profile.reduced_motion) {
		document.querySelectorAll('video, audio').forEach((media) => {
			media.removeAttribute('autoplay');
			if (!media.paused) media.pause();
		});
	}

	if (profile.bionic_reading) {
		applyBionicReading();
	} else {
		revertBionicReading();
	}

	renderFocusWidgets(profile, detectLessonIdentifier(), fetchLessonTldr);
}

function detectLessonIdentifier() {
	const match = window.location.pathname.match(/\/courses\/[^/]+\/learn\/([^/?#]+)/);
	return match ? decodeURIComponent(match[1]) : '';
}

async function rpcCall(method, args = {}, httpMethod = 'GET') {
	const url = `/api/method/${method}`;
	const headers = { Accept: 'application/json' };

	if (httpMethod === 'POST') {
		headers['Content-Type'] = 'application/json';
		if (window.frappe && window.frappe.csrf_token) {
			headers['X-Frappe-CSRF-Token'] = window.frappe.csrf_token;
		}
		const res = await fetch(url, {
			method: 'POST',
			credentials: 'same-origin',
			headers,
			body: JSON.stringify(args),
		});
		const data = await res.json();
		return data.message;
	}

	const res = await fetch(url, { credentials: 'same-origin', headers });
	const data = await res.json();
	return data.message;
}

async function fetchLessonTldr(lessonName) {
	try {
		const res = await rpcCall(
			`lms_neuro_a11y.api.get_lesson_tldr?lesson_name=${encodeURIComponent(lessonName)}`
		);
		return res?.tldr_summary || '';
	} catch {
		return '';
	}
}

async function handleSettingToggle(field, value) {
	const next = { ...currentProfile, [field]: value };
	saveLocalProfile(next);
	applyAttributes(next);

	if (!currentProfile.is_guest) {
		try {
			const updated = await rpcCall(
				'lms_neuro_a11y.api.update_a11y_setting',
				{ field, value },
				'POST'
			);
			if (updated) saveLocalProfile(updated);
		} catch {
			/* Keep optimistic local state if offline */
		}
	}
}

async function handleCalibrationComplete(answers) {
	try {
		if (!currentProfile.is_guest) {
			const updated = await rpcCall(
				'lms_neuro_a11y.api.save_calibration_results',
				{ answers_dict: answers },
				'POST'
			);
			if (updated) {
				saveLocalProfile(updated);
				applyAttributes(updated);
				return;
			}
		}
	} catch {
		/* Fallback to local persistence */
	}

	const fallback = { ...currentProfile, calibration_completed: 1 };
	if (!answers.skipped) {
		fallback.focus_mode = answers.visual_density === 'tunnel' ? 1 : 0;
		fallback.dyslexia_font = answers.text_processing === 'dyslexia_sepia' ? 1 : 0;
		fallback.reduced_motion = answers.sensory_control === 'manual_reduced' ? 1 : 0;
		fallback.preferred_modality =
			answers.info_consumption === 'text_structured' ? 'Text_First' : 'Video_First';
	}
	saveLocalProfile(fallback);
	applyAttributes(fallback);
}

function applyLogiSentinelBranding() {
	if (document.title && document.title.includes('Frappe Learning')) {
		document.title = document.title.replace(/Frappe Learning/g, 'LogiSentinel Academy');
	} else if (!document.title || document.title === 'Learning') {
		document.title = 'LogiSentinel Academy';
	}
}

function observeLessonDom() {
	const observer = new MutationObserver(() => {
		clearTimeout(observerTimer);
		observerTimer = setTimeout(() => {
			applyLogiSentinelBranding();
			if (currentProfile.bionic_reading) applyBionicReading();
			renderFocusWidgets(currentProfile, detectLessonIdentifier(), fetchLessonTldr);
		}, 120);
	});
	observer.observe(document.body, { childList: true, subtree: true });
}

async function init() {
	applyLogiSentinelBranding();
	applyAttributes(currentProfile);
	mountA11yDrawer(
		() => currentProfile,
		handleSettingToggle,
		() => showCalibrationModal(handleCalibrationComplete)
	);
	observeLessonDom();

	const isLmsRoute = window.location.pathname.includes('/lms');

	try {
		const remote = await rpcCall('lms_neuro_a11y.api.get_user_a11y_profile');
		if (remote) {
			const merged = remote.is_guest ? { ...currentProfile, is_guest: true } : remote;
			saveLocalProfile(merged);
			applyAttributes(merged);
			if (isLmsRoute && Number(merged.calibration_completed) === 0) {
				showCalibrationModal(handleCalibrationComplete);
			}
			return;
		}
	} catch {
		/* Continue with local profile if API unreachable */
	}

	if (isLmsRoute && Number(currentProfile.calibration_completed) === 0) {
		showCalibrationModal(handleCalibrationComplete);
	}
}

if (document.readyState === 'loading') {
	document.addEventListener('DOMContentLoaded', init);
} else {
	init();
}
