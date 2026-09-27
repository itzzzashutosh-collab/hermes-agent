import sqlite3
import os
import sys

# Force stdout to UTF-8
sys.stdout.reconfigure(encoding='utf-8')

db_path = r"C:\Users\itzzz\AppData\Local\hermes\state.db"
if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Query delivery obligations & messages
    try:
        cursor.execute("SELECT * FROM delivery_obligations ORDER BY rowid DESC LIMIT 10;")
        rows = cursor.fetchall()
        print("\n=== DELIVERY OBLIGATIONS ===")
        for r in rows:
            print(r)
    except Exception as e:
        print("Error reading delivery_obligations:", e)
        
    try:
        cursor.execute("SELECT * FROM messages ORDER BY rowid DESC LIMIT 10;")
        rows = cursor.fetchall()
        print("\n=== MESSAGES ===")
        for r in rows:
            print(r)
    except Exception as e:
        print("Error reading messages:", e)

log_path = r"C:\Users\itzzz\AppData\Local\hermes\logs\agent.log"
if os.path.exists(log_path):
    print("\n=== AGENT LOG (LAST 50 LINES) ===")
    with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()
        for line in lines[-50:]:
            print(line.strip())
