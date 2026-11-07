# Phuriphat Earth Tone Bento Dashboard & 3-Page Academic Submission Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Redesign and build a completely distinct, Minimal Earth Tone & Bento Grid sales analytics web dashboard and 3-page formal academic submission document for student ภูริพัฒน์ เหมกุล (`6752300313`), then submit to PIM e-Learning.

**Architecture:** 
- Frontend: Single-file zero-dependency HTML5/CSS3/JavaScript featuring High-Density Modular Bento Grid, interactive 3D Carousel (CSS 3D perspective transforms), SVG-based interactive gradient area chart and donut charts, inline data bars in a searchable table, 2D Glass Modal popups, and light/dark Earth Tone themes.
- Document: Python `python-docx` script generating an exact 3-page academic document formatted to university standards with full-width hero image, compliance matrix, and deep-dive financial tables.
- Automation: Headless/DevTools screenshot capture and Moodle e-Learning upload verification.

**Tech Stack:** HTML5, CSS3 Glassmorphism & 3D Transforms, Vanilla JavaScript (ES6+), SVG Charts, Python (`python-docx`, `zipfile`), Chrome DevTools Protocol / Browser Automation.

**Spec:** `docs/superpowers/specs/2026-10-29-phuriphat-earthtone-dashboard-design.md`

## Global Constraints
- Target Student: นายภูริพัฒน์ เหมกุล (Phuriphat Hemakul), ID: `6752300313`, Group: 1.2-1 CAI PIM, Email: `phuriphathem@gmail.com`.
- Strict Prompt 1 Compliance: Total Revenue ฿72,530, Volume 1,000 units, Gross Profit ฿38,825 (53.53%), Top 3 Products: ชีสเค้ก (18.5%), ลาเต้ (14.0%), ครัวซองต์ (13.8%).
- Strict Prompt 2 Compliance: Cross-tab 8 products × 3 branches, Category share (Bakery 40.7%, Coffee 38.5%, Other 20.9%), 31-day timeline.
- Anti-Plagiarism Guarantee: 100% distinct identity from class peers (White/Earth Tone theme, Bento Grid, 3D Carousel, no strategic framework section).
- Document Formatting: Exact 3-page academic format in `TH SarabunPSK`.

## Review Focus
1. Bento Grid responsiveness and visual harmony in both Light Mode (White + Earth Tone) and Dark Mode (Inverted Dark Espresso).
2. 3D Carousel mechanics (smooth rotation, card stacking perspective, clear product volume/margin display, keyboard/click navigation).
3. Complete absence of Strategic Framework / Business IT Pillars in both HTML and Word documents.
4. Document page layout integrity (strict 3-page budget: Page 1 Metadata & Highlights, Page 2 Full-Width Hero & Matrix, Page 3 Financial Deep-Dive).
5. Zip archive and Moodle submission verification (all required files present and valid).

---

### Task 1: Construct the Minimal Earth Tone Bento Grid HTML Dashboard
**Files:**
- Create/Modify: `Dashboard-6752300313.html`
- Copy to: `02_Labs_Assignments/Week5/Dashboard-6752300313.html`

**Interfaces:**
- Consumes: Specifications in `docs/superpowers/specs/2026-10-29-phuriphat-earthtone-dashboard-design.md` and dataset numbers.
- Produces: Standalone HTML dashboard ready for preview and screenshot.

- [ ] **Step 1: Write HTML Structure with Bento Grid Layout**
  - Implement Navbar with PIM/CAI title, Live dataset badge, Theme Toggle, and Floating Glass Identity Badge (`6752300313`).
  - Row 1: Bento KPI 4 cards (`Revenue ฿72,530`, `Volume 1,000 pcs`, `Profit ฿38,825`, `Margin 53.53%`) with 3D Tilt and Glowing Accent.
  - Row 2: 3D Carousel showing Top 3 Bestsellers (Cheesecake, Latte, Croissant).
  - Row 3: Split Dual-View (Interactive Gradient Area Chart for 31 days + Category Donut & 3-Branch comparison).
  - Row 4: Searchable Cross-tab Matrix with inline visual data bars and 2D Glass Modal click handler.
  - Footer with student identity and course metadata (No Strategic Framework).

- [ ] **Step 2: Add CSS Styles for Minimal Earth Tone Palette and 3D Carousel**
  - Define CSS custom properties: `--bg-primary: #FDFBF7`, `--surface: #FFFFFF`, `--accent-terracotta: #C86D51`, `--accent-amber: #D98A2C`, `--accent-sage: #6B8E78`, `--text-espresso: #2B231D`, `--border-sand: #E8E2D9`.
  - Dark mode styles: `--bg-primary: #1C1714`, `--surface: #26201B`, `--text-espresso: #F4EFEA`.
  - CSS 3D perspective rules: `perspective: 1000px`, `transform-style: preserve-3d`.

- [ ] **Step 3: Implement Vanilla JS Interactivity**
  - 3D Carousel slide rotation logic (Next/Prev buttons and auto-rotate option).
  - 31-day Area chart hover tooltip tracker.
  - Table real-time search filter and column sort.
  - 2D Glass Modal trigger for product drill-down details.

- [ ] **Step 4: Synchronize to Week5 directory**
  - Copy `Dashboard-6752300313.html` to `02_Labs_Assignments/Week5/Dashboard-6752300313.html`.

- [ ] **Step 5: Verify HTML rendering and data accuracy**
  - Verify all KPI totals, Top 3 shares, and branch amounts via headless test script.

---

### Task 2: Capture High-Resolution Full-Page Screenshots
**Files:**
- Create: `dashboard_preview_6752300313.png`
- Create: `02_Labs_Assignments/Week5/dashboard_preview.png`
- Create: `dashboard_carousel_focus.png` (optional high-res detail image for docx)

**Interfaces:**
- Consumes: `Dashboard-6752300313.html`
- Produces: PNG screenshots for document embedding and submission zip.

- [ ] **Step 1: Capture full dashboard screenshot using browser automation**
  - Launch Chrome/Edge to load `Dashboard-6752300313.html`.
  - Take full-page viewport screenshot at 1600x1200 or higher resolution.
  - Save to `dashboard_preview_6752300313.png` and `02_Labs_Assignments/Week5/dashboard_preview.png`.

- [ ] **Step 2: Validate screenshot visual output**
  - Verify that Bento boxes, 3D Carousel, charts, table, and student badge are clearly visible and cleanly rendered.

---

### Task 3: Develop 3-Page Academic Submission Document Script
**Files:**
- Modify: `create_phuriphat_dashboard_submission_doc.py`
- Generate: `Dashboard-6752300313-Submission.docx`
- Copy to: `02_Labs_Assignments/Week5/Dashboard-6752300313-Submission.docx`

**Interfaces:**
- Consumes: `dashboard_preview_6752300313.png` and sales statistics dataset.
- Produces: 3-page formal academic docx adhering strictly to PIM formatting.

- [ ] **Step 1: Build Page 1 - Metadata & Executive Summary**
  - Banner header: PIM CAI SC60107 with subtle Earth Tone accent.
  - 2-Column Student Metadata Table (Phuriphat Hemakul, 6752300313, 1.2-1 CAI).
  - Highlighted Callout Box with direct links and instructions for `Dashboard-6752300313.html` and dataset.
  - Balanced Technical & Business Highlights Table (Bento Grid, 3D Carousel, Prompt 1 & 2 figures).

- [ ] **Step 2: Build Page 2 - Visual Hero & Compliance Matrix**
  - Insert page break.
  - Frameless full-width hero image of the live dashboard screenshot with academic caption.
  - 3-Column Requirement Compliance Matrix (Prompt 1 KPIs, Prompt 2 Analytics Dimensions, Non-Functional Standards - all marked "ครบถ้วน 100%").

- [ ] **Step 3: Build Page 3 - Deep-Dive Financial & Sales Performance Tables**
  - Insert page break.
  - Section title: "รายงานแจกแจงสถิติผลประกอบการและมิติข้อมูลเจาะลึก (Financial & Sales Deep-Dive)".
  - Comprehensive Table 1: Product Master Breakdown (8 products: Revenue, Volume, Cost, Profit, Margin %).
  - Comprehensive Table 2: 3-Branch Performance Breakdown (University, Office, Mall with transaction count and revenue share).
  - Academic Verification note and sign-off.

- [ ] **Step 4: Execute script and verify 3-page layout**
  - Run `python create_phuriphat_dashboard_submission_doc.py`.
  - Confirm file size, paragraph heights, and exact 3-page boundary.
  - Copy output to `02_Labs_Assignments/Week5/Dashboard-6752300313-Submission.docx`.

---

### Task 4: Package Zip Archive and Verify Submission Bundle
**Files:**
- Create: `Dashboard-6752300313.zip`
- Copy to: `02_Labs_Assignments/Week5/Dashboard-6752300313.zip`

**Interfaces:**
- Consumes: `Dashboard-6752300313.html`, `dashboard_preview.png`, `1Amazon_Quick_Workshop test.xlsx`.
- Produces: ZIP file conforming to submission guidelines.

- [ ] **Step 1: Create ZIP archive with required deliverables**
  - Pack `Dashboard-6752300313.html`, `dashboard_preview.png`, and `1Amazon_Quick_Workshop test.xlsx`.
  - Ensure total archive size is well within Moodle limits (< 10 MB).

- [ ] **Step 2: Verify contents of ZIP archive**
  - List and test extraction of files from `Dashboard-6752300313.zip`.
  - Copy archive to `02_Labs_Assignments/Week5/Dashboard-6752300313.zip`.

---

### Task 5: Upload Deliverables to PIM e-Learning
**Files:**
- Target URL: `https://new-elearning.pim.ac.th/mod/assign/view.php?id=573236`
- Uploads: `Dashboard-6752300313-Submission.docx` and `Dashboard-6752300313.zip`
- Output: `workshop_screenshots/phuriphat_dashboard_earthtone_completed.png`

**Interfaces:**
- Consumes: Moodle session in Chrome, updated `.docx` and `.zip` files.
- Produces: Completed submission on Moodle and screenshot proof.

- [ ] **Step 1: Access Assignment Submission on PIM e-Learning**
  - Navigate to assignment page ID `573236`.
  - Click "แก้ไขงานที่ส่ง" (Edit submission).

- [ ] **Step 2: Upload updated files and overwrite previous versions**
  - Upload `Dashboard-6752300313-Submission.docx`.
  - Upload `Dashboard-6752300313.zip`.
  - Handle overwrite confirmation modals cleanly.

- [ ] **Step 3: Save changes and verify submission status**
  - Click "บันทึกการเปลี่ยนแปลง" (Save changes).
  - Capture full confirmation screenshot showing both uploaded files, submission timestamp, and student name `6752300313 PHURIPHAT HAEMAKUL`.
