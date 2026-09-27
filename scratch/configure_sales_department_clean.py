import os
import json
import csv

SALES_DIR = r"d:\Sharma Industries Erp Software\erp_system\01_sales_market"

print("Configuring 01_sales_market folder, removing base prices and fake data...")

# 1. Remove employee_product_base_prices.csv from 01_sales_market
base_price_file = os.path.join(SALES_DIR, "employee_product_base_prices.csv")
if os.path.exists(base_price_file):
    os.remove(base_price_file)
    print("Removed employee_product_base_prices.csv from 01_sales_market.")

# 2. Create products_master.csv (Standard Product Catalog with MRP and Dealer Price)
products_master_csv = """product_code,product_name,pack_size,mrp_price_inr,dealer_price_inr,unit_of_measure,hsn_code,status
EM-WE-20L,Weather Shield Exterior Emulsion,20L,4800.00,3850.00,20L Bucket,3209,ACTIVE
EM-WE-04L,Weather Shield Exterior Emulsion,4L,1150.00,920.00,4L Can,3209,ACTIVE
PR-WP-20L,Acrylic Wall Primer Waterbased,20L,2400.00,1920.00,20L Bucket,3209,ACTIVE
WT-TX-25KG,Rustic Wall Texture Finish Bucket,25KG,3200.00,2560.00,25KG Bucket,3214,ACTIVE
EM-IE-20L,Interior Luxury Emulsion,20L,3900.00,3120.00,20L Bucket,3209,ACTIVE
PR-EP-20L,Damp Defense Waterproof Primer,20L,2900.00,2320.00,20L Bucket,3209,ACTIVE
"""

with open(os.path.join(SALES_DIR, "products_master.csv"), "w", encoding="utf-8") as f:
    f.write(products_master_csv)
print("Created products_master.csv with MRP and Dealer Prices.")

# 3. Clean monthly_sales_targets.csv (No fake names)
targets_csv = """month,sales_exec_id,sales_exec_name,territory,target_revenue_inr,target_volume_ltrs,actual_revenue_inr,achievement_percent
2026-09,SALES-REG-01,Rajasthan Regional Territory,Rajasthan,5000000.00,30000.00,0.00,0.0
2026-09,SALES-REG-02,UP & Delhi NCR Territory,UP & Delhi NCR,6000000.00,40000.00,0.00,0.0
"""

with open(os.path.join(SALES_DIR, "monthly_sales_targets.csv"), "w", encoding="utf-8") as f:
    f.write(targets_csv)
print("Updated monthly_sales_targets.csv with territory accounts.")

# 4. Clean dealer_master.csv header
dealer_header = """dealer_id,dealer_name,firm_name,gstin,phone,address,city,state,credit_limit_inr,payment_terms_days,dealer_category,status
"""
with open(os.path.join(SALES_DIR, "dealer_master.csv"), "w", encoding="utf-8") as f:
    f.write(dealer_header)

# 5. Clean sales_orders_log.csv header
orders_header = """order_id,order_date,dealer_id,dealer_name,product_code,product_name,quantity_ltrs,unit_price_inr,total_value_inr,dispatch_status,payment_status
"""
with open(os.path.join(SALES_DIR, "sales_orders_log.csv"), "w", encoding="utf-8") as f:
    f.write(orders_header)

print("Sales department files cleanly reconfigured!")
