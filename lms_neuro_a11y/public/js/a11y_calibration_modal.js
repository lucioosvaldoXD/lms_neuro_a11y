/**
 * 4-Step Cognitive Calibration Modal (non-clinical, ~45s, 1 click per step).
 */

const STEPS = [
	{
		key: 'visual_density',
		title: '1/4 · Densidad Visual',
		subtitle: '¿Cómo prefieres ver el espacio de estudio?',
		options: [
			{
				value: 'standard',
				label: 'Pantalla completa con menús',
				desc: 'Navegación lateral visible y vista estándar del curso.',
			},
			{
				value: 'tunnel',
				label: 'Modo Túnel sin distracciones',
				desc: 'Oculta barras laterales y activa temporizador Pomodoro.',
			},
		],
	},
	{
		key: 'text_processing',
		title: '2/4 · Procesamiento de Texto',
		subtitle: 'Elige la tipografía y contraste más cómodo para tus ojos:',
		options: [
			{
				value: 'standard',
				label: 'Fuente estándar limpia',
				desc: 'Tipografía nativa del sistema sobre fondo neutro.',
				previewClass: '',
			},
			{
				value: 'dyslexia_sepia',
				label: 'Atkinson Hyperlegible + Sepia suave',
				desc: 'Interlineado amplio (1.8) y fondo crema #FAF8F5 de baja fatiga.',
				previewClass: 'sepia-preview',
			},
		],
	},
	{
		key: 'info_consumption',
		title: '3/4 · Consumo de Información',
		subtitle: '¿Qué formato te ayuda a retener mejor las lecciones?',
		options: [
			{
				value: 'video_transcript',
				label: 'Video con transcripción',
				desc: 'Prioriza contenido audiovisual acompañado de guía escrita.',
			},
			{
				value: 'text_structured',
				label: 'Texto estructurado paso a paso',
				desc: 'Resumen ejecutivo (TL;DR) arriba y bloques claros.',
			},
		],
	},
	{
		key: 'sensory_control',
		title: '4/4 · Control Sensorial',
		subtitle: 'Define cómo debe comportarse el movimiento y multimedia:',
		options: [
			{
				value: 'standard',
				label: 'Estándar dinámico',
				desc: 'Transiciones normales y reproducción habitual.',
			},
			{
				value: 'manual_reduced',
				label: 'Control manual total',
				desc: 'Sin animaciones CSS ni reproducción automática (autoplay).',
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
		modal.innerHTML = `
			<div style="display:flex;align-items:center;justify-content:space-between;gap:1rem;">
				<div style="display:flex;align-items:center;gap:0.6rem;">
					<img src="/assets/lms_neuro_a11y/images/logisentinel-icon-transparent.png" alt="LogiSentinel" style="width:28px;height:28px;" />
					<span style="font-size:0.85rem;color:#94A3B8;font-weight:600;">LogiSentinel Academy · Calibración rápida</span>
				</div>
				<button type="button" id="ls-cal-skip" style="background:transparent;border:none;color:#94A3B8;cursor:pointer;font-size:0.85rem;text-decoration:underline;">
					Saltar y usar estándar
				</button>
			</div>
			<h2 style="margin:1rem 0 0.25rem;font-size:1.25rem;font-weight:700;">${step.title}</h2>
			<p style="margin:0;color:#CBD5E1;font-size:0.95rem;">${step.subtitle}</p>
			<div class="ls-cal-options">
				${step.options
					.map(
						(opt) => `
					<button type="button" class="ls-cal-card ${opt.previewClass || ''}" data-value="${opt.value}">
						<div style="font-weight:700;margin-bottom:0.35rem;">${opt.label}</div>
						<div style="font-size:0.85rem;opacity:0.85;">${opt.desc}</div>
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
