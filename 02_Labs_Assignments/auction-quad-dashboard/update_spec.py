import json
import os

base_dir = os.path.join('02_Labs_Assignments', 'auction-quad-dashboard')
compact_path = os.path.join(base_dir, 'sales_compact.json')
md_path = os.path.join(base_dir, 'AUCTION_QUAD_DESIGN_SYSTEM.md')

with open(compact_path, 'r', encoding='utf-8') as f:
    compact_json = f.read()

content = f"""# Auction Quad Design System & AWS Quick Master Prompt
## ระบบดีไซน์และชุดคำสั่งแม่บทสำหรับ Amazon Quick (AWS Quick Suite Action Integration)
**เวอร์ชัน:** 2.0.0 (AWS Quick Ready) | **เป้าหมาย:** สร้าง Dashboard จบงานใน Amazon Quick ได้ทันที  
**Target URL:** [https://quick.aws.com/sn/account/492462084477/start/integrations?tab=action](https://quick.aws.com/sn/account/492462084477/start/integrations?tab=action)  
**วัตถุประสงค์การแข่งขัน:** ชิงคะแนนอันดับ 1 (+10 คะแนน) ด้วยความละเอียดของข้อมูล (Analytical Depth) และ 3D Immersive Elements (Three.js)

---

## ⚡ 1. Master Prompt สำหรับ Copy ไปใส่ใน Amazon Quick (One-Shot Execution)

> [!IMPORTANT]
> **วิธีใช้งานใน Amazon Quick (`quick.aws.com`):**  
> คัดลอกข้อความในบล็อก Markdown ด้านล่างนี้ทั้งหมด แล้วนำไปวางในช่อง **Action Prompt / Instruction** บนหน้าต่าง Amazon Quick AI Builder ระบบจะสร้างและส่งมอบโค้ดแดชบอร์ดที่สมบูรณ์ 100% ในไฟล์เดียวจบงานได้ทันทีโดยไม่ต้องเชื่อมต่อฐานข้อมูลภายนอก

```markdown
คุณคือ Senior Principal UI/UX Architect และ Data Visualization Engineer
จงสร้าง Dashboard ยอดขายภาษาไทยแบบไฟล์ HTML หน้าเดียว (Single-file HTML) ชื่อ "Auction Quad Sales Dashboard" โดยรวม CSS, JavaScript, 3D Three.js และข้อมูล JSON ไว้ในไฟล์เดียว สามารถเปิดบนเบราว์เซอร์ได้ทันทีโดยไม่ต้องติดตั้งโปรแกรมหรือเซิร์ฟเวอร์

### 1. ข้อกำหนดทางธุรกิจและการคำนวณ (Strict Business & Math Logic):
- ข้อมูลจำลองเพื่อการเรียนรู้: ต้องมี Badge ระบุชัดเจนว่า "ข้อมูลจำลองเพื่อการเรียนรู้"
- หน่วยเงิน: ต้องแสดงเป็นสกุลเงินบาท (฿ หรือ บาท) ทุกจุด และใช้ฟอนต์ Prompt คู่กับ font-variant-numeric: tabular-nums
- สูตรการคำนวณ:
  * รายได้ (Revenue) = จำนวนขาย × ราคาขายต่อหน่วย
  * กำไรขั้นต้น (Gross Profit) = จำนวนขาย × (ราคาขายต่อหน่วย − ต้นทุนต่อหน่วย)
  * รวมข้อมูลของสินค้าเดียวกันจากทุกสาขาก่อนนำมาจัดอันดับ
- ตัวเลขตรวจสอบความถูกต้องจากข้อมูลจริง 100 รายการ (ห้ามแต่งตัวเลข):
  * รายได้รวมทั้งสิ้น = ฿72,530.00 บาท
  * จำนวนหน่วยขายรวม = 1,000 หน่วย (100 บิลธุรกรรม)
  * กำไรขั้นต้นรวม = ฿38,825.00 บาท
  * อัตรากำไรขั้นต้น (% GP Margin) = 53.53%
  * สินค้า Top 3 รายได้สูงสุด: 1. ชีสเค้ก (฿13,420), 2. ลาเต้ (฿10,125), 3. ครัวซองต์ (฿10,030)
  * เปรียบเทียบ 3 สาขา: มหาวิทยาลัย (฿33,395 / 46.0%), สำนักงาน (฿21,245 / 29.3%), ห้างสรรพสินค้า (฿17,890 / 24.7%)

### 2. องค์ประกอบ UI และการแสดงผล (Visual & UI Elements):
- สไตล์และธีม: Modern FinTech Dark Glassmorphism พื้นหลังสีกรมท่าเข้ม (#060b18) ขอบกระจกโปร่งแสง (backdrop-filter: blur(16px)) โทนสีหลัก "น้ำเงิน–ส้ม" (Blue #2563eb / Orange #f97316)
- ฟอนต์และไอคอน: โหลด Google Fonts "Prompt" (น้ำหนัก 300, 400, 500, 600, 700) และ Google Material Symbols Rounded ผ่าน CDN
- 3D Immersive Hero (Three.js):
  * ใช้ Three.js (r128) + OrbitControls โหลดผ่าน CDN
  * แสดงแท่นหมุน 3 มิติ (Top 3 Holographic Cylindrical Podium) จัดอันดับสินค้าอันดับ 1, 2, 3
  * สามารถหมุนดูได้ 360 องศาด้วยเมาส์ และมีปุ่มสลับการหมุนอัตโนมัติ (Auto-Rotate)
  * มีปุ่มสลับดู 3D ตาม "รายได้ (Revenue)" หรือ "กำไร (Gross Profit)" โดยแท่ง 3D จะปรับความสูงตามสัดส่วนจริง
  * มีระบบ Fallback 2D อัตโนมัติหากอุปกรณ์ไม่รองรับ WebGL
- การ์ด 4 KPI Matrix: รายได้รวม, จำนวนขายรวม, กำไรขั้นต้นรวม, อัตรากำไรขั้นต้น
- โครงสร้าง 4 มิติ (The 4 Analytical Quadrants):
  * Quad I: จัดอันดับสินค้าขายดี (Bar Chart Top 3 พร้อมปุ่ม Toggle สลับดูทั้ง 8 สินค้า)
  * Quad II: ตารางเปรียบเทียบผลงาน 3 สาขา (จำนวนบิล, ชิ้นขาย, รายได้, สัดส่วน %, กำไร)
  * Quad III: แนวโน้มยอดขายรายวัน 1-31 ส.ค. 2026 พร้อมสถิติวันธรรมดา vs วันหยุด และ Peak Day (21 ส.ค.)
  * Quad IV: โครงสร้างหมวดหมู่สินค้า (เบเกอรี 40.7%, กาแฟ 38.5%, เครื่องดื่มอื่น 20.9%) และ BCG-Style 4-Quadrant Matrix (สินค้าดาวเด่น vs สินค้าเครื่องจักรเงินสด)
- Interactive Cross-Filters:
  * ปุ่ม Filter สาขา (ทั้งหมด, มหาวิทยาลัย, สำนักงาน, ห้างสรรพสินค้า)
  * ปุ่ม Filter หมวดหมู่ (ทุกหมวดหมู่, กาแฟ, เบเกอรี, เครื่องดื่มอื่น)
  * แถบค้นหาธุรกรรมสด (Live Search)
  * เมื่อกด Filter ข้อมูลทุกการ์ด, กราฟ, ตาราง และ 3D Stage ต้อง Recalculate อัปเดตสัมพันธ์กันทันที
- Detailed Transaction Explorer:
  * ตารางแสดงข้อมูลธุรกรรม 100 รายการ พร้อมคลิกหัวคอลัมน์เพื่อ Sort ได้
  * มีระบบแบ่งหน้า (Pagination 10 รายการ/หน้า)
  * มีปุ่ม "ส่งออก CSV (Export CSV)" เพื่อดาวน์โหลดข้อมูลที่กำลังกรองอยู่ได้ทันที

### 3. ชุดข้อมูลธุรกรรมจริง 100 รายการ (Embedded Raw JSON):
นำชุดข้อมูล JSON ด้านล่างนี้ไปฝังเป็นตัวแปร RAW_DATA ในแท็ก <script> ของ HTML โดยตรง:
{compact_json}

จงสร้างและส่งมอบโค้ด HTML ฉบับเต็มที่สมบูรณ์ ไร้ข้อผิดพลาด และพร้อมเซฟเป็น dashboard.html ได้ทันที!
```

---

## 🛠️ 2. การตั้งค่า Action ใน Amazon Quick (AWS Quick Integration Spec)

หากคุณกำลังตั้งค่าในแท็บ **Integrations > Action** ของ Amazon Quick (`https://quick.aws.com/sn/account/492462084477/start/integrations?tab=action`) ให้กำหนดค่าตามสเปกนี้:

```yaml
Integration_Type: Custom AI Action / Web Generator
Action_Name: GenerateAuctionQuadDashboard
Display_Name: Auction Quad — 3D Sales Intelligence Dashboard Generator
Description: >
  Generates a production-grade, standalone single-file HTML sales dashboard 
  with embedded 100-row transactions, Three.js 3D holographic podium, 
  and multi-dimensional cross-filtering analytics (Blue-Orange theme).

Execution_Mode: Direct Single-File HTML Generation
Input_Parameters:
  - name: dataset
    type: JSON
    default: Embedded 100 Cafe Sales Transactions (Aug 2026)
    description: 100 rows containing id, date, branch, product, category, qty, price, cost
  - name: theme_palette
    type: String
    default: "Blue-Orange Modern Dark Glassmorphism"
  - name: immersive_3d_engine
    type: String
    default: "Three.js r128 via CDN with OrbitControls"

Output_Format: text/html (Standalone, Zero Local Dependencies)
```

---

## 🎨 3. ดีไซน์โทเค็นและข้อกำหนดด้านภาพ (Design System Specifications)

### 3.1 ระบบสี Blue–Orange Spectrum
* **Canvas Base:** `#060b18` (กรมท่าเข้มลึกระดับ 95% Black)
* **Glass Surface:** `rgba(13, 23, 46, 0.75)` + `backdrop-filter: blur(16px)`
* **Primary Blue:** `#2563eb` (Core), `#3b82f6` (Light), `#38bdf8` (Neon Cyan Glow)
* **Accent Orange:** `#f97316` (Flame), `#ea580c` (Deep), `#f59e0b` (Amber Gold)
* **Semantic Profit:** `#10b981` (กำไรขั้นต้น / Positive Margin)
* **Semantic Cost:** `#ef4444` (ต้นทุนสินค้า / Expense)
* **Text Primary:** `#f8fafc` (ขาวคมชัด 100%)
* **Text Muted:** `#94a3b8` (เทาเงินสำหรับ Label ตัวชี้วัด)

### 3.2 Typography & Iconography
* **Typography:** Google Fonts `Prompt` (Thai & Latin) — น้ำหนัก 300, 400, 500, 600, 700
* **Tabular Numbers:** กำหนดคลาส `.tabular, td.num-cell` ให้มี `font-variant-numeric: tabular-nums;` เสมอ
* **Icons:** Google `Material Symbols Rounded` ผ่าน CDN:
  - `payments` (รายได้)
  - `inventory_2` (จำนวนขาย)
  - `trending_up` (กำไรขั้นต้น)
  - `percent` (อัตรากำไร)
  - `3d_rotation` (เวที 3D)
  - `storefront` (สาขา)
  - `download` (ส่งออก CSV)

---

## 📐 4. สถาปัตยกรรมข้อมูลและการตรวจสอบความถูกต้อง (Ground Truth Audit)

ชุดข้อมูลธุรกรรม 100 รายการ (S001 ถึง S100) มียอดรวมทางการเงินที่ตรวจสอบแล้วดังนี้:

| มิติการวิเคราะห์ | ค่าตัวเลขที่ถูกต้อง (Exact Calculated Truth) |
| :--- | :--- |
| **ยอดขายรวม (Total Revenue)** | **฿72,530.00** |
| **จำนวนชิ้นขายรวม (Total Units Sold)** | **1,000 หน่วย** |
| **จำนวนบิลธุรกรรมทั้งหมด** | **100 รายการ** |
| **ต้นทุนรวม (Total Cost)** | **฿33,705.00** |
| **กำไรขั้นต้นรวม (Gross Profit)** | **฿38,825.00** |
| **อัตรากำไรขั้นต้น (% GP Margin)** | **53.53%** |
| **ยอดขายเฉลี่ยต่อบิล (AOV)** | **฿725.30** |

### ยอดขายจำแนกรายสินค้า (Top Products Ranking)
1. **ชีสเค้ก (เบเกอรี):** 122 ชิ้น • รายได้ ฿13,420.00 • กำไร ฿4,636.00 (34.5%)
2. **ลาเต้ (กาแฟ):** 135 ชิ้น • รายได้ ฿10,125.00 • กำไร ฿6,345.00 (62.7%)
3. **ครัวซองต์ (เบเกอรี):** 118 ชิ้น • รายได้ ฿10,030.00 • กำไร ฿2,950.00 (29.4%)
4. **คาปูชิโน (กาแฟ):** 125 ชิ้น • รายได้ ฿9,375.00 • กำไร ฿6,000.00 (64.0%)
5. **โกโก้ (เครื่องดื่มอื่น):** 138 ชิ้น • รายได้ ฿8,970.00 • กำไร ฿5,520.00 (61.5%)
6. **อเมริกาโน (กาแฟ):** 140 ชิ้น • รายได้ ฿8,400.00 • กำไร ฿5,600.00 (66.7%)
7. **ชาไทย (เครื่องดื่มอื่น):** 112 ชิ้น • รายได้ ฿6,160.00 • กำไร ฿4,144.00 (67.3%)
8. **บราวนี (เบเกอรี):** 110 ชิ้น • รายได้ ฿6,050.00 • กำไร ฿3,630.00 (60.0%)

### ยอดขายจำแนกรายสาขา (Branch Performance)
* **มหาวิทยาลัย:** 34 บิล • 465 ชิ้น • รายได้ ฿33,395.00 (46.0%) • กำไร ฿18,152.00 (54.4%)
* **สำนักงาน:** 33 บิล • 290 ชิ้น • รายได้ ฿21,245.00 (29.3%) • กำไร ฿10,967.00 (51.6%)
* **ห้างสรรพสินค้า:** 33 บิล • 245 ชิ้น • รายได้ ฿17,890.00 (24.7%) • กำไร ฿9,706.00 (54.3%)

---

## 🚀 5. สรุปขั้นตอนการนำไปจบงานใน Amazon Quick

1. เปิดเบราว์เซอร์ไปที่ลิงก์ของคุณ: [https://quick.aws.com/sn/account/492462084477/start/integrations?tab=action](https://quick.aws.com/sn/account/492462084477/start/integrations?tab=action)
2. คลิกเลือกสร้าง Action หรือใส่คำสั่งในช่อง Chat / Prompt Builder
3. คัดลอกเนื้อหาทั้งหมดใน **หมวดที่ 1 (Master Prompt)** ด้านบนไปวาง
4. สั่งให้ AI รันเพื่อ Generate โค้ด
5. คัดลอกโค้ด HTML ที่ได้บันทึกเป็น `dashboard.html` หรือเปิดพรีวิวใน AWS Quick ได้ทันที 100%
"""

with open(md_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated AUCTION_QUAD_DESIGN_SYSTEM.md successfully!')
