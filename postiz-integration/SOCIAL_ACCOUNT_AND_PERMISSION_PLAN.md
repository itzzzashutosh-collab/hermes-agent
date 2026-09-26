# Social Media Account & Permission Plan

**Document ID:** PLN-SOCIAL-ACC-PERM-01  
**Version:** 1.0.0  
**Security Mandate:** Strict Least-Privilege, Zero-Chat Credential Exposure, Hard Account Boundaries  

---

## 1. Brand Account Governance
Swatch Paints will operate official business profiles across 4 core B2B channels:

| Platform | Handle / Profile Type | Primary B2B Purpose | Allowed Post Types |
| :--- | :--- | :--- | :--- |
| **LinkedIn** | Swatch Paints Official (Company Page) | Builder credibility, dealer network expansion, corporate milestones | Articles, project photos, technical data sheets |
| **Instagram** | `@swatchpaintsofficial` (Business Account)| Painter education, shade guides, finish demonstrations, dealer branding | Reels, single image, carousel |
| **Facebook** | Swatch Paints India (Verified Page) | Contractor community, regional painter meet highlights, local retailer tags | Video, photo, event announcements |
| **YouTube** | Swatch Paints Academy (Brand Channel) | Detailed application tutorials (primer, putty, waterproof coating) | Shorts, long-form technical guides |

---

## 2. Access Control & Permission Stages

```
STAGE 0: Mock Sandbox (Local Hermes file storage, offline mock server, zero live credentials)
   ↓
STAGE 1: Read-Only Channel Sync & Draft Creation (Fetch connected channels, stage drafts in Postiz)
   ↓ (Owner Approval Required)
STAGE 2: Single-Post Controlled Scheduling (Approved schedule window, verified human review)
   ↓ (Pilot Operational Review)
STAGE 3: Active Production Publishing (Scheduled weekly B2B calendar with real-time audit logging)
```

### Hermes Tool Permissions for Social Integration:
- **`postiz_sync_channels`**: Read-only (`GET /integrations`).
- **`postiz_create_draft`**: Internal write only (`type: "draft"`).
- **`postiz_schedule_post`**: Restricted execution (`type: "schedule"`). **Requires signed approval token.**
- **`postiz_publish_now`**: **HARD BLOCKED**. Hermes is prohibited from immediate publishing. All posts must sit in a minimum 30-minute review queue.

---

## 3. Anti-Disaster & Wrong-Account Guardrails
1. **Hardcoded Whitelist:** Hermes will reject any post where `integration.id` does not match the approved Swatch Paints business profile UUIDs.
2. **Personal Account Immunity:** If a personal social account is connected to Postiz, Hermes will automatically blacklist it from API requests.
3. **Secret Isolation:** The Postiz API key will reside strictly in `.env.secret` under `POSTIZ_API_KEY`. It will never be echoed in prompt outputs, chat windows, or committed to Git.
