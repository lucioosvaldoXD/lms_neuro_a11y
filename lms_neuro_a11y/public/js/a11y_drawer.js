/**
 * Quick-Switch Floating/Header Button & Slide-over Accessibility Drawer.
 */

const SWITCHES = [
	{
		key: 'focus_mode',
		label: 'Modo Enfoque (Túnel)',
		desc: 'Oculta barras laterales y muestra Pomodoro.',
	},
	{
		key: 'bionic_reading',
		label: 'Lectura Biónica',
		desc: 'Resalta sílabas iniciales para lectura ágil.',
	},
	{
		key: 'beeline_reading',
		label: 'Lectura BeeLine (Degradado)',
		desc: 'Degradado suave por renglón para no saltar líneas.',
	},
	{
		key: 'dyslexia_font',
		label: 'Tipografía Dislexia + Sepia',
		desc: 'Atkinson Hyperlegible, interlineado 1.8 y #FAF8F5.',
	},
	{
		key: 'reading_ruler',
		label: 'Regla de Lectura',
		desc: 'Guía horizontal que sigue el cursor.',
	},
	{
		key: 'reduced_motion',
		label: 'Movimiento Reducido',
		desc: 'Desactiva animaciones y autoplay multimedia.',
	},
	{
		key: 'tldr_first',
		label: 'TL;DR Primero',
		desc: 'Destaca el resumen ejecutivo al inicio.',
	},
];

export function mountA11yDrawer(getProfile, onToggle, onRecalibrate) {
	if (document.getElementById('ls-a11y-trigger')) return;

	const trigger = document.createElement('button');
	trigger.id = 'ls-a11y-trigger';
	trigger.type = 'button';
	trigger.setAttribute('aria-haspopup', 'dialog');
	trigger.setAttribute('aria-expanded', 'false');
	trigger.innerHTML = `
		<img src="/assets/lms_neuro_a11y/images/logisentinel-icon-transparent.png" alt="" />
		<span>Ajustes de Lectura y Enfoque</span>
	`;

	const drawer = document.createElement('aside');
	drawer.id = 'ls-a11y-drawer';
	drawer.setAttribute('role', 'dialog');
	drawer.setAttribute('aria-label', 'Ajustes de Lectura y Enfoque');

	document.body.appendChild(trigger);
	document.body.appendChild(drawer);

	function renderDrawer() {
		const profile = getProfile();
		drawer.innerHTML = `
			<div class="ls-a11y-brand-bar">
				<div class="ls-a11y-brand-title">
					<img src="/assets/lms_neuro_a11y/images/logisentinel-icon-transparent.png" alt="LogiSentinel" />
					<span>Lectura y Enfoque</span>
				</div>
				<button type="button" id="ls-a11y-close" aria-label="Cerrar panel" style="background:transparent;border:none;color:#CBD5E1;font-size:1.25rem;cursor:pointer;">&times;</button>
			</div>
			${SWITCHES.map((s) => {
				const checked = Boolean(profile[s.key]);
				return `
				<div class="ls-a11y-switch-row">
					<div class="ls-a11y-switch-label">
						<strong>${s.label}</strong>
						<span>${s.desc}</span>
					</div>
					<button
						type="button"
						class="ls-a11y-toggle"
						role="switch"
						aria-checked="${checked ? 'true' : 'false'}"
						data-field="${s.key}"
						aria-label="${s.label}"
					></button>
				</div>`;
			}).join('')}
			<div class="ls-a11y-switch-row">
				<div class="ls-a11y-switch-label">
					<strong>Modalidad Preferida</strong>
					<span>Formato prioritario de contenido</span>
				</div>
				<select id="ls-a11y-modality" style="background:#131528;color:#F8FAFC;border:1px solid rgba(124,92,255,0.4);border-radius:0.4rem;padding:0.35rem 0.5rem;font-size:0.8rem;">
					<option value="Balanced" ${profile.preferred_modality === 'Balanced' ? 'selected' : ''}>Balanceado</option>
					<option value="Video_First" ${profile.preferred_modality === 'Video_First' ? 'selected' : ''}>Video primero</option>
					<option value="Text_First" ${profile.preferred_modality === 'Text_First' ? 'selected' : ''}>Texto primero</option>
					<option value="Audio_Only" ${profile.preferred_modality === 'Audio_Only' ? 'selected' : ''}>Solo audio</option>
				</select>
			</div>
			<button type="button" id="ls-a11y-recalibrate" class="ls-pomo-btn" style="width:100%;padding:0.65rem;">
				Repetir calibración cognitiva (45s)
			</button>
		`;

		drawer.querySelector('#ls-a11y-close').addEventListener('click', () => {
			drawer.classList.remove('open');
			trigger.setAttribute('aria-expanded', 'false');
		});

		drawer.querySelectorAll('.ls-a11y-toggle').forEach((btn) => {
			btn.addEventListener('click', () => {
				const field = btn.getAttribute('data-field');
				const next = btn.getAttribute('aria-checked') !== 'true' ? 1 : 0;
				btn.setAttribute('aria-checked', next ? 'true' : 'false');
				onToggle(field, next);
			});
		});

		drawer.querySelector('#ls-a11y-modality').addEventListener('change', (e) => {
			onToggle('preferred_modality', e.target.value);
		});

		drawer.querySelector('#ls-a11y-recalibrate').addEventListener('click', () => {
			drawer.classList.remove('open');
			trigger.setAttribute('aria-expanded', 'false');
			onRecalibrate();
		});
	}

	trigger.addEventListener('click', () => {
		const isOpen = drawer.classList.toggle('open');
		trigger.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
		if (isOpen) renderDrawer();
	});

	return { refresh: renderDrawer };
}
