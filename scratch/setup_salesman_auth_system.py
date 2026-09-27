import os
import csv
import json
import random

SALES_DIR = r"d:\Sharma Industries Erp Software\erp_system\01_sales_market"
SALESMEN_FILE = os.path.join(SALES_DIR, "salesmen_directory.csv")
SESSIONS_FILE = os.path.join(SALES_DIR, "salesman_sessions.json")

print("Setting up Salesmen Directory & 6-Digit PIN Authentication System...")

# 1. Create salesmen_directory.csv with test salesmen + Ashutosh Sharma Admin
salesmen_csv = """salesman_id,full_name,mobile_number,secret_pin_6digit,territory,role,status
SALES-0001,Ashutosh Sharma,+919810011111,111111,Pan-India Corporate,SUPER_ADMIN,ACTIVE
SALES-0002,Suresh Kumar Sharma,+918949896211,894921,Rajasthan West,SALES_EXECUTIVE,ACTIVE
SALES-0003,Vikram Singh,+919829012345,654321,Jaipur Metro,SALES_EXECUTIVE,ACTIVE
SALES-0004,Rakesh Sharma,+919810054321,123456,Delhi NCR Beat,SALES_EXECUTIVE,ACTIVE
"""

with open(SALESMEN_FILE, "w", encoding="utf-8") as f:
    f.write(salesmen_csv)
print("Created salesmen_directory.csv with 6-digit secret PINs.")

# 2. Create default salesman_sessions.json
default_sessions = {
    "1661525228": {
        "salesman_id": "SALES-0001",
        "full_name": "Ashutosh Sharma",
        "mobile_number": "+919810011111",
        "role": "SUPER_ADMIN",
        "authenticated": True,
        "login_time": "2026-09-27 12:15:00"
    }
}

with open(SESSIONS_FILE, "w", encoding="utf-8") as f:
    json.dump(default_sessions, f, indent=4)
print("Initialized salesman_sessions.json with admin session.")

print("Salesman authentication setup complete!")
