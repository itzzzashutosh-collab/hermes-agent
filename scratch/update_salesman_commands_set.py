import os
import json
import csv

SALES_DIR = r"d:\Sharma Industries Erp Software\erp_system\01_sales_market"

print("Updating Salesman Commands Set: Dealer Programs & Structured Offers...")

# 1. Create dealer_programs_master.csv
programs_csv = """program_code,program_name,target_category,benefits,min_annual_commitment_inr,status
PROG-GOLD-CLUB,Swatch Gold Club Stockist,A_B,Free LED Glow Signboard + Priority Dispatch + Extra 2% Rebate,2500000.00,ACTIVE
PROG-PAINTER-HUB,Painter Loyalty Hub,ALL,Painter Cashback Scanning Kit + T-Shirt Kits + Monthly Meet Budget,1000000.00,ACTIVE
PROG-TEXTURE-EXPERT,Wall Texture Studio Partner,ALL,Texture Display Stand + Sample Bucket Kits + Applicator Training,500000.00,ACTIVE
PROG-MONSOON-WARRIOR,Monsoon Waterproofing Growth League,A_B,Direct Factory Price Support + Waterproofing Warranty Certs,1500000.00,ACTIVE
"""

with open(os.path.join(SALES_DIR, "dealer_programs_master.csv"), "w", encoding="utf-8") as f:
    f.write(programs_csv)
print("Created dealer_programs_master.csv.")

# 2. Create dealer_program_enrollments.csv header
enroll_header = """enrollment_id,enrollment_date,dealer_id,dealer_name,program_code,program_name,salesman_id,salesman_name,status
"""
with open(os.path.join(SALES_DIR, "dealer_program_enrollments.csv"), "w", encoding="utf-8") as f:
    f.write(enroll_header)
print("Created dealer_program_enrollments.csv header.")
