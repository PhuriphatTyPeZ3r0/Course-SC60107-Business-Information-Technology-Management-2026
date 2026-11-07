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

def set_cell_margins(cell, top=60, bottom=60, left=120, right=120):
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

def build_workshop_document():
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
        section.top_margin = Inches(0.45)
        section.bottom_margin = Inches(0.45)
        section.left_margin = Inches(0.55)
        section.right_margin = Inches(0.55)
        
    current_dir = os.path.dirname(os.path.abspath(__file__))
    screenshots_dir = os.path.join(current_dir, "workshop_screenshots")

    # 1. Header Banner
    header_table = doc.add_table(rows=1, cols=1)
    header_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    header_cell = header_table.cell(0, 0)
    header_cell.width = Inches(7.4)
    set_cell_background(header_cell, "0F172A")
    set_cell_margins(header_cell, top=100, bottom=100, left=180, right=180)
    
    hp1 = header_cell.paragraphs[0]
    hp1.paragraph_format.space_before = Pt(0)
    hp1.paragraph_format.space_after = Pt(2)
    hp1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = hp1.add_run("สถาบันการจัดการปัญญาภิวัฒน์ (PIM) · คณะวิศวกรรมศาสตร์และเทคโนโลยี · สาขาวิศวกรรมคอมพิวเตอร์และปัญญาประดิษฐ์ (CAI)")
    format_run(r_sub, size_pt=13.5, color_rgb=(148, 163, 184), bold=False)
    
    hp2 = header_cell.add_paragraph()
    hp2.paragraph_format.space_before = Pt(2)
    hp2.paragraph_format.space_after = Pt(2)
    hp2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = hp2.add_run("เอกสารส่งมอบงาน: รวมไฟล์ผลงาน Workshop AI Coaching (10 คะแนนเต็ม)")
    format_run(r_title, size_pt=20, color_rgb=(255, 255, 255), bold=True)
    
    hp3 = header_cell.add_paragraph()
    hp3.paragraph_format.space_before = Pt(2)
    hp3.paragraph_format.space_after = Pt(0)
    hp3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_course = hp3.add_run("รายวิชา SC60107 การจัดการเทคโนโลยีสารสนเทศทางธุรกิจ (Business IT Management) · ภาคการศึกษา 1/2569")
    format_run(r_course, size_pt=14, color_rgb=(56, 189, 248), bold=True)
    
    # 2. Student Info Table
    info_table = doc.add_table(rows=2, cols=2)
    info_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    info_widths = [Inches(3.7), Inches(3.7)]
    
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
    format_run(r2, size_pt=15.5, color_rgb=(15, 23, 42), bold=True)
    
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
    format_run(r2, size_pt=15.5, color_rgb=(37, 99, 235), bold=True)
    
    row1 = info_table.rows[1]
    c2 = row1.cells[0]
    c2.width = info_widths[0]
    set_cell_background(c2, "F8FAFC")
    set_cell_margins(c2, top=50, bottom=50, left=100, right=100)
    p = c2.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.space_before = Pt(0)
    r1 = p.add_run("🎯 กลุ่มที่นำเสนอในคลาส: ")
    format_run(r1, size_pt=14.5, color_rgb=(100, 116, 139), bold=True)
    r2 = p.add_run("Whisper AI (24/9/69)")
    format_run(r2, size_pt=14.5, color_rgb=(15, 23, 42), bold=False)
    
    c3 = row1.cells[1]
    c3.width = info_widths[1]
    set_cell_background(c3, "F8FAFC")
    set_cell_margins(c3, top=50, bottom=50, left=100, right=100)
    p = c3.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.space_before = Pt(0)
    r1 = p.add_run("📊 สถานะความสมบูรณ์: ")
    format_run(r1, size_pt=14.5, color_rgb=(100, 116, 139), bold=True)
    r2 = p.add_run("เข้าร่วมและส่งครบถ้วน 9/9 เครื่องมือ (100%)")
    format_run(r2, size_pt=14.5, color_rgb=(22, 101, 52), bold=True)
    
    # 3. Summary Scorecard Table
    p_sec = doc.add_paragraph()
    p_sec.paragraph_format.space_before = Pt(14)
    p_sec.paragraph_format.space_after = Pt(4)
    r_sec = p_sec.add_run("📋 ตารางสรุปภาพรวมการทำ Workshop AI ครบ 9 เครื่องมือ")
    format_run(r_sec, size_pt=16.5, color_rgb=(15, 23, 42), bold=True)
    
    workshops_data = [
        ("1. Reclaim.ai", "24/9/69", "AI Calendar & Intelligent Time Blocking บริหารเวลาและตารางงานอัตโนมัติ", "จัดตาราง Habit & Tasks สำเร็จ", "สำเร็จ 100%"),
        ("2. Soniox Speech AI", "1/10/69", "Real-time Multilingual Speech-to-Text & Transcription ภาษาไทย", "ส่งไฟล์สรุปเสียง Sonox.txt", "สำเร็จ 100%"),
        ("3. Zapier AI + Gemini", "1/10/69", "Automation Flow: Webhook + Gemini Sentiment Analysis & Email Alert", "ไฟล์ zapier_alert_preview.html", "สำเร็จ 100%"),
        ("4. AI TyPhoon OCR", "8/10/69", "Thai LLM & Document OCR สกัดข้อมูลสลิป/ใบเสร็จภาษาไทย (SCB 10X)", "ส่งแบบทดสอบ Typhoon OCR Form", "สำเร็จ 100%"),
        ("5. Napkin AI", "8/10/69", "Generative Text-to-Visual Diagram แปลงข้อความประกาศเป็น Infographic", "Quiz 20/20 เต็ม + ไฟล์ SVG", "สำเร็จ 100%"),
        ("6. Lindy AI", "15/10/69", "Autonomous AI Agents จัดการข้อมูล Triage และประสาน SciSpace Research", "ออกแบบ Flow AI Agent คัดกรอง", "สำเร็จ 100%"),
        ("7. Bolt.new / Notion", "15/10/69", "Fullstack AI Web Generator & Notion Agile Project Task Dashboard", "ไฟล์ bolt_notion_dashboard.html", "สำเร็จ 100%"),
        ("8. Scribe AI", "22/10/69", "AI Auto-SOP Generator สร้างคู่มือการทำงานมาตรฐานและบันทึกภาพขั้นตอน", "ไฟล์คู่มือ scribe_sop_guide.html", "สำเร็จ 100%"),
        ("9. Khui AI", "22/10/69", "Enterprise Thai Conversational Platform & Character AI Chatbot", "ทำแบบทดสอบ Quiz ได้ 20/20 เต็ม", "สำเร็จ 100%")
    ]
    
    summary_table = doc.add_table(rows=len(workshops_data) + 1, cols=5)
    summary_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    s_widths = [Inches(1.5), Inches(0.8), Inches(2.7), Inches(1.6), Inches(0.8)]
    
    hdr = summary_table.rows[0].cells
    hdr_titles = ["ชื่อเครื่องมือ AI", "วันที่", "ขอบเขตและรูปแบบของระบบ", "ผลลัพธ์ / ไฟล์ส่งมอบ", "สถานะ"]
    for i, t in enumerate(hdr_titles):
        hdr[i].width = s_widths[i]
        set_cell_background(hdr[i], "1E293B")
        set_cell_margins(hdr[i], top=40, bottom=40, left=70, right=70)
        p = hdr[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if i in [1, 4] else WD_ALIGN_PARAGRAPH.LEFT
        r = p.add_run(t)
        format_run(r, size_pt=13.5, color_rgb=(255, 255, 255), bold=True)
        
    for r_idx, (name, date_str, desc, res, stat) in enumerate(workshops_data):
        row_cells = summary_table.rows[r_idx + 1].cells
        bg = "FFFFFF" if r_idx % 2 == 0 else "F8FAFC"
        for c_idx, val in enumerate([name, date_str, desc, res, stat]):
            row_cells[c_idx].width = s_widths[c_idx]
            set_cell_background(row_cells[c_idx], bg)
            set_cell_margins(row_cells[c_idx], top=35, bottom=35, left=70, right=70)
            p = row_cells[c_idx].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if c_idx in [1, 4] else WD_ALIGN_PARAGRAPH.LEFT
            r = p.add_run(val)
            color = (22, 101, 52) if c_idx == 4 else (15, 23, 42)
            format_run(r, size_pt=13, color_rgb=color, bold=(c_idx in [0, 4]))

    # Section 4: Detailed Showcase for ALL 9 Tools
    tools_detail = [
        {
            "id": "1",
            "name": "Reclaim.ai",
            "date": "24 กันยายน 2569",
            "badge": "AI Calendar & Intelligent Time Blocking",
            "desc": "Reclaim AI เป็นระบบอัจฉริยะที่เชื่อมโยงกับปฏิทินการทำงาน (เช่น Google Calendar) เพื่อช่วยจัดสรรเวลาอย่างมีประสิทธิภาพสูงสุด โดยใช้ขั้นตอนวิธี Time Defense อัตโนมัติในการล็อกเวลาสำหรับ Focus Time, การสร้างนิสัยการทำงาน (Habits), การกำหนดเวลาพักผ่อน และการปรับตารางเวลานัดหมายแบบยืดหยุ่นตามลำดับความสำคัญของงาน",
            "business_value": "ช่วยเพิ่มประสิทธิภาพของทีมในการทำงานที่ต้องใช้สมาธิสูง (Deep Work) ลดปัญหาตารางงานชนกัน (Scheduling Conflicts) และป้องกันภาวะหมดไฟในการทำงาน (Burnout) ของบุคลากรในองค์กร",
            "action": "ทำการศึกษาและทดลองตั้งค่า Smart Calendar สำหรับการบริหารเวลาเรียนและการทำงานกลุ่ม ออกแบบเวลาช่วง Focus Time และ Habits ประจำวัน",
            "output": "ภาพบันทึกฟีเจอร์การบริหารจัดการตารางเวลาบนหน้าเว็บ Reclaim.ai พร้อมโครงสร้าง Smart Blocking",
            "img": os.path.join(screenshots_dir, "01_reclaim.png"),
            "caption": "ภาพที่ 1: หน้าแดชบอร์ดและการตั้งค่า AI Smart Calendar บนแพลตฟอร์ม Reclaim.ai"
        },
        {
            "id": "2",
            "name": "Soniox Speech AI",
            "date": "1 ตุลาคม 2569",
            "badge": "Multilingual Real-time Speech-to-Text & Meeting AI",
            "desc": "Soniox เป็นเทคโนโลยีปัญญาประดิษฐ์ด้านการแปลงเสียงพูดเป็นข้อความ (Speech-to-Text) ที่มีความแม่นยำสูง รองรับการประมวลผลเสียงภาษาไทยแบบผสมผสานคำทับศัพท์ภาษาอังกฤษ เหมาะสำหรับใช้ในการถอดเสียงการประชุมทางธุรกิจและการบันทึกรายงานการประชุมแบบเรียลไทม์",
            "business_value": "ลดระยะเวลาในการสรุปรายงานการประชุมลงกว่า 80% ป้องกันการตกหล่นของข้อมูลสำคัญ และเพิ่มความโปร่งใสในการตรวจสอบบันทึกการประชุมขององค์กร",
            "action": "นำไฟล์เสียงจากการประชุมคลาสเรียนหรือเสียงสนทนามาประมวลผลผ่านระบบของ Soniox เพื่อถอดเสียงและจัดหมวดหมู่คำสำคัญ",
            "output": "ไฟล์รายงานการถอดเสียงภาษาไทย 'Sonox-2026-10-01-08-46.txt' ซึ่งได้ทำการอัปโหลดส่งในระบบ e-Learning แล้ว",
            "img": os.path.join(screenshots_dir, "02_soniox.png"),
            "caption": "ภาพที่ 2: หน้าแพลตฟอร์ม Soniox แสดงการวิเคราะห์ Speech AI และความสามารถในการถอดเสียงภาษาไทย"
        },
        {
            "id": "3",
            "name": "Zapier AI + Google Gemini",
            "date": "1 ตุลาคม 2569",
            "badge": "Workflow Automation & AI Sentiment Alert Flow",
            "desc": "การสร้างระบบอัตโนมัติ (Automation Pipeline) โดยผสานรวม Zapier Webhook เข้ากับโมเดล Google Gemini 1.5 Flash เพื่อวิเคราะห์ความรู้สึก (Sentiment Analysis) ของข้อความฟีดแบ็กจากลูกค้า และตั้งกฎเงื่อนไข (Conditional Branching) ว่าหากพบฟีดแบ็กเชิงลบ (Negative Sentiment) ให้ส่งอีเมลแจ้งเตือนผู้บริหารทันทีด้วยการ์ดเทมเพลตสีแดง",
            "business_value": "ยกระดับการบริการลูกค้า (Customer Experience) โดยองค์กรสามารถรับรู้ปัญหาและข้อร้องเรียนของลูกค้าได้แบบทันท่วงที (Real-time Incident Response) ภายในไม่กี่วินาที",
            "action": "สร้าง Automation Workflow รับ Webhook, เขียน Prompt สั่ง Gemini ตรวจจับอารมณ์และประเภทปัญหา, และออกแบบ HTML Email Alert Template สำหรับส่งแจ้งเตือนทีมสนับสนุน",
            "output": "สคริปต์อัตโนมัติ 'automation/03_zapier_gemini_webhook.py' และไฟล์ตัวอย่างการ์ดแจ้งเตือน 'zapier_alert_preview.html'",
            "img": os.path.join(screenshots_dir, "03_zapier_ai.png"),
            "caption": "ภาพที่ 3: ระบบกิจกรรม Zapier Class Portal และเวิร์กโฟลว์เชื่อมต่อ Webhook ร่วมกับ Gemini AI"
        },
        {
            "id": "4",
            "name": "AI TyPhoon (SCB 10X) & Typhoon OCR",
            "date": "8 ตุลาคม 2569",
            "badge": "Thai Large Language Model & Intelligent Document OCR",
            "desc": "โมเดลปัญญาประดิษฐ์ขนาดใหญ่ภาษาไทยที่พัฒนาโดย SCB 10X มีจุดเด่นด้านความเข้าใจไวยากรณ์ วัฒนธรรม และศัพท์ทางธุรกิจของไทย ร่วมกับโมเดล Typhoon OCR ที่มีความเชี่ยวชาญในการแปลงภาพถ่ายเอกสาร สลิปการโอนเงิน และใบเสร็จรับเงินภาษาไทยให้กลายเป็นข้อมูลเชิงโครงสร้าง (Structured JSON Data)",
            "business_value": "ปฏิรูปกระบวนการทางบัญชีและการเงิน (Accounting Automation) ลดข้อผิดพลาดจากการคีย์ข้อมูลด้วยมนุษย์ และตรวจสอบความถูกต้องของสลิปโอนเงินได้แบบอัตโนมัติ",
            "action": "ทดสอบโมเดล Typhoon OCR ในการสกัดข้อมูลใบเสร็จรับเงินไทย และทำแบบทดสอบความรู้ Typhoon OCR Quiz ผ่านระบบ Google Forms",
            "output": "คะแนนแบบทดสอบความรู้ Typhoon OCR เต็ม 20/20 พร้อมรูปถ่ายยืนยันบนระบบฟอร์ม",
            "img": os.path.join(screenshots_dir, "04_typhoon_ai.png"),
            "caption": "ภาพที่ 4: หน้า Typhoon Playground ทดสอบการทำงานของโมเดล Typhoon OCR กับเอกสารใบเสร็จไทย"
        },
        {
            "id": "5",
            "name": "Napkin AI",
            "date": "8 ตุลาคม 2569",
            "badge": "Generative Text-to-Visual Diagram & Information Design",
            "desc": "เครื่องมือ Generative AI ที่ช่วยแปลงเนื้อหาข้อความยาวๆ เช่น ประกาศ ข้อบังคับ หรือขั้นตอนการทำงาน ให้กลายเป็นแผนภาพทางความคิด (Visual Diagram, Infographic, Flowchart, Process Hierarchy) ที่เข้าใจง่ายและสวยงามในระดับมืออาชีพ",
            "business_value": "ช่วยเพิ่มประสิทธิภาพในการสื่อสารภายในองค์กร ทำให้ผู้บริหารและทีมงานเข้าใจขั้นตอนหรือประกาศที่ซับซ้อนได้อย่างรวดเร็วผ่านภาพกราฟิก",
            "action": "นำข้อความประกาศตรวจเยี่ยมฝึกงานของ อ.ตาล และแผนงานการประชุมกลุ่ม 6 คน มาสร้างเป็น Infographic และทำแบบทดสอบความรู้ Napkin AI Quiz",
            "output": "ผลคะแนนสอบ 20/20 เต็ม (ไฟล์ 'napkin_ai_quiz_score_20_20.png') และไฟล์เวกเตอร์แผนภาพ 'napkin_prompt1_diagram.svg'",
            "img": os.path.join(screenshots_dir, "05_napkin_ai.png"),
            "caption": "ภาพที่ 5: หน้าแพลตฟอร์ม Napkin AI สำหรับการสร้าง Visual Diagram จากข้อความประกาศอัตโนมัติ"
        },
        {
            "id": "6",
            "name": "Lindy AI & SciSpace Research",
            "date": "15 ตุลาคม 2569",
            "badge": "Autonomous AI Agents & Intelligent Document Processing",
            "desc": "แพลตฟอร์มสำหรับสร้างตัวแทนปัญญาประดิษฐ์อัตโนมัติ (Autonomous AI Agent) เพื่อทำหน้าที่เป็นเสมือนพนักงานจัดการงานประจำ (Routine Tasks) เช่น การคัดแยกเอกสารงานวิจัยใน SciSpace, การวิเคราะห์ข้อมูลใน Google Sheets, และการประสานงานตอบข้อซักถามผ่านระบบอัตโนมัติ",
            "business_value": "ช่วยให้พนักงานสามารถลดเวลาที่ต้องเสียไปกับงานซ้ำซ้อน (Repetitive Manual Tasks) และมุ่งเน้นไปที่งานเชิงกลยุทธ์และการวิเคราะห์ขั้นสูง",
            "action": "ศึกษาและทดสอบเวิร์กโฟลว์ AI Agent ตามโจทย์การจัดการเอกสารวิชาการและการประสานงานร่วมกับฐานข้อมูลสเปรดชีต",
            "output": "ภาพบันทึกขั้นตอนการออกแบบ Agent Flow และอินเทอร์เฟซของระบบ SciSpace / Lindy AI Guide",
            "img": os.path.join(screenshots_dir, "06_lindy_ai.png"),
            "caption": "ภาพที่ 6: หน้าระบบ SciSpace / Lindy AI Interactive Guide และโครงสร้าง Agent Workflow"
        },
        {
            "id": "7",
            "name": "Bolt.new & Notion AI",
            "date": "15 ตุลาคม 2569",
            "badge": "Fullstack Web Generator & Notion Agile Project Dashboard",
            "desc": "การประยุกต์ใช้ AI ในการพัฒนาเว็บแอปพลิเคชันอย่างรวดเร็ว (Prompt-to-App) ร่วมกับการออกแบบฐานข้อมูลและแดชบอร์ดบริหารโครงการ (Agile Project Management Dashboard) บน Notion เพื่อติดตามสถานะงาน, ผู้รับผิดชอบ (Assignee), ระดับความสำคัญ (Priority), และกำหนดส่งมอบ (Sprint Deadline)",
            "business_value": "ย่นระยะเวลาการพัฒนาต้นแบบซอฟต์แวร์ (Prototyping) จากหลายสัปดาห์เหลือเพียงไม่กี่ชั่วโมง และช่วยให้ผู้จัดการฝ่าย IT มองเห็นภาพรวมสถานะของโครงการได้อย่างชัดเจน",
            "action": "ออกแบบ Data Model ตารางงาน และพัฒนาแดชบอร์ดติดตามสถานะงานโครงการ 5 งานพร้อมฟีเจอร์ Interactive Filter",
            "output": "ไฟล์แดชบอร์ด 'bolt_notion_dashboard.html' สร้างจากสคริปต์ 'automation/07_bolt_notion_dashboard.py'",
            "img": os.path.join(screenshots_dir, "07_bolt_new.png"),
            "caption": "ภาพที่ 7: หน้า Notion Learning Hub และ AI x Notion Dashboard สำหรับบริหารจัดการงานโปรเจกต์"
        },
        {
            "id": "8",
            "name": "Scribe AI",
            "date": "22 ตุลาคม 2569",
            "badge": "Automated SOP & Process Documentation Generator",
            "desc": "เครื่องมือ AI สำหรับสร้างคู่มือการปฏิบัติงานมาตรฐาน (Standard Operating Procedure - SOP) แบบอัตโนมัติ โดยระบบจะทำการบันทึกทุกคลิกและการเลื่อนหน้าจอของผู้ใช้งาน จากนั้นจะนำมาเรียบเรียงเป็นขั้นตอนคำอธิบายภาษาธรรมชาติพร้อมภาพประกอบและจุดเน้นย้ำ (Callouts) อย่างแม่นยำ",
            "business_value": "ลดเวลาในการจัดทำคู่มือฝึกอบรมพนักงานลงได้มากกว่า 90% และทำให้การส่งต่องานภายในองค์กรเป็นไปตามมาตรฐานเดียวกันอย่างถูกต้อง",
            "action": "ทำการบันทึกและสร้างคู่มือ SOP ขั้นตอนการส่งงานในระบบ PIM e-Learning อย่างละเอียดเป็นขั้นเป็นตอน",
            "output": "ไฟล์คู่มือการทำงาน 'scribe_sop_guide.html' ที่บันทึกขั้นตอนการส่งงานอย่างเป็นระบบ",
            "img": os.path.join(screenshots_dir, "08_scribe.png"),
            "caption": "ภาพที่ 8: หน้าแพลตฟอร์ม Scribe AI ในการสร้างขั้นตอนและคู่มือ SOP แบบอัตโนมัติ"
        },
        {
            "id": "9",
            "name": "Khui AI",
            "date": "22 ตุลาคม 2569",
            "badge": "Enterprise Thai Conversational Platform & Character AI",
            "desc": "แพลตฟอร์มระบบสนทนาปัญญาประดิษฐ์ภาษาไทยระดับองค์กร ที่มีความโดดเด่นในการสร้างคาร์แรกเตอร์ AI (Custom Persona) และการโต้ตอบที่เข้าใจสำนวน บริบททางอารมณ์ และความสุภาพตามมารยาทสังคมไทยอย่างเป็นเลิศ",
            "business_value": "ยกระดับระบบบริการลูกค้าสัมพันธ์ (CRM & Call Center Bot) ให้มีความเป็นมิตร ดูเป็นธรรมชาติ และสามารถตอบคำถามซับซ้อนได้อย่างน่าประทับใจ",
            "action": "ทดสอบการสร้างบทสนทนาและการตอบสนองของระบบ และทำแบบทดสอบ Khui AI Quiz วัดความรู้ความเข้าใจ",
            "output": "ผลคะแนนแบบทดสอบ Khui AI เต็ม 20/20 (100%) พร้อมชื่อ-รหัสนักศึกษาบนหน้าระบบ",
            "img": os.path.join(screenshots_dir, "09_khui_ai.png"),
            "caption": "ภาพที่ 9: หน้าผลคะแนนแบบทดสอบ Khui AI Quiz ได้คะแนนเต็ม 20/20 (นายภูริพัฒน์ เหมกุล 6752300313)"
        }
    ]

    for tool in tools_detail:
        doc.add_page_break()
        
        # Tool Header Box
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell = tbl.cell(0, 0)
        cell.width = Inches(7.4)
        set_cell_background(cell, "1E293B")
        set_cell_margins(cell, top=60, bottom=60, left=120, right=120)
        
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run(f"เครื่องมือลำดับที่ {tool['id']}: {tool['name']}")
        format_run(r, size_pt=18, color_rgb=(255, 255, 255), bold=True)
        
        p2 = cell.add_paragraph()
        p2.paragraph_format.space_before = Pt(0)
        p2.paragraph_format.space_after = Pt(0)
        r_meta = p2.add_run(f"📅 วันที่ทำ Workshop: {tool['date']}  |  🏷️ หมวดหมู่: {tool['badge']}")
        format_run(r_meta, size_pt=13.5, color_rgb=(147, 197, 253), bold=False)
        
        # Description
        p_desc = doc.add_paragraph()
        p_desc.paragraph_format.space_before = Pt(10)
        p_desc.paragraph_format.space_after = Pt(4)
        r_lbl = p_desc.add_run("🔍 ภาพรวมและสถาปัตยกรรมเทคโนโลยี: ")
        format_run(r_lbl, size_pt=14.5, color_rgb=(30, 64, 175), bold=True)
        r_txt = p_desc.add_run(tool['desc'])
        format_run(r_txt, size_pt=14.5, color_rgb=(15, 23, 42), bold=False)
        
        # Business Value
        p_val = doc.add_paragraph()
        p_val.paragraph_format.space_before = Pt(4)
        p_val.paragraph_format.space_after = Pt(4)
        r_lbl2 = p_val.add_run("💡 คุณค่าและการประยุกต์ใช้ในธุรกิจ (Business & IT Value): ")
        format_run(r_lbl2, size_pt=14.5, color_rgb=(180, 83, 9), bold=True)
        r_txt2 = p_val.add_run(tool['business_value'])
        format_run(r_txt2, size_pt=14.5, color_rgb=(15, 23, 42), bold=False)
        
        # Action & Output
        p_act = doc.add_paragraph()
        p_act.paragraph_format.space_before = Pt(4)
        p_act.paragraph_format.space_after = Pt(8)
        r_lbl3 = p_act.add_run("🛠️ กิจกรรมที่ปฏิบัติและผลงานที่ส่งมอบ: ")
        format_run(r_lbl3, size_pt=14.5, color_rgb=(22, 101, 52), bold=True)
        r_txt3 = p_act.add_run(f"{tool['action']} โดยมีชิ้นงานส่งมอบคือ {tool['output']}")
        format_run(r_txt3, size_pt=14.5, color_rgb=(15, 23, 42), bold=False)
        
        # Screenshot Image
        if os.path.exists(tool['img']):
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(4)
            p_img.paragraph_format.space_after = Pt(2)
            run_img = p_img.add_run()
            run_img.add_picture(tool['img'], width=Inches(6.4))
            
            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_before = Pt(2)
            p_cap.paragraph_format.space_after = Pt(6)
            r_cap = p_cap.add_run(tool['caption'])
            format_run(r_cap, size_pt=12.5, color_rgb=(100, 116, 139), italic=True)

    # Section 5: Additional Quiz Full Scores Showcase
    doc.add_page_break()
    p_quiz_hdr = doc.add_paragraph()
    r_qh = p_quiz_hdr.add_run("🏆 ภาคผนวก: หลักฐานคะแนนแบบทดสอบความรู้เต็ม 20/20 (Quiz Scorecards)")
    format_run(r_qh, size_pt=17, color_rgb=(15, 23, 42), bold=True)
    
    extra_quizzes = [
        {
            "name": "Napkin AI Knowledge Assessment Form",
            "score": "ผลคะแนน: 20 / 20 คะแนนเต็ม (100%)",
            "img": os.path.join(current_dir, "napkin_ai_quiz_score_20_20.png"),
            "caption": "ภาคผนวกที่ 1: ผลคะแนนแบบทดสอบ Napkin AI เต็ม 20/20 ผ่านระบบ Google Forms อัตโนมัติ"
        },
        {
            "name": "Typhoon OCR Knowledge Assessment Form",
            "score": "ผลคะแนน: 20 / 20 คะแนนเต็ม (100%)",
            "img": os.path.join(current_dir, "typhoon_ocr_quiz_score.png"),
            "caption": "ภาคผนวกที่ 2: ผลคะแนนการส่งแบบทดสอบ Typhoon OCR Quiz Form ครบถ้วนถูกต้อง"
        }
    ]
    
    for q in extra_quizzes:
        p_qt = doc.add_paragraph()
        p_qt.paragraph_format.space_before = Pt(10)
        p_qt.paragraph_format.space_after = Pt(2)
        r = p_qt.add_run(f"🎯 {q['name']} · {q['score']}")
        format_run(r, size_pt=15, color_rgb=(22, 101, 52), bold=True)
        
        if os.path.exists(q['img']):
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(2)
            p_img.paragraph_format.space_after = Pt(2)
            run_img = p_img.add_run()
            run_img.add_picture(q['img'], width=Inches(6.2))
            
            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_before = Pt(0)
            p_cap.paragraph_format.space_after = Pt(8)
            r_cap = p_cap.add_run(q['caption'])
            format_run(r_cap, size_pt=12.5, color_rgb=(100, 116, 139), italic=True)

    doc_out = os.path.join(current_dir, "Workshop_AI_Coaching_6752300313.docx")
    doc.save(doc_out)
    print(f"[+] Successfully generated master DOCX at: {doc_out}")

if __name__ == "__main__":
    build_workshop_document()
