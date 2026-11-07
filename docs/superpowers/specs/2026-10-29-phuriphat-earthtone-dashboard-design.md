# Design Specification: Phuriphat Hemakul Dashboard & 3-Page Submission Document
**Document ID:** `2026-10-29-phuriphat-earthtone-dashboard-design`  
**Author:** Senior Software Engineer (Antigravity)  
**Student:** นายภูริพัฒน์ เหมกุล (Phuriphat Hemakul)  
**Student ID:** `6752300313` | กลุ่ม 1.2-1 สาขาวิศวกรรมคอมพิวเตอร์และปัญญาประดิษฐ์ (CAI)  
**Course:** SC60107 การจัดการเทคโนโลยีสารสนเทศทางธุรกิจ (Business IT Management)  
**Date:** 29 ตุลาคม 2569  

---

## 1. Intent & Executive Summary
การออกแบบและพัฒนาแดชบอร์ดวิเคราะห์ยอดขาย (Cafe & Bakery Sales Analytics Dashboard) พร้อมเอกสารส่งมอบงานทางวิชาการฉบับสมบูรณ์ (3 หน้า) เพื่อส่งในระบบ PIM e-Learning (10 คะแนน) โดยสร้างอัตลักษณ์เฉพาะตัวของนายภูริพัฒน์ เหมกุล ให้มีความแตกต่างจากเพื่อนร่วมชั้นเรียน 100% ทั้งในมิติแนวคิดสถาปัตยกรรม (High-Density Modular Bento Grid), ปฏิสัมพันธ์ 3D (3D Carousel), โทนสี Minimal Earth Tone & Sand, ตลอดจนรูปแบบเอกสารวิชาการทางการมาตรฐานสถาบัน

---

## 2. Core Constraints & Boundaries
1. **Zero Overlap Guarantee:** ไม่มีความซ้ำซ้อนกับผลงานของนักศึกษาอื่น (เช่น สไตล์ Emerald Executive BI ขององอาจ โพธิ์ดี 6752301409) ทั้งด้าน Palette, Typography, Component Layout และ Code Structure
2. **No Strategic Framework Section:** ถอดส่วนกรอบกลยุทธ์ (Strategic Framework) ออกทั้งหมดตามคำสั่งผู้ใช้งาน มุ่งเน้นการวิเคราะห์ข้อมูลเชิงลึก (Data & Sales Performance Analytics)
3. **100% Strict Prompt Compliance:**
   - **Prompt 1:** รายได้รวม `฿72,530`, ปริมาณขาย `1,000` ชิ้น, กำไรขั้นต้น `฿38,825` (`53.53%`), Top 3 สินค้า (ชีสเค้ก, ลาเต้, ครัวซองต์)
   - **Prompt 2:** ตาราง Cross-tab สินค้า 8 รายการ × 3 สาขา, สัดส่วนรายได้แยกตามหมวดหมู่ (เบเกอรี 40.7%, กาแฟ 38.5%, เครื่องดื่มอื่น 20.9%), แนวโน้มยอดขายรายวันตลอด 31 วัน
4. **Standalone & Offline Native:** ทำงานได้ 100% บนเบราว์เซอร์โดยไม่มี Dependency ภายนอกที่ไม่จำเป็น

---

## 3. Part 1: Dashboard UI/UX Specification

### 3.1 Design System & Palette (Minimal Earth Tone)
- **Primary Background (Light Mode - Default):** `#FDFBF7` (Alabaster Cream / Warm White)
- **Card & Surface Background:** `#FFFFFF` with subtle border `#E8E2D9` (Sand Stone) and soft shadow `rgba(43, 35, 29, 0.04)`
- **Accent Primary (Terracotta / Warm Clay):** `#C86D51` (ใช้สำหรับปุ่มสำคัญ, ไฮไลต์, เส้นกราฟหลัก)
- **Accent Secondary (Warm Amber / Ochre):** `#D98A2C`
- **Muted Natural Accent (Sage Green):** `#6B8E78` (ใช้กับ Margin, กำไร, สถานะสำเร็จ)
- **Primary Text:** `#2B231D` (Deep Espresso)
- **Secondary Text:** `#6E655F` (Warm Slate / Clay Grey)
- **Inverted Dark Mode (Toggle):** Deep Dark Espresso `#1C1714`, Card Surface `#26201B`, Border `#3D342C`, Text `#F4EFEA`

### 3.2 Layout: High-Density Modular Bento Grid
โครงสร้างหน้าจอจัดวางแบบ Bento Box ที่มีสัดส่วนสมมาตรและลื่นไหล:
- **Navbar Header:**
  - โลโก้ & ชื่อระบบ: `CAI · Cafe & Bakery Performance Analytics`
  - กล่องแสดงสถานะ: Live Dataset `1Amazon_Quick_Workshop test.xlsx`
  - ปุ่ม Toggle Dark/Light Mode (Earth Tone Invert)
  - **Integrated Floating Glass Badge:** นายภูริพัฒน์ เหมกุล | รหัส `6752300313` | กลุ่ม 1.2-1 CAI PIM
- **Row 1 - Bento KPI Metrics (4 การ์ดพร้อม 3D Tilt & Glowing Accent):**
  - Card 1: รายได้รวม `฿72,530` (เทียบเป้าหมาย, ไอคอนยอดเงิน, เรืองแสง Terracotta)
  - Card 2: ปริมาณการขาย `1,000` ชิ้น (เทียบความจุ, ไอคอนตะกร้า, เรืองแสง Amber)
  - Card 3: กำไรขั้นต้น `฿38,825` (ไอคอนกราฟกำไร, เรืองแสง Sage Green)
  - Card 4: อัตรากำไรสุทธิ `53.53%` (ไอคอนเปอร์เซ็นต์, เรืองแสง Sage/Clay)
- **Row 2 - Interactive 3D Carousel (Top 3 Bestsellers):**
  - คอมโพเนนต์ 3D Carousel แสดงสินค้าขายดีอันดับ 1 (ชีสเค้ก ฿13,440), อันดับ 2 (ลาเต้ ฿10,120), อันดับ 3 (ครัวซองต์ ฿10,000)
  - มีปุ่มหมุนสลับการ์ด 3D พร้อมแสดงสถิติ Margin และสัดส่วนยอดขาย
- **Row 3 - Sales Dynamics & Distribution (Split Dual-View):**
  - **Left Box (60%):** Interactive Gradient Area Chart with Cursor Tooltip แสดงยอดขายตลอด 31 วัน
  - **Right Box (40%):** Donut Chart แสดงสัดส่วนหมวดหมู่ (เบเกอรี 40.7%, กาแฟ 38.5%, เครื่องดื่มอื่น 20.9%) ควบคู่กับแท่งสัดส่วน 3 สาขา (มหาวิทยาลัย 46.04%, อาคารสำนักงาน 31.96%, ห้างสรรพสินค้า 22.00%)
- **Row 4 - Interactive Cross-Tab Matrix (Product × Branch):**
  - ตารางไขว้สินค้า 8 ชนิด × 3 สาขา
  - มีช่อง Search & Filter สินค้าแบบ Realtime
  - มี Inline Data Bar แสดงสัดส่วนยอดขายในเซลล์ตาราง
  - คลิกที่แถวสินค้าเพื่อเปิด **2D Glass Modal Popup** เจาะลึกต้นทุน กำไร และส่วนแบ่งสาขา
- **Footer:** ข้อมูลวิชา SC60107, สถาบันการจัดการปัญญาภิวัฒน์, สิทธิ์ผลงานเฉพาะบุคคล ภูริพัฒน์ เหมกุล

---

## 4. Part 2: Submission Document Specification (`Dashboard-6752300313-Submission.docx`)

### 4.1 รูปแบบเอกสาร (Pure Academic Black & White with Earth Tone Accent)
- ความยาวเอกสาร: **3 หน้าบริบูรณ์** จัดหน้าสวยงามตามระเบียบสถาบัน
- ฟอนต์: **TH SarabunPSK** (หัวข้อ 16-18pt ตัวหนา, เนื้อหา 15pt, คำบรรยายภาพ 13pt)
- ขอบกระดาษ: บน-ล่าง 0.45 นิ้ว, ซ้าย-ขวา 0.6 นิ้ว

### 4.2 โครงสร้างเนื้อหา 3 หน้า
- **หน้า 1: ข้อมูลนักศึกษา, สรุปผลงาน & ไฮไลต์, ช่องทางการตรวจงาน**
  - ส่วนหัวเอกสาร: แบนเนอร์ PIM CAI SC60107 หัวกระดาษ
  - ตารางข้อมูลนักศึกษา: 2-Column Clean Metadata Grid (ชื่อ-สกุล, รหัส 6752300313, กลุ่ม 1.2-1, อีเมล, วันที่ส่ง)
  - กล่องช่องทางการเข้าชม (Highlighted Callout Box): อธิบายไฟล์ `Dashboard-6752300313.html`, ไฟล์ข้อมูล `1Amazon_Quick_Workshop test.xlsx`, และ `Dashboard-6752300313.zip`
  - ตารางสรุปไฮไลต์ Balanced Technical & Business Matrix (แบ่ง 2 ฝั่งชัดเจน: ฝั่ง UI Bento & 3D Carousel vs ฝั่งความถูกต้องของตัวเลข Prompt 1 & 2)
- **หน้า 2: ภาพแคปหน้าจอจริง & ตารางความสอดคล้องตามเกณฑ์ประเมิน**
  - ภาพแคปหน้าจอ Dashboard จริง: Frameless Full-Width Hero Image ความละเอียดสูง
  - คำบรรยายใต้ภาพสไตล์นิตยสารวิชาการ
  - ตารางตรวจสอบความสอดคล้องตามเกณฑ์ประเมิน (Requirement Compliance Matrix 3 คอลัมน์): เกณฑ์ | รายละเอียดผลงาน Prompt 1 & 2 | สถานะครบถ้วน 100%
- **หน้า 3: การแจกแจงตัวเลขสถิติและมิติข้อมูลเชิงลึก (Deep-Dive Performance Breakdown)**
  - ตารางสรุปตัวเลขสถิติสินค้า 8 รายการ (ยอดขาย, ปริมาณ, ต้นทุน, กำไร, Margin %)
  - ตารางเปรียบเทียบยอดขาย 3 สาขา (มหาวิทยาลัย, อาคารสำนักงาน, ห้างสรรพสินค้า)
  - สรุปตัวเลขทางการตามโจทย์อาจารย์ ครบถ้วนตามมาตรฐานการจัดการเทคโนโลยีสารสนเทศทางธุรกิจ SC60107

---

## 5. Verification & Submission Workflow
1. ปรับปรุงโค้ด `Dashboard-6752300313.html` ให้ได้ตาม Bento Grid, 3D Carousel, Minimal Earth Tone
2. ถ่ายภาพความละเอียดสูง `dashboard_preview_6752300313.png`
3. เขียนสคริปต์สร้างเอกสาร Word 3 หน้า `Dashboard-6752300313-Submission.docx`
4. แพ็กเกจ `Dashboard-6752300313.zip`
5. ส่งมอบไฟล์ผ่าน Moodle PIM e-Learning (ID: 573236)
