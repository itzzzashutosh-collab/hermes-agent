"""
Enrichment script to guarantee every skill exceeds 215-240+ lines.
"""
import os

ws_base = r"d:\Sharma Industries Erp Software\hermes-agent\skills"
app_base = r"C:\Users\itzzz\AppData\Local\hermes\skills"

# Enrich pain-is-the-pitch
pip_path = os.path.join(ws_base, "pain-is-the-pitch", "SKILL.md")
with open(pip_path, "r", encoding="utf-8") as f:
    pip_content = f.read()

extra_pip = """
### Scenario 4: Architectural & Structural Consultant Pain Pitch
- **Before (Generic Feature Pitch):**
  *"Sir, our exterior emulsions have high crack-bridging capability, zero VOC, and meet all green building norms."*
- **After (Pain-Is-The-Pitch Transformation):**
  *"Sir, an architect’s greatest nightmare is visiting a completed luxury villa 18 months after handover, only to find hairline micro-cracks and efflorescence stains bleeding through the exterior facade. The client blames the design, not the paint.*
  *Standard 50-micron coatings lack the elastomeric elongation required for Rajasthan’s extreme 45°C thermal expansion. Swatch WeatherShield Elastomeric Coating provides 300% elongation, sealing 2mm dynamic cracks permanently. Your architectural vision remains pristine, protecting your firm's professional legacy."*

### Scenario 5: Rural Hardware Counter (Challenger Pitch)
- **Before (Generic Feature Pitch):**
  *"Bhaiya, hamara distemper aur primer dono sasta hai aur badiya quality hai."*
- **After (Pain-Is-The-Pitch Transformation):**
  *"Bhaiya ji, gaon dehat ke grahak jab sasta chuna ya local distemper lagate hain, toh har saal Diwali par unka deewar jhadne lagta hai. Wo sochte hain paint kharab hai, aur aapki dukan ki shikayat karte hain.*
  *Aap unhe Swatch Acrylic Primer aur Polymer Putty ka combo dijiye. 1 coat mein pura safedi aati hai aur 3 saal tak chuna jhadna band ho jata hai. Grahak ka paisa bachta hai aur aapko local product ke muqable 3 guna saaf margin milta hai."*
"""

target_pip = "## 8. SURGICAL DIAGNOSTIC QUESTION BANK"
if target_pip in pip_content and "Scenario 4: Architectural" not in pip_content:
    pip_content = pip_content.replace(target_pip, extra_pip.strip() + "\n\n---\n\n" + target_pip)
    with open(pip_path, "w", encoding="utf-8") as f:
        f.write(pip_content)
    with open(os.path.join(app_base, "pain-is-the-pitch", "SKILL.md"), "w", encoding="utf-8") as f:
        f.write(pip_content)

# Enrich hormozi-evaluator
he_path = os.path.join(ws_base, "hormozi-evaluator", "SKILL.md")
with open(he_path, "r", encoding="utf-8") as f:
    he_content = f.read()

extra_he = """
### 3. The Retailer "Diwali Mandi Dhamaka" Pre-Booking Bundle
- **Avatar:** Medium and large retail paint counters preparing for peak festive Diwali whitewashing demand.
- **The Core Offer:** Pre-book 100 buckets of Swatch Interior & Exterior Emulsions 45 days before Navratri.
- **The Stack:** Guaranteed 22% festive margin + Free motorized colorant dispenser machine + 50 painter festive gift packs (branded wristwatches and sweets) for his contractor network + Direct factory truck priority dispatch.
- **Risk Reversal:** "Unsold festive stock buyback guarantee. Any bucket remaining in your godown 15 days after Diwali is collected by our factory van with 100% credit note issued immediately."

### 4. The Industrial Fabricator "Corrosion Shield" Contract
- **Avatar:** Steel fabricators, PEB shed manufacturers, and industrial gate/grill workshops.
- **The Core Offer:** Bulk drum supply of Swatch Anti-Corrosive Red Oxide Primer and Synthetic Enamels.
- **The Stack:** Direct factory wholesale pricing + 500-hour salt spray test certification + Free airless spray nozzle kit + 30-day payment cycle.
- **Risk Reversal:** "If any structural member shows rust bleeding within 24 months of application, we supply replacement primer and pay 100% of recoating labor."
"""

target_he = "## 9. DYNAMIC ERP UNIT ECONOMICS QUERY PROTOCOL"
if target_he in he_content and "Diwali Mandi Dhamaka" not in he_content:
    he_content = he_content.replace(target_he, extra_he.strip() + "\n\n---\n\n" + target_he)
    with open(he_path, "w", encoding="utf-8") as f:
        f.write(he_content)
    with open(os.path.join(app_base, "hormozi-evaluator", "SKILL.md"), "w", encoding="utf-8") as f:
        f.write(he_content)

print("Enrichment complete. Re-checking line counts:")
names = ['porter-strategy', 'influence-psychology', 'gtm-strategy', 'sales-strategist', 'marketing-council', 'pain-is-the-pitch', 'hormozi-evaluator']
for name in names:
    ws_file = os.path.join(ws_base, name, 'SKILL.md')
    with open(ws_file, 'r', encoding='utf-8') as f:
        lines = len(f.readlines())
    print(f"  {name}: {lines} lines")
