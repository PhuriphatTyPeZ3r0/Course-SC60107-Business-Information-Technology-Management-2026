"""
Workshop 7: Bolt.new / Notion Agile Project Dashboard
Student: นายภูริพัฒน์ เหมกุล (6752300313)
Course: SC60107 Business IT Management
Prompt: ออกแบบตัวอย่าง Data ที่ใช้สร้างงาน/โปรเจกต์ เช่น หน้า Login ที่มีประเภท ชื่องาน/รายละเอียดงาน/ประเภท/สถานะ/ผู้รับผิดชอบ/กำหนดส่ง/หมวดงาน และเชื่อมต่อข้อมูลเข้ากับ Dashboard และ Status
"""
import json

SAMPLE_TASKS = [
    {
        "task_id": "TASK-101",
        "task_name": "ออกแบบ UI หน้า Login & Auth Flow",
        "description": "จัดทำ Mockup หน้าจอเข้าสู่ระบบ รองรับ Email/Password และ Single Sign-On (PIM Account)",
        "task_type": "Design / UI",
        "category": "Authentication",
        "status": "Done",
        "assignee": "นายภูริพัฒน์ เหมกุล",
        "due_date": "2026-10-14"
    },
    {
        "task_id": "TASK-102",
        "task_name": "พัฒนา API Backend ระบบตรวจสอบสิทธิ์",
        "description": "สร้าง Endpoint /api/login ตรวจสอบ Credential และออก JWT Session Token",
        "task_type": "Backend",
        "category": "Authentication",
        "status": "Done",
        "assignee": "ธีรภัทร ทองตำลึง",
        "due_date": "2026-10-15"
    },
    {
        "task_id": "TASK-103",
        "task_name": "เชื่อมต่อระบบฐานข้อมูลผู้ใช้งาน",
        "description": "ออกแบบตาราง Users พร้อมเข้ารหัสผ่านด้วย bcrypt และตั้งค่าสิทธิ์ RBAC",
        "task_type": "Database",
        "category": "Security",
        "status": "Done",
        "assignee": "จิมมี่ โกรทเฮีนร์",
        "due_date": "2026-10-16"
    },
    {
        "task_id": "TASK-104",
        "task_name": "ทดสอบระบบความปลอดภัย & Brute-force Prevention",
        "description": "เขียน Unit & Integration test ดักจับ Rate-limiting และป้องกัน SQL Injection",
        "task_type": "QA & Security",
        "category": "Quality Assurance",
        "status": "In Progress",
        "assignee": "พงษ์ดนัย สมภาร",
        "due_date": "2026-10-18"
    },
    {
        "task_id": "TASK-105",
        "task_name": "Deploy Live Environment บน Cloudflare/Vercel",
        "description": "ตั้งค่า CI/CD Pipeline เชื่อมต่อ GitHub Actions เข้ากับ Vercel Production",
        "task_type": "DevOps",
        "category": "Infrastructure",
        "status": "Pending",
        "assignee": "กิตติภัทร์ เพ้งน้ำคำ",
        "due_date": "2026-10-20"
    }
]

def generate_notion_bolt_dashboard_html(output_file="bolt_notion_dashboard.html"):
    rows_html = ""
    for t in SAMPLE_TASKS:
        status_color = "#16A34A" if t["status"] == "Done" else ("#CA8A04" if t["status"] == "In Progress" else "#64748B")
        rows_html += f"""
        <tr style="border-bottom: 1px solid #E2E8F0;">
            <td style="padding: 12px; font-weight: bold; color: #1E293B;">{t["task_id"]}</td>
            <td style="padding: 12px; color: #0F172A;"><strong>{t["task_name"]}</strong><br/><span style="font-size: 12px; color: #64748B;">{t["description"]}</span></td>
            <td style="padding: 12px;"><span style="background: #EEF2FF; color: #4338CA; padding: 4px 10px; border-radius: 9999px; font-size: 12px;">{t["task_type"]}</span></td>
            <td style="padding: 12px; color: #475569;">{t["category"]}</td>
            <td style="padding: 12px;"><span style="background: {status_color}20; color: {status_color}; padding: 4px 10px; border-radius: 9999px; font-weight: bold; font-size: 12px;">● {t["status"]}</span></td>
            <td style="padding: 12px; color: #334155;">{t["assignee"]}</td>
            <td style="padding: 12px; color: #64748B;">{t["due_date"]}</td>
        </tr>
        """

    html = f"""<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<title>Bolt.new & Notion Agile Task Dashboard - 6752300313</title>
<style>
  body {{ font-family: 'Segoe UI', Tahoma, sans-serif; background: #F8FAFC; margin: 0; padding: 24px; color: #0F172A; }}
  .container {{ max-width: 1000px; margin: 0 auto; background: white; border-radius: 16px; box-shadow: 0 4px 20px rgba(0,0,0,0.06); padding: 32px; }}
  .header {{ border-bottom: 2px solid #F1F5F9; padding-bottom: 20px; margin-bottom: 24px; }}
  .metrics {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin-bottom: 28px; }}
  .metric-card {{ background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 12px; padding: 18px; }}
  .metric-val {{ font-size: 28px; font-weight: bold; color: #2563EB; margin-top: 6px; }}
  table {{ width: 100%; border-collapse: collapse; text-align: left; font-size: 14px; }}
  th {{ background: #0F172A; color: white; padding: 12px; font-weight: 600; }}
</style>
</head>
<body>
<div class="container">
  <div class="header">
    <span style="color: #64748B; font-size: 13px;">SC60107 Business IT Management · Workshop: Bolt.new & Notion</span>
    <h1 style="margin: 6px 0 0 0; font-size: 24px;">🚀 Agile Sprint Status & Task Dashboard</h1>
    <p style="margin: 4px 0 0 0; color: #475569;">ผู้รับผิดชอบ: นายภูริพัฒน์ เหมกุล (6752300313) · กลุ่ม 1.2-1</p>
  </div>

  <div class="metrics">
    <div class="metric-card">
      <div style="color: #64748B; font-size: 13px;">งานทั้งหมดใน Sprint</div>
      <div class="metric-val">5 Tasks</div>
    </div>
    <div class="metric-card">
      <div style="color: #64748B; font-size: 13px;">สถานะงานที่เสร็จสิ้น (Done)</div>
      <div class="metric-val" style="color: #16A34A;">60% (3/5)</div>
    </div>
    <div class="metric-card">
      <div style="color: #64748B; font-size: 13px;">กำหนดส่งรอบปัจจุบัน</div>
      <div class="metric-val" style="color: #D97706; font-size: 20px;">18 ต.ค. 2569</div>
    </div>
  </div>

  <table>
    <thead>
      <tr>
        <th>รหัสงาน</th>
        <th>ชื่องาน / รายละเอียด</th>
        <th>ประเภท</th>
        <th>หมวดงาน</th>
        <th>สถานะ</th>
        <th>ผู้รับผิดชอบ</th>
        <th>กำหนดส่ง</th>
      </tr>
    </thead>
    <tbody>
      {rows_html}
    </tbody>
  </table>
</div>
</body>
</html>"""
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[+] Successfully generated Bolt/Notion Dashboard at {output_file}")

if __name__ == "__main__":
    generate_notion_bolt_dashboard_html()
