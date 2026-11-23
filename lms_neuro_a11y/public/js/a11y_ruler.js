/**
 * Horizontal Reading Ruler following pointer Y position.
 */

let rulerEl = null;
let listenerAttached = false;

export function ensureReadingRuler(enabled) {
	if (!rulerEl) {
		rulerEl = document.createElement('div');
		rulerEl.id = 'ls-a11y-ruler';
		rulerEl.setAttribute('aria-hidden', 'true');
		document.body.appendChild(rulerEl);
	}

	if (enabled && !listenerAttached) {
		window.addEventListener('pointermove', onPointerMove, { passive: true });
		listenerAttached = true;
	}
}

function onPointerMove(event) {
	if (!rulerEl) return;
	if (document.documentElement.getAttribute('data-a11y-ruler') !== '1') return;
	rulerEl.style.top = `${event.clientY}px`;
}
