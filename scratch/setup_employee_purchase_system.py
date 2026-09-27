import os
import json

ERP_DIR = r"d:\Sharma Industries Erp Software\erp_system"
HR_DIR = os.path.join(ERP_DIR, "06_hr_legal")
SALES_DIR = os.path.join(ERP_DIR, "01_sales_market")
HERMES_SCRATCH = r"d:\Sharma Industries Erp Software\hermes-agent\scratch"

# 1. Update employee_directory.csv with real Telegram employees & Secret PINs
emp_csv_content = """employee_id,full_name,mobile_number,secondary_phone,email,department,designation,joining_date,employment_type,base_salary_inr,salary_payout_day,secret_pin,status
EMP-1001,Ashutosh Sharma,+919810011111,,ashutosh@swatchpaints.com,Executive,Founder & Supreme Administrator (CEO),2024-01-01,PERMANENT,0.00,1st,1111,ACTIVE
EMP-1002,Suresh Kumar Sharma,+918949896211,+919784832210,suresh.sharma@swatchpaints.com,Production & Operations,Factory Operations Manager,2024-02-01,PERMANENT,30000.00,10th,8949,ACTIVE
EMP-1003,Shahrukh Mohammad,+917340090063,,shahrukh.m@swatchpaints.com,Production & QA Lab,Lead Chemist,2024-03-01,PERMANENT,24000.00,2nd,7340,ACTIVE
EMP-1004,On Prakash Saini,+919571412351,,onprakash.s@swatchpaints.com,Production & Operations,Factory Helper,2024-04-01,PERMANENT,12000.00,5th,9571,ACTIVE
EMP-1005,Dr. Ananya Roy,+919810022222,,ananya.roy@swatchpaints.com,Production & QA Lab,Chief Technical Officer,2024-03-15,PERMANENT,120000.00,1st,9948,ACTIVE
EMP-1006,Rohan Mehta,+919810044444,,rohan.mehta@swatchpaints.com,Sales & Market,Regional Sales Manager,2024-04-10,PERMANENT,85000.00,1st,8821,ACTIVE
"""

with open(os.path.join(HR_DIR, "employee_directory.csv"), "w", encoding="utf-8") as f:
    f.write(emp_csv_content)
print("Updated employee_directory.csv with Telegram employee profiles & secret PINs.")

# 2. Create product_base_prices.csv for employee purchase program
base_prices_csv = """product_code,product_name,pack_size,mrp_price_inr,employee_base_price_inr,discount_percent
EM-WE-20L,Weather Shield Exterior Emulsion,20L,4800.00,2800.00,41.67
EM-WE-04L,Weather Shield Exterior Emulsion,4L,1150.00,680.00,40.87
PR-WP-20L,Acrylic Wall Primer (Waterbased),20L,2400.00,1350.00,43.75
WT-TX-25KG,Rustic Texture Finish Bucket,25KG,3200.00,1850.00,42.19
EM-IE-20L,Interior Luxury Emulsion,20L,3900.00,2200.00,43.59
PR-EP-20L,Damp Defense Waterproof Primer,20L,2900.00,1600.00,44.83
"""

with open(os.path.join(HR_DIR, "product_base_prices.csv"), "w", encoding="utf-8") as f:
    f.write(base_prices_csv)

with open(os.path.join(SALES_DIR, "employee_product_base_prices.csv"), "w", encoding="utf-8") as f:
    f.write(base_prices_csv)
print("Created product_base_prices.csv with employee discount base pricing.")

# 3. Create employee_product_orders.csv
emp_orders_csv = """order_id,order_date,employee_id,employee_name,mobile_number,product_code,product_name,quantity,base_price_inr,total_amount_inr,auth_status,salary_deduction_status
EMP-ORD-001,2026-09-27,EMP-1002,Suresh Kumar Sharma,+918949896211,EM-WE-20L,Weather Shield Exterior Emulsion,2,2800.00,5600.00,AUTHENTICATED_PIN,DEDUCTION_SCHEDULED
EMP-ORD-002,2026-09-27,EMP-1003,Shahrukh Mohammad,+917340090063,PR-WP-20L,Acrylic Wall Primer (Waterbased),1,1350.00,1350.00,AUTHENTICATED_PIN,DEDUCTION_SCHEDULED
EMP-ORD-003,2026-09-27,EMP-1004,On Prakash Saini,+919571412351,EM-IE-20L,Interior Luxury Emulsion,1,2200.00,2200.00,AUTHENTICATED_PIN,DEDUCTION_SCHEDULED
"""

with open(os.path.join(HR_DIR, "employee_product_orders.csv"), "w", encoding="utf-8") as f:
    f.write(emp_orders_csv)
print("Created employee_product_orders.csv ledger.")

# 4. Update monthly_attendance_payroll.csv with salary deduction integration
payroll_csv = """record_month,employee_id,employee_name,base_salary_inr,working_days,days_present,gross_salary_inr,employee_purchases_deduction_inr,statutory_pf_esi_tax_inr,net_payable_salary_inr,salary_payout_day,payout_status
2026-09,EMP-1001,Ashutosh Sharma,0.00,26,26.0,0.00,0.00,0.00,0.00,1st,N/A_EQUITY
2026-09,EMP-1002,Suresh Kumar Sharma,30000.00,26,26.0,30000.00,5600.00,1800.00,22600.00,10th,SCHEDULED
2026-09,EMP-1003,Shahrukh Mohammad,24000.00,26,25.0,23076.92,1350.00,1440.00,20286.92,2nd,SCHEDULED
2026-09,EMP-1004,On Prakash Saini,12000.00,26,26.0,12000.00,2200.00,720.00,9080.00,5th,SCHEDULED
2026-09,EMP-1005,Dr. Ananya Roy,120000.00,26,26.0,120000.00,0.00,12000.00,108000.00,1st,SCHEDULED
2026-09,EMP-1006,Rohan Mehta,85000.00,26,25.0,81730.77,0.00,8500.00,73230.77,1st,SCHEDULED
"""

with open(os.path.join(HR_DIR, "monthly_attendance_payroll.csv"), "w", encoding="utf-8") as f:
    f.write(payroll_csv)
print("Updated monthly_attendance_payroll.csv with automated purchase salary deductions.")

# 5. Build Python Employee Order Authentication & Deduction Engine
engine_code = '''import csv
import os
import json
from datetime import datetime

HR_DIR = r"d:\\Sharma Industries Erp Software\\erp_system\\06_hr_legal"

class EmployeePurchaseEngine:
    def __init__(self):
        self.emp_file = os.path.join(HR_DIR, "employee_directory.csv")
        self.base_price_file = os.path.join(HR_DIR, "product_base_prices.csv")
        self.orders_file = os.path.join(HR_DIR, "employee_product_orders.csv")
        self.payroll_file = os.path.join(HR_DIR, "monthly_attendance_payroll.csv")

    def authenticate_employee(self, mobile_number, secret_pin):
        """Authenticates employee mobile number against secret PIN."""
        clean_mobile = mobile_number.replace(" ", "").replace("-", "")
        if not clean_mobile.startswith("+91"):
            clean_mobile = "+91" + clean_mobile.lstrip("0")
            
        with open(self.emp_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                p1 = row["mobile_number"].replace(" ", "").replace("-", "")
                p2 = row.get("secondary_phone", "").replace(" ", "").replace("-", "")
                if clean_mobile in [p1, p2]:
                    if str(secret_pin).strip() == str(row["secret_pin"]).strip():
                        return True, row
                    else:
                        return False, f"Invalid secret PIN for employee {row['full_name']}."
        return False, f"Mobile number {mobile_number} not found in Employee Directory."

    def get_product_base_price(self, product_code):
        """Retrieves base price for a product."""
        with open(self.base_price_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["product_code"].upper() == product_code.upper():
                    return float(row["employee_base_price_inr"]), row["product_name"]
        return None, None

    def process_order(self, mobile_number, secret_pin, product_code, quantity):
        """Processes order, calculates base total, logs order, and deducts from payroll."""
        is_auth, emp_or_err = self.authenticate_employee(mobile_number, secret_pin)
        if not is_auth:
            return {"success": False, "message": f"Authentication Failed: {emp_or_err}"}

        emp = emp_or_err
        base_price, product_name = self.get_product_base_price(product_code)
        if not base_price:
            return {"success": False, "message": f"Invalid product code: {product_code}"}

        total_amount = base_price * int(quantity)
        order_id = f"EMP-ORD-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        today_date = datetime.now().strftime("%Y-%m-%d")

        # 1. Append order to employee_product_orders.csv
        order_row = {
            "order_id": order_id,
            "order_date": today_date,
            "employee_id": emp["employee_id"],
            "employee_name": emp["full_name"],
            "mobile_number": mobile_number,
            "product_code": product_code,
            "product_name": product_name,
            "quantity": quantity,
            "base_price_inr": f"{base_price:.2f}",
            "total_amount_inr": f"{total_amount:.2f}",
            "auth_status": "AUTHENTICATED_PIN",
            "salary_deduction_status": "DEDUCTION_SCHEDULED"
        }

        file_exists = os.path.exists(self.orders_file)
        with open(self.orders_file, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(order_row.keys()))
            if not file_exists:
                writer.writeheader()
            writer.writerow(order_row)

        # 2. Update monthly_attendance_payroll.csv to deduct amount
        updated_rows = []
        with open(self.payroll_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            fieldnames = reader.fieldnames
            for row in reader:
                if row["employee_id"] == emp["employee_id"]:
                    current_ded = float(row.get("employee_purchases_deduction_inr", 0.0))
                    new_ded = current_ded + total_amount
                    row["employee_purchases_deduction_inr"] = f"{new_ded:.2f}"
                    
                    gross = float(row["gross_salary_inr"])
                    statutory = float(row.get("statutory_pf_esi_tax_inr", 0.0))
                    net = gross - new_ded - statutory
                    row["net_payable_salary_inr"] = f"{net:.2f}"
                    
                updated_rows.append(row)

        with open(self.payroll_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(updated_rows)

        return {
            "success": True,
            "order_id": order_id,
            "employee_name": emp["full_name"],
            "product_name": product_name,
            "quantity": quantity,
            "unit_base_price": base_price,
            "total_amount_deducted": total_amount,
            "message": f"Order confirmed! ₹{total_amount:.2f} deducted from next salary cycle (Payout Day: {emp.get('salary_payout_day', '1st')})."
        }

if __name__ == "__main__":
    engine = EmployeePurchaseEngine()
    print("Testing Employee Purchase Authentication & Salary Deduction Engine:")
    # Test order for Suresh Kumar Sharma (+918949896211, PIN: 8949)
    res = engine.process_order("+918949896211", "8949", "EM-WE-20L", 1)
    print(json.dumps(res, indent=2))
'''

with open(os.path.join(HR_DIR, "employee_purchase_engine.py"), "w", encoding="utf-8") as f:
    f.write(engine_code)

with open(os.path.join(HERMES_SCRATCH, "employee_purchase_engine.py"), "w", encoding="utf-8") as f:
    f.write(engine_code)

print("Created Employee Purchase Engine script in HR folder and hermes scratch.")
