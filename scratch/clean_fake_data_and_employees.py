import os
import csv
import json

ERP_DIR = r"d:\Sharma Industries Erp Software\erp_system"
HR_DIR = os.path.join(ERP_DIR, "06_hr_legal")
SALES_DIR = os.path.join(ERP_DIR, "01_sales_market")
PROD_DIR = os.path.join(ERP_DIR, "02_production_lab")
FIN_DIR = os.path.join(ERP_DIR, "03_finance_gst")
SCM_DIR = os.path.join(ERP_DIR, "04_supply_chain")
MKT_DIR = os.path.join(ERP_DIR, "05_marketing_brand")
VIS_DIR = os.path.join(ERP_DIR, "07_vision_growth")
SYS_DIR = os.path.join(ERP_DIR, "08_systems_sops")

print("Cleaning all fake data and removing Dr. Ananya Roy & Rohan Mehta...")

# 1. 06_hr_legal/employee_directory.csv (Only 4 real employees)
real_emp_csv = """employee_id,full_name,mobile_number,secondary_phone,email,department,designation,joining_date,employment_type,base_salary_inr,salary_payout_day,secret_pin,status
EMP-1001,Ashutosh Sharma,+919810011111,,ashutosh@swatchpaints.com,Executive,Founder & Supreme Administrator (CEO),2024-01-01,PERMANENT,0.00,1st,1111,ACTIVE
EMP-1002,Suresh Kumar Sharma,+918949896211,+919784832210,suresh.sharma@swatchpaints.com,Production & Operations,Factory Operations Manager,2024-02-01,PERMANENT,30000.00,10th,8949,ACTIVE
EMP-1003,Shahrukh Mohammad,+917340090063,,shahrukh.m@swatchpaints.com,Production & QA Lab,Lead Chemist,2024-03-01,PERMANENT,24000.00,2nd,7340,ACTIVE
EMP-1004,On Prakash Saini,+919571412351,,onprakash.s@swatchpaints.com,Production & Operations,Factory Helper,2024-04-01,PERMANENT,12000.00,5th,9571,ACTIVE
"""

with open(os.path.join(HR_DIR, "employee_directory.csv"), "w", encoding="utf-8") as f:
    f.write(real_emp_csv)

# 2. 06_hr_legal/monthly_attendance_payroll.csv (Only 4 real employees)
real_payroll_csv = """record_month,employee_id,employee_name,base_salary_inr,working_days,days_present,gross_salary_inr,employee_purchases_deduction_inr,statutory_pf_esi_tax_inr,net_payable_salary_inr,salary_payout_day,payout_status
2026-09,EMP-1001,Ashutosh Sharma,0.00,26,26.0,0.00,0.00,0.00,0.00,1st,N/A_EQUITY
2026-09,EMP-1002,Suresh Kumar Sharma,30000.00,26,26.0,30000.00,2800.00,1800.00,25400.00,10th,SCHEDULED
2026-09,EMP-1003,Shahrukh Mohammad,24000.00,26,25.0,23076.92,1350.00,1440.00,20286.92,2nd,SCHEDULED
2026-09,EMP-1004,On Prakash Saini,12000.00,26,26.0,12000.00,2200.00,720.00,9080.00,5th,SCHEDULED
"""

with open(os.path.join(HR_DIR, "monthly_attendance_payroll.csv"), "w", encoding="utf-8") as f:
    f.write(real_payroll_csv)

# 3. 06_hr_legal/employee_product_orders.csv (Clean orders for real employees)
real_orders_csv = """order_id,order_date,employee_id,employee_name,mobile_number,product_code,product_name,quantity,base_price_inr,total_amount_inr,auth_status,salary_deduction_status
EMP-ORD-001,2026-09-27,EMP-1002,Suresh Kumar Sharma,+918949896211,EM-WE-20L,Weather Shield Exterior Emulsion,1,2800.00,2800.00,AUTHENTICATED_PIN,DEDUCTION_SCHEDULED
EMP-ORD-002,2026-09-27,EMP-1003,Shahrukh Mohammad,+917340090063,PR-WP-20L,Acrylic Wall Primer (Waterbased),1,1350.00,1350.00,AUTHENTICATED_PIN,DEDUCTION_SCHEDULED
EMP-ORD-003,2026-09-27,EMP-1004,On Prakash Saini,+919571412351,EM-IE-20L,Interior Luxury Emulsion,1,2200.00,2200.00,AUTHENTICATED_PIN,DEDUCTION_SCHEDULED
"""

with open(os.path.join(HR_DIR, "employee_product_orders.csv"), "w", encoding="utf-8") as f:
    f.write(real_orders_csv)

# 4. 06_hr_legal/leave_applications_log.csv (Real employees only)
real_leave_csv = """leave_id,employee_id,leave_type,start_date,end_date,reason,approval_status
LEV-2026-01,EMP-1003,SICK,2026-09-18,2026-09-18,Lab equipment maintenance leave,APPROVED
"""

with open(os.path.join(HR_DIR, "leave_applications_log.csv"), "w", encoding="utf-8") as f:
    f.write(real_leave_csv)

# 5. 06_hr_legal/legal_statutory_licenses.csv (Suresh Kumar Sharma / Real Manager)
real_lic_csv = """license_id,license_name,issuing_authority,license_number,issue_date,expiry_date,renewal_lead_days,responsible_officer
LIC-01,Factory Operating License,Department of Factories & Boilers,FACT-DL-2024-991,2024-01-01,2026-12-31,60,Suresh Kumar Sharma
LIC-02,Consent to Operate (Water & Air),State Pollution Control Board,PCB-CTO-88210,2024-04-01,2027-03-31,90,Shahrukh Mohammad
LIC-03,GST Registration Certificate,Government of India GSTN,07AAAAA0000A1Z5,2024-01-15,2099-12-31,365,Ashutosh Sharma
"""

with open(os.path.join(HR_DIR, "legal_statutory_licenses.csv"), "w", encoding="utf-8") as f:
    f.write(real_lic_csv)

# 6. 02_production_lab/batch_production_log.csv & qc_inspection_log.csv (Real team: Suresh Kumar Sharma & Shahrukh Mohammad)
real_batch_csv = """batch_id,batch_date,product_name,sku_code,planned_qty_ltrs,actual_yield_ltrs,batch_master,status
BTH-2026-101,2026-09-21,Weather Shield Exterior Emulsion,EM-WE-001,5000.00,4950.00,Suresh Kumar Sharma,RELEASED
BTH-2026-102,2026-09-22,Interior Luxury Emulsion,EM-IE-004,3000.00,2980.00,Suresh Kumar Sharma,RELEASED
BTH-2026-103,2026-09-23,Acrylic Wall Primer (Waterbased),PR-WP-002,10000.00,9920.00,Suresh Kumar Sharma,RELEASED
"""

with open(os.path.join(PROD_DIR, "batch_production_log.csv"), "w", encoding="utf-8") as f:
    f.write(real_batch_csv)

real_qc_csv = """test_id,batch_id,test_date,viscosity_ku,opacity_percent,ph_level,drying_time_mins,qc_status,lab_chemist
QC-2026-501,BTH-2026-101,2026-09-21,105.5,98.6,8.9,25,PASSED,Shahrukh Mohammad
QC-2026-502,BTH-2026-102,2026-09-22,102.0,99.1,9.0,20,PASSED,Shahrukh Mohammad
QC-2026-503,BTH-2026-103,2026-09-23,98.0,97.8,8.7,15,PASSED,Shahrukh Mohammad
"""

with open(os.path.join(PROD_DIR, "qc_inspection_log.csv"), "w", encoding="utf-8") as f:
    f.write(real_qc_csv)

# 7. 02_production_lab/lab_rm_testing.csv
real_rm_test_csv = """sample_id,raw_material_code,supplier_name,batch_no,purity_percent,impurity_pass,qa_manager_signature,test_date
RMS-2026-01,RM-TiO2-01,DuPont Chemicals,DUP-9948,99.5,YES,Shahrukh Mohammad,2026-09-18
RMS-2026-02,RM-ACR-02,Basf India Ltd,BAS-8831,48.2,YES,Shahrukh Mohammad,2026-09-19
"""

with open(os.path.join(PROD_DIR, "lab_rm_testing.csv"), "w", encoding="utf-8") as f:
    f.write(real_rm_test_csv)

# 8. 07_vision_growth/rd_innovation_pipeline.csv (Lead Chemist: Shahrukh Mohammad)
real_rd_csv = """project_code,innovation_title,phase,est_market_size_cr_inr,lead_chemist,commercial_target_date
RD-2026-01,Nano Thermally Reflective Exterior Paint,LAB_TRIAL,500.0,Shahrukh Mohammad,2027-03-31
RD-2026-02,Anti-Viral Scrub Resistant Luxury Emulsion,COMMERCIAL_LAUNCH,800.0,Shahrukh Mohammad,2026-11-15
RD-2026-03,Self-Cleaning Hydrophobic Wall Texture,FIELD_TEST,350.0,Shahrukh Mohammad,2027-01-31
"""

with open(os.path.join(VIS_DIR, "rd_innovation_pipeline.csv"), "w", encoding="utf-8") as f:
    f.write(real_rd_csv)

# 9. 08_systems_sops/erp_user_roles.csv (Real employees only)
real_roles_csv = """user_id,employee_id,username,role,department_access,active_status
USR-01,EMP-1001,ashutosh_admin,SUPER_ADMIN,ALL,ACTIVE
USR-02,EMP-1002,suresh_ops,OPERATIONS_MANAGER,02_production_lab;04_supply_chain,ACTIVE
USR-03,EMP-1003,shahrukh_chemist,LEAD_CHEMIST,02_production_lab,ACTIVE
USR-04,EMP-1004,onprakash_helper,FACTORY_HELPER,02_production_lab,ACTIVE
"""

with open(os.path.join(SYS_DIR, "erp_user_roles.csv"), "w", encoding="utf-8") as f:
    f.write(real_roles_csv)

# 10. Clean out dummy dealer and sales logs to leave clean CSV headers for ERP ingestion
clean_dealers_csv = """dealer_id,dealer_name,firm_name,gstin,phone,address,city,state,credit_limit_inr,payment_terms_days,dealer_category,status
"""
with open(os.path.join(SALES_DIR, "dealer_master.csv"), "w", encoding="utf-8") as f:
    f.write(clean_dealers_csv)

clean_sales_orders_csv = """order_id,order_date,dealer_id,product_code,quantity_ltrs,unit_price_inr,total_value_inr,dispatch_status,payment_status
"""
with open(os.path.join(SALES_DIR, "sales_orders_log.csv"), "w", encoding="utf-8") as f:
    f.write(clean_sales_orders_csv)

clean_painter_csv = """painter_id,painter_name,phone_number,city,preferred_dealer_id,reward_points_accumulated,tier_level
"""
with open(os.path.join(MKT_DIR, "painter_loyalty_members.csv"), "w", encoding="utf-8") as f:
    f.write(clean_painter_csv)

print("Cleaned up all fake data across erp_system successfully!")
