# -*- coding: utf-8 -*-
import os

def update_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Add student badge to nav-right if not present
    badge_html = '''    <span class="badge" style="background: rgba(37, 99, 235, 0.15); color: var(--cyan); border-color: rgba(56, 189, 248, 0.3);">
      <span class="icon">🎓</span> 6752300313 นายภูริพัฒน์ เหมกุล · กลุ่ม 1.2-1 CAI PIM
    </span>\n'''

    if '6752300313 นายภูริพัฒน์ เหมกุล' not in html:
        target_nav = '<span class="badge"><span class="icon" id="infoIcon"></span> ข้อมูลจำลองเพื่อการเรียนรู้ · ส.ค. 2569</span>'
        if target_nav in html:
            html = html.replace(target_nav, badge_html + '    ' + target_nav)
            print(f'Added badge in {path}')
        else:
            print(f'target_nav not found in {path}')

    # 2. Add Strategic Insights and Footer before closing container div
    insights_html = '''
  <!-- SECTION 4: STRATEGIC BUSINESS IT INSIGHTS -->
  <div class="fade" style="margin-top: 24px;">
    <div class="section-title">
      <span class="st-icon st-a"><span class="icon" style="font-size:16px;">💡</span></span> 
      <span>ข้อเสนอแนะเชิงกลยุทธ์ทางธุรกิจ (Executive Strategic Insights) · SC60107</span>
    </div>
    <div class="card" style="padding: 22px;">
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px;">
        <div style="background: var(--card-sub-bg); border: 1px solid var(--border-sub); border-radius: 12px; padding: 18px;">
          <div style="display:flex; align-items:center; gap:8px; font-weight:600; font-size:14px; color:var(--orange); margin-bottom:10px;">
            <span style="font-size:18px;">🎯</span> 1. Menu Engineering &amp; High-Margin Bundling
          </div>
          <p style="font-size:12.5px; color:var(--txt-sub); line-height:1.65;">
            สินค้ากลุ่มเบเกอรี (ชีสเค้ก ฿13,420 และครัวซองต์ ฿10,030) สร้างรายได้สูงสุดรวมกันถึง 32.3% ควรจัดเซตคู่ (Bundle) ร่วมกับเครื่องดื่มกาแฟกำไรสูง เช่น ลาเต้ (GP 62.7%) เพื่อผลักดันยอดขายเฉลี่ยต่อบิล (AOV) จากปัจจุบัน ฿725.30 ให้เติบโตยิ่งขึ้น
          </p>
        </div>
        <div style="background: var(--card-sub-bg); border: 1px solid var(--border-sub); border-radius: 12px; padding: 18px;">
          <div style="display:flex; align-items:center; gap:8px; font-weight:600; font-size:14px; color:var(--cyan); margin-bottom:10px;">
            <span style="font-size:18px;">🚚</span> 2. สาขาและการจัดสรรสินค้า (Branch Allocation)
          </div>
          <p style="font-size:12.5px; color:var(--txt-sub); line-height:1.65;">
            สาขามหาวิทยาลัยสร้างยอดขายสูงสุดถึง ฿33,395 (46.0%) โดดเด่นทั้งกาแฟและชีสเค้ก ในขณะที่สาขาสำนักงานมียอดบราวนีและชาไทยหนาแน่น ควรวางแผนระบบ Supply Chain กระจายวัตถุดิบและรอบอบเบเกอรีให้สอดคล้องกับพฤติกรรมลูกค้าแต่ละทำเล
          </p>
        </div>
        <div style="background: var(--card-sub-bg); border: 1px solid var(--border-sub); border-radius: 12px; padding: 18px;">
          <div style="display:flex; align-items:center; gap:8px; font-weight:600; font-size:14px; color:var(--green); margin-bottom:10px;">
            <span style="font-size:18px;">⚡</span> 3. Real-time POS &amp; Demand Forecasting
          </div>
          <p style="font-size:12.5px; color:var(--txt-sub); line-height:1.65;">
            ยอดขายแสดงแนวโน้มพุ่งสูงชัดเจนในวันที่ 15 และ 28 ของเดือน ควบรวมระบบ Cloud POS ร่วมกับโมเดล AI Demand Forecasting ในการแจ้งเตือนสต็อกวัตถุดิบขาดแคลนล่วงหน้า 3 วัน เพื่อป้องกันปัญหา Lost Sales Opportunities อย่างมีประสิทธิภาพ
          </p>
        </div>
      </div>
    </div>
  </div>

  <!-- FOOTER -->
  <footer style="margin-top: 36px; padding-top: 20px; border-top: 1px solid var(--glass-b); display: flex; justify-content: space-between; align-items: center; font-size: 12px; color: var(--muted); flex-wrap: wrap; gap: 12px;">
    <div>เอกสารส่งมอบงาน: Dashboard (10 คะแนน) · วิชา SC60107 การจัดการเทคโนโลยีสารสนเทศทางธุรกิจ · สถาบันการจัดการปัญญาภิวัฒน์ (PIM)</div>
    <div style="font-weight:600; color:var(--orange);">ผู้จัดทำ: นายภูริพัฒน์ เหมกุล (Phuriphat Hemakul) · รหัสนักศึกษา: 6752300313 · กลุ่ม 1.2-1 CAI PIM</div>
  </footer>
'''

    if 'ข้อเสนอแนะเชิงกลยุทธ์ทางธุรกิจ' not in html:
        # Find position right before the closing </div> of container
        # Let's inspect where modal2D begins
        marker = '<!-- ==========================================================================\n     2D MINIMALIST DETAIL MODAL POP-UP'
        is_crlf = '\r\n' in html
        if is_crlf:
            marker = marker.replace('\n', '\r\n')
            insights_html = insights_html.replace('\n', '\r\n')
            badge_html = badge_html.replace('\n', '\r\n')

        idx = html.find(marker)
        if idx != -1:
            # find last </div> before idx
            last_div_idx = html.rfind('</div>', 0, idx)
            if last_div_idx != -1:
                html = html[:last_div_idx] + insights_html + '\n' + html[last_div_idx:]
                print(f'Added insights and footer in {path}')
        else:
            print(f'marker not found in {path}')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Successfully updated {path}')

if __name__ == '__main__':
    update_file('Dashboard-6752300313.html')
    update_file('02_Labs_Assignments/Week5/Dashboard-6752300313.html')
