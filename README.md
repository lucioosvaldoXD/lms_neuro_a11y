# LMS Neuro A11y (LogiSentinel Edition)

Custom Frappe application that extends `frappe/lms` **without modifying core `apps/lms/` or `apps/frappe/` files**.

## Features
- **LogiSentinel Branding**: Applies LogiSentinel brand identity, logos, and color palette (`#070B13`, `#0C111D`, `#7C5CFF`, `#10B981`).
- **DocType `LMS Accessibility Profile`**: 1-to-1 user cognitive & reading accessibility preferences.
- **Custom Field `tldr_summary` on `Course Lesson`**: 3-bullet executive summary rendered in Focus / TL;DR-first mode.
- **45-Second Cognitive Calibration Modal**: 4-step non-clinical onboarding on `/lms`.
- **Quick-Switch Drawer + FOUC-free CSS Engine**: Instant `localStorage` + `data-a11y-*` attributes + background RPC sync.
- **Bionic Reading (`TreeWalker`)**, **Reading Ruler**, **Dyslexia Mode** (Atkinson Hyperlegible / OpenDyslexic + `#FAF8F5` + `1.8` line-height), **Reduced Motion**, and **Pomodoro Widget** (`15/3` & `25/5`).

## Installation (after bench setup)
```bash
bench get-app /path/to/lms_neuro_a11y
bench --site your-site.localhost install-app lms_neuro_a11y
bench --site your-site.localhost migrate
```
