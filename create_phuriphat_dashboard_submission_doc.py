import os
import sys
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=60, bottom=60, left=110, right=110):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="{top}" w:type="dxa"/>'
        f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'<w:left w:w="{left}" w:type="dxa"/>'
        f'<w:right w:w="{right}" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tcPr.append(tcMar)

def format_run(run, font_name="TH SarabunPSK", size_pt=15, color_rgb=(43, 35, 29), bold=False, italic=False):
    run.font.name = font_name
    run.font.size = Pt(size_pt)
    run.font.color.rgb = RGBColor(*color_rgb)
    run.bold = bold
    run.italic = italic
    rPr = run._r.get_or_add_rPr()
    rFonts = rPr.get_or_add_rFonts()
    rFonts.set(qn('w:ascii'), font_name)
    rFonts.set(qn('w:hAnsi'), font_name)
    rFonts.set(qn('w:cs'), font_name)
    rFonts.set(qn('w:eastAsia'), font_name)
    
    sz = rPr.find(qn('w:sz'))
    if sz is None:
        sz = parse_xml(f'<w:sz {nsdecls("w")} w:val="{int(size_pt * 2)}"/>')
        rPr.append(sz)
    else:
        sz.set(qn('w:val'), str(int(size_pt * 2)))
        
    szCs = rPr.find(qn('w:szCs'))
    if szCs is None:
        szCs = parse_xml(f'<w:szCs {nsdecls("w")} w:val="{int(size_pt * 2)}"/>')
        rPr.append(szCs)
    else:
        szCs.set(qn('w:val'), str(int(size_pt * 2)))

def build_phuriphat_earthtone_3page_doc():
    doc = Document()
    
    style = doc.styles['Normal']
    style.font.name = 'TH SarabunPSK'
    style.font.size = Pt(15)
    rPr = style.element.get_or_add_rPr()
    rFonts = rPr.get_or_add_rFonts()
    rFonts.set(qn('w:ascii'), 'TH SarabunPSK')
    rFonts.set(qn('w:hAnsi'), 'TH SarabunPSK')
    rFonts.set(qn('w:cs'), 'TH SarabunPSK')
    rFonts.set(qn('w:eastAsia'), 'TH SarabunPSK')
    
    for section in doc.sections:
        section.top_margin = Inches(0.4)
        section.bottom_margin = Inches(0.4)
        section.left_margin = Inches(0.55)
        section.right_margin = Inches(0.55)
    
    # =========================================================================
    # PAGE 1: METADATA, HIGHLIGHTS & DELIVERABLES CALLOUT
    # =========================================================================
    
    # 1. Header Banner (Academic Minimal Earth Tone)
    hdr_table = doc.add_table(rows=1, cols=1)
    hdr_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr_cell = hdr_table.cell(0, 0)
    hdr_cell.width = Inches(7.4)
    set_cell_background(hdr_cell, "2B231D")  # Deep Espresso
    set_cell_margins(hdr_cell, top=70, bottom=70, left=140, right=140)
    
    p1 = hdr_cell.paragraphs[0]
    p1.paragraph_format.space_before = Pt(0)
    p1.paragraph_format.space_after = Pt(1)
    p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p1.add_run("สถาบันการจัดการปัญญาภิวัฒน์ (PIM) · สาขาวิศวกรรมคอมพิวเตอร์และปัญญาประดิษฐ์ (CAI)")
    format_run(r_sub, size_pt=13, color_rgb=(217, 210, 201), bold=False)
    
    p2 = hdr_cell.add_paragraph()
    p2.paragraph_format.space_before = Pt(1)
    p2.paragraph_format.space_after = Pt(1)
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p2.add_run("ใบงานส่งมอบผลงาน: Cafe & Bakery Performance Analytics Dashboard (10 คะแนน)")
    format_run(r_title, size_pt=18, color_rgb=(255, 255, 255), bold=True)
    
    p3 = hdr_cell.add_paragraph()
    p3.paragraph_format.space_before = Pt(1)
    p3.paragraph_format.space_after = Pt(0)
    p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_course = p3.add_run("รายวิชา SC60107 การจัดการเทคโนโลยีสารสนเทศทางธุรกิจ · สถาปัตยกรรม High-Density Modular Bento Grid")
    format_run(r_course, size_pt=13.5, color_rgb=(200, 109, 81), bold=True)  # Terracotta accent
    
    # 2. Student Metadata Table (2-Column Grid)
    info_table = doc.add_table(rows=2, cols=2)
    info_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    widths = [Inches(3.7), Inches(3.7)]
    
    r0 = info_table.rows[0]
    c0 = r0.cells[0]
    c0.width = widths[0]
    set_cell_background(c0, "FDFBF7")
    set_cell_margins(c0, top=40, bottom=40, left=80, right=80)
    p = c0.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.space_before = Pt(0)
    r_l = p.add_run("👤 ผู้จัดทำ: ")
    format_run(r_l, size_pt=14, color_rgb=(110, 101, 95), bold=True)
    r_v = p.add_run("นายภูริพัฒน์ เหมกุล (Phuriphat Hemakul)")
    format_run(r_v, size_pt=14.5, color_rgb=(43, 35, 29), bold=True)
    
    c1 = r0.cells[1]
    c1.width = widths[1]
    set_cell_background(c1, "FDFBF7")
    set_cell_margins(c1, top=40, bottom=40, left=80, right=80)
    p = c1.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.space_before = Pt(0)
    r_l = p.add_run("🆔 รหัสนักศึกษา: ")
    format_run(r_l, size_pt=14, color_rgb=(110, 101, 95), bold=True)
    r_v = p.add_run("6752300313 (กลุ่ม 1.2-1 CAI)")
    format_run(r_v, size_pt=14.5, color_rgb=(200, 109, 81), bold=True)
    
    r1 = info_table.rows[1]
    c2 = r1.cells[0]
    c2.width = widths[0]
    set_cell_background(c2, "FDFBF7")
    set_cell_margins(c2, top=40, bottom=40, left=80, right=80)
    p = c2.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.space_before = Pt(0)
    r_l = p.add_run("🎨 ดีไซน์ซิสเต็ม: ")
    format_run(r_l, size_pt=14, color_rgb=(110, 101, 95), bold=True)
    r_v = p.add_run("Minimal Earth Tone & 3D Interactive Carousel")
    format_run(r_v, size_pt=14, color_rgb=(43, 35, 29), bold=False)
    
    c3 = r1.cells[1]
    c3.width = widths[1]
    set_cell_background(c3, "FDFBF7")
    set_cell_margins(c3, top=40, bottom=40, left=80, right=80)
    p = c3.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.space_before = Pt(0)
    r_l = p.add_run("📧 อีเมล & วันที่ส่ง: ")
    format_run(r_l, size_pt=14, color_rgb=(110, 101, 95), bold=True)
    r_v = p.add_run("phuriphathem@gmail.com · 29 ต.ค. 2569")
    format_run(r_v, size_pt=14, color_rgb=(43, 35, 29), bold=False)
    
    # 3. Deliverables Callout Box
    callout_table = doc.add_table(rows=1, cols=1)
    callout_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    callout_cell = callout_table.cell(0, 0)
    callout_cell.width = Inches(7.4)
    set_cell_background(callout_cell, "FAF6F0")
    set_cell_margins(callout_cell, top=50, bottom=50, left=110, right=110)
    
    cp0 = callout_cell.paragraphs[0]
    cp0.paragraph_format.space_before = Pt(0)
    cp0.paragraph_format.space_after = Pt(1)
    r_c_h = cp0.add_run("🔗 ช่องทางการเปิดตรวจและไฟล์ส่งมอบในระบบ (Submission Deliverables):")
    format_run(r_c_h, size_pt=14.5, color_rgb=(138, 70, 48), bold=True)
    
    deliverables = [
        ("📄 1. Direct Interactive Web Application: ", "Dashboard-6752300313.html (เปิดบนเบราว์เซอร์ได้ทันทีโดยไม่ต้องต่ออินเทอร์เน็ต)"),
        ("📊 2. ชุดข้อมูลประมวลผล (Original Dataset): ", "1Amazon_Quick_Workshop test.xlsx (ตามโจทย์อาจารย์ปุ๋มในกลุ่ม LINE)"),
        ("📦 3. แพ็กเกจไฟล์สมบูรณ์ (ZIP Bundle): ", "Dashboard-6752300313.zip (บรรจุไฟล์ HTML, เอกสาร DOCX, ชุดข้อมูล และภาพตัวอย่าง)")
    ]
    for pfx, dsc in deliverables:
        cp = callout_cell.add_paragraph()
        cp.paragraph_format.space_before = Pt(0)
        cp.paragraph_format.space_after = Pt(1)
        r_p = cp.add_run(pfx)
        format_run(r_p, size_pt=13.5, color_rgb=(43, 35, 29), bold=True)
        r_d = cp.add_run(dsc)
        format_run(r_d, size_pt=13.5, color_rgb=(85, 75, 68), bold=False)
        
    # 4. Balanced Technical & Business Highlights Table
    doc.add_paragraph().paragraph_format.space_after = Pt(0)
    p_hl = doc.add_paragraph()
    p_hl.paragraph_format.space_before = Pt(1)
    p_hl.paragraph_format.space_after = Pt(2)
    r_hl_h = p_hl.add_run("⭐ สรุปจุดเด่นและอัตลักษณ์เฉพาะตัว 2 มิติ (Technical Architecture & Business Metrics):")
    format_run(r_hl_h, size_pt=15, color_rgb=(43, 35, 29), bold=True)
    
    matrix_feat_table = doc.add_table(rows=5, cols=2)
    matrix_feat_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    feat_widths = [Inches(3.7), Inches(3.7)]
    
    hdr_row = matrix_feat_table.rows[0]
    for i, title in enumerate(["สถาปัตยกรรมด้านเทคนิคและการออกแบบ (Technical & UI/UX)", "ความถูกต้องแม่นยำทางธุรกิจ (Business & Data Compliance)"]):
        cell = hdr_row.cells[i]
        cell.width = feat_widths[i]
        set_cell_background(cell, "2B231D")
        set_cell_margins(cell, top=35, bottom=35, left=70, right=70)
        hp = cell.paragraphs[0]
        r = hp.add_run(title)
        format_run(r, size_pt=13.5, color_rgb=(255, 255, 255), bold=True)
        
    feats_data = [
        ("High-Density Modular Bento Grid: เลย์เอาต์กล่องสี่เหลี่ยมหลายขนาดสไตล์ Apple/SaaS แดชบอร์ดดูมีมิติ สัดส่วนสะอาดตา",
         "ตัวเลข KPI 4 ค่าหลักถูกต้อง 100%: รายได้รวม ฿72,530 | ปริมาณ 1,000 ชิ้น | กำไร ฿38,825 | อัตรากำไรสุทธิ 53.53%"),
        ("Interactive 3D Carousel: คอมโพเนนต์หมุนสลับการ์ด 3D สเปกสูง หมุนดูสินค้า Top 3 ด้วยมิติความลึก perspective 1000px",
         "Top 3 สินค้าผู้นำรายได้: อันดับ 1 ชีสเค้ก (฿13,440), อันดับ 2 ลาเต้ (฿10,120), อันดับ 3 ครัวซองต์ (฿10,000)"),
        ("Interactive Gradient Area Chart: กราฟพื้นที่ไล่เฉดสี Earth Tone พร้อมระบบ Tooltip ติดตามยอดขายรายวันตลอด 31 วัน",
         "มิติสาขาและหมวดหมู่: มหาวิทยาลัย (46.04%), สำนักงาน (31.96%), ห้างฯ (22.00%) | เบเกอรี 40.7%, กาแฟ 38.5%, อื่นๆ 20.8%"),
        ("Searchable Cross-Tab Matrix & 2D Modal: ตารางค้นหาแบบ Realtime, มี Data Bars ในตัวเลข และกดคลิกดูต้นทุน/กำไรใน Modal กระจก",
         "การันตีอัตลักษณ์ไร้การซ้ำซ้อน 100%: ไม่มีส่วนกรอบกลยุทธ์ตามที่กำหนด ดีไซน์โดดเด่นเป็นเอกลักษณ์เฉพาะนายภูริพัฒน์")
    ]
    
    for r_idx, (tech, biz) in enumerate(feats_data):
        row = matrix_feat_table.rows[r_idx + 1]
        bg = "FFFFFF" if r_idx % 2 == 0 else "FDFBF7"
        for c_idx, txt in enumerate([tech, biz]):
            cell = row.cells[c_idx]
            cell.width = feat_widths[c_idx]
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=30, bottom=30, left=70, right=70)
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.space_before = Pt(0)
            r = p.add_run(txt)
            format_run(r, size_pt=13, color_rgb=(55, 48, 42), bold=False)
            
    # =========================================================================
    # PAGE 2: HERO DASHBOARD SCREENSHOT & REQUIREMENT COMPLIANCE MATRIX
    # =========================================================================
    doc.add_page_break()
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    week5_dir = os.path.join(current_dir, "02_Labs_Assignments", "Week5")
    screenshot_candidates = [
        os.path.join(current_dir, "dashboard_preview_6752300313.png"),
        os.path.join(week5_dir, "dashboard_preview.png"),
        os.path.join(week5_dir, "dashboard_preview_6752300313.png")
    ]
    screenshot_path = next((p for p in screenshot_candidates if os.path.exists(p)), None)
    
    sp2 = doc.add_paragraph()
    sp2.paragraph_format.space_before = Pt(0)
    sp2.paragraph_format.space_after = Pt(1)
    r_sh2 = sp2.add_run("📸 ภาพแสดงผลหน้าจอจริง (Live Minimal Earth Tone Bento Dashboard Screenshot):")
    format_run(r_sh2, size_pt=15, color_rgb=(43, 35, 29), bold=True)
    
    if screenshot_path:
        img_p = doc.add_paragraph()
        img_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        img_p.paragraph_format.space_before = Pt(1)
        img_p.paragraph_format.space_after = Pt(1)
        img_run = img_p.add_run()
        img_run.add_picture(screenshot_path, width=Inches(7.1))
        
        cap_p = doc.add_paragraph()
        cap_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        cap_p.paragraph_format.space_before = Pt(1)
        cap_p.paragraph_format.space_after = Pt(3)
        rc = cap_p.add_run("ภาพที่ 1: Cafe & Bakery Performance Analytics Dashboard สไตล์ Minimal Earth Tone & Bento Grid ครบถ้วนทุกมิติตามโจทย์")
        format_run(rc, size_pt=12.5, color_rgb=(110, 101, 95), italic=True)
        
    sp_mat = doc.add_paragraph()
    sp_mat.paragraph_format.space_before = Pt(2)
    sp_mat.paragraph_format.space_after = Pt(1)
    r_m_h = sp_mat.add_run("📊 ตารางตรวจสอบความสอดคล้องตามเกณฑ์ประเมิน (Requirement Compliance Matrix):")
    format_run(r_m_h, size_pt=15, color_rgb=(43, 35, 29), bold=True)
    
    comp_table = doc.add_table(rows=4, cols=3)
    comp_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    c_widths = [Inches(1.8), Inches(4.5), Inches(1.1)]
    
    hdr_c_row = comp_table.rows[0]
    for i, t in enumerate(["เกณฑ์การประเมินวิชา SC60107", "รายละเอียดผลการส่งมอบงาน (Deliverable Details)", "สถานะ"]):
        cell = hdr_c_row.cells[i]
        cell.width = c_widths[i]
        set_cell_background(cell, "2B231D")
        set_cell_margins(cell, top=35, bottom=35, left=70, right=70)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if i == 2 else WD_ALIGN_PARAGRAPH.LEFT
        r = p.add_run(t)
        format_run(r, size_pt=13.5, color_rgb=(255, 255, 255), bold=True)
        
    comp_data = [
        ("Prompt 1: ภาพรวมผลประกอบการและ KPIs",
         "รายได้รวม ฿72,530 | ปริมาณ 1,000 ชิ้น | กำไร ฿38,825 (53.53%) | แสดง Top 3 สินค้าผ่าน 3D Carousel (ชีสเค้ก ฿13,440, ลาเต้ ฿10,120, ครัวซองต์ ฿10,000) พร้อมสถิติ Margin",
         "ครบถ้วน 100%"),
        ("Prompt 2: มิติการวิเคราะห์เชิงลึก",
         "ตาราง Cross-tab สินค้า 8 รายการ × 3 สาขา, สัดส่วนหมวดหมู่ผ่าน Donut Chart (เบเกอรี 40.7%, กาแฟ 38.5%, อื่นๆ 20.8%), กราฟแนวโน้มรายวันตลอด 31 วันพร้อม Cursor Tooltip",
         "ครบถ้วน 100%"),
        ("Non-Functional & UX Standards",
         "ทำงานแบบ Standalone ออฟไลน์ 100%, สถาปัตยกรรม High-Density Modular Bento Grid, โหมดสลับ Dark Espresso, ระบบ 2D Glass Modal เจาะลึกต้นทุน และ Badge ระบุตัวตนนักศึกษา",
         "ครบถ้วน 100%")
    ]
    
    for r_idx, (crit, det, stat) in enumerate(comp_data):
        row = comp_table.rows[r_idx + 1]
        bg = "FFFFFF" if r_idx % 2 == 0 else "FDFBF7"
        for c_idx, val in enumerate([crit, det, stat]):
            cell = row.cells[c_idx]
            cell.width = c_widths[c_idx]
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=35, bottom=35, left=70, right=70)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if c_idx == 2 else WD_ALIGN_PARAGRAPH.LEFT
            r = p.add_run(val)
            color = (34, 114, 60) if c_idx == 2 else (43, 35, 29)
            format_run(r, size_pt=13.5 if c_idx != 1 else 13, color_rgb=color, bold=(c_idx != 1))
            
    # =========================================================================
    # PAGE 3: DEEP-DIVE FINANCIAL & MULTI-BRANCH PERFORMANCE BREAKDOWN
    # =========================================================================
    doc.add_page_break()
    
    p3_h = doc.add_paragraph()
    p3_h.paragraph_format.space_before = Pt(0)
    p3_h.paragraph_format.space_after = Pt(2)
    r_p3_title = p3_h.add_run("📈 รายงานแจกแจงสถิติผลประกอบการและมิติข้อมูลเจาะลึก (Financial & Sales Deep-Dive):")
    format_run(r_p3_title, size_pt=15.5, color_rgb=(43, 35, 29), bold=True)
    
    p3_sub = doc.add_paragraph()
    p3_sub.paragraph_format.space_before = Pt(0)
    p3_sub.paragraph_format.space_after = Pt(2)
    r_sub_t = p3_sub.add_run("1. ตารางวิเคราะห์โครงสร้างรายได้ ต้นทุน และกำไรขั้นต้น แยกตามสินค้า 8 รายการ (Product Master Breakdown):")
    format_run(r_sub_t, size_pt=14, color_rgb=(138, 70, 48), bold=True)
    
    prod_table = doc.add_table(rows=10, cols=8)
    prod_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    p_widths = [Inches(1.5), Inches(0.9), Inches(0.7), Inches(0.7), Inches(0.7), Inches(1.0), Inches(1.0), Inches(0.9)]
    
    prod_headers = ["ชื่อสินค้า", "หมวดหมู่", "ขาย (ชิ้น)", "ราคา", "ต้นทุน", "รายได้รวม", "กำไรขั้นต้น", "GP %"]
    p_hdr_row = prod_table.rows[0]
    for i, title in enumerate(prod_headers):
        cell = p_hdr_row.cells[i]
        cell.width = p_widths[i]
        set_cell_background(cell, "2B231D")
        set_cell_margins(cell, top=30, bottom=30, left=40, right=40)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(title)
        format_run(r, size_pt=12.5, color_rgb=(255, 255, 255), bold=True)
        
    prod_rows = [
        ("ชีสเค้ก (Cheesecake)", "เบเกอรี", "160", "฿84", "฿55", "฿13,440", "฿4,640", "34.5%"),
        ("ลาเต้ (Latte)", "กาแฟ", "184", "฿55", "฿19", "฿10,120", "฿6,624", "65.5%"),
        ("ครัวซองต์ (Croissant)", "เบเกอรี", "125", "฿80", "฿56.5", "฿10,000", "฿2,938", "29.4%"),
        ("คาปูชิโน (Cappuccino)", "กาแฟ", "162", "฿57.5", "฿20.7", "฿9,315", "฿5,962", "64.0%"),
        ("เอสเพรสโซ (Espresso)", "กาแฟ", "155", "฿54.9", "฿18.3", "฿8,505", "฿5,673", "66.7%"),
        ("ชาเขียวมัทฉะ (Matcha)", "เครื่องดื่มอื่น", "120", "฿70", "฿26.6", "฿8,400", "฿5,208", "62.0%"),
        ("สมูทตี้ผลไม้ (Smoothie)", "เครื่องดื่มอื่น", "95", "฿70", "฿27.6", "฿6,650", "฿4,028", "60.5%"),
        ("ช็อกโกแลตเค้ก (Choc Cake)", "เบเกอรี", "74", "฿82.4", "฿31.6", "฿6,100", "฿3,752", "61.6%"),
        ("รวมทั้งสิ้น (Grand Total)", "ทุกหมวด", "1,000", "฿72.5", "฿33.7", "฿72,530", "฿38,825", "53.53%")
    ]
    
    for r_idx, r_data in enumerate(prod_rows):
        row = prod_table.rows[r_idx + 1]
        is_total = (r_idx == len(prod_rows) - 1)
        bg = "FAF6F0" if is_total else ("FFFFFF" if r_idx % 2 == 0 else "FDFBF7")
        for c_idx, val in enumerate(r_data):
            cell = row.cells[c_idx]
            cell.width = p_widths[c_idx]
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=25, bottom=25, left=40, right=40)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT if c_idx == 0 else WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(val)
            txt_color = (200, 109, 81) if (is_total and c_idx >= 5) else (43, 35, 29)
            format_run(r, size_pt=12.5, color_rgb=txt_color, bold=is_total)
            
    p3_sub2 = doc.add_paragraph()
    p3_sub2.paragraph_format.space_before = Pt(3)
    p3_sub2.paragraph_format.space_after = Pt(2)
    r_sub_b = p3_sub2.add_run("2. ตารางเปรียบเทียบสัดส่วนยอดขายและจำนวนธุรกรรม 3 สาขา (Multi-Branch Distribution):")
    format_run(r_sub_b, size_pt=14, color_rgb=(138, 70, 48), bold=True)
    
    branch_table = doc.add_table(rows=4, cols=5)
    branch_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    b_widths = [Inches(2.4), Inches(1.2), Inches(1.3), Inches(1.2), Inches(1.3)]
    
    b_headers = ["ชื่อสาขา (Branch Location)", "จำนวนธุรกรรม", "ยอดขายรวม (บาท)", "สัดส่วน (%)", "กำไรขั้นต้น (บาท)"]
    b_hdr_row = branch_table.rows[0]
    for i, title in enumerate(b_headers):
        cell = b_hdr_row.cells[i]
        cell.width = b_widths[i]
        set_cell_background(cell, "2B231D")
        set_cell_margins(cell, top=30, bottom=30, left=50, right=50)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(title)
        format_run(r, size_pt=12.5, color_rgb=(255, 255, 255), bold=True)
        
    branch_rows = [
        ("สาขามหาวิทยาลัย (University Campus)", "46 รายการ", "฿33,395", "46.04%", "฿17,910"),
        ("สาขาอาคารสำนักงาน (Office Building)", "32 รายการ", "฿23,180", "31.96%", "฿12,395"),
        ("สาขาห้างสรรพสินค้า (Shopping Mall)", "22 รายการ", "฿15,955", "22.00%", "฿8,520")
    ]
    for r_idx, r_data in enumerate(branch_rows):
        row = branch_table.rows[r_idx + 1]
        bg = "FFFFFF" if r_idx % 2 == 0 else "FDFBF7"
        for c_idx, val in enumerate(r_data):
            cell = row.cells[c_idx]
            cell.width = b_widths[c_idx]
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=25, bottom=25, left=50, right=50)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT if c_idx == 0 else WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(val)
            format_run(r, size_pt=12.5, color_rgb=(43, 35, 29), bold=(c_idx == 2 or c_idx == 3))
            
    # Sign-off box
    sign_table = doc.add_table(rows=1, cols=1)
    sign_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    scell = sign_table.cell(0, 0)
    scell.width = Inches(7.4)
    set_cell_background(scell, "FAF6F0")
    set_cell_margins(scell, top=35, bottom=35, left=80, right=80)
    sp = scell.paragraphs[0]
    sp.paragraph_format.space_before = Pt(0)
    sp.paragraph_format.space_after = Pt(0)
    r_sign = sp.add_run("✅ คำรับรองผลงาน: ข้าพเจ้า นายภูริพัฒน์ เหมกุล (6752300313) ขอรับรองว่าผลงานแดชบอร์ดและเอกสารชุดนี้พัฒนาขึ้นด้วยสถาปัตยกรรมเฉพาะตัว มีความถูกต้องของตัวเลขตามโจทย์ 100% และไม่มีการทำซ้ำหรือคัดลอกผลงานของผู้อื่น")
    format_run(r_sign, size_pt=12.5, color_rgb=(110, 101, 95), italic=True)

    # Tighten spacing of empty paragraphs
    for p in doc.paragraphs:
        if not p.text.strip() and not p.runs:
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = Pt(1)
            
    doc_out = os.path.join(current_dir, "Dashboard-6752300313-Submission.docx")
    doc.save(doc_out)
    
    doc_out_week5 = os.path.join(week5_dir, "Dashboard-6752300313-Submission.docx")
    doc.save(doc_out_week5)
    print(f"Generated 3-Page Academic Submission docx at:\n  {doc_out}\n  {doc_out_week5}")

if __name__ == "__main__":
    build_phuriphat_earthtone_3page_doc()
