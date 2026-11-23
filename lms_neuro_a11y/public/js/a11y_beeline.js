/**
 * BeeLine Reader-inspired line-by-line color gradient engine.
 * End of line N matches the start of line N+1 so the eye tracks line breaks effortlessly.
 * Composes cleanly with Bionic Reading (.ls-word spans).
 */

const SKIP_TAGS = new Set([
	'PRE',
	'CODE',
	'A',
	'SCRIPT',
	'STYLE',
	'TEXTAREA',
	'INPUT',
	'SELECT',
	'BUTTON',
	'SVG',
]);

const LIGHT_PALETTE = {
	A: [30, 41, 59], // #1E293B
	B: [91, 33, 182], // #5B21B6 (LogiSentinel violet)
	C: [15, 118, 110], // #0F766E (Cyber teal)
};

const DARK_PALETTE = {
	A: [241, 245, 249], // #F1F5F9
	B: [167, 139, 250], // #A78BFA
	C: [52, 211, 153], // #34D399
};

function lerpColor(c1, c2, t) {
	const r = Math.round(c1[0] + (c2[0] - c1[0]) * t);
	const g = Math.round(c1[1] + (c2[1] - c1[1]) * t);
	const b = Math.round(c1[2] + (c2[2] - c1[2]) * t);
	return `rgb(${r}, ${g}, ${b})`;
}

function getLineEndpoints(lineIndex, palette) {
	const phase = lineIndex % 4;
	if (phase === 0) return [palette.A, palette.B];
	if (phase === 1) return [palette.B, palette.A];
	if (phase === 2) return [palette.A, palette.C];
	return [palette.C, palette.A];
}

function shouldSkipNode(node) {
	let parent = node.parentElement;
	while (parent) {
		if (SKIP_TAGS.has(parent.tagName)) return true;
		if (parent.classList && (parent.classList.contains('ls-word') || parent.classList.contains('ls-beeline-only'))) {
			return true;
		}
		if (parent.isContentEditable) return true;
		parent = parent.parentElement;
	}
	return false;
}

function ensureWordSpans(container) {
	const walker = document.createTreeWalker(container, NodeFilter.SHOW_TEXT, {
		acceptNode(node) {
			if (!node.nodeValue || !node.nodeValue.trim()) return NodeFilter.FILTER_REJECT;
			if (shouldSkipNode(node)) return NodeFilter.FILTER_REJECT;
			return NodeFilter.FILTER_ACCEPT;
		},
	});

	const textNodes = [];
	let cur;
	while ((cur = walker.nextNode())) textNodes.push(cur);

	textNodes.forEach((textNode) => {
		const text = textNode.nodeValue;
		const parts = text.split(/(\s+)/);
		const frag = document.createDocumentFragment();
		parts.forEach((part) => {
			if (!part || /^\s+$/.test(part)) {
				frag.appendChild(document.createTextNode(part));
				return;
			}
			const span = document.createElement('span');
			span.className = 'ls-word ls-beeline-only';
			span.textContent = part;
			frag.appendChild(span);
		});
		if (textNode.parentNode) {
			textNode.parentNode.replaceChild(frag, textNode);
		}
	});
}

function isDarkModeWithoutSepia() {
	const root = document.documentElement;
	return root.getAttribute('data-theme') === 'dark' && root.getAttribute('data-a11y-dyslexia') !== '1';
}

export function applyBeelineReading(rootSelector = '.ProseMirror, .lms-lesson-content') {
	const palette = isDarkModeWithoutSepia() ? DARK_PALETTE : LIGHT_PALETTE;
	const containers = document.querySelectorAll(rootSelector);

	containers.forEach((container) => {
		ensureWordSpans(container);

		const blocks = container.querySelectorAll('p, li, blockquote, h1, h2, h3, h4');
		const targets = blocks.length ? Array.from(blocks) : [container];

		targets.forEach((block) => {
			const words = Array.from(block.querySelectorAll('.ls-word'));
			if (!words.length) return;

			// Group words into visual lines using their vertical midpoint
			const lines = [];
			let currentLine = [];
			let currentTop = null;

			words.forEach((word) => {
				const rect = word.getBoundingClientRect();
				if (rect.width === 0 && rect.height === 0) return;
				const midY = rect.top + rect.height / 2;
				if (currentTop === null || Math.abs(midY - currentTop) <= 8) {
					currentLine.push(word);
					if (currentTop === null) currentTop = midY;
				} else {
					lines.push(currentLine);
					currentLine = [word];
					currentTop = midY;
				}
			});
			if (currentLine.length) lines.push(currentLine);

			lines.forEach((lineWords, lineIdx) => {
				const [startColor, endColor] = getLineEndpoints(lineIdx, palette);
				const count = lineWords.length;
				lineWords.forEach((word, wordIdx) => {
					const t = count <= 1 ? 0 : wordIdx / (count - 1);
					word.style.color = lerpColor(startColor, endColor, t);
				});
			});
		});
	});
}

export function revertBeelineReading() {
	document.querySelectorAll('.ls-word').forEach((word) => {
		word.style.removeProperty('color');
		if (word.classList.contains('ls-beeline-only') && word.parentNode) {
			word.parentNode.replaceChild(document.createTextNode(word.textContent || ''), word);
		}
	});
}
