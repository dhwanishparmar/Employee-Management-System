import sqlite3

def connect_db():
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        department TEXT,
        salary INTEGER
    )
    """)

    conn.commit()
    return conn, cursor