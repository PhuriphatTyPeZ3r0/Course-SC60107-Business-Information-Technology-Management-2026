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

def set_cell_margins(cell, top=50, bottom=50, left=100, right=100):
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

def add_hyperlink(paragraph, url, text, color="1D4ED8", underline=True, font_name="TH SarabunPSK", font_size=14.5, bold=False):
    part = paragraph.part
    r_id = part.relate_to(url, docx.opc.constants.RELATIONSHIP_TYPE.HYPERLINK, is_external=True)
    
    hyperlink = parse_xml(
        f'<w:hyperlink {nsdecls("w")} r:id="{r_id}" {nsdecls("r")}/>'
    )
    new_run = parse_xml(f'<w:r {nsdecls("w")}/>')
    new_run_text = parse_xml(f'<w:t {nsdecls("w")}>{text}</w:t>')
    new_run.append(new_run_text)
    
    rPr = parse_xml(f'<w:rPr {nsdecls("w")}/>')
    if color:
        c = parse_xml(f'<w:color {nsdecls("w")} w:val="{color}"/>')
        rPr.append(c)
    if underline:
        u = parse_xml(f'<w:u {nsdecls("w")} w:val="single"/>')
        rPr.append(u)
    if bold:
        b = parse_xml(f'<w:b {nsdecls("w")}/>')
        rPr.append(b)
    
    # Fonts
    rFonts = parse_xml(f'<w:rFonts {nsdecls("w")} w:ascii="{font_name}" w:hAnsi="{font_name}" w:cs="{font_name}" w:eastAsia="{font_name}"/>')
    rPr.append(rFonts)
    
    sz = parse_xml(f'<w:sz {nsdecls("w")} w:val="{int(font_size * 2)}"/>')
    rPr.append(sz)
    szCs = parse_xml(f'<w:szCs {nsdecls("w")} w:val="{int(font_size * 2)}"/>')
    rPr.append(szCs)
    
    new_run.append(rPr)
    hyperlink.append(new_run)
    paragraph._p.append(hyperlink)
    return hyperlink

def format_run(run, font_name="TH SarabunPSK", size_pt=15, color_rgb=(15, 23, 42), bold=False, italic=False):
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

def build_document():
    doc = Document()
    
    # Configure Normal Style for TH SarabunPSK
    style = doc.styles['Normal']
    style.font.name = 'TH SarabunPSK'
    style.font.size = Pt(15)
    rPr = style.element.get_or_add_rPr()
    rFonts = rPr.get_or_add_rFonts()
    rFonts.set(qn('w:ascii'), 'TH SarabunPSK')
    rFonts.set(qn('w:hAnsi'), 'TH SarabunPSK')
    rFonts.set(qn('w:cs'), 'TH SarabunPSK')
    rFonts.set(qn('w:eastAsia'), 'TH SarabunPSK')
    
    # Page Setup: Standard A4 with 0.45 in top/bottom margins, 0.6 in left/right margins
    for section in doc.sections:
        section.top_margin = Inches(0.45)
        section.bottom_margin = Inches(0.45)
        section.left_margin = Inches(0.6)
        section.right_margin = Inches(0.6)
    
    # ================= PAGE 1 =================
    # 1. Header Banner Table (Card Style)
    header_table = doc.add_table(rows=1, cols=1)
    header_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    header_cell = header_table.cell(0, 0)
    header_cell.width = Inches(7.1)
    set_cell_background(header_cell, "0F172A") # Navy dark slate
    set_cell_margins(header_cell, top=90, bottom=90, left=160, right=160)
    
    hp1 = header_cell.paragraphs[0]
    hp1.paragraph_format.space_before = Pt(0)
    hp1.paragraph_format.space_after = Pt(1)
    hp1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = hp1.add_run("สถาบันการจัดการปัญญาภิวัฒน์ (PIM) · สาขาวิศวกรรมคอมพิวเตอร์และปัญญาประดิษฐ์ (CAI)")
    format_run(r_sub, size_pt=13.5, color_rgb=(148, 163, 184), bold=False)
    
    hp2 = header_cell.add_paragraph()
    hp2.paragraph_format.space_before = Pt(1)
    hp2.paragraph_format.space_after = Pt(1)
    hp2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = hp2.add_run("ใบงานส่งมอบผลงาน: Dashboard (5 คะแนน)")
    format_run(r_title, size_pt=19, color_rgb=(255, 255, 255), bold=True)
    
    hp3 = header_cell.add_paragraph()
    hp3.paragraph_format.space_before = Pt(1)
    hp3.paragraph_format.space_after = Pt(0)
    hp3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_course = hp3.add_run("รายวิชา SC60107 การจัดการเทคโนโลยีสารสนเทศทางธุรกิจ · ภาคการศึกษา 1/2569")
    format_run(r_course, size_pt=14, color_rgb=(56, 189, 248), bold=True)
    
    # 2. Student Info & Meta Section
    info_table = doc.add_table(rows=2, cols=2)
    info_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    info_widths = [Inches(3.55), Inches(3.55)]
    
    row0 = info_table.rows[0]
    c0 = row0.cells[0]
    c0.width = info_widths[0]
    set_cell_background(c0, "F8FAFC")
    set_cell_margins(c0, top=50, bottom=50, left=100, right=100)
    p = c0.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.space_before = Pt(0)
    r1 = p.add_run("👤 ผู้จัดทำ: ")
    format_run(r1, size_pt=14.5, color_rgb=(100, 116, 139), bold=True)
    r2 = p.add_run("นายภูริพัฒน์ เหมกุล")
    format_run(r2, size_pt=15, color_rgb=(15, 23, 42), bold=True)
    
    c1 = row0.cells[1]
    c1.width = info_widths[1]
    set_cell_background(c1, "F8FAFC")
    set_cell_margins(c1, top=50, bottom=50, left=100, right=100)
    p = c1.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.space_before = Pt(0)
    r1 = p.add_run("🆔 รหัสนักศึกษา: ")
    format_run(r1, size_pt=14.5, color_rgb=(100, 116, 139), bold=True)
    r2 = p.add_run("6752300313 (กลุ่ม 1.2-1)")
    format_run(r2, size_pt=15, color_rgb=(37, 99, 235), bold=True)
    
    row1 = info_table.rows[1]
    c2 = row1.cells[0]
    c2.width = info_widths[0]
    set_cell_background(c2, "F8FAFC")
    set_cell_margins(c2, top=50, bottom=50, left=100, right=100)
    p = c2.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.space_before = Pt(0)
    r1 = p.add_run("🎯 หัวข้องาน: ")
    format_run(r1, size_pt=14.5, color_rgb=(100, 116, 139), bold=True)
    r2 = p.add_run("Cafe & Bakery Sales Analytics Dashboard")
    format_run(r2, size_pt=14.5, color_rgb=(15, 23, 42), bold=False)
    
    c3 = row1.cells[1]
    c3.width = info_widths[1]
    set_cell_background(c3, "F8FAFC")
    set_cell_margins(c3, top=50, bottom=50, left=100, right=100)
    p = c3.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.space_before = Pt(0)
    r1 = p.add_run("📅 วันที่ส่งงาน: ")
    format_run(r1, size_pt=14.5, color_rgb=(100, 116, 139), bold=True)
    r2 = p.add_run("16 ตุลาคม 2569")
    format_run(r2, size_pt=14.5, color_rgb=(15, 23, 42), bold=False)
    
    # 3. Key Web Links Box (Prominent Callout)
    links_table = doc.add_table(rows=1, cols=1)
    links_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    lcell = links_table.cell(0, 0)
    lcell.width = Inches(7.1)
    set_cell_background(lcell, "EFF6FF") # Soft Blue Tint
    set_cell_margins(lcell, top=70, bottom=70, left=140, right=140)
    
    lp0 = lcell.paragraphs[0]
    lp0.paragraph_format.space_before = Pt(0)
    lp0.paragraph_format.space_after = Pt(1)
    r_lh = lp0.add_run("🔗 ช่องทางการเข้าชมและตรวจประเมินผลงาน (Clickable Links):")
    format_run(r_lh, size_pt=15.5, color_rgb=(30, 58, 138), bold=True)
    
    # Link 1: Live GitHub Pages
    lp1 = lcell.add_paragraph()
    lp1.paragraph_format.space_before = Pt(0)
    lp1.paragraph_format.space_after = Pt(1)
    r = lp1.add_run("🌐 1. Live Web Application (GitHub Pages): ")
    format_run(r, size_pt=14.5, color_rgb=(15, 23, 42), bold=True)
    add_hyperlink(
        lp1, 
        "https://phuriphattypez3r0.github.io/Course-SC60107-Business-Information-Technology-Management-2026/",
        "https://phuriphattypez3r0.github.io/Course-SC60107-Business-Information-Technology-Management-2026/",
        color="1D4ED8",
        font_size=14.5,
        bold=True
    )
    
    # Link 2: Direct File Link
    lp2 = lcell.add_paragraph()
    lp2.paragraph_format.space_before = Pt(0)
    lp2.paragraph_format.space_after = Pt(1)
    r = lp2.add_run("📄 2. Direct HTML URL (ไฟล์ตรง): ")
    format_run(r, size_pt=14.5, color_rgb=(15, 23, 42), bold=True)
    add_hyperlink(
        lp2,
        "https://phuriphattypez3r0.github.io/Course-SC60107-Business-Information-Technology-Management-2026/Dashboard-6752300313.html",
        "Dashboard-6752300313.html (คลิกเพื่อเปิด)",
        color="2563EB",
        font_size=14.5,
        bold=False
    )
    
    # Link 3: GitHub Repo
    lp3 = lcell.add_paragraph()
    lp3.paragraph_format.space_before = Pt(0)
    lp3.paragraph_format.space_after = Pt(0)
    r = lp3.add_run("💻 3. GitHub Course Repository (Source Code): ")
    format_run(r, size_pt=14.5, color_rgb=(15, 23, 42), bold=True)
    add_hyperlink(
        lp3,
        "https://github.com/PhuriphatTyPeZ3r0/Course-SC60107-Business-Information-Technology-Management-2026",
        "PhuriphatTyPeZ3r0/Course-SC60107-Business-Information-Technology-Management-2026",
        color="2563EB",
        font_size=14.5,
        bold=False
    )
    
    # 4. Key Feature Highlights Card on Page 1
    feat_table = doc.add_table(rows=1, cols=1)
    feat_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    fcell = feat_table.cell(0, 0)
    fcell.width = Inches(7.1)
    set_cell_background(fcell, "F8FAFC")
    set_cell_margins(fcell, top=70, bottom=70, left=140, right=140)
    
    fp0 = fcell.paragraphs[0]
    fp0.paragraph_format.space_before = Pt(0)
    fp0.paragraph_format.space_after = Pt(2)
    rf_h = fp0.add_run("⭐ จุดเด่นและการตอบโจทย์ตามข้อกำหนด (Technical & Business Highlights):")
    format_run(rf_h, size_pt=15.5, color_rgb=(15, 23, 42), bold=True)
    
    highlights = [
        ("⚡ Clean Minimalist Architecture: ", "การจัดวางโครงสร้างแบบ Executive Dashboard ที่เรียบหรู กระชับ ไร้ความซ้ำซ้อน นำเสนอตัวเลขผลประกอบการ 3 สาขา, สัดส่วนหมวดหมู่, และตาราง Cross-tab สินค้า × สาขาอย่างถูกต้องตามหลักสถิติ"),
        ("📷 High-res 2D Studio Photography: ", "ภาพถ่ายสินค้าแบบสตูดิโอความละเอียดสูง เพิ่มความน่าเชื่อถือระดับมืออาชีพ พร้อมระบบ Zero-fail Inline SVG Fallback เมื่อเปิดในโหมดออฟไลน์"),
        ("🎯 100% Strict Compliance: ", "ครอบคลุมครบทั้ง Prompt 1 (KPI รวม ฿72,530, ยอดขาย 1,000 ชิ้น, กำไร ฿38,825 / 53.53%, Top 3 สินค้าสูงสุดพร้อม % สัดส่วนที่ถูกต้อง) และ Prompt 2 (ตาราง Cross-tab สินค้า × สาขา, สัดส่วนหมวดหมู่, ไทม์ไลน์ 31 วัน)"),
        ("🚀 Zero-Dependency Architecture: ", "เปิดใช้งานบนเว็บเบราว์เซอร์ได้ทันทีโดยไม่ต้องเชื่อมต่อระบบภายนอกหรือติดตั้งโปรแกรมเสริมใดๆ รองรับ Light/Dark Theme และ Print Stylesheet สมบูรณ์แบบ")
    ]
    
    for prefix, desc in highlights:
        fp = fcell.add_paragraph()
        fp.paragraph_format.space_before = Pt(1)
        fp.paragraph_format.space_after = Pt(1)
        r_pre = fp.add_run(prefix)
        format_run(r_pre, size_pt=14.5, color_rgb=(30, 58, 138), bold=True)
        r_desc = fp.add_run(desc)
        format_run(r_desc, size_pt=14.5, color_rgb=(51, 65, 85), bold=False)
        
    # ================= PAGE 2 =================
    doc.add_page_break()
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    screenshot_path = os.path.join(current_dir, "dashboard_preview.png")
    if os.path.exists(screenshot_path):
        sp = doc.add_paragraph()
        sp.paragraph_format.space_before = Pt(0)
        sp.paragraph_format.space_after = Pt(1)
        r_sh = sp.add_run("📸 ภาพตัวอย่างหน้าจอระบบจริง (Live Dashboard Screenshot):")
        format_run(r_sh, size_pt=15.5, color_rgb=(15, 23, 42), bold=True)
        
        img_p = doc.add_paragraph()
        img_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        img_p.paragraph_format.space_before = Pt(0)
        img_p.paragraph_format.space_after = Pt(1)
        img_run = img_p.add_run()
        # 5.1 inches width gives height ~ 5.3 inches, showing all sections down to the matrix table
        img_run.add_picture(screenshot_path, width=Inches(5.1))
        
        caption_p = doc.add_paragraph()
        caption_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        caption_p.paragraph_format.space_before = Pt(1)
        caption_p.paragraph_format.space_after = Pt(2)
        rc = caption_p.add_run("ภาพที่ 1: หน้าจอแสดงผล Cafe & Bakery Sales Analytics Dashboard ครบถ้วนทุกส่วนตั้งแต่ KPIs, กราฟ, จนถึงตาราง Cross-tab สินค้า × สาขา")
        format_run(rc, size_pt=13, color_rgb=(100, 116, 139), italic=True)
        
        sp4 = doc.add_paragraph()
        sp4.paragraph_format.space_before = Pt(1)
        sp4.paragraph_format.space_after = Pt(1)
        r_mat_h = sp4.add_run("📊 สรุปความสอดคล้องตามเกณฑ์ประเมิน (Requirement Compliance Matrix):")
        format_run(r_mat_h, size_pt=15.5, color_rgb=(15, 23, 42), bold=True)
        
        # Compliance Matrix Table
        matrix_table = doc.add_table(rows=4, cols=3)
        matrix_table.alignment = WD_TABLE_ALIGNMENT.CENTER
        col_widths = [Inches(1.7), Inches(4.4), Inches(1.0)]
        
        # Header Row
        hdr_cells = matrix_table.rows[0].cells
        hdr_titles = ["เกณฑ์การประเมิน", "รายละเอียดผลการส่งมอบงาน (Deliverables)", "สถานะ"]
        for idx, title in enumerate(hdr_titles):
            hdr_cells[idx].width = col_widths[idx]
            set_cell_background(hdr_cells[idx], "1E293B")
            set_cell_margins(hdr_cells[idx], top=40, bottom=40, left=90, right=90)
            hp = hdr_cells[idx].paragraphs[0]
            hp.alignment = WD_ALIGN_PARAGRAPH.CENTER if idx == 2 else WD_ALIGN_PARAGRAPH.LEFT
            r = hp.add_run(title)
            format_run(r, size_pt=14.5, color_rgb=(255, 255, 255), bold=True)
            
        rows_data = [
            ("Prompt 1: ภาพรวมและ KPIs", "รายได้รวม ฿72,530 | ปริมาณขาย 1,000 ชิ้น | กำไร ฿38,825 (53.53%) | สินค้า Top 3: ชีสเค้ก (18.5%), ลาเต้ (14.0%), ครัวซองต์ (13.8%)", "ครบถ้วน 100%"),
            ("Prompt 2: มิติการวิเคราะห์", "ตาราง Cross-tab สินค้า × 3 สาขา, สัดส่วนรายได้แยกตามหมวดหมู่ (เบเกอรี 40.7%, กาแฟ 38.5%, เครื่องดื่มอื่น 20.9%), และแนวโน้มยอดขาย 31 วัน", "ครบถ้วน 100%"),
            ("Non-Functional Standards", "ทำงานแบบ Standalone ไม่พึ่งพาอินเทอร์เน็ต, สลับธีมมืด/สว่างได้, และจัดวางโครงสร้าง Clean Executive ตามหลัก UX/UI", "ครบถ้วน 100%")
        ]
        
        for r_idx, (crit, detail, stat) in enumerate(rows_data):
            row_cells = matrix_table.rows[r_idx + 1].cells
            bg = "FFFFFF" if r_idx % 2 == 0 else "F8FAFC"
            for c_idx, val in enumerate([crit, detail, stat]):
                row_cells[c_idx].width = col_widths[c_idx]
                set_cell_background(row_cells[c_idx], bg)
                set_cell_margins(row_cells[c_idx], top=35, bottom=35, left=90, right=90)
                p = row_cells[c_idx].paragraphs[0]
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER if c_idx == 2 else WD_ALIGN_PARAGRAPH.LEFT
                r = p.add_run(val)
                stat_color = (22, 101, 52) if c_idx == 2 else (15, 23, 42)
                format_run(r, size_pt=14 if c_idx == 1 else 14.5, color_rgb=stat_color, bold=(c_idx != 1))
    
    # Format any trailing paragraphs in body to 1pt so Word never breaks an empty page
    for p in doc.paragraphs:
        if not p.text.strip() and not p.runs:
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = Pt(1)
            
    doc_path = os.path.join(current_dir, "Dashboard-6752300313-Submission.docx")
    doc.save(doc_path)
    print(f"DOCX created successfully at: {doc_path}")

if __name__ == "__main__":
    build_document()
