# Platform-Specific Technical Limitations & Safe Harbor Rules

**Document ID:** LIM-PLATFORM-01  
**Version:** 1.0.0  
**Scope:** API Constraints for Meta, LinkedIn, X, and YouTube  

---

## 1. Platform-Specific Constraints Matrix

| Platform | Text / Caption Cap | Media Supported | Aspect Ratio Limits | Critical API Limitation |
| :--- | :--- | :--- | :--- | :--- |
| **Instagram** | 2,200 chars (Ideal: < 150 words) | JPEG, PNG, MP4 | 1:1 (Square), 4:5 (Portrait), 9:16 (Reels) | Cannot include clickable hyperlinks in captions. Must use bio link or QR. |
| **LinkedIn** | 3,000 chars (Ideal: 150-250 words) | PDF (Carousel), PNG, MP4 | 1.91:1 (Landscape) or 1:1 | Excessive tagging triggers spam filters. Minimum 2-hour gap between posts. |
| **Facebook** | 63,206 chars (Ideal: < 80 words) | Images, Video | Any standard | Organic reach heavily favors video/reels over static link previews. |
| **YouTube Shorts**| 100 chars (Title), 5,000 (Desc) | MP4 (Vertical 9:16) | 9:16 strictly (< 60s duration) | Strict audio copyright detection; must use royalty-free licensed audio. |

---

## 2. Technical Claims Safe-Harbor Quarantine
Indian advertising law (ASCI Guidelines) and paints standard compliance prohibit unsubstantiated claims:

| Prohibited Unverified Phrase | Failure Mode / Legal Risk | Required Technical Verification Before Post |
| :--- | :--- | :--- |
| *"100% Waterproof"* | Consumer Protection Act violation; paints provide water resistance, not submarine sealing. | Use: *"High Hydrostatic Water Resistance tested up to 4 bars"*. Must cite Lab Test Report #. |
| *"Anti-Fungal for 5 Years"* | False warranty claim if wall has moisture seepage. | Use: *"Biocide formulation protects against fungal growth under standard curing conditions"*. |
| *"Cheaper than Asian Paints"* | Unfair trade practice / trademark infringement litigation. | Strict prohibition on comparative brand names. Use: *"Optimized direct-from-factory value"*. |
| *"Zero Toxic Chemicals"* | Misleading greenwashing claim. | Must specify: *"Zero Added Lead (< 90 ppm as per BIS IS 15489)"*. |
