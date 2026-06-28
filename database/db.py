"""Database helpers for Spendly.

Exposes:
  get_db()   — a SQLite connection with row_factory and foreign keys enabled
  init_db()  — creates all tables using CREATE TABLE IF NOT EXISTS
  seed_db()  — inserts sample data for development
"""

import os
import sqlite3

# Store the database file at the project root (one level up from this package).
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "expense_tracker.db")


def get_db():
    """Return a SQLite connection with dict-like rows and foreign keys on."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    """Create all tables if they do not already exist."""
    conn = get_db()
    try:
        conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS users (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                name       TEXT    NOT NULL,
                email      TEXT    NOT NULL UNIQUE,
                password   TEXT    NOT NULL,
                created_at TEXT    NOT NULL DEFAULT (datetime('now'))
            );

            CREATE TABLE IF NOT EXISTS expenses (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id     INTEGER NOT NULL,
                amount      REAL    NOT NULL,
                category    TEXT    NOT NULL,
                description TEXT,
                spent_on    TEXT    NOT NULL DEFAULT (date('now')),
                created_at  TEXT    NOT NULL DEFAULT (datetime('now')),
                FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
            );
            """
        )
        conn.commit()
    finally:
        conn.close()


def seed_db():
    """Insert sample data for development. Safe to run repeatedly."""
    conn = get_db()
    try:
        # Skip seeding if data already exists.
        existing = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
        if existing:
            return

        cur = conn.execute(
            "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
            ("Nitish Kumar", "nitish@example.com", "password123"),
        )
        user_id = cur.lastrowid

        sample_expenses = [
            (user_id, 450.0, "Food", "Lunch at cafe", "2026-06-01"),
            (user_id, 1200.0, "Transport", "Monthly metro pass", "2026-06-02"),
            (user_id, 2999.0, "Shopping", "Running shoes", "2026-06-05"),
            (user_id, 199.0, "Entertainment", "Movie ticket", "2026-06-10"),
            (user_id, 850.0, "Utilities", "Electricity bill", "2026-06-15"),
        ]
        conn.executemany(
            "INSERT INTO expenses (user_id, amount, category, description, spent_on) "
            "VALUES (?, ?, ?, ?, ?)",
            sample_expenses,
        )
        conn.commit()
    finally:
        conn.close()


if __name__ == "__main__":
    init_db()
    seed_db()
    print(f"Initialized and seeded {DB_PATH}")
