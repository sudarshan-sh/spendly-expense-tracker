# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Spendly — a personal expense tracker built with Flask. This is a **teaching scaffold**: the marketing/auth-facing pages (landing, login, register, terms, privacy) are fully built, while the core expense-tracking features are intentionally left as guided student exercises. Treat the placeholders accordingly — don't "finish" them unless explicitly asked.

## Commands

```bash
# Activate the venv (already present in repo)
venv\Scripts\activate              # Windows PowerShell
# source venv/bin/activate         # macOS / Linux

pip install -r requirements.txt    # install deps

python app.py                      # run dev server -> http://localhost:5001 (debug, port 5001)

pytest                             # run all tests
pytest path/to/test_file.py::test_name   # run a single test
```

Note: the server runs on **port 5001**, not Flask's default 5000.

## Architecture

- **`app.py`** — the entire Flask app: app instance + all route definitions in one file. Routes split into two groups:
  - *Implemented* (render real templates): `/`, `/register`, `/login`, `/terms`, `/privacy`.
  - *Placeholder* (return `"... — coming in Step N"` strings): `/logout`, `/profile`, `/expenses/add`, `/expenses/<id>/edit`, `/expenses/<id>/delete`. These are deliberate stubs awaiting student implementation.

- **`database/db.py`** — currently a **stub with only comments**. It is the intended Step 1 exercise and should expose `get_db()` (SQLite connection with `row_factory` + foreign keys enabled), `init_db()` (`CREATE TABLE IF NOT EXISTS`), and `seed_db()`. The DB file is `expense_tracker.db` (git-ignored, created at runtime).

- **`templates/`** — Jinja2. `base.html` defines the shared shell (navbar + footer + font/CSS includes) and exposes `title`, `head`, `content`, `scripts` blocks; every page extends it. Use `url_for('static', ...)` and `url_for('<view>')` for asset/route references, matching existing templates.

- **`static/css/style.css`** and **`static/js/main.js`** — single global stylesheet and script, vanilla CSS/JS (no build step, no framework).

## Conventions

- Brand name in UI is **Spendly**; brand mark is the `◈` glyph. Currency is Indian Rupees (₹) throughout.
- Fonts are DM Serif Display + DM Sans, loaded from Google Fonts in `base.html`.
- No build tooling — edit templates/CSS/JS directly and refresh.
