import os

base_dir = os.path.dirname(os.path.abspath(__file__))
md_path = os.path.join(base_dir, 'AUCTION_QUAD_DESIGN_SYSTEM.md')

with open(md_path, 'r', encoding='utf-8') as f:
    existing = f.read()

# Add detailed section for 3D Pop-Up and Light/Dark Mode
addon_spec = """
---

## 🌟 6. ข้อมูลจำเพาะฟีเจอร์เพิ่มเติม (3D Card Pop Up & Dual Theme Switch)

### 6.1 3D Card Pop Up (Interactive 3D Detail Modal)
* **จุดกระตุ้นการทำงาน (Trigger Points):**
  - คลิกที่รายการสินค้าใดๆ ใน **Quad I (Top Rankings)**
  - คลิกที่แถวสินค้าใน **ตารางรายละเอียดสินค้า × กำไร (Quad II)**
  - คลิกที่การ์ดหมวดหมู่ใน **Quad IV** หรือการ์ด **BCG Insight**
  - คลิกที่การ์ด **Executive KPI Cards**
* **สถาปัตยกรรม 3D Modal (Three.js Engine):**
  - แสดงหน้าต่างลอยตัว (Modal Overlay) แบบ Glassmorphism มีเอฟเฟกต์ `backdrop-filter: blur(12px)`
  - ฝั่งซ้ายคือ **3D Interactive Stage** แสดงโมเดล 3 มิติของสินค้าบนแท่นหมุนเรืองแสง (Reflective Base + Neon Ring):
    - **หมวดเบเกอรี (Bakery):** เรนเดอร์เป็นเค้กทรงกระบอก 2 ชั้น (Tiered Cylinder) สีทองแอมเบอร์ `#f59e0b`
    - **หมวดกาแฟ (Coffee):** เรนเดอร์เป็นแก้วกาแฟพร้อมชั้นโฟม (Coffee Cup with Foam Rim) สีกรมท่าแซฟไฟร์ `#3b82f6`
    - **หมวดเครื่องดื่มอื่น (Drinks):** เรนเดอร์เป็นแก้วปริซึมเรืองแสง (Faceted Prism) สีเขียวมรกต `#10b981`
    - ควบคุมมุมกล้องอิสระด้วย `OrbitControls` (หมุน 360°, ซูมเข้าออก, มีระบบหมุนอัตโนมัติ)
  - ฝั่งขวาคือ **Detailed Financial Matrix**:
    - ราคาขายต่อหน่วย, ต้นทุนต่อหน่วย, กำไรต่อหน่วย และอัตรากำไรขั้นต้น (GP Margin %)
    - ยอดขายรวมทั้งสิ้น (ชิ้น, รายได้, กำไร)
    - แถบความคืบหน้า (Progress Bars) สัดส่วนยอดขายแยกตาม 3 สาขา (มหาวิทยาลัย, สำนักงาน, ห้างสรรพสินค้า)
  - **การปิดหน้าต่าง:** รองรับทั้งการคลิกปุ่ม `×`, คลิกพื้นหลัง (Backdrop Click) หรือกดปุ่ม `Escape` บนคีย์บอร์ด

### 6.2 ระบบสลับโหมดสว่างและโหมดมืด (Light Mode & Dark Mode Switch)
* **ตำแหน่งปุ่ม:** วางอยู่บนแถบ Navigation ด้านขวา (`.nav-right`) ติดกับ Badge แสดงข้อมูลจำลอง
* **ปุ่มสลับ (Theme Switcher):** ใช้ไอคอน Material Symbols Rounded (`light_mode` สัญลักษณ์ดวงอาทิตย์ในโหมดมืด และ `dark_mode` สัญลักษณ์พระจันทร์ในโหมดสว่าง) พร้อมแอนิเมชันหมุน 15 องศาเมื่อนำเมาส์ไปชี้
* **การจดจำสถานะ (Persistence):** บันทึกค่าลงใน `localStorage.setItem('aq_theme', theme)` เมื่อเปิดเว็บใหม่จะโหลดโหมดเดิมที่ผู้ใช้เลือกไว้ทันที
* **ตารางเปรียบเทียบโทเค็นสี (Dual-Theme Color Tokens):**

| CSS Token | Dark Theme (Default) | Light Theme | วัตถุประสงค์การใช้งาน |
| :--- | :--- | :--- | :--- |
| `--canvas` | `#060b18` (Dark Navy 95%) | `#f8fafc` (Clean Slate 50) | พื้นหลังหลักทั้งหน้าจอ |
| `--glass` | `rgba(13, 23, 46, 0.75)` | `rgba(255, 255, 255, 0.88)` | แผงการ์ด Glassmorphism |
| `--glass-b` | `rgba(255, 255, 255, 0.08)`| `rgba(0, 0, 0, 0.08)` | เส้นขอบแผงการ์ดบางคมชัด |
| `--txt` | `#f8fafc` (Off-white) | `#0f172a` (Slate 900) | สีตัวอักษรหลัก |
| `--muted` | `#94a3b8` (Slate 400) | `#64748b` (Slate 500) | สีคำอธิบายและ Label |
| `--blue` | `#2563eb` | `#2563eb` | สีเอกลักษณ์หลัก (น้ำเงิน) |
| `--orange` | `#f97316` | `#ea580c` | สีไฮไลต์และแอ็กชัน (ส้ม) |
| `--modal-bg` | `#0c162e` | `#ffffff` | พื้นหลังของหน้าต่าง 3D Modal |
"""

# Append or update section 6 in the markdown
if "## 🌟 6. ข้อมูลจำเพาะฟีเจอร์เพิ่มเติม" not in existing:
    updated = existing + "\n" + addon_spec
else:
    parts = existing.split("## 🌟 6. ข้อมูลจำเพาะฟีเจอร์เพิ่มเติม")
    updated = parts[0] + addon_spec

with open(md_path, 'w', encoding='utf-8') as f:
    f.write(updated)

print('Updated AUCTION_QUAD_DESIGN_SYSTEM.md with Section 6 successfully!')
