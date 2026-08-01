import sqlite3

conn = sqlite3.connect(
    "pillvision.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS history(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT,
    title TEXT,
    content TEXT,
    time TEXT
)
""")

conn.commit()
