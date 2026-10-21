# Auction Quad Design System & AWS Quick Master Prompt
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
[{"id":"S001","date":"2026-08-01","branch":"มหาวิทยาลัย","product":"อเมริกาโน","category":"กาแฟ","qty":14,"price":60.0,"cost":20.0,"rev":840.0,"profit":560.0},{"id":"S002","date":"2026-08-01","branch":"สำนักงาน","product":"ชาไทย","category":"เครื่องดื่มอื่น","qty":6,"price":55.0,"cost":18.0,"rev":330.0,"profit":222.0},{"id":"S003","date":"2026-08-01","branch":"ห้างสรรพสินค้า","product":"บราวนี","category":"เบเกอรี","qty":5,"price":55.0,"cost":22.0,"rev":275.0,"profit":165.0},{"id":"S004","date":"2026-08-01","branch":"มหาวิทยาลัย","product":"ลาเต้","category":"กาแฟ","qty":7,"price":75.0,"cost":28.0,"rev":525.0,"profit":329.0},{"id":"S005","date":"2026-08-02","branch":"สำนักงาน","product":"โกโก้","category":"เครื่องดื่มอื่น","qty":5,"price":65.0,"cost":25.0,"rev":325.0,"profit":200.0},{"id":"S006","date":"2026-08-02","branch":"ห้างสรรพสินค้า","product":"ชีสเค้ก","category":"เบเกอรี","qty":4,"price":110.0,"cost":72.0,"rev":440.0,"profit":152.0},{"id":"S007","date":"2026-08-02","branch":"มหาวิทยาลัย","product":"คาปูชิโน","category":"กาแฟ","qty":20,"price":75.0,"cost":27.0,"rev":1500.0,"profit":960.0},{"id":"S008","date":"2026-08-03","branch":"สำนักงาน","product":"ครัวซองต์","category":"เบเกอรี","qty":6,"price":85.0,"cost":60.0,"rev":510.0,"profit":150.0},{"id":"S009","date":"2026-08-03","branch":"ห้างสรรพสินค้า","product":"ลาเต้","category":"กาแฟ","qty":9,"price":75.0,"cost":28.0,"rev":675.0,"profit":423.0},{"id":"S010","date":"2026-08-03","branch":"มหาวิทยาลัย","product":"โกโก้","category":"เครื่องดื่มอื่น","qty":13,"price":65.0,"cost":25.0,"rev":845.0,"profit":520.0},{"id":"S011","date":"2026-08-04","branch":"สำนักงาน","product":"ชีสเค้ก","category":"เบเกอรี","qty":13,"price":110.0,"cost":72.0,"rev":1430.0,"profit":494.0},{"id":"S012","date":"2026-08-04","branch":"ห้างสรรพสินค้า","product":"คาปูชิโน","category":"กาแฟ","qty":12,"price":75.0,"cost":27.0,"rev":900.0,"profit":576.0},{"id":"S013","date":"2026-08-04","branch":"มหาวิทยาลัย","product":"ครัวซองต์","category":"เบเกอรี","qty":16,"price":85.0,"cost":60.0,"rev":1360.0,"profit":400.0},{"id":"S014","date":"2026-08-05","branch":"สำนักงาน","product":"อเมริกาโน","category":"กาแฟ","qty":8,"price":60.0,"cost":20.0,"rev":480.0,"profit":320.0},{"id":"S015","date":"2026-08-05","branch":"ห้างสรรพสินค้า","product":"ชาไทย","category":"เครื่องดื่มอื่น","qty":9,"price":55.0,"cost":18.0,"rev":495.0,"profit":333.0},{"id":"S016","date":"2026-08-05","branch":"มหาวิทยาลัย","product":"บราวนี","category":"เบเกอรี","qty":19,"price":55.0,"cost":22.0,"rev":1045.0,"profit":627.0},{"id":"S017","date":"2026-08-05","branch":"สำนักงาน","product":"คาปูชิโน","category":"กาแฟ","qty":5,"price":75.0,"cost":27.0,"rev":375.0,"profit":240.0},{"id":"S018","date":"2026-08-06","branch":"ห้างสรรพสินค้า","product":"ครัวซองต์","category":"เบเกอรี","qty":2,"price":85.0,"cost":60.0,"rev":170.0,"profit":50.0},{"id":"S019","date":"2026-08-06","branch":"มหาวิทยาลัย","product":"อเมริกาโน","category":"กาแฟ","qty":16,"price":60.0,"cost":20.0,"rev":960.0,"profit":640.0},{"id":"S020","date":"2026-08-06","branch":"สำนักงาน","product":"ชาไทย","category":"เครื่องดื่มอื่น","qty":6,"price":55.0,"cost":18.0,"rev":330.0,"profit":222.0},{"id":"S021","date":"2026-08-07","branch":"ห้างสรรพสินค้า","product":"บราวนี","category":"เบเกอรี","qty":9,"price":55.0,"cost":22.0,"rev":495.0,"profit":297.0},{"id":"S022","date":"2026-08-07","branch":"มหาวิทยาลัย","product":"ลาเต้","category":"กาแฟ","qty":19,"price":75.0,"cost":28.0,"rev":1425.0,"profit":893.0},{"id":"S023","date":"2026-08-07","branch":"สำนักงาน","product":"โกโก้","category":"เครื่องดื่มอื่น","qty":9,"price":65.0,"cost":25.0,"rev":585.0,"profit":360.0},{"id":"S024","date":"2026-08-08","branch":"ห้างสรรพสินค้า","product":"ชีสเค้ก","category":"เบเกอรี","qty":4,"price":110.0,"cost":72.0,"rev":440.0,"profit":152.0},{"id":"S025","date":"2026-08-08","branch":"มหาวิทยาลัย","product":"ชาไทย","category":"เครื่องดื่มอื่น","qty":8,"price":55.0,"cost":18.0,"rev":440.0,"profit":296.0},{"id":"S026","date":"2026-08-08","branch":"สำนักงาน","product":"บราวนี","category":"เบเกอรี","qty":14,"price":55.0,"cost":22.0,"rev":770.0,"profit":462.0},{"id":"S027","date":"2026-08-09","branch":"ห้างสรรพสินค้า","product":"ลาเต้","category":"กาแฟ","qty":9,"price":75.0,"cost":28.0,"rev":675.0,"profit":423.0},{"id":"S028","date":"2026-08-09","branch":"มหาวิทยาลัย","product":"โกโก้","category":"เครื่องดื่มอื่น","qty":11,"price":65.0,"cost":25.0,"rev":715.0,"profit":440.0},{"id":"S029","date":"2026-08-09","branch":"สำนักงาน","product":"ชีสเค้ก","category":"เบเกอรี","qty":13,"price":110.0,"cost":72.0,"rev":1430.0,"profit":494.0},{"id":"S030","date":"2026-08-09","branch":"ห้างสรรพสินค้า","product":"คาปูชิโน","category":"กาแฟ","qty":6,"price":75.0,"cost":27.0,"rev":450.0,"profit":288.0},{"id":"S031","date":"2026-08-10","branch":"มหาวิทยาลัย","product":"ครัวซองต์","category":"เบเกอรี","qty":12,"price":85.0,"cost":60.0,"rev":1020.0,"profit":300.0},{"id":"S032","date":"2026-08-10","branch":"สำนักงาน","product":"อเมริกาโน","category":"กาแฟ","qty":6,"price":60.0,"cost":20.0,"rev":360.0,"profit":240.0},{"id":"S033","date":"2026-08-10","branch":"ห้างสรรพสินค้า","product":"โกโก้","category":"เครื่องดื่มอื่น","qty":11,"price":65.0,"cost":25.0,"rev":715.0,"profit":440.0},{"id":"S034","date":"2026-08-11","branch":"มหาวิทยาลัย","product":"ชีสเค้ก","category":"เบเกอรี","qty":13,"price":110.0,"cost":72.0,"rev":1430.0,"profit":494.0},{"id":"S035","date":"2026-08-11","branch":"สำนักงาน","product":"คาปูชิโน","category":"กาแฟ","qty":3,"price":75.0,"cost":27.0,"rev":225.0,"profit":144.0},{"id":"S036","date":"2026-08-11","branch":"ห้างสรรพสินค้า","product":"ครัวซองต์","category":"เบเกอรี","qty":12,"price":85.0,"cost":60.0,"rev":1020.0,"profit":300.0},{"id":"S037","date":"2026-08-12","branch":"มหาวิทยาลัย","product":"อเมริกาโน","category":"กาแฟ","qty":14,"price":60.0,"cost":20.0,"rev":840.0,"profit":560.0},{"id":"S038","date":"2026-08-12","branch":"สำนักงาน","product":"ชาไทย","category":"เครื่องดื่มอื่น","qty":14,"price":55.0,"cost":18.0,"rev":770.0,"profit":518.0},{"id":"S039","date":"2026-08-12","branch":"ห้างสรรพสินค้า","product":"บราวนี","category":"เบเกอรี","qty":3,"price":55.0,"cost":22.0,"rev":165.0,"profit":99.0},{"id":"S040","date":"2026-08-13","branch":"มหาวิทยาลัย","product":"ลาเต้","category":"กาแฟ","qty":13,"price":75.0,"cost":28.0,"rev":975.0,"profit":611.0},{"id":"S041","date":"2026-08-13","branch":"สำนักงาน","product":"ครัวซองต์","category":"เบเกอรี","qty":9,"price":85.0,"cost":60.0,"rev":765.0,"profit":225.0},{"id":"S042","date":"2026-08-13","branch":"ห้างสรรพสินค้า","product":"อเมริกาโน","category":"กาแฟ","qty":10,"price":60.0,"cost":20.0,"rev":600.0,"profit":400.0},{"id":"S043","date":"2026-08-14","branch":"มหาวิทยาลัย","product":"ชาไทย","category":"เครื่องดื่มอื่น","qty":14,"price":55.0,"cost":18.0,"rev":770.0,"profit":518.0},{"id":"S044","date":"2026-08-14","branch":"สำนักงาน","product":"บราวนี","category":"เบเกอรี","qty":4,"price":55.0,"cost":22.0,"rev":220.0,"profit":132.0},{"id":"S045","date":"2026-08-14","branch":"ห้างสรรพสินค้า","product":"ลาเต้","category":"กาแฟ","qty":3,"price":75.0,"cost":28.0,"rev":225.0,"profit":141.0},{"id":"S046","date":"2026-08-14","branch":"มหาวิทยาลัย","product":"โกโก้","category":"เครื่องดื่มอื่น","qty":11,"price":65.0,"cost":25.0,"rev":715.0,"profit":440.0},{"id":"S047","date":"2026-08-15","branch":"สำนักงาน","product":"ชีสเค้ก","category":"เบเกอรี","qty":3,"price":110.0,"cost":72.0,"rev":330.0,"profit":114.0},{"id":"S048","date":"2026-08-15","branch":"ห้างสรรพสินค้า","product":"คาปูชิโน","category":"กาแฟ","qty":4,"price":75.0,"cost":27.0,"rev":300.0,"profit":192.0},{"id":"S049","date":"2026-08-15","branch":"มหาวิทยาลัย","product":"บราวนี","category":"เบเกอรี","qty":12,"price":55.0,"cost":22.0,"rev":660.0,"profit":396.0},{"id":"S050","date":"2026-08-16","branch":"สำนักงาน","product":"ลาเต้","category":"กาแฟ","qty":12,"price":75.0,"cost":28.0,"rev":900.0,"profit":564.0},{"id":"S051","date":"2026-08-16","branch":"ห้างสรรพสินค้า","product":"โกโก้","category":"เครื่องดื่มอื่น","qty":11,"price":65.0,"cost":25.0,"rev":715.0,"profit":440.0},{"id":"S052","date":"2026-08-16","branch":"มหาวิทยาลัย","product":"ชีสเค้ก","category":"เบเกอรี","qty":15,"price":110.0,"cost":72.0,"rev":1650.0,"profit":570.0},{"id":"S053","date":"2026-08-17","branch":"สำนักงาน","product":"คาปูชิโน","category":"กาแฟ","qty":11,"price":75.0,"cost":27.0,"rev":825.0,"profit":528.0},{"id":"S054","date":"2026-08-17","branch":"ห้างสรรพสินค้า","product":"ครัวซองต์","category":"เบเกอรี","qty":2,"price":85.0,"cost":60.0,"rev":170.0,"profit":50.0},{"id":"S055","date":"2026-08-17","branch":"มหาวิทยาลัย","product":"อเมริกาโน","category":"กาแฟ","qty":20,"price":60.0,"cost":20.0,"rev":1200.0,"profit":800.0},{"id":"S056","date":"2026-08-18","branch":"สำนักงาน","product":"ชาไทย","category":"เครื่องดื่มอื่น","qty":14,"price":55.0,"cost":18.0,"rev":770.0,"profit":518.0},{"id":"S057","date":"2026-08-18","branch":"ห้างสรรพสินค้า","product":"ชีสเค้ก","category":"เบเกอรี","qty":9,"price":110.0,"cost":72.0,"rev":990.0,"profit":342.0},{"id":"S058","date":"2026-08-18","branch":"มหาวิทยาลัย","product":"คาปูชิโน","category":"กาแฟ","qty":19,"price":75.0,"cost":27.0,"rev":1425.0,"profit":912.0},{"id":"S059","date":"2026-08-18","branch":"สำนักงาน","product":"ครัวซองต์","category":"เบเกอรี","qty":3,"price":85.0,"cost":60.0,"rev":255.0,"profit":75.0},{"id":"S060","date":"2026-08-19","branch":"ห้างสรรพสินค้า","product":"อเมริกาโน","category":"กาแฟ","qty":12,"price":60.0,"cost":20.0,"rev":720.0,"profit":480.0},{"id":"S061","date":"2026-08-19","branch":"มหาวิทยาลัย","product":"ชาไทย","category":"เครื่องดื่มอื่น","qty":10,"price":55.0,"cost":18.0,"rev":550.0,"profit":370.0},{"id":"S062","date":"2026-08-19","branch":"สำนักงาน","product":"บราวนี","category":"เบเกอรี","qty":4,"price":55.0,"cost":22.0,"rev":220.0,"profit":132.0},{"id":"S063","date":"2026-08-20","branch":"ห้างสรรพสินค้า","product":"ลาเต้","category":"กาแฟ","qty":15,"price":75.0,"cost":28.0,"rev":1125.0,"profit":705.0},{"id":"S064","date":"2026-08-20","branch":"มหาวิทยาลัย","product":"โกโก้","category":"เครื่องดื่มอื่น","qty":19,"price":65.0,"cost":25.0,"rev":1235.0,"profit":760.0},{"id":"S065","date":"2026-08-20","branch":"สำนักงาน","product":"อเมริกาโน","category":"กาแฟ","qty":5,"price":60.0,"cost":20.0,"rev":300.0,"profit":200.0},{"id":"S066","date":"2026-08-21","branch":"ห้างสรรพสินค้า","product":"ชาไทย","category":"เครื่องดื่มอื่น","qty":2,"price":55.0,"cost":18.0,"rev":110.0,"profit":74.0},{"id":"S067","date":"2026-08-21","branch":"มหาวิทยาลัย","product":"บราวนี","category":"เบเกอรี","qty":20,"price":55.0,"cost":22.0,"rev":1100.0,"profit":660.0},{"id":"S068","date":"2026-08-21","branch":"สำนักงาน","product":"ลาเต้","category":"กาแฟ","qty":14,"price":75.0,"cost":28.0,"rev":1050.0,"profit":658.0},{"id":"S069","date":"2026-08-22","branch":"ห้างสรรพสินค้า","product":"โกโก้","category":"เครื่องดื่มอื่น","qty":5,"price":65.0,"cost":25.0,"rev":325.0,"profit":200.0},{"id":"S070","date":"2026-08-22","branch":"มหาวิทยาลัย","product":"ชีสเค้ก","category":"เบเกอรี","qty":13,"price":110.0,"cost":72.0,"rev":1430.0,"profit":494.0},{"id":"S071","date":"2026-08-22","branch":"สำนักงาน","product":"คาปูชิโน","category":"กาแฟ","qty":7,"price":75.0,"cost":27.0,"rev":525.0,"profit":336.0},{"id":"S072","date":"2026-08-23","branch":"ห้างสรรพสินค้า","product":"ครัวซองต์","category":"เบเกอรี","qty":8,"price":85.0,"cost":60.0,"rev":680.0,"profit":200.0},{"id":"S073","date":"2026-08-23","branch":"มหาวิทยาลัย","product":"ลาเต้","category":"กาแฟ","qty":10,"price":75.0,"cost":28.0,"rev":750.0,"profit":470.0},{"id":"S074","date":"2026-08-23","branch":"สำนักงาน","product":"โกโก้","category":"เครื่องดื่มอื่น","qty":2,"price":65.0,"cost":25.0,"rev":130.0,"profit":80.0},{"id":"S075","date":"2026-08-23","branch":"ห้างสรรพสินค้า","product":"ชีสเค้ก","category":"เบเกอรี","qty":9,"price":110.0,"cost":72.0,"rev":990.0,"profit":342.0},{"id":"S076","date":"2026-08-24","branch":"มหาวิทยาลัย","product":"คาปูชิโน","category":"กาแฟ","qty":19,"price":75.0,"cost":27.0,"rev":1425.0,"profit":912.0},{"id":"S077","date":"2026-08-24","branch":"สำนักงาน","product":"ครัวซองต์","category":"เบเกอรี","qty":9,"price":85.0,"cost":60.0,"rev":765.0,"profit":225.0},{"id":"S078","date":"2026-08-24","branch":"ห้างสรรพสินค้า","product":"อเมริกาโน","category":"กาแฟ","qty":12,"price":60.0,"cost":20.0,"rev":720.0,"profit":480.0},{"id":"S079","date":"2026-08-25","branch":"มหาวิทยาลัย","product":"ชาไทย","category":"เครื่องดื่มอื่น","qty":8,"price":55.0,"cost":18.0,"rev":440.0,"profit":296.0},{"id":"S080","date":"2026-08-25","branch":"สำนักงาน","product":"บราวนี","category":"เบเกอรี","qty":10,"price":55.0,"cost":22.0,"rev":550.0,"profit":330.0},{"id":"S081","date":"2026-08-25","branch":"ห้างสรรพสินค้า","product":"คาปูชิโน","category":"กาแฟ","qty":7,"price":75.0,"cost":27.0,"rev":525.0,"profit":336.0},{"id":"S082","date":"2026-08-26","branch":"มหาวิทยาลัย","product":"ครัวซองต์","category":"เบเกอรี","qty":9,"price":85.0,"cost":60.0,"rev":765.0,"profit":225.0},{"id":"S083","date":"2026-08-26","branch":"สำนักงาน","product":"อเมริกาโน","category":"กาแฟ","qty":15,"price":60.0,"cost":20.0,"rev":900.0,"profit":600.0},{"id":"S084","date":"2026-08-26","branch":"ห้างสรรพสินค้า","product":"ชาไทย","category":"เครื่องดื่มอื่น","qty":10,"price":55.0,"cost":18.0,"rev":550.0,"profit":370.0},{"id":"S085","date":"2026-08-27","branch":"มหาวิทยาลัย","product":"บราวนี","category":"เบเกอรี","qty":8,"price":55.0,"cost":22.0,"rev":440.0,"profit":264.0},{"id":"S086","date":"2026-08-27","branch":"สำนักงาน","product":"ลาเต้","category":"กาแฟ","qty":10,"price":75.0,"cost":28.0,"rev":750.0,"profit":470.0},{"id":"S087","date":"2026-08-27","branch":"ห้างสรรพสินค้า","product":"โกโก้","category":"เครื่องดื่มอื่น","qty":11,"price":65.0,"cost":25.0,"rev":715.0,"profit":440.0},{"id":"S088","date":"2026-08-27","branch":"มหาวิทยาลัย","product":"ชีสเค้ก","category":"เบเกอรี","qty":7,"price":110.0,"cost":72.0,"rev":770.0,"profit":266.0},{"id":"S089","date":"2026-08-28","branch":"สำนักงาน","product":"ชาไทย","category":"เครื่องดื่มอื่น","qty":11,"price":55.0,"cost":18.0,"rev":605.0,"profit":407.0},{"id":"S090","date":"2026-08-28","branch":"ห้างสรรพสินค้า","product":"บราวนี","category":"เบเกอรี","qty":2,"price":55.0,"cost":22.0,"rev":110.0,"profit":66.0},{"id":"S091","date":"2026-08-28","branch":"มหาวิทยาลัย","product":"ลาเต้","category":"กาแฟ","qty":14,"price":75.0,"cost":28.0,"rev":1050.0,"profit":658.0},{"id":"S092","date":"2026-08-29","branch":"สำนักงาน","product":"โกโก้","category":"เครื่องดื่มอื่น","qty":10,"price":65.0,"cost":25.0,"rev":650.0,"profit":400.0},{"id":"S093","date":"2026-08-29","branch":"ห้างสรรพสินค้า","product":"ชีสเค้ก","category":"เบเกอรี","qty":5,"price":110.0,"cost":72.0,"rev":550.0,"profit":190.0},{"id":"S094","date":"2026-08-29","branch":"มหาวิทยาลัย","product":"คาปูชิโน","category":"กาแฟ","qty":7,"price":75.0,"cost":27.0,"rev":525.0,"profit":336.0},{"id":"S095","date":"2026-08-30","branch":"สำนักงาน","product":"ครัวซองต์","category":"เบเกอรี","qty":15,"price":85.0,"cost":60.0,"rev":1275.0,"profit":375.0},{"id":"S096","date":"2026-08-30","branch":"ห้างสรรพสินค้า","product":"อเมริกาโน","category":"กาแฟ","qty":8,"price":60.0,"cost":20.0,"rev":480.0,"profit":320.0},{"id":"S097","date":"2026-08-30","branch":"มหาวิทยาลัย","product":"โกโก้","category":"เครื่องดื่มอื่น","qty":20,"price":65.0,"cost":25.0,"rev":1300.0,"profit":800.0},{"id":"S098","date":"2026-08-31","branch":"สำนักงาน","product":"ชีสเค้ก","category":"เบเกอรี","qty":14,"price":110.0,"cost":72.0,"rev":1540.0,"profit":532.0},{"id":"S099","date":"2026-08-31","branch":"ห้างสรรพสินค้า","product":"คาปูชิโน","category":"กาแฟ","qty":5,"price":75.0,"cost":27.0,"rev":375.0,"profit":240.0},{"id":"S100","date":"2026-08-31","branch":"มหาวิทยาลัย","product":"ครัวซองต์","category":"เบเกอรี","qty":15,"price":85.0,"cost":60.0,"rev":1275.0,"profit":375.0}]

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


---

## 🌟 6. ข้อมูลจำเพาะฟีเจอร์เพิ่มเติม (3D Card Pop Up & Dual Theme Switch)

### 6.1 3D Card Pop Up (Interactive 3D Detail Modal with Realistic & Open-Source GLB Models)
* **จุดกระตุ้นการทำงาน (Trigger Points):**
  - คลิกที่รายการสินค้าใดๆ ใน **Quad I (Top Rankings)**
  - คลิกที่แถวสินค้าใน **ตารางรายละเอียดสินค้า × กำไร (Quad II)**
  - คลิกที่การ์ดหมวดหมู่ใน **Quad IV** หรือการ์ด **BCG Insight**
  - คลิกที่การ์ด **Executive KPI Cards**
* **สถาปัตยกรรม 3D Modal (Three.js Studio Engine):**
  - แสดงหน้าต่างลอยตัว (Modal Overlay) แบบ Glassmorphism มีเอฟเฟกต์ `backdrop-filter: blur(12px)`
  - ฝั่งซ้ายคือ **3D Interactive Stage** แสดงโมเดล 3 มิติของสินค้าบนแท่นหมุนเรืองแสง (Reflective Base Pedestal + Cyan Neon Ring):
    - **ชีสเค้กสตรอว์เบอร์รี (Strawberry Cheesecake):** จานของหวานเซรามิกสีขาวมุก, ชิ้นเค้กรูปทรงสามเหลี่ยมมุมตัด (Beveled Triangular Wedge slice สร้างด้วย `ExtrudeGeometry`), ฐานแป้งแครกเกอร์กรุบกรอบ (Graham Cracker Crust), เนื้อครีมชีสเนียนนุ่ม, ซอสเกลซสตรอว์เบอร์รีสีทับทิมเคลือบมันวาว, และผลเบอร์รี 3D ตกแต่งด้านบน
    - **ลาเต้ (Hot Cafe Latte):** จานรองเซรามิก, แก้วกาแฟพร้อมหูจับทรงโค้งมนตามหลักสรีรศาสตร์ (Curved Torus Handle), ผิวกาแฟเอสเปรสโซนุ่มละมุน, และโฟมนมลาเต้อาร์ตรูปหัวใจ (Latte Art Foam Heart)
    - **คาปูชิโน (Hot Cappuccino):** จานรองเซรามิก, แก้วกาแฟ, ฐานกาแฟเอสเปรสโซเข้มข้น, โดมโฟมนมหนานุ่ม, พร้อมผงโกโก้โรยละเอียดบนฟองนม (Fine Cocoa Powder Dusting)
    - **อเมริกาโน (Hot Americano):** จานรองและแก้วกาแฟเซรามิก, กาแฟดำเอสเปรสโซเข้มข้นพร้อมวงประกาย Crema ผิวกาแฟ
    - **ครัวซองต์เนยสด (Butter Croissant):** จานเซรามิกสำหรับเสิร์ฟ, ตัวขนมปังทรงพระจันทร์เสี้ยวโค้งมน 9 ส่วนซ้อนชั้น (9-Segment Curved Crescent Body) พร้อมไล่เฉดสีอบสีทองเหลืองอร่าม
    - **ฟัดจ์บราวนี (Chocolate Fudge Brownie):** จานของหวาน, ก้อนบราวนีทรงลูกบาศก์เนื้อโกโก้เข้มข้น, ซอสช็อกโกแลตราดด้านบน (Glossy Ganache Glaze), และเม็ดวอลนัตคั่วกรุบกรอบ
    - **ชาไทยเย็น (Iced Thai Tea):** ที่รองแก้วสเลท, แก้วทรงกระบอกใส Translucent Highball Glass (`MeshPhysicalMaterial` พร้อม Transmission 85% และ Refraction IOR 1.5), เสาน้ำชาไทยสีส้มอำพัน, ชั้นโฟมนมด้านบน, ก้อนน้ำแข็ง 3D ใสลอยตัว, และหลอดดูดน้ำ
    - **โกโก้เย็น (Iced Cocoa):** ที่รองแก้วสเลท, แก้วใสทรงสูง, เสาน้ำโกโก้ช็อกโกแลตเข้มข้น, ชั้นโฟมนม, ก้อนน้ำแข็งใส 3D, และหลอดดูดน้ำ
    - ควบคุมมุมกล้องอิสระด้วย `OrbitControls` (หมุน 360°, ซูมเข้าออก, ดับเบิลคลิก/แดร็กหมุนได้อย่างลื่นไหล)
  - **ฟังก์ชันรองรับโมเดล Open-Source (.glb / .gltf):**
    - มี **3D Toolbar** อยู่ด้านบนแคนวาส พร้อมปุ่ม **"📂 นำเข้า .GLB"** สามารถเลือกไฟล์โมเดล 3D มาแสดงผลได้ทันที
    - รองรับการ **Drag & Drop** ลากไฟล์ `.glb` หรือ `.gltf` มาวางบนแคนวาส 3D ได้โดยตรง (แสดงเอฟเฟกต์เส้นประเรืองแสงเมื่อลากไฟล์มาวาง)
    - ทำงานแบบ 100% Offline ผ่าน `FileReader` และ `THREE.GLTFLoader` ไม่ติดปัญหา CORS เมื่อเปิดด้วย `file:///`
    - ระบบ **Auto-Fit & Centering** ปรับขนาดและจัดกึ่งกลางโมเดลภายนอกให้พอดีกับแท่นหมุนโดยอัตโนมัติ
    - ปุ่ม **"🔄 รีเซ็ต"** สำหรับสลับกลับสู่โมเดลสมจริงแบบ Procedural ตั้งต้นได้ทันที
    - มีลิงก์แนะนำแหล่งดาวน์โหลดโมเดล 3D อาหารและเครื่องดื่มฟรีแบบลิขสิทธิ์เสรี (CC0 / Open-Source):
      * **Poly Pizza (poly.pizza):** แหล่งรวมโมเดล Low-poly และ Stylized คาเฟ่/เบเกอรี ฟรี CC0
      * **Sketchfab (sketchfab.com):** คลังโมเดล 3D คุณภาพสูง ค้นหาหมวด Food & Drink
      * **Khronos glTF Sample Models:** โมเดลมาตรฐานสากล เช่น DiffuseTransmissionTeacup
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
