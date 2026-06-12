# Spendly — Expense Tracker

A personal finance tracking web application built with **Flask**. This repository is a teaching scaffold: the landing, login, and register pages are fully built, while the core expense-tracking features are left as guided student exercises.

> *Track every rupee. Own your finances.*

---

## Tech Stack

| Layer    | Technology                  |
|----------|-----------------------------|
| Backend  | Flask 3.1.3 (Python)        |
| WSGI     | Werkzeug 3.1.6              |
| Database | SQLite (`expense_tracker.db`) |
| Testing  | pytest 8.3.5, pytest-flask 1.3.0 |
| Frontend | Jinja2 templates, vanilla CSS & JS |
| Fonts    | DM Serif Display, DM Sans (Google Fonts) |

---

## Project Structure

```
expense-tracker/
├── app.py                  # Flask app + route definitions
├── requirements.txt        # Python dependencies
├── .gitignore
├── database/
│   ├── __init__.py
│   └── db.py               # DB helpers (to be implemented — Step 1)
├── static/
│   ├── css/style.css       # Styling
│   └── js/main.js          # Client-side JS
└── templates/
    ├── base.html           # Shared layout (navbar, footer)
    ├── landing.html        # Marketing landing page
    ├── login.html          # Sign-in page
    └── register.html       # Registration page
```

---

## Routes

### Implemented

| Method | Path         | View       | Description              |
|--------|--------------|------------|--------------------------|
| GET    | `/`          | `landing`  | Marketing landing page   |
| GET    | `/register`  | `register` | Registration form        |
| GET    | `/login`     | `login`    | Sign-in form             |

### Placeholder (to be implemented by students)

| Method | Path                      | View             | Planned Step |
|--------|---------------------------|------------------|--------------|
| GET    | `/logout`                 | `logout`         | Step 3       |
| GET    | `/profile`                | `profile`        | Step 4       |
| GET    | `/expenses/add`           | `add_expense`    | Step 7       |
| GET    | `/expenses/<int:id>/edit` | `edit_expense`   | Step 8       |
| GET    | `/expenses/<int:id>/delete` | `delete_expense` | Step 9    |

---

## Database Layer (`database/db.py`)

Currently a stub. It is expected to provide:

- **`get_db()`** — returns a SQLite connection with `row_factory` set and foreign keys enabled.
- **`init_db()`** — creates all tables using `CREATE TABLE IF NOT EXISTS`.
- **`seed_db()`** — inserts sample data for development.

---

## Getting Started

```bash
# 1. Create & activate a virtual environment
python -m venv venv
venv\Scripts\activate          # Windows (PowerShell)
# source venv/bin/activate     # macOS / Linux

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the development server
python app.py
```

The app runs in debug mode on **http://localhost:5001**.

---

## Notes

- The UI brand name is **Spendly**; the navbar and footer live in `templates/base.html`, which all pages extend.
- Currency is rendered in Indian Rupees (₹) throughout the mockups.
- `expense_tracker.db`, `venv/`, and `__pycache__/` are git-ignored.

---

*Generated on 2026-06-09.*