import os
import json

BASE_DIR = r"d:\Sharma Industries Erp Software\erp_system"

departments = {
    "01_sales_market": {
        "title": "Sales & Market Intelligence Department",
        "sop": """# Standard Operating Procedure (SOP) - Sales & Market Intelligence

## 1. Objective & Scope
To drive dealer expansion, trade scheme execution, order processing, and market intelligence gathering across all regional territories for Swatch Paints to capture market dominance.

## 2. Key Responsibilities
- Dealer Onboarding & Credit Verification (GSTIN, Address, Bank Solvency).
- Managing Dealer Trade Schemes (Volume Discounts, Free Litre Offertories).
- Order Ingestion & ERP Fulfillment Tracking.
- Field Sales Representative Target Allocation and Achievement Monitoring.

## 3. Operational Workflow
1. **Dealer Registration**: Sales Representative submits new dealer details into ERP. Credit evaluation is automated based on category (A, B, C).
2. **Order Placement**: Dealers place orders via ERP / WhatsApp Bot / Sales Representative. Order validated against available credit limit.
3. **Trade Schemes Application**: ERP automatically applies active promotional discounts based on SKU volume.
4. **Dispatch Request**: Order pushed to Supply Chain (`04_supply_chain`) upon credit approval.

## 4. Key Performance Indicators (KPIs)
- Monthly Sales Volume Target (Litres) vs Actual.
- Dealer Activation Rate (% Active Dealers ordering monthly).
- Average Order Value (AOV) & Days Sales Outstanding (DSO).
""",
        "schema": {
            "module": "Sales & Market Intelligence",
            "tables": {
                "dealer_master": {
                    "fields": [
                        {"name": "dealer_id", "type": "VARCHAR(20)", "primary_key": True},
                        {"name": "dealer_name", "type": "VARCHAR(100)"},
                        {"name": "firm_name", "type": "VARCHAR(150)"},
                        {"name": "gstin", "type": "VARCHAR(15)"},
                        {"name": "phone", "type": "VARCHAR(15)"},
                        {"name": "address", "type": "TEXT"},
                        {"name": "city", "type": "VARCHAR(50)"},
                        {"name": "state", "type": "VARCHAR(50)"},
                        {"name": "credit_limit_inr", "type": "DECIMAL(12,2)"},
                        {"name": "payment_terms_days", "type": "INT"},
                        {"name": "dealer_category", "type": "VARCHAR(5)"},
                        {"name": "status", "type": "VARCHAR(15)"}
                    ]
                },
                "sales_orders_log": {
                    "fields": [
                        {"name": "order_id", "type": "VARCHAR(20)", "primary_key": True},
                        {"name": "order_date", "type": "DATE"},
                        {"name": "dealer_id", "type": "VARCHAR(20)", "foreign_key": "dealer_master.dealer_id"},
                        {"name": "product_code", "type": "VARCHAR(20)"},
                        {"name": "quantity_ltrs", "type": "DECIMAL(10,2)"},
                        {"name": "unit_price_inr", "type": "DECIMAL(10,2)"},
                        {"name": "total_value_inr", "type": "DECIMAL(12,2)"},
                        {"name": "dispatch_status", "type": "VARCHAR(20)"},
                        {"name": "payment_status", "type": "VARCHAR(20)"}
                    ]
                }
            }
        },
        "csvs": {
            "dealer_master.csv": """dealer_id,dealer_name,firm_name,gstin,phone,address,city,state,credit_limit_inr,payment_terms_days,dealer_category,status
DLR-001,Rajesh Sharma,Sharma Paint House,07AAAAA0000A1Z5,+919810012345,12 Industrial Area Phase 1,New Delhi,Delhi,500000.00,30,A,ACTIVE
DLR-002,Amit Kumar,Kumar Hardware & Paints,08BBBBB1111B2Z6,+919829023456,45 Station Road,Jaipur,Rajasthan,300000.00,21,B,ACTIVE
DLR-003,Sunil Verma,Verma Traders,09CCCCC2222C3Z7,+919839034567,88 GT Road,Kanpur,Uttar Pradesh,750000.00,45,A,ACTIVE
DLR-004,Vikram Patel,Patel Color Mart,24DDDDD3333D4Z8,+919849045678,10 Ring Road,Ahmedabad,Gujarat,400000.00,30,B,ACTIVE
DLR-005,Ramesh Gupta,Gupta Paint Depot,10EEEEE4444E5Z9,+919859056789,5 Main Market,Patna,Bihar,250000.00,15,C,ACTIVE
""",
            "sales_orders_log.csv": """order_id,order_date,dealer_id,product_code,quantity_ltrs,unit_price_inr,total_value_inr,dispatch_status,payment_status
ORD-2026-001,2026-09-20,DLR-001,EM-WE-001,500.00,180.00,90000.00,DISPATCHED,PAID
ORD-2026-002,2026-09-21,DLR-003,PR-WP-002,1000.00,95.00,95000.00,DISPATCHED,PARTIAL
ORD-2026-003,2026-09-22,DLR-002,WT-TX-003,300.00,240.00,72000.00,IN_TRANSIT,PENDING
ORD-2026-004,2026-09-24,DLR-004,EM-IE-004,800.00,150.00,120000.00,PROCESSING,PENDING
ORD-2026-005,2026-09-25,DLR-005,PR-EP-005,400.00,110.00,44000.00,APPROVED,PENDING
""",
            "dealer_schemes_and_offers.csv": """scheme_id,scheme_name,min_order_ltrs,discount_percent,free_litres,start_date,end_date,applicable_category
SCH-2026-Q3,Monsoon Dhamaka Scheme,500,5.0,25,2026-07-01,2026-09-30,ALL
SCH-2026-DIWALI,Festival Gold Target,1000,8.0,100,2026-09-15,2026-11-15,A_B
SCH-2026-TEXTURE,Wall Texture Launch Special,300,10.0,30,2026-09-01,2026-10-31,ALL
""",
            "monthly_sales_targets.csv": """month,sales_exec_id,sales_exec_name,target_revenue_inr,target_volume_ltrs,actual_revenue_inr,achievement_percent
2026-09,EXEC-01,Rohan Mehta,5000000.00,30000.00,4850000.00,97.0
2026-09,EXEC-02,Priya Singh,4000000.00,25000.00,4120000.00,103.0
2026-09,EXEC-03,Sandeep Joshi,6000000.00,40000.00,5700000.00,95.0
"""
        }
    },
    "02_production_lab": {
        "title": "Production & Quality Assurance Lab Department",
        "sop": """# Standard Operating Procedure (SOP) - Production & QA Lab

## 1. Objective & Scope
To ensure zero-defect manufacturing of waterbased emulsions, primers, and wall textures through strict batch dosing, quality control testing, and ERP yield reconciliation.

## 2. Production Steps
1. **Raw Material Pre-Weighing**: Verify raw materials against formulation sheet in ERP.
2. **High-Speed Dispersion (HSD)**: Charge water, biocides, dispersants, TiO2, and extenders. Run HSD at 1400 RPM for 45 minutes until fineness of grind < 25 microns.
3. **Let-Down & Resin Addition**: Lower speed to 400 RPM. Add acrylic emulsion polymer, coalescing solvents, and thickeners.
4. **Lab Testing**: Sample drawn by QC Chemist for Viscosity (KU), Opacity (%), pH, and Sheen.

## 3. QC Testing Standards
- **Viscosity**: 100 - 110 KU (Krebs Units) at 25°C.
- **Opacity / Hiding Power**: Minimum 98% contrast ratio at 120 micron wet film thickness.
- **Drying Time**: Surface dry < 30 mins, Hard dry < 4 hours.
- **pH Level**: 8.5 - 9.5.

## 4. Batch Release Criteria
No batch can be packed or transferred to Finished Goods inventory without a signed QC Clearance Certificate logged in ERP.
""",
        "schema": {
            "module": "Production & QA Lab",
            "tables": {
                "batch_production_log": {
                    "fields": [
                        {"name": "batch_id", "type": "VARCHAR(20)", "primary_key": True},
                        {"name": "batch_date", "type": "DATE"},
                        {"name": "product_name", "type": "VARCHAR(100)"},
                        {"name": "sku_code", "type": "VARCHAR(20)"},
                        {"name": "planned_qty_ltrs", "type": "DECIMAL(10,2)"},
                        {"name": "actual_yield_ltrs", "type": "DECIMAL(10,2)"},
                        {"name": "batch_master", "type": "VARCHAR(50)"},
                        {"name": "status", "type": "VARCHAR(20)"}
                    ]
                },
                "qc_inspection_log": {
                    "fields": [
                        {"name": "test_id", "type": "VARCHAR(20)", "primary_key": True},
                        {"name": "batch_id", "type": "VARCHAR(20)", "foreign_key": "batch_production_log.batch_id"},
                        {"name": "test_date", "type": "DATE"},
                        {"name": "viscosity_ku", "type": "DECIMAL(5,2)"},
                        {"name": "opacity_percent", "type": "DECIMAL(5,2)"},
                        {"name": "ph_level", "type": "DECIMAL(4,2)"},
                        {"name": "drying_time_mins", "type": "INT"},
                        {"name": "qc_status", "type": "VARCHAR(15)"},
                        {"name": "lab_chemist", "type": "VARCHAR(50)"}
                    ]
                }
            }
        },
        "csvs": {
            "batch_production_log.csv": """batch_id,batch_date,product_name,sku_code,planned_qty_ltrs,actual_yield_ltrs,batch_master,status
BTH-2026-101,2026-09-21,Weather Shield Exterior Emulsion,EM-WE-001,5000.00,4950.00,Mahesh Verma,RELEASED
BTH-2026-102,2026-09-22,Interior Luxury Emulsion,EM-IE-004,3000.00,2980.00,Suresh Kumar,RELEASED
BTH-2026-103,2026-09-23,Acrylic Wall Primer (Waterbased),PR-WP-002,10000.00,9920.00,Mahesh Verma,RELEASED
BTH-2026-104,2026-09-24,Rustic Wall Texture Finish,WT-TX-003,4000.00,3960.00,Rakesh Sharma,QA_HOLD
BTH-2026-105,2026-09-25,Damp Defense Waterproof Coating,PR-EP-005,2000.00,1990.00,Suresh Kumar,PROCESSING
""",
            "qc_inspection_log.csv": """test_id,batch_id,test_date,viscosity_ku,opacity_percent,ph_level,drying_time_mins,qc_status,lab_chemist
QC-2026-501,BTH-2026-101,2026-09-21,105.5,98.6,8.9,25,PASSED,Dr. Ananya Roy
QC-2026-502,BTH-2026-102,2026-09-22,102.0,99.1,9.0,20,PASSED,Dr. Ananya Roy
QC-2026-503,BTH-2026-103,2026-09-23,98.0,97.8,8.7,15,PASSED,Vikram Lab Chemist
QC-2026-504,BTH-2026-104,2026-09-24,118.0,96.5,8.2,45,REJECTED,Dr. Ananya Roy
QC-2026-505,BTH-2026-105,2026-09-25,108.0,98.9,9.1,30,PASSED,Vikram Lab Chemist
""",
            "paint_formulation_master.csv": """formulation_code,product_name,base_resin_percent,titanium_dioxide_percent,calcium_carbonate_percent,water_solvent_percent,additives_percent,target_density_g_ml
FRM-EM-01,Weather Shield Exterior Emulsion,32.0,18.0,25.0,21.0,4.0,1.38
FRM-PR-02,Acrylic Wall Primer,22.0,10.0,35.0,30.0,3.0,1.42
FRM-WT-03,Rustic Wall Texture,18.0,5.0,55.0,18.0,4.0,1.65
FRM-EM-04,Interior Luxury Emulsion,28.0,20.0,22.0,25.0,5.0,1.34
""",
            "lab_rm_testing.csv": """sample_id,raw_material_code,supplier_name,batch_no,purity_percent,impurity_pass,qa_manager_signature,test_date
RMS-2026-01,RM-TiO2-01,DuPont Chemicals,DUP-9948,99.5,YES,Dr. Ananya Roy,2026-09-18
RMS-2026-02,RM-ACR-02,Basf India Ltd,BAS-8831,48.2,YES,Dr. Ananya Roy,2026-09-19
RMS-2026-03,RM-CAL-03,Deccan Minerals,DEC-1102,96.8,YES,Vikram Lab Chemist,2026-09-20
"""
        }
    },
    "03_finance_gst": {
        "title": "Finance, Accounting & GST Compliance Department",
        "sop": """# Standard Operating Procedure (SOP) - Finance & GST Compliance

## 1. Objective & Scope
To manage corporate accounting, GST e-invoicing, e-way bills, vendor payouts, customer credit ledger control, and financial reporting for Swatch Paints.

## 2. Invoicing & GST Protocols
1. **GST E-Invoicing**: Every order dispatched must automatically generate an IRN (Invoice Reference Number) via GST Portal integration.
2. **E-Way Bill Generation**: Required for all inter-state and intra-state shipments exceeding INR 50,000 value.
3. **HSN Codes**:
   - 3209: Waterbased Paints & Varnishes (18% GST).
   - 3214: Wall Putty & Fillers (18% GST).

## 3. Credit & Collections SOP
- Outstanding payments > 45 days automatically trigger credit hold on dealer accounts in ERP.
- Weekly aging reports reviewed by CFO and Head of Sales.

## 4. Statutory Audit & Filing Timelines
- GST Return (GSTR-1 & GSTR-3B): Filed by 11th and 20th of every month.
- TDS Remittance: 7th of every month.
""",
        "schema": {
            "module": "Finance & GST Compliance",
            "tables": {
                "chart_of_accounts": {
                    "fields": [
                        {"name": "account_code", "type": "VARCHAR(20)", "primary_key": True},
                        {"name": "account_name", "type": "VARCHAR(100)"},
                        {"name": "account_type", "type": "VARCHAR(30)"},
                        {"name": "current_balance_inr", "type": "DECIMAL(14,2)"},
                        {"name": "status", "type": "VARCHAR(15)"}
                    ]
                },
                "gst_sales_invoices": {
                    "fields": [
                        {"name": "invoice_no", "type": "VARCHAR(30)", "primary_key": True},
                        {"name": "invoice_date", "type": "DATE"},
                        {"name": "dealer_name", "type": "VARCHAR(100)"},
                        {"name": "gstin", "type": "VARCHAR(15)"},
                        {"name": "hsn_code", "type": "VARCHAR(10)"},
                        {"name": "taxable_amount_inr", "type": "DECIMAL(12,2)"},
                        {"name": "cgst_inr", "type": "DECIMAL(10,2)"},
                        {"name": "sgst_inr", "type": "DECIMAL(10,2)"},
                        {"name": "igst_inr", "type": "DECIMAL(10,2)"},
                        {"name": "total_invoice_amount_inr", "type": "DECIMAL(12,2)"},
                        {"name": "eway_bill_no", "type": "VARCHAR(20)"}
                    ]
                }
            }
        },
        "csvs": {
            "chart_of_accounts.csv": """account_code,account_name,account_type,current_balance_inr,status
1001,HDFC Bank Operating Account,ASSET,14500000.00,ACTIVE
1002,ICICI Bank Cash Credit Account,ASSET,-2500000.00,ACTIVE
1100,Accounts Receivable - Dealers,ASSET,38500000.00,ACTIVE
1200,Raw Material Inventory Stock,ASSET,18200000.00,ACTIVE
1201,Finished Goods Inventory Stock,ASSET,24100000.00,ACTIVE
2001,Accounts Payable - Suppliers,LIABILITY,12800000.00,ACTIVE
2100,GST Output Tax Payable,LIABILITY,4300000.00,ACTIVE
4001,Gross Sales Revenue - Paint Products,REVENUE,125000000.00,ACTIVE
5001,Raw Material Cost of Goods Sold,EXPENSE,68000000.00,ACTIVE
""",
            "gst_sales_invoices.csv": """invoice_no,invoice_date,dealer_name,gstin,hsn_code,taxable_amount_inr,cgst_inr,sgst_inr,igst_inr,total_invoice_amount_inr,eway_bill_no
INV-2026-8801,2026-09-20,Sharma Paint House,07AAAAA0000A1Z5,3209,90000.00,8100.00,8100.00,0.00,106200.00,EWB-991029381
INV-2026-8802,2026-09-21,Verma Traders,09CCCCC2222C3Z7,3209,95000.00,0.00,0.00,17100.00,112100.00,EWB-991029382
INV-2026-8803,2026-09-22,Kumar Hardware & Paints,08BBBBB1111B2Z6,3209,72000.00,0.00,0.00,12960.00,84960.00,EWB-991029383
INV-2026-8804,2026-09-24,Patel Color Mart,24DDDDD3333D4Z8,3209,120000.00,0.00,0.00,21600.00,141600.00,EWB-991029384
""",
            "accounts_receivable_aging.csv": """dealer_id,dealer_name,total_outstanding_inr,current_0_30_days,days_31_60,days_61_90,overdue_above_90,credit_hold_status
DLR-001,Sharma Paint House,106200.00,106200.00,0.00,0.00,0.00,CLEAR
DLR-002,Kumar Hardware & Paints,84960.00,84960.00,0.00,0.00,0.00,CLEAR
DLR-003,Verma Traders,245000.00,112100.00,132900.00,0.00,0.00,CLEAR
DLR-005,Gupta Paint Depot,185000.00,0.00,45000.00,60000.00,80000.00,HOLD_ACTIVE
""",
            "vendor_payments_ledger.csv": """voucher_no,voucher_date,vendor_name,vendor_invoice_no,gross_amount_inr,tds_deducted_inr,net_paid_inr,payment_method
VCH-2026-401,2026-09-18,DuPont Chemicals,DUP-9948,450000.00,9000.00,441000.00,NEFT_HDFC
VCH-2026-402,2026-09-19,Basf India Ltd,BAS-8831,820000.00,16400.00,803600.00,RTGS_HDFC
VCH-2026-403,2026-09-20,Deccan Minerals,DEC-1102,150000.00,3000.00,147000.00,NEFT_HDFC
"""
        }
    },
    "04_supply_chain": {
        "title": "Supply Chain, Procurement & Logistics Department",
        "sop": """# Standard Operating Procedure (SOP) - Supply Chain & Logistics

## 1. Objective & Scope
To manage raw material procurement, inventory optimization, warehouse bin management, and outbound logistics to ensure 99.5% on-time delivery across all dealer channels.

## 2. Inventory Management Protocol
- **Safety Stock Threshold**: Maintain 15 days of production capacity in Titanium Dioxide (TiO2) and Monomer Resins.
- **Reorder Point (ROP)**: ROP = (Average Daily Usage x Lead Time in Days) + Safety Stock.
- **Warehouse Storage**: Raw materials segregated into Binder Storage, Pigment Silos, and Solvent Drums following ISO safety protocols.

## 3. Outbound Shipping SOP
- Dispatch manifest verified against E-Way Bill and ERP Order.
- Weight bridge check mandatory for all outgoing 20L drum shipments.
""",
        "schema": {
            "module": "Supply Chain & Logistics",
            "tables": {
                "raw_materials_inventory": {
                    "fields": [
                        {"name": "material_code", "type": "VARCHAR(20)", "primary_key": True},
                        {"name": "material_name", "type": "VARCHAR(100)"},
                        {"name": "stock_quantity_kg", "type": "DECIMAL(12,2)"},
                        {"name": "unit_of_measure", "type": "VARCHAR(10)"},
                        {"name": "reorder_level_kg", "type": "DECIMAL(10,2)"},
                        {"name": "safety_stock_kg", "type": "DECIMAL(10,2)"},
                        {"name": "unit_cost_inr", "type": "DECIMAL(10,2)"},
                        {"name": "bin_location", "type": "VARCHAR(20)"}
                    ]
                },
                "finished_goods_inventory": {
                    "fields": [
                        {"name": "sku_code", "type": "VARCHAR(20)", "primary_key": True},
                        {"name": "product_name", "type": "VARCHAR(100)"},
                        {"name": "pack_size", "type": "VARCHAR(10)"},
                        {"name": "warehouse_stock_units", "type": "INT"},
                        {"name": "reserved_stock_units", "type": "INT"},
                        {"name": "min_threshold_units", "type": "INT"},
                        {"name": "mrp_inr", "type": "DECIMAL(10,2)"}
                    ]
                }
            }
        },
        "csvs": {
            "raw_materials_inventory.csv": """material_code,material_name,stock_quantity_kg,unit_of_measure,reorder_level_kg,safety_stock_kg,unit_cost_inr,bin_location
RM-TiO2-01,Rutile Titanium Dioxide Pigment,12500.00,KG,5000.00,2500.00,240.00,BIN-A-01
RM-ACR-02,Pure Acrylic Emulsion Resin,28000.00,KG,10000.00,5000.00,115.00,TANK-SILO-1
RM-CAL-03,Micronized Calcium Carbonate,45000.00,KG,15000.00,8000.00,18.00,BIN-B-04
RM-BIO-04,In-Can Preservative Biocide,850.00,KG,300.00,150.00,680.00,CHEM-ROOM-2
RM-THK-05,HEC Cellulose Thickener,1200.00,KG,400.00,200.00,850.00,CHEM-ROOM-1
""",
            "finished_goods_inventory.csv": """sku_code,product_name,pack_size,warehouse_stock_units,reserved_stock_units,min_threshold_units,mrp_inr
EM-WE-20L,Weather Shield Exterior Emulsion,20L,850,200,150,4800.00
EM-WE-04L,Weather Shield Exterior Emulsion,4L,1400,300,250,1150.00
PR-WP-20L,Acrylic Wall Primer Waterbased,20L,1200,450,200,2400.00
WT-TX-25KG,Rustic Texture Finish Bucket,25KG,600,100,100,3200.00
EM-IE-20L,Interior Luxury Emulsion,20L,950,150,150,3900.00
""",
            "purchase_orders_log.csv": """po_number,po_date,supplier_name,material_code,ordered_qty_kg,expected_delivery_date,unit_price_inr,po_status
PO-2026-901,2026-09-15,DuPont Chemicals,RM-TiO2-01,10000.00,2026-09-22,240.00,DELIVERED
PO-2026-902,2026-09-18,Basf India Ltd,RM-ACR-02,20000.00,2026-09-26,115.00,IN_TRANSIT
PO-2026-903,2026-09-22,Deccan Minerals,RM-CAL-03,30000.00,2026-09-28,18.00,APPROVED
""",
            "dispatch_transport_log.csv": """dispatch_id,dispatch_date,vehicle_no,transporter_name,destination_city,total_litres_loaded,lr_number,driver_phone,delivery_status
DSP-2026-301,2026-09-21,HR-38-X-9948,VRL Logistics,New Delhi,4500.00,LR-882910,+919988776655,DELIVERED
DSP-2026-302,2026-09-22,RJ-14-GA-1102,TCI Express,Jaipur,3200.00,LR-882911,+919876543210,IN_TRANSIT
DSP-2026-303,2026-09-24,UP-78-BT-4412,Safexpress,Kanpur,6000.00,LR-882912,+919765432109,DISPATCHED
"""
        }
    },
    "05_marketing_brand": {
        "title": "Marketing, Branding & Dealer Activation Department",
        "sop": """# Standard Operating Procedure (SOP) - Marketing & Branding

## 1. Objective & Scope
To position Swatch Paints as India's premier, highest-durability, anti-fungal paint brand; manage painter loyalty networks, dealer POS branding, and digital acquisition campaigns.

## 2. Key Initiatives
- **Painter Loyalty App / Program**: Token redemption program for painters earning INR cashbacks and merchandise per 20L bucket.
- **Dealer POS Branding**: In-store shade card stands, LED glow signboards, and product sample displays.
- **Digital Campaigns**: Performance marketing targeting contractors, architects, and house owners.

## 3. Competitor Intelligence Protocol
Weekly collection of rival trade pricing (Asian Paints, Berger, Nerolac, NCL Alltek) to ensure Swatch Paints offers superior dealer margins (18-22% vs industry 10-12%).
""",
        "schema": {
            "module": "Marketing & Branding",
            "tables": {
                "marketing_campaigns": {
                    "fields": [
                        {"name": "campaign_id", "type": "VARCHAR(20)", "primary_key": True},
                        {"name": "campaign_name", "type": "VARCHAR(100)"},
                        {"name": "channel", "type": "VARCHAR(30)"},
                        {"name": "budget_inr", "type": "DECIMAL(12,2)"},
                        {"name": "actual_spend_inr", "type": "DECIMAL(12,2)"},
                        {"name": "leads_generated", "type": "INT"},
                        {"name": "roi_ratio", "type": "DECIMAL(5,2)"}
                    ]
                },
                "painter_loyalty_members": {
                    "fields": [
                        {"name": "painter_id", "type": "VARCHAR(20)", "primary_key": True},
                        {"name": "painter_name", "type": "VARCHAR(100)"},
                        {"name": "phone_number", "type": "VARCHAR(15)"},
                        {"name": "city", "type": "VARCHAR(50)"},
                        {"name": "preferred_dealer_id", "type": "VARCHAR(20)"},
                        {"name": "reward_points_accumulated", "type": "INT"},
                        {"name": "tier_level", "type": "VARCHAR(15)"}
                    ]
                }
            }
        },
        "csvs": {
            "marketing_campaigns.csv": """campaign_id,campaign_name,channel,budget_inr,actual_spend_inr,leads_generated,roi_ratio
CMP-2026-01,Architect & Builder Summit 2026,EVENTS,500000.00,480000.00,120,4.5
CMP-2026-02,Monsoon Waterproofing Digital Ads,META_GOOGLE,300000.00,295000.00,850,3.8
CMP-2026-03,Dealer Signboard Branding Blitz,OUTDOOR_POS,1200000.00,1150000.00,450,5.2
""",
            "painter_loyalty_members.csv": """painter_id,painter_name,phone_number,city,preferred_dealer_id,reward_points_accumulated,tier_level
PTR-1001,Radhe Shyam Contractor,+919911223344,New Delhi,DLR-001,4500,GOLD
PTR-1002,Mohan Lal Painter,+919922334455,Jaipur,DLR-002,2100,SILVER
PTR-1003,Dinesh Yadav,+919933445566,Kanpur,DLR-003,8900,PLATINUM
PTR-1004,Sanjay Solanki,+919944556677,Ahmedabad,DLR-004,1200,SILVER
""",
            "branding_assets_inventory.csv": """item_id,asset_name,total_units_printed,allocated_to_dealers,in_stock_units,unit_cost_inr
AST-01,Swatch Paints Fandeck Shade Card 2026,5000,3200,1800,250.00
AST-02,Dealer LED Glow Signboard (8x3 ft),500,380,120,4500.00
AST-03,Painter T-Shirts & Cap Kits,10000,6500,3500,180.00
""",
            "competitor_price_tracking.csv": """record_date,competitor_name,product_name,pack_size,competitor_dealer_price_inr,swatch_paints_equivalent_price_inr,price_advantage_percent
2026-09-20,Asian Paints,Apex Weatherproof Emulsion,20L,5400.00,4800.00,11.1
2026-09-20,Berger Paints,WeatherCoat Long Life,20L,5250.00,4800.00,8.5
2026-09-20,NCL Buildtek,Alltek Wall Texture Bucket,25KG,3500.00,3200.00,8.6
"""
        }
    },
    "06_hr_legal": {
        "title": "Human Resources, Payroll & Legal Compliance Department",
        "sop": """# Standard Operating Procedure (SOP) - HR, Payroll & Legal Compliance

## 1. Objective & Scope
To manage employee onboarding, attendance, payroll processing, statutory compliance (PF, ESI, Factory License), workplace safety, and legal governance for Swatch Paints.

## 2. Onboarding Workflow via Hermes Telegram Bot
1. **Details Capture**: Employee names, phone numbers, assigned department, and designations captured via Telegram HR prompt.
2. **Master Log**: Employee profile added to `employee_directory.csv` and assigned an ERP Employee ID (`EMP-100X`).
3. **Document Verification**: Aadhaar, PAN, Bank Details, and Educational certificates stored in encrypted ERP storage.

## 3. Monthly Payroll Processing (28th - 1st)
- Attendance synced from biometric devices & field app.
- Loss of Pay (LOP) calculated for unauthorized absences.
- Salary dislocated via HDFC Direct Payroll API on the 1st of every month.

## 4. Statutory & Factory License Protocols
- Factory License renewal filed 60 days prior to expiry.
- Pollution Control Board (PCB) Air & Water consent compliance checked quarterly.
""",
        "schema": {
            "module": "Human Resources & Legal",
            "tables": {
                "employee_directory": {
                    "fields": [
                        {"name": "employee_id", "type": "VARCHAR(20)", "primary_key": True},
                        {"name": "full_name", "type": "VARCHAR(100)"},
                        {"name": "mobile_number", "type": "VARCHAR(15)"},
                        {"name": "email", "type": "VARCHAR(100)"},
                        {"name": "department", "type": "VARCHAR(50)"},
                        {"name": "designation", "type": "VARCHAR(50)"},
                        {"name": "joining_date", "type": "DATE"},
                        {"name": "employment_type", "type": "VARCHAR(20)"},
                        {"name": "base_salary_inr", "type": "DECIMAL(10,2)"},
                        {"name": "status", "type": "VARCHAR(15)"}
                    ]
                },
                "monthly_attendance_payroll": {
                    "fields": [
                        {"name": "record_month", "type": "VARCHAR(7)"},
                        {"name": "employee_id", "type": "VARCHAR(20)", "foreign_key": "employee_directory.employee_id"},
                        {"name": "total_working_days", "type": "INT"},
                        {"name": "days_present", "type": "DECIMAL(4,1)"},
                        {"name": "paid_leave_days", "type": "DECIMAL(4,1)"},
                        {"name": "overtime_hours", "type": "DECIMAL(5,1)"},
                        {"name": "gross_salary_inr", "type": "DECIMAL(10,2)"},
                        {"name": "deductions_inr", "type": "DECIMAL(10,2)"},
                        {"name": "net_salary_inr", "type": "DECIMAL(10,2)"}
                    ]
                }
            }
        },
        "csvs": {
            "employee_directory.csv": """employee_id,full_name,mobile_number,email,department,designation,joining_date,employment_type,base_salary_inr,status
EMP-1001,Rajesh Sharma,+919810011111,rajesh.sharma@swatchpaints.com,Executive,Managing Director,2024-01-01,PERMANENT,250000.00,ACTIVE
EMP-1002,Dr. Ananya Roy,+919810022222,ananya.roy@swatchpaints.com,Production & QA Lab,Head Chemist & QA Lead,2024-03-15,PERMANENT,120000.00,ACTIVE
EMP-1003,Mahesh Verma,+919810033333,mahesh.verma@swatchpaints.com,Production & QA Lab,Factory Plant Manager,2024-02-01,PERMANENT,95000.00,ACTIVE
EMP-1004,Rohan Mehta,+919810044444,rohan.mehta@swatchpaints.com,Sales & Market,Regional Sales Manager,2024-04-10,PERMANENT,85000.00,ACTIVE
EMP-1005,Vikram Lab Chemist,+919810055555,vikram.c@swatchpaints.com,Production & QA Lab,QC Chemist,2024-06-01,PERMANENT,45000.00,ACTIVE
EMP-1006,Suresh Kumar,+919810066666,suresh.k@swatchpaints.com,Production & QA Lab,Batch Master Operator,2024-05-15,PERMANENT,38000.00,ACTIVE
EMP-1007,Priya Singh,+919810077777,priya.singh@swatchpaints.com,Sales & Market,Area Sales Executive,2024-07-01,PERMANENT,55000.00,ACTIVE
""",
            "monthly_attendance_payroll.csv": """record_month,employee_id,total_working_days,days_present,paid_leave_days,overtime_hours,gross_salary_inr,deductions_inr,net_salary_inr
2026-08,EMP-1001,26,26.0,0.0,0.0,250000.00,25000.00,225000.00
2026-08,EMP-1002,26,25.0,1.0,12.0,125000.00,12000.00,113000.00
2026-08,EMP-1003,26,26.0,0.0,18.0,102000.00,9500.00,92500.00
2026-08,EMP-1004,26,24.0,2.0,0.0,85000.00,8500.00,76500.00
2026-08,EMP-1005,26,26.0,0.0,10.0,48000.00,4500.00,43500.00
""",
            "legal_statutory_licenses.csv": """license_id,license_name,issuing_authority,license_number,issue_date,expiry_date,renewal_lead_days,responsible_officer
LIC-01,Factory Operating License,Department of Factories & Boilers,FACT-DL-2024-991,2024-01-01,2026-12-31,60,Mahesh Verma
LIC-02,Consent to Operate (Water & Air),State Pollution Control Board,PCB-CTO-88210,2024-04-01,2027-03-31,90,Dr. Ananya Roy
LIC-03,GST Registration Certificate,Government of India GSTN,07AAAAA0000A1Z5,2024-01-15,2099-12-31,365,Finance Manager
""",
            "leave_applications_log.csv": """leave_id,employee_id,leave_type,start_date,end_date,reason,approval_status
LEV-2026-12,EMP-1004,CASUAL,2026-09-10,2026-09-11,Personal work,APPROVED
LEV-2026-13,EMP-1002,SICK,2026-09-18,2026-09-18,Medical checkup,APPROVED
"""
        }
    },
    "07_vision_growth": {
        "title": "Vision, Strategy & Trillion-Dollar Growth Engine",
        "sop": """# Standard Operating Procedure (SOP) - Vision & Trillion-Dollar Growth Strategy

## 1. Objective & Scope
To orchestrate Swatch Paints' aggressive expansion into becoming a global leader paint manufacturer with an ambitious trajectory towards a $1 Trillion valuation benchmark through scale, automation, high-margin formulations, and pan-India dealer acquisition.

## 2. Growth Pillars
1. **Technological Supremacy**: Zero-VOC, nano-emulsion heat-reflective coatings and 100% water-repellent exterior primers.
2. **Dealer Network Expansion**: Target 10,000 active dealers across Tier-1, Tier-2, and Tier-3 cities within 36 months.
3. **Automated Factory Model**: 24/7 continuous high-speed dispersion and robotic packing lines.
4. **Margin Dominance**: Direct raw material sourcing eliminating middleman markups.

## 3. Valuation & Financial Milestones
- Phase 1 (2026-2027): ₹100 Cr Annual Turnover | 1,000 Dealers.
- Phase 2 (2027-2029): ₹1,000 Cr Annual Turnover | 5,000 Dealers | IPO Filing.
- Phase 3 (2030-2035): Global Brand Takeover & Trillion Dollar Market Valuation.
""",
        "schema": {
            "module": "Vision & Strategy",
            "tables": {
                "strategic_kpis_tracker": {
                    "fields": [
                        {"name": "metric_id", "type": "VARCHAR(20)", "primary_key": True},
                        {"name": "strategic_objective", "type": "VARCHAR(150)"},
                        {"name": "target_year", "type": "INT"},
                        {"name": "target_value", "type": "VARCHAR(50)"},
                        {"name": "current_value", "type": "VARCHAR(50)"},
                        {"name": "growth_rate_percent", "type": "DECIMAL(5,2)"},
                        {"name": "executive_owner", "type": "VARCHAR(50)"}
                    ]
                }
            }
        },
        "csvs": {
            "strategic_kpis_tracker.csv": """metric_id,strategic_objective,target_year,target_value,current_value,growth_rate_percent,executive_owner
STR-01,Active Pan-India Dealer Network,2027,5000 Dealers,850 Dealers,45.0,Head of Sales
STR-02,Annual Production Capacity,2027,100000 KL,25000 KL,60.0,Factory Plant Manager
STR-03,Annual Revenue (INR),2027,1000 Cr,125 Cr,85.0,Managing Director
STR-04,Gross Margin Percentage,2027,42.0%,38.5%,3.5,Chief Financial Officer
""",
            "factory_expansion_roadmap.csv": """project_phase,location,planned_capacity_kl_year,est_capex_cr_inr,start_date,target_commission_date,status
Phase 1 Extension,Bhiwadi Industrial Zone,30000,15.00,2026-06-01,2027-01-15,UNDER_CONSTRUCTION
Phase 2 Mega Plant,Gujarat Industrial Hub,60000,45.00,2027-03-01,2028-06-30,PLANNING
Phase 3 South Hub,Chennai Logistics Zone,50000,35.00,2028-09-01,2029-12-31,PROPOSED
""",
            "rd_innovation_pipeline.csv": """project_code,innovation_title,phase,est_market_size_cr_inr,lead_scientist,commercial_target_date
RD-2026-01,Nano Thermally Reflective Exterior Paint,LAB_TRIAL,500.0,Dr. Ananya Roy,2027-03-31
RD-2026-02,Anti-Viral Scrub Resistant Luxury Emulsion,COMMERCIAL_LAUNCH,800.0,Dr. Ananya Roy,2026-11-15
RD-2026-03,Self-Cleaning Hydrophobic Wall Texture,FIELD_TEST,350.0,Dr. Ananya Roy,2027-01-31
""",
            "valuation_milestones.csv": """milestone_level,projected_annual_revenue_cr_inr,target_market_share_percent,valuation_multiplier,target_date,status
Milestone 1 - Regional Dominance,100.0,2.5,5.0x,2026-12-31,ON_TRACK
Milestone 2 - National Player (IPO),1000.0,8.0,8.0x,2028-12-31,PLANNED
Milestone 3 - Trillion Valuation Engine,50000.0,25.0,15.0x,2035-12-31,VISIONARY
"""
        }
    },
    "08_systems_sops": {
        "title": "Systems, IT, Hermes AI & Enterprise SOP Registry",
        "sop": """# Standard Operating Procedure (SOP) - Systems, IT & Hermes AI Engine

## 1. Objective & Scope
To govern the digital architecture, ERP database integrity, Hermes 24/7 autonomous learning daemon, role-based security access, and API integrations across Swatch Paints.

## 2. Hermes AI Engine Operations
- **Autonomous Daemon**: Runs continuously in background (`night_learning_agent.py`), performing market intelligence scans, stock level monitoring, and auto-report generation.
- **Model Preset**: Configured to `auto/best-smart` Omni-Route switching on `http://localhost:20128/v1`.
- **MCP Tool Integration**: Firecrawl MCP connected for web scraping & competitor pricing tracking.

## 3. Security & Access Control
- Strict Role-Based Access Control (RBAC) enforced across API endpoints.
- Database backups captured every 6 hours and replicated to secure offsite storage.
""",
        "schema": {
            "module": "Systems & Enterprise IT",
            "tables": {
                "sop_master_registry": {
                    "fields": [
                        {"name": "sop_id", "type": "VARCHAR(20)", "primary_key": True},
                        {"name": "department_id", "type": "VARCHAR(30)"},
                        {"name": "sop_title", "type": "VARCHAR(150)"},
                        {"name": "version", "type": "VARCHAR(10)"},
                        {"name": "file_path", "type": "TEXT"},
                        {"name": "last_reviewed_date", "type": "DATE"},
                        {"name": "system_integrated", "type": "BOOLEAN"}
                    ]
                }
            }
        },
        "csvs": {
            "sop_master_registry.csv": """sop_id,department_id,sop_title,version,file_path,last_reviewed_date,system_integrated
SOP-SAL-01,01_sales_market,Sales Pipeline & Dealer Onboarding,v2.1,01_sales_market/SOP_GOVERNANCE.md,2026-09-27,TRUE
SOP-PRD-02,02_production_lab,Batch Production & Quality Control,v2.5,02_production_lab/SOP_GOVERNANCE.md,2026-09-27,TRUE
SOP-FIN-03,03_finance_gst,Finance Ledger & GST Compliance,v1.8,03_finance_gst/SOP_GOVERNANCE.md,2026-09-27,TRUE
SOP-SCM-04,04_supply_chain,Raw Material Procurement & Logistics,v2.0,04_supply_chain/SOP_GOVERNANCE.md,2026-09-27,TRUE
SOP-MKT-05,05_marketing_brand,Brand Marketing & Painter Loyalty,v1.5,05_marketing_brand/SOP_GOVERNANCE.md,2026-09-27,TRUE
SOP-HR-06,06_hr_legal,Human Resources & Statutory Licensing,v2.0,06_hr_legal/SOP_GOVERNANCE.md,2026-09-27,TRUE
SOP-VIS-07,07_vision_growth,Trillion-Dollar Strategic Growth Roadmap,v3.0,07_vision_growth/SOP_GOVERNANCE.md,2026-09-27,TRUE
SOP-SYS-08,08_systems_sops,IT Infrastructure & Hermes AI Daemon,v2.2,08_systems_sops/SOP_GOVERNANCE.md,2026-09-27,TRUE
""",
            "erp_user_roles.csv": """user_id,employee_id,username,role,department_access,active_status
USR-01,EMP-1001,admin_rajesh,SUPER_ADMIN,ALL,ACTIVE
USR-02,EMP-1002,ananya_lab,DEPT_HEAD,02_production_lab,ACTIVE
USR-03,EMP-1003,mahesh_plant,PLANT_MANAGER,02_production_lab;04_supply_chain,ACTIVE
USR-04,EMP-1004,rohan_sales,SALES_HEAD,01_sales_market;05_marketing_brand,ACTIVE
""",
            "hermes_autonomous_cron_jobs.csv": """task_id,job_name,execution_schedule,target_department,action_type,last_execution_time,health_status
CRON-01,Competitor Price Scrape,0 0 * * *,01_sales_market,FIRECRAWL_SCRAPE,2026-09-27 00:00:00,HEALTHY
CRON-02,Stock Threshold Alert Check,*/30 * * * *,04_supply_chain,INVENTORY_AUDIT,2026-09-27 10:30:00,HEALTHY
CRON-03,Telegram HR Onboarding Daemon,0 9 * * *,06_hr_legal,TELEGRAM_PROMPT,2026-09-27 11:05:00,HEALTHY
""",
            "erp_api_endpoints_registry.csv": """endpoint_id,module_name,http_method,url_path,access_level_required,data_format
API-01,Dealers,GET,/api/v1/sales/dealers,SALES_VIEW,JSON
API-02,Batch Log,POST,/api/v1/production/batches,LAB_WRITE,JSON
API-03,GST Invoices,POST,/api/v1/finance/invoices,FINANCE_WRITE,JSON
API-04,Employee Directory,GET,/api/v1/hr/employees,HR_ADMIN,JSON
"""
        }
    }
}

for folder, content in departments.items():
    folder_path = os.path.join(BASE_DIR, folder)
    os.makedirs(folder_path, exist_ok=True)
    
    # Write SOP_GOVERNANCE.md
    sop_path = os.path.join(folder_path, "SOP_GOVERNANCE.md")
    with open(sop_path, "w", encoding="utf-8") as f:
        f.write(content["sop"])
        
    # Write DATA_SCHEMA.json
    schema_path = os.path.join(folder_path, "DATA_SCHEMA.json")
    with open(schema_path, "w", encoding="utf-8") as f:
        json.dump(content["schema"], f, indent=4)
        
    # Write CSVs
    for csv_name, csv_data in content["csvs"].items():
        csv_path = os.path.join(folder_path, csv_name)
        with open(csv_path, "w", encoding="utf-8") as f:
            f.write(csv_data)

print(f"Successfully generated all 8 department folders with SOPs, Schemas, and CSVs in {BASE_DIR}")
