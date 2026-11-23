/**
 * 4-Step Cognitive Calibration Modal (non-clinical, ~45s, 1 click per step).
 */

const STEPS = [
	{
		key: 'visual_density',
		badge: 'Paso 1 de 4 · Densidad Visual',
		title: '¿Cómo prefieres tu espacio de estudio?',
		subtitle: 'Puedes cambiarlo en cualquier momento desde Ajustes de Lectura.',
		options: [
			{
				value: 'standard',
				icon: '◫',
				label: 'Vista completa con menús',
				desc: 'Navegación lateral siempre visible y estructura clásica del curso.',
			},
			{
				value: 'tunnel',
				icon: '◎',
				label: 'Modo Túnel sin distracciones',
				desc: 'Oculta barras laterales y activa un temporizador Pomodoro integrado.',
			},
		],
	},
	{
		key: 'text_processing',
		badge: 'Paso 2 de 4 · Procesamiento de Texto',
		title: 'Elige la lectura más cómoda para tu vista',
		subtitle: 'Compara el estilo estándar frente a tipografía de alta legibilidad.',
		options: [
			{
				value: 'standard',
				icon: 'Aa',
				label: 'Tipografía estándar limpia',
				desc: 'Fuente nativa del sistema con contraste neutro habitual.',
				previewClass: '',
			},
			{
				value: 'dyslexia_sepia',
				icon: 'Aa',
				label: 'Atkinson Hyperlegible + Sepia',
				desc: 'Interlineado 1.8 y papel crema suave #FAF8F5 de baja fatiga visual.',
				previewClass: 'sepia-preview',
			},
			{
				value: 'bionic_beeline',
				icon: '⚡',
				label: 'Bionic + BeeLine Reader',
				desc: 'Negritas guía en sílabas iniciales + degradado de color por línea.',
				previewClass: '',
			},
		],
	},
	{
		key: 'info_consumption',
		badge: 'Paso 3 de 4 · Consumo de Información',
		title: '¿Qué formato te ayuda a retener mejor?',
		subtitle: 'Priorizaremos los bloques de contenido según tu preferencia.',
		options: [
			{
				value: 'video_transcript',
				icon: '▶',
				label: 'Video con guía escrita',
				desc: 'Contenido audiovisual acompañado de notas y transcripción.',
			},
			{
				value: 'text_structured',
				icon: '☰',
				label: 'Texto estructurado + TL;DR',
				desc: 'Resumen ejecutivo de 3 puntos al inicio y lectura paso a paso.',
			},
		],
	},
	{
		key: 'sensory_control',
		badge: 'Paso 4 de 4 · Control Sensorial',
		title: 'Define el comportamiento multimedia',
		subtitle: 'Controla transiciones visuales y reproducción de audio o video.',
		options: [
			{
				value: 'standard',
				icon: '✦',
				label: 'Estándar dinámico',
				desc: 'Transiciones suaves y comportamiento multimedia habitual.',
			},
			{
				value: 'manual_reduced',
				icon: '⏸',
				label: 'Control manual total',
				desc: 'Cero animaciones CSS y sin reproducción automática (autoplay).',
			},
		],
	},
];

export function showCalibrationModal(onComplete) {
	if (document.getElementById('ls-a11y-modal-backdrop')) return;

	let currentStep = 0;
	const answers = {};

	const backdrop = document.createElement('div');
	backdrop.id = 'ls-a11y-modal-backdrop';
	backdrop.setAttribute('role', 'dialog');
	backdrop.setAttribute('aria-modal', 'true');
	backdrop.setAttribute('aria-label', 'Calibración cognitiva de lectura');

	const modal = document.createElement('div');
	modal.id = 'ls-a11y-modal';
	backdrop.appendChild(modal);
	document.body.appendChild(backdrop);

	function renderStep() {
		const step = STEPS[currentStep];
		const progressPct = ((currentStep + 1) / STEPS.length) * 100;

		modal.innerHTML = `
			<div class="ls-cal-header">
				<div class="ls-cal-brand">
					<img src="/assets/lms_neuro_a11y/images/logisentinel-icon-transparent.png" alt="LogiSentinel" />
					<div>
						<div class="ls-cal-brand-name">LogiSentinel Academy</div>
						<div class="ls-cal-brand-sub">Calibración rápida · 45 seg</div>
					</div>
				</div>
				<button type="button" id="ls-cal-skip" class="ls-cal-skip">
					Saltar y usar estándar
				</button>
			</div>

			<div class="ls-cal-progress-track" aria-hidden="true">
				<div class="ls-cal-progress-fill" style="width:${progressPct}%"></div>
			</div>

			<div class="ls-cal-step-badge">${step.badge}</div>
			<h2 class="ls-cal-title">${step.title}</h2>
			<p class="ls-cal-subtitle">${step.subtitle}</p>

			<div class="ls-cal-options">
				${step.options
					.map(
						(opt) => `
					<button type="button" class="ls-cal-card ${opt.previewClass || ''}" data-value="${opt.value}">
						<div class="ls-cal-card-top">
							<span class="ls-cal-card-icon">${opt.icon}</span>
							<span class="ls-cal-card-arrow">→</span>
						</div>
						<div class="ls-cal-card-title">${opt.label}</div>
						<div class="ls-cal-card-desc">${opt.desc}</div>
					</button>`
					)
					.join('')}
			</div>
		`;

		modal.querySelector('#ls-cal-skip').addEventListener('click', () => {
			backdrop.remove();
			onComplete({ skipped: true });
		});

		modal.querySelectorAll('.ls-cal-card').forEach((btn) => {
			btn.addEventListener('click', () => {
				answers[step.key] = btn.getAttribute('data-value');
				if (currentStep < STEPS.length - 1) {
					currentStep += 1;
					renderStep();
				} else {
					backdrop.remove();
					onComplete(answers);
				}
			});
		});
	}

	renderStep();
}
