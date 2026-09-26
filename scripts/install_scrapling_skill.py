"""
Installer script for Scrapling Skill into Hermes Agent.
Installs to both workspace skills/ and AppData/hermes/skills/.
"""
import os

src = r"d:\Sharma Industries Erp Software\hermes-agent\optional-skills\research\scrapling\SKILL.md"
with open(src, "r", encoding="utf-8") as f:
    content = f.read()

swatch_section = """

## Swatch Paints (Sharma Industries) Operational Scraping Use Cases

Hermes uses Scrapling via both CLI and the built-in `scrapling_scrape` tool for competitive market intelligence:

### 1. Competitor Retail Paint Pricing Audits
Extract current retail MRP and dealer billing rates across Asian Paints, Berger, and Nerolac product lines from online distributor catalogs:
```python
from scrapling.fetchers import Fetcher

# Extract product titles and prices
page = Fetcher.get('https://example-paint-distributor.com/decorative/emulsions')
for p in page.css('.product-card'):
    name = p.css('.title::text').get()
    price = p.css('.price::text').get()
    print(f'{name}: {price}')
```

### 2. Raw Material Chemical Spot Rate Tracking
Track daily spot prices for core coatings chemicals (Monomers: MMA, Butyl Acrylate, VAM; Titanium Dioxide Rutile grades; Extenders: Calcite/Dolomite) on domestic chemical trade bulletins:
```python
from scrapling.fetchers import FetcherSession

with FetcherSession(impersonate='chrome') as session:
    page = session.get('https://example-chemical-market.in/indices/acrylic-monomers')
    rates = page.css('table.spot-rates tr').getall()
```

### 3. Government & PWD e-Tender Monitoring
Monitor public procurement portals (Rajasthan eProc, CPWD, Indian Railways, AIIMS) for architectural and industrial paint supply tenders:
```python
from scrapling.fetchers import StealthyFetcher

# Bypass portal protection to extract active tenders
page = StealthyFetcher.fetch(
    'https://eproc.rajasthan.gov.in/tenders/paint-supply',
    solve_cloudflare=True,
    headless=True
)
tenders = page.css('.tender-row').getall()
```

### 4. Built-in Hermes Tool Integration: `scrapling_scrape`
Hermes agents can call the native tool `scrapling_scrape`:
```json
{
  "url": "https://competitor-catalog.com/luxury-emulsions",
  "css_selector": ".product-item, .price-box",
  "stealth": false,
  "extract_text": true
}
```
"""

full_content = content.strip() + "\n" + swatch_section.strip() + "\n"

ws_dest = r"d:\Sharma Industries Erp Software\hermes-agent\skills\scrapling"
app_dest = r"C:\Users\itzzz\AppData\Local\hermes\skills\scrapling"

os.makedirs(ws_dest, exist_ok=True)
os.makedirs(app_dest, exist_ok=True)

with open(os.path.join(ws_dest, "SKILL.md"), "w", encoding="utf-8") as f:
    f.write(full_content)

with open(os.path.join(app_dest, "SKILL.md"), "w", encoding="utf-8") as f:
    f.write(full_content)

lines = len(full_content.splitlines())
print(f"Successfully installed scrapling skill to workspace ({lines} lines) and AppData!")
