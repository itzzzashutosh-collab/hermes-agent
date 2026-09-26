# Postiz Capability & Architecture Audit (Without Docker)

**Document ID:** AUD-POSTIZ-01  
**Audit Date:** 2026-09-25  
**Auditor:** Hermes Tooling & Social Integration Architect  
**Target Repository:** `gitroomhq/postiz-app` (Official Gitroom HQ)  
**Documentation Base:** `https://docs.postiz.com/public-api`  
**Execution Constraint:** **Zero Docker Dependency — 100% Native Hermes Integration**  

---

## 1. Official Repository & License Identity
- **Repository:** `gitroomhq/postiz-app` (GitHub verified, ~16.5k stars).
- **Organization:** Gitroom HQ (Nevo David & team).
- **License:** Open Source (AGPL-3.0 / Fair-code components).
- **Official API Documentation:** `https://docs.postiz.com/public-api`.
- **Public API Base URL:** `https://api.postiz.com/public/v1` (Cloud) or `{CUSTOM_POSTIZ_URL}/public/v1` (Self-hosted).
- **Authentication:** HTTP Header `Authorization: <API_KEY>` or OAuth2 Bearer token.

---

## 2. Docker vs. Non-Docker Evaluation for Swatch Paints

| Feature / Dimension | Full Docker Deployment | Standalone Hermes Native Connector (RECOMMENDED) |
| :--- | :--- | :--- |
| **Prerequisites** | Docker Desktop, WSL2, Docker Compose, 6GB+ RAM | Python 3.11 (`.venv`), Standard HTTP / JSON library |
| **Host Impact** | High background memory, VM overhead, port conflicts | Zero overhead, native Python process in `hermes-agent` |
| **Database & Services** | Requires local PostgreSQL + Redis + Prisma | None locally. Uses Cloud API or lightweight JSON staging |
| **Stability on Windows** | Known WSL2 daemon sleep / file sync latency issues | 100% reliable, zero daemon freeze risk |
| **Maintenance Burden** | Container updates, volume backups, network bridging | Single Python client connector module in Hermes |
| **Verdict** | **REJECTED (Per Owner Mandate)** | **APPROVED FOR IMPLEMENTATION** |

---

## 3. Verified Postiz API Capabilities

### A. Channel / Integration Discovery
- **Endpoint:** `GET /public/v1/integrations`
- **Output:** Array of connected channels with `id`, `name`, `platform`, and platform-specific profile metadata.
- **Hermes Usage:** Discovers which channels (Instagram, LinkedIn, Facebook, X, YouTube) are connected and extracts their unique `integration.id` values.

### B. Post Scheduling & Draft Creation
- **Endpoint:** `POST /public/v1/posts`
- **Supported `type` Modes:**
  - `draft`: Saves content in Postiz composer without publishing or queuing. Safe default.
  - `schedule`: Queues post for specified ISO-8601 UTC timestamp (`"date": "YYYY-MM-DDTHH:MM:SS.000Z"`).
  - `now`: Immediate publishing (restricted by Hermes approval gates).
- **Multi-Platform Support:** Single request can target multiple channels with platform-tailored text and media arrays.

### C. Media Upload
- **Multipart Upload:** `POST /public/v1/upload` (accepts `file` form-data for local image/video assets).
- **URL Ingestion:** `POST /public/v1/upload-from-url` (downloads and hosts assets from approved staging URLs).

### D. Post Status & Analytics
- **Endpoint:** `GET /public/v1/posts`
- **Fields:** Returns post status (`SCHEDULED`, `PUBLISHED`, `FAILED`), error message if failed, and engagement metrics where supported by the platform API.

---

## 4. Rate Limits & Technical Constraints
- **Public API Rate Limit:** 90 requests/hour on `POST /posts` by default.
- **Platform Limitations:**
  - **Instagram:** Direct image/carousel/reel publishing requires Instagram Business Account connected to Facebook Page.
  - **LinkedIn:** Company page publishing requires `w_organization_social` scope.
  - **X (Twitter):** Media count capped at 4 images or 1 video per post.
- **Webhook Sync:** Webhook callbacks are available for post status updates; however, Hermes will use scheduled polling (every 1 hour) to avoid opening public listening ports on the local machine.
