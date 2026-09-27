import os
import json
import csv

ERP_DIR = r"d:\Sharma Industries Erp Software\erp_system"
HR_DIR = os.path.join(ERP_DIR, "06_hr_legal")
SALES_DIR = os.path.join(ERP_DIR, "01_sales_market")

print("Updating real products catalog across HR and Sales departments...")

# 1. Update 06_hr_legal/product_base_prices.csv (Internal Base Prices for Employee Purchases)
hr_base_prices_csv = """product_code,product_name,pack_size,mrp_price_inr,employee_base_price_inr,dealer_price_inr,consumer_price_inr
SWP-RUSTIC-25KG,Swatch Rustic Texture Paints,25KG Bag,1150.00,450.00,690.00,950.00
SWP-WG-20L,Swatch Weatherguard Exterior Emulsion,20L Bucket,4100.00,2100.00,2600.00,3200.00
SWP-WG-10L,Swatch Weatherguard Exterior Emulsion,10L Bucket,2400.00,1150.00,1450.00,1800.00
SWP-WG-04L,Swatch Weatherguard Exterior Emulsion,4L Bucket,1450.00,520.00,700.00,900.00
SWP-WG-01L,Swatch Weatherguard Exterior Emulsion,1L Pack,250.00,100.00,150.00,200.00
SWP-SE-20L,Swatch Shine Interior Emulsion,20L Bucket,4100.00,2000.00,2450.00,3050.00
SWP-SE-10L,Swatch Shine Interior Emulsion,10L Bucket,2300.00,1150.00,1450.00,1800.00
SWP-SE-04L,Swatch Shine Interior Emulsion,4L Bucket,1400.00,520.00,700.00,900.00
SWP-SE-01L,Swatch Shine Interior Emulsion,1L Pack,230.00,90.00,140.00,180.00
SWP-RC-25KG,Swatch Roller Coat Texture,25KG Packing,1150.00,550.00,850.00,950.00
SWP-TC-01L,Swatch Clear Top Coat Sealer,1L Bottle,500.00,250.00,280.00,400.00
SWP-TC-05L,Swatch Clear Top Coat Sealer,5L Jerry Can,2500.00,1100.00,1400.00,2000.00
SWP-WP-01L,Swatch Waterproofing Solution Membrane,1L Bottle,380.00,180.00,250.00,350.00
SWP-WP-05L,Swatch Waterproofing Solution Membrane,5L Jerry Can,1800.00,800.00,1100.00,1500.00
"""

with open(os.path.join(HR_DIR, "product_base_prices.csv"), "w", encoding="utf-8") as f:
    f.write(hr_base_prices_csv)
print("Updated 06_hr_legal/product_base_prices.csv with official Swatch Paints product lineup.")

# 2. Update 01_sales_market/products_master.csv (Public & Dealer Products Catalog - NO Base Price)
sales_products_csv = """product_code,product_name,pack_size,mrp_price_inr,dealer_price_inr,consumer_price_inr,unit_of_measure,hsn_code,status
SWP-RUSTIC-25KG,Swatch Rustic Texture Paints,25KG Bag,1150.00,690.00,950.00,25KG Bag,3214,ACTIVE
SWP-WG-20L,Swatch Weatherguard Exterior Emulsion,20L Bucket,4100.00,2600.00,3200.00,20L Bucket,3209,ACTIVE
SWP-WG-10L,Swatch Weatherguard Exterior Emulsion,10L Bucket,2400.00,1450.00,1800.00,10L Bucket,3209,ACTIVE
SWP-WG-04L,Swatch Weatherguard Exterior Emulsion,4L Bucket,1450.00,700.00,900.00,4L Bucket,3209,ACTIVE
SWP-WG-01L,Swatch Weatherguard Exterior Emulsion,1L Pack,250.00,150.00,200.00,1L Pack,3209,ACTIVE
SWP-SE-20L,Swatch Shine Interior Emulsion,20L Bucket,4100.00,2450.00,3050.00,20L Bucket,3209,ACTIVE
SWP-SE-10L,Swatch Shine Interior Emulsion,10L Bucket,2300.00,1450.00,1800.00,10L Bucket,3209,ACTIVE
SWP-SE-04L,Swatch Shine Interior Emulsion,4L Bucket,1400.00,700.00,900.00,4L Bucket,3209,ACTIVE
SWP-SE-01L,Swatch Shine Interior Emulsion,1L Pack,230.00,140.00,180.00,1L Pack,3209,ACTIVE
SWP-RC-25KG,Swatch Roller Coat Texture,25KG Packing,1150.00,850.00,950.00,25KG Packing,3214,ACTIVE
SWP-TC-01L,Swatch Clear Top Coat Sealer,1L Bottle,500.00,280.00,400.00,1L Bottle,3209,ACTIVE
SWP-TC-05L,Swatch Clear Top Coat Sealer,5L Jerry Can,2500.00,1400.00,2000.00,5L Jerry Can,3209,ACTIVE
SWP-WP-01L,Swatch Waterproofing Solution Membrane,1L Bottle,380.00,250.00,350.00,1L Bottle,3209,ACTIVE
SWP-WP-05L,Swatch Waterproofing Solution Membrane,5L Jerry Can,1800.00,1100.00,1500.00,5L Jerry Can,3209,ACTIVE
"""

with open(os.path.join(SALES_DIR, "products_master.csv"), "w", encoding="utf-8") as f:
    f.write(sales_products_csv)
print("Updated 01_sales_market/products_master.csv with official Swatch Paints product lineup.")
