import csv
import os
import json
from datetime import datetime

HR_DIR = r"d:\Sharma Industries Erp Software\erp_system\06_hr_legal"

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
