# -*- coding: utf-8 -*-
import os

new_section4_html = '''  <!-- SECTION 4: STRATEGIC BUSINESS IT INSIGHTS -->
  <div class="fade" style="margin-top: 28px;">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; flex-wrap: wrap; gap: 10px;">
      <div class="section-title" style="margin-bottom: 0;">
        <span class="st-icon st-o"><span class="icon" style="font-size:16px;">💡</span></span> 
        <span style="font-size:16px; font-weight:700; letter-spacing:-0.01em;">กรอบกลยุทธ์การจัดการเทคโนโลยีสารสนเทศทางธุรกิจ (SC60107 Executive Strategic Framework)</span>
      </div>
      <div style="display: flex; gap: 8px;">
        <span class="badge" style="background: rgba(56, 189, 248, 0.12); color: var(--cyan); border-color: rgba(56, 189, 248, 0.3); font-size: 11px;">
          ✦ Data-Driven Decision Model
        </span>
        <span class="badge" style="background: rgba(249, 115, 22, 0.12); color: var(--orange); border-color: rgba(249, 115, 22, 0.3); font-size: 11px;">
          ✦ Phuriphat Custom Architecture
        </span>
      </div>
    </div>

    <!-- Strategic Grid (3 Specialized Pillars) -->
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 18px;">
      
      <!-- PILLAR 1: Campus Digital Subscription -->
      <div class="card" style="padding: 22px; background: linear-gradient(180deg, rgba(37, 99, 235, 0.08) 0%, var(--glass) 100%); border: 1px solid rgba(56, 189, 248, 0.25); position: relative; overflow: hidden;">
        <div style="position: absolute; top: 0; left: 0; right: 0; height: 3px; background: linear-gradient(90deg, var(--blue), var(--cyan));"></div>
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;">
          <span style="font-size: 11px; font-weight: 700; color: var(--cyan); letter-spacing: 0.08em; text-transform: uppercase;">[ Pillar 01 · Digital Ecosystem ]</span>
          <span style="font-size: 20px;">🎓</span>
        </div>
        <h4 style="font-size: 15px; font-weight: 700; color: var(--txt); margin-bottom: 10px; line-height: 1.4;">
          Campus Digital Subscription &amp; Gen Z Loyalty Wallet
        </h4>
        <div style="background: var(--track-bg); border-radius: 8px; padding: 10px 12px; margin-bottom: 12px; font-size: 11.5px; color: var(--txt-sub); border-left: 3px solid var(--cyan);">
          <b>Data Insight:</b> สาขามหาวิทยาลัยครองส่วนแบ่งยอดขายสูงสุดถึง <b>46.04% (฿33,395)</b> และมียอดซื้อ 453 ชิ้น แสดงถึงความหนาแน่นของกลุ่มลูกค้านิสิตและบุคลากร
        </div>
        <p style="font-size: 12.5px; color: var(--muted); line-height: 1.65; margin-bottom: 14px;">
          พัฒนาระบบ <b>"Campus Coffee &amp; Bakery Pass"</b> ในรูปแบบ Mobile Subscription บน LINE OA หรือ Progressive Web App (PWA) ให้สิทธิ์สมาชิกจ่ายล่วงหน้าแบบเหมาจ่ายรายเดือน เพื่อรับเครื่องดื่มและเบเกอรีในราคาเฉลี่ยต่อหน่วยที่ประหยัดลง สร้างกระแสเงินสดรับล่วงหน้า (Predictable Cash Flow) และล็อกพฤติกรรมลูกค้ากลุ่ม Gen Z
        </p>
        <div style="display: flex; flex-wrap: wrap; gap: 6px; padding-top: 10px; border-top: 1px solid var(--border-sub);">
          <span style="font-size: 10.5px; padding: 2px 8px; border-radius: 4px; background: rgba(56,189,248,0.12); color: var(--cyan); font-weight: 600;">ROI: +35% Retention</span>
          <span style="font-size: 10.5px; padding: 2px 8px; border-radius: 4px; background: var(--card-sub-bg); color: var(--muted);">Tech: Cloud Wallet &amp; PWA</span>
        </div>
      </div>

      <!-- PILLAR 2: SCM & COGS Restructuring -->
      <div class="card" style="padding: 22px; background: linear-gradient(180deg, rgba(249, 115, 22, 0.08) 0%, var(--glass) 100%); border: 1px solid rgba(249, 115, 22, 0.25); position: relative; overflow: hidden;">
        <div style="position: absolute; top: 0; left: 0; right: 0; height: 3px; background: linear-gradient(90deg, var(--orange), var(--amber));"></div>
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;">
          <span style="font-size: 11px; font-weight: 700; color: var(--orange); letter-spacing: 0.08em; text-transform: uppercase;">[ Pillar 02 · Supply Chain SCM ]</span>
          <span style="font-size: 20px;">🥐</span>
        </div>
        <h4 style="font-size: 15px; font-weight: 700; color: var(--txt); margin-bottom: 10px; line-height: 1.4;">
          Bakery COGS Optimization &amp; Central Kitchen ERP
        </h4>
        <div style="background: var(--track-bg); border-radius: 8px; padding: 10px 12px; margin-bottom: 12px; font-size: 11.5px; color: var(--txt-sub); border-left: 3px solid var(--orange);">
          <b>Data Insight:</b> ชีสเค้กและครัวซองต์สร้างรายได้รวม <b>32.3% (฿23,450)</b> แต่มี Gross Margin ต่ำที่สุดเพียง <b>34.5%</b> และ <b>29.4%</b> ตามลำดับ (ต้นทุนสูง ฿72 และ ฿60)
        </div>
        <p style="font-size: 12.5px; color: var(--muted); line-height: 1.65; margin-bottom: 14px;">
          ปรับโครงสร้างต้นทุนขาย (COGS) ด้วยระบบ <b>Central Kitchen ERP &amp; Raw Material Forecasting</b> จัดซื้อแป้ง เนย และชีสแบบรวมศูนย์ (Volume Aggregation) ควบคุมการสูญเสียในสายการผลิต พร้อมทั้งปรับขนาดแบบ Mini-Portion หรือขายแบบ Dual-Pack เพื่อขยายอัตรากำไรขั้นต้น (GP Margin) ของเบเกอรีขึ้นอย่างน้อย +8-10% ส่งผลให้กำไรสุทธิรวมเติบโตทันที
        </p>
        <div style="display: flex; flex-wrap: wrap; gap: 6px; padding-top: 10px; border-top: 1px solid var(--border-sub);">
          <span style="font-size: 10.5px; padding: 2px 8px; border-radius: 4px; background: rgba(249,115,22,0.12); color: var(--orange); font-weight: 600;">Profit: +฿3,200/mo</span>
          <span style="font-size: 10.5px; padding: 2px 8px; border-radius: 4px; background: var(--card-sub-bg); color: var(--muted);">Tech: Central ERP &amp; SCM</span>
        </div>
      </div>

      <!-- PILLAR 3: Smart POS & Dynamic Promotion -->
      <div class="card" style="padding: 22px; background: linear-gradient(180deg, rgba(16, 185, 129, 0.08) 0%, var(--glass) 100%); border: 1px solid rgba(16, 185, 129, 0.25); position: relative; overflow: hidden;">
        <div style="position: absolute; top: 0; left: 0; right: 0; height: 3px; background: linear-gradient(90deg, var(--green), #6ee7b7);"></div>
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;">
          <span style="font-size: 11px; font-weight: 700; color: var(--green); letter-spacing: 0.08em; text-transform: uppercase;">[ Pillar 03 · Dynamic Operation ]</span>
          <span style="font-size: 20px;">⚡</span>
        </div>
        <h4 style="font-size: 15px; font-weight: 700; color: var(--txt); margin-bottom: 10px; line-height: 1.4;">
          Daypart Dynamic Pricing &amp; Off-Peak Load Balancing
        </h4>
        <div style="background: var(--track-bg); border-radius: 8px; padding: 10px 12px; margin-bottom: 12px; font-size: 11.5px; color: var(--txt-sub); border-left: 3px solid var(--green);">
          <b>Data Insight:</b> ยอดขายสาขาห้างสรรพสินค้า (24.67%) และสำนักงาน (29.29%) ชะลอตัวในช่วงบ่ายวันธรรมดา และยอดขายรายวันมีความผันผวนสูง
        </div>
        <p style="font-size: 12.5px; color: var(--muted); line-height: 1.65; margin-bottom: 14px;">
          ติดตั้งระบบ <b>Smart POS Daypart Analytics</b> ซิงค์กับระบบ Digital Signage หน้าร้าน เพื่อปล่อยโปรโมชัน Dynamic Flash Sale อัตโนมัติเฉพาะช่วงบ่าย (13:30 - 15:30 น.) สำหรับเมนูกาแฟกำไรสูง (ลาเต้ GP 62.7%, คาปูชิโน GP 64.0%) กระจายโหลดกำลังการผลิตให้สม่ำเสมอ ลดภาระการรอคิวในช่วงเช้า และลด Food Waste ของสินค้าสด
        </p>
        <div style="display: flex; flex-wrap: wrap; gap: 6px; padding-top: 10px; border-top: 1px solid var(--border-sub);">
          <span style="font-size: 10.5px; padding: 2px 8px; border-radius: 4px; background: rgba(16,185,129,0.12); color: var(--green); font-weight: 600;">Capacity: +22% Utilization</span>
          <span style="font-size: 10.5px; padding: 2px 8px; border-radius: 4px; background: var(--card-sub-bg); color: var(--muted);">Tech: Smart POS &amp; IoT Signage</span>
        </div>
      </div>

    </div>
  </div>
'''

def update_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    marker_start = '  <!-- SECTION 4: STRATEGIC BUSINESS IT INSIGHTS -->'
    marker_end = '  <!-- FOOTER -->'

    s_idx = html.find(marker_start)
    e_idx = html.find(marker_end, s_idx) if s_idx != -1 else -1

    if s_idx != -1 and e_idx != -1:
        html = html[:s_idx] + new_section4_html + '\n\n' + html[e_idx:]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'Successfully updated unique insights in {filepath}')
    else:
        print(f'Could not find markers in {filepath}')

if __name__ == '__main__':
    update_html('Dashboard-6752300313.html')
    update_html('02_Labs_Assignments/Week5/Dashboard-6752300313.html')
