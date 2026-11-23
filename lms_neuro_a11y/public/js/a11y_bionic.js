/**
 * Safe TreeWalker-based Bionic Reading transformer for lesson content.
 * Skips code blocks, links, scripts, styles, and already-transformed nodes.
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

function getFixationLength(word) {
	const len = word.length;
	if (len <= 1) return 0;
	if (len <= 3) return 1;
	if (len <= 6) return Math.ceil(len * 0.45);
	return Math.ceil(len * 0.4);
}

function shouldSkipNode(node) {
	let parent = node.parentElement;
	while (parent) {
		if (SKIP_TAGS.has(parent.tagName)) return true;
		if (parent.classList && parent.classList.contains('ls-bionic-wrapper')) return true;
		if (parent.isContentEditable) return true;
		parent = parent.parentElement;
	}
	return false;
}

export function applyBionicReading(rootSelector = '.ProseMirror, .lms-lesson-content') {
	const containers = document.querySelectorAll(rootSelector);
	containers.forEach((container) => {
		const walker = document.createTreeWalker(container, NodeFilter.SHOW_TEXT, {
			acceptNode(node) {
				if (!node.nodeValue || !node.nodeValue.trim()) return NodeFilter.FILTER_REJECT;
				if (shouldSkipNode(node)) return NodeFilter.FILTER_REJECT;
				return NodeFilter.FILTER_ACCEPT;
			},
		});

		const textNodes = [];
		let current;
		while ((current = walker.nextNode())) {
			textNodes.push(current);
		}

		textNodes.forEach((textNode) => {
			const text = textNode.nodeValue;
			const parts = text.split(/(\s+)/);
			const wrapper = document.createElement('span');
			wrapper.className = 'ls-bionic-wrapper';
			wrapper.setAttribute('data-original-text', text);

			parts.forEach((part) => {
				if (!part || /^\s+$/.test(part)) {
					wrapper.appendChild(document.createTextNode(part));
					return;
				}
				const fixLen = getFixationLength(part);
				if (fixLen <= 0) {
					wrapper.appendChild(document.createTextNode(part));
					return;
				}
				const bold = document.createElement('strong');
				bold.className = 'ls-bionic-fixation';
				bold.textContent = part.slice(0, fixLen);
				wrapper.appendChild(bold);
				wrapper.appendChild(document.createTextNode(part.slice(fixLen)));
			});

			if (textNode.parentNode) {
				textNode.parentNode.replaceChild(wrapper, textNode);
			}
		});
	});
}

export function revertBionicReading() {
	document.querySelectorAll('.ls-bionic-wrapper').forEach((wrapper) => {
		const original = wrapper.getAttribute('data-original-text') || wrapper.textContent || '';
		const textNode = document.createTextNode(original);
		if (wrapper.parentNode) {
			wrapper.parentNode.replaceChild(textNode, wrapper);
		}
	});
}
