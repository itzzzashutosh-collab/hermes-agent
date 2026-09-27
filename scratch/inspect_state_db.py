import sqlite3
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

db_path = r"C:\Users\itzzz\AppData\Local\hermes\state.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = [t[0] for t in cursor.fetchall()]

for t in tables:
    try:
        cursor.execute(f"PRAGMA table_info({t});")
        cols = [c[1] for c in cursor.fetchall()]
        print(f"Table {t} columns:", cols)
        
        cursor.execute(f"SELECT * FROM {t} ORDER BY rowid DESC LIMIT 5;")
        rows = cursor.fetchall()
        for r in rows:
            print(f"  {r}")
    except Exception as e:
        print(f"Error reading {t}: {e}")
