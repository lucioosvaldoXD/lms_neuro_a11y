/**
 * Minimalist Pomodoro Timer (15/3 or 25/5) and TL;DR Summary Banner for Lesson view.
 */

let timerInterval = null;
let remainingSeconds = 25 * 60;
let currentPreset = 25;
let isRunning = false;

function formatClock(sec) {
	const m = Math.floor(sec / 60)
		.toString()
		.padStart(2, '0');
	const s = (sec % 60).toString().padStart(2, '0');
	return `${m}:${s}`;
}

export function renderFocusWidgets(profile, lessonName, fetchTldrFn) {
	const lessonRoot = document.querySelector('.ProseMirror, .lms-lesson-content');
	if (!lessonRoot || !lessonRoot.parentElement) return;

	const host = lessonRoot.parentElement;

	// 1. Pomodoro widget when focus_mode == 1
	const existingPomo = document.getElementById('ls-pomodoro-widget');
	if (profile.focus_mode) {
		if (!existingPomo) {
			const widget = document.createElement('div');
			widget.id = 'ls-pomodoro-widget';
			widget.innerHTML = `
				<div style="display:flex;align-items:center;gap:0.75rem;">
					<span style="font-weight:700;color:#10B981;">Enfoque Pomodoro</span>
					<strong id="ls-pomo-clock" style="font-size:1.15rem;font-variant-numeric:tabular-nums;">${formatClock(remainingSeconds)}</strong>
				</div>
				<div style="display:flex;align-items:center;gap:0.4rem;flex-wrap:wrap;">
					<button type="button" class="ls-pomo-btn" data-preset="15">15/3 min</button>
					<button type="button" class="ls-pomo-btn" data-preset="25">25/5 min</button>
					<button type="button" id="ls-pomo-toggle" class="ls-pomo-btn primary">${isRunning ? 'Pausar' : 'Iniciar'}</button>
					<button type="button" id="ls-pomo-reset" class="ls-pomo-btn">Reiniciar</button>
				</div>
			`;
			host.insertBefore(widget, host.firstChild);

			const updateClock = () => {
				const el = document.getElementById('ls-pomo-clock');
				if (el) el.textContent = formatClock(remainingSeconds);
			};

			widget.querySelectorAll('[data-preset]').forEach((btn) => {
				btn.addEventListener('click', () => {
					currentPreset = parseInt(btn.getAttribute('data-preset'), 10);
					isRunning = false;
					clearInterval(timerInterval);
					remainingSeconds = currentPreset * 60;
					widget.querySelector('#ls-pomo-toggle').textContent = 'Iniciar';
					updateClock();
				});
			});

			widget.querySelector('#ls-pomo-toggle').addEventListener('click', () => {
				isRunning = !isRunning;
				widget.querySelector('#ls-pomo-toggle').textContent = isRunning ? 'Pausar' : 'Iniciar';
				clearInterval(timerInterval);
				if (isRunning) {
					timerInterval = setInterval(() => {
						if (remainingSeconds > 0) {
							remainingSeconds -= 1;
							updateClock();
						} else {
							clearInterval(timerInterval);
							isRunning = false;
						}
					}, 1000);
				}
			});

			widget.querySelector('#ls-pomo-reset').addEventListener('click', () => {
				isRunning = false;
				clearInterval(timerInterval);
				remainingSeconds = currentPreset * 60;
				widget.querySelector('#ls-pomo-toggle').textContent = 'Iniciar';
				updateClock();
			});
		}
	} else if (existingPomo) {
		existingPomo.remove();
	}

	// 2. TL;DR Executive Summary when tldr_first == 1 or focus_mode == 1
	const existingTldr = document.getElementById('ls-tldr-banner');
	if ((profile.tldr_first || profile.focus_mode) && lessonName) {
		if (!existingTldr || existingTldr.getAttribute('data-lesson') !== lessonName) {
			fetchTldrFn(lessonName).then((tldr) => {
				if (!tldr) return;
				const prev = document.getElementById('ls-tldr-banner');
				if (prev) prev.remove();
				const banner = document.createElement('div');
				banner.id = 'ls-tldr-banner';
				banner.setAttribute('data-lesson', lessonName);
				const lines = tldr
					.split('\n')
					.map((l) => l.trim())
					.filter(Boolean)
					.map((l) => `<li>${l.replace(/^[-*•]\s*/, '')}</li>`)
					.join('');
				banner.innerHTML = `
					<h3>Resumen Ejecutivo (TL;DR)</h3>
					<ul style="margin:0;padding-left:1.25rem;display:flex;flex-direction:column;gap:0.25rem;">${lines}</ul>
				`;
				const targetHost = lessonRoot.parentElement;
				if (targetHost) {
					targetHost.insertBefore(banner, lessonRoot);
				}
			});
		}
	} else if (existingTldr) {
		existingTldr.remove();
	}
}
