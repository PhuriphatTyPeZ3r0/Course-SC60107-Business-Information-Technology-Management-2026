import os
import re

# Read RAW_SALES from Week5 original
with open(r'02_Labs_Assignments\Week5\Dashboard-6752300313.html', 'r', encoding='utf-8') as f:
    orig_text = f.read()

m = re.search(r'const RAW_SALES = (\[.*?\]);', orig_text, re.DOTALL)
raw_sales_json = m.group(1)

html_template = f'''<!DOCTYPE html>
<html lang="th" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cobalt Executive BI — Cafe &amp; Bakery Sales Analytics (6752300313)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Prompt:wght@300;400;500;600;700&display=swap" rel="stylesheet">

<style>
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

:root {{
  --bg-base: #070d1e;
  --bg-surface: #0c1736;
  --bg-card: rgba(15, 29, 66, 0.75);
  --bg-card-hover: rgba(22, 42, 94, 0.9);
  --border-card: rgba(59, 130, 246, 0.2);
  --border-card-hover: rgba(59, 130, 246, 0.45);
  --primary: #2563eb;
  --primary-glow: rgba(37, 99, 235, 0.3);
  --blue: #3b82f6;
  --cyan: #38bdf8;
  --gold: #f59e0b;
  --gold-glow: rgba(245, 158, 11, 0.25);
  --orange: #f97316;
  --emerald: #10b981;
  --rose: #f43f5e;
  --txt-main: #f8fafc;
  --txt-muted: #94a3b8;
  --txt-sub: #cbd5e1;
  --pill-bg: rgba(37, 99, 235, 0.12);
  --pill-border: rgba(37, 99, 235, 0.32);
  --font-main: 'Plus Jakarta Sans', 'Prompt', system-ui, -apple-system, sans-serif;
  --shadow-lg: 0 16px 36px -8px rgba(0, 0, 0, 0.65), 0 0 24px rgba(37, 99, 235, 0.1);
  --shadow-card: 0 8px 24px -4px rgba(0, 0, 0, 0.45);
}}

[data-theme="light"] {{
  --bg-base: #f0f4fd;
  --bg-surface: #ffffff;
  --bg-card: rgba(255, 255, 255, 0.95);
  --bg-card-hover: #ffffff;
  --border-card: rgba(37, 99, 235, 0.18);
  --border-card-hover: rgba(37, 99, 235, 0.45);
  --primary: #1d4ed8;
  --primary-glow: rgba(29, 78, 216, 0.15);
  --blue: #2563eb;
  --cyan: #0284c7;
  --gold: #d97706;
  --gold-glow: rgba(217, 119, 6, 0.15);
  --orange: #ea580c;
  --emerald: #059669;
  --rose: #e11d48;
  --txt-main: #0f172a;
  --txt-muted: #64748b;
  --txt-sub: #334155;
  --pill-bg: rgba(37, 99, 235, 0.08);
  --pill-border: rgba(37, 99, 235, 0.25);
  --shadow-lg: 0 16px 36px -8px rgba(30, 58, 138, 0.12);
  --shadow-card: 0 8px 24px -4px rgba(30, 58, 138, 0.08);
}}

body {{
  font-family: var(--font-main);
  background: var(--bg-base);
  color: var(--txt-main);
  min-height: 100vh;
  line-height: 1.5;
  background-image: 
    radial-gradient(circle at 12% 18%, rgba(37, 99, 235, 0.1) 0%, transparent 45%),
    radial-gradient(circle at 88% 82%, rgba(245, 158, 11, 0.07) 0%, transparent 45%);
  transition: background-color 0.3s ease, color 0.3s ease;
}}

/* Navbar */
.navbar {{
  position: sticky;
  top: 0;
  z-index: 100;
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  background: rgba(12, 23, 54, 0.88);
  border-bottom: 1px solid var(--border-card);
  padding: 12px 32px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
}}
[data-theme="light"] .navbar {{
  background: rgba(255, 255, 255, 0.92);
}}

.brand-wrapper {{
  display: flex;
  align-items: center;
  gap: 14px;
}}
.brand-icon {{
  width: 42px;
  height: 42px;
  border-radius: 12px;
  background: linear-gradient(135deg, var(--primary), #1e40af);
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 0 16px var(--primary-glow);
  color: #fff;
  font-size: 22px;
}}
.brand-title {{
  font-size: 17px;
  font-weight: 800;
  letter-spacing: -0.01em;
  background: linear-gradient(90deg, var(--txt-main), var(--cyan));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}}
.brand-sub {{
  font-size: 12px;
  color: var(--txt-muted);
  font-weight: 500;
}}

.student-badge {{
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 6px 16px;
  border-radius: 9999px;
  background: var(--pill-bg);
  border: 1px solid var(--pill-border);
  font-size: 13px;
  font-weight: 600;
  color: var(--cyan);
}}
.student-badge .dot {{
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--cyan);
  box-shadow: 0 0 8px var(--cyan);
}}

.nav-controls {{
  display: flex;
  align-items: center;
  gap: 12px;
}}
.filter-select {{
  background: var(--bg-surface);
  border: 1px solid var(--border-card);
  color: var(--txt-main);
  padding: 8px 14px;
  border-radius: 10px;
  font-family: inherit;
  font-size: 13px;
  cursor: pointer;
  outline: none;
  transition: all 0.2s;
}}
.filter-select:focus {{
  border-color: var(--primary);
  box-shadow: 0 0 0 2px var(--primary-glow);
}}
.btn-theme {{
  width: 38px;
  height: 38px;
  border-radius: 10px;
  background: var(--bg-surface);
  border: 1px solid var(--border-card);
  color: var(--txt-main);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  font-size: 18px;
  transition: all 0.2s;
}}
.btn-theme:hover {{
  border-color: var(--primary);
  transform: scale(1.05);
}}

/* Container */
.container {{
  max-width: 1340px;
  margin: 0 auto;
  padding: 28px 24px;
}}

/* KPI Row */
.kpi-row {{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
  margin-bottom: 28px;
}}
.kpi-card {{
  background: var(--bg-card);
  border: 1px solid var(--border-card);
  border-radius: 18px;
  padding: 22px;
  position: relative;
  overflow: hidden;
  box-shadow: var(--shadow-card);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
}}
.kpi-card:hover {{
  transform: translateY(-3px);
  border-color: var(--border-card-hover);
  box-shadow: var(--shadow-lg);
}}
.kpi-card::before {{
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: linear-gradient(90deg, var(--blue), var(--cyan), var(--gold));
  opacity: 0.85;
}}
.kpi-header {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 12px;
}}
.kpi-title {{
  font-size: 13px;
  font-weight: 600;
  color: var(--txt-muted);
  text-transform: uppercase;
  letter-spacing: 0.04em;
}}
.kpi-icon-pill {{
  width: 36px;
  height: 36px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
}}
.kpi-num {{
  font-size: 32px;
  font-weight: 800;
  letter-spacing: -0.02em;
  line-height: 1.15;
  margin-bottom: 8px;
}}
.kpi-meta {{
  font-size: 12.5px;
  color: var(--txt-sub);
  display: flex;
  align-items: center;
  gap: 6px;
}}
.badge-up {{
  color: var(--cyan);
  font-weight: 700;
  background: rgba(56, 189, 248, 0.15);
  padding: 2px 7px;
  border-radius: 6px;
  font-size: 11.5px;
}}

/* Bento Grid */
.bento-grid {{
  display: grid;
  grid-template-columns: 1.25fr 0.95fr;
  gap: 22px;
  margin-bottom: 28px;
}}
.card {{
  background: var(--bg-card);
  border: 1px solid var(--border-card);
  border-radius: 20px;
  padding: 26px;
  box-shadow: var(--shadow-card);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
}}
.card-header {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
}}
.card-heading {{
  display: flex;
  align-items: center;
  gap: 10px;
}}
.card-title {{
  font-size: 17px;
  font-weight: 700;
}}
.card-sub {{
  font-size: 12.5px;
  color: var(--txt-muted);
}}

/* Top 3 Champions */
.champion-list {{
  display: flex;
  flex-direction: column;
  gap: 14px;
}}
.champ-item {{
  display: grid;
  grid-template-columns: 56px 64px 1fr 130px;
  align-items: center;
  gap: 16px;
  padding: 12px 16px;
  border-radius: 14px;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.05);
  transition: all 0.2s;
}}
.champ-item:hover {{
  background: var(--bg-card-hover);
  border-color: var(--border-card);
}}
.champ-rank {{
  width: 44px;
  height: 44px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 800;
  font-size: 16px;
}}
.rank-1 {{ background: linear-gradient(135deg, #fbbf24, #d97706); color: #000; box-shadow: 0 0 12px var(--gold-glow); }}
.rank-2 {{ background: linear-gradient(135deg, #94a3b8, #64748b); color: #fff; }}
.rank-3 {{ background: linear-gradient(135deg, #f97316, #c2410c); color: #fff; }}

.champ-thumb {{
  width: 60px;
  height: 60px;
  border-radius: 12px;
  object-fit: cover;
  border: 1px solid var(--border-card);
}}
.champ-info .name {{
  font-size: 15px;
  font-weight: 700;
  margin-bottom: 2px;
}}
.champ-info .sub {{
  font-size: 12px;
  color: var(--txt-muted);
}}
.champ-bar {{
  height: 6px;
  background: rgba(255, 255, 255, 0.08);
  border-radius: 999px;
  margin-top: 6px;
  overflow: hidden;
}}
.champ-fill {{
  height: 100%;
  border-radius: 999px;
  background: linear-gradient(90deg, var(--blue), var(--cyan), var(--gold));
}}
.champ-val {{
  text-align: right;
}}
.champ-val .rev {{
  font-size: 16px;
  font-weight: 800;
  color: var(--cyan);
}}
.champ-val .pct {{
  font-size: 12px;
  color: var(--txt-muted);
}}

/* Category Breakdown */
.cat-list {{
  display: flex;
  flex-direction: column;
  gap: 16px;
}}
.cat-item {{
  padding: 16px;
  border-radius: 14px;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.05);
}}
.cat-item-top {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
}}
.cat-name {{
  font-size: 14.5px;
  font-weight: 700;
  display: flex;
  align-items: center;
  gap: 8px;
}}
.cat-dot {{
  width: 10px;
  height: 10px;
  border-radius: 50%;
}}
.cat-bar-bg {{
  height: 8px;
  background: rgba(255, 255, 255, 0.06);
  border-radius: 999px;
  overflow: hidden;
  margin-bottom: 8px;
}}
.cat-bar-fill {{
  height: 100%;
  border-radius: 999px;
}}
.cat-footer {{
  display: flex;
  justify-content: space-between;
  font-size: 12px;
  color: var(--txt-muted);
}}

/* Second Grid */
.second-grid {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 22px;
  margin-bottom: 28px;
}}
.branch-card {{
  display: flex;
  flex-direction: column;
  gap: 12px;
}}
.branch-row {{
  display: grid;
  grid-template-columns: 140px 1fr 100px;
  align-items: center;
  gap: 14px;
  padding: 12px 14px;
  border-radius: 12px;
  background: rgba(255, 255, 255, 0.025);
  font-size: 13.5px;
}}
.branch-track {{
  height: 8px;
  background: rgba(255, 255, 255, 0.06);
  border-radius: 999px;
  overflow: hidden;
}}
.branch-fill {{
  height: 100%;
  border-radius: 999px;
  background: linear-gradient(90deg, var(--blue), var(--cyan));
}}

/* Timeline Chart */
.chart-container {{
  position: relative;
  width: 100%;
  height: 190px;
  margin-top: 10px;
}}
svg.timeline-chart {{
  width: 100%;
  height: 100%;
  overflow: visible;
}}

/* Table Section */
.table-card {{
  overflow-x: auto;
  margin-bottom: 28px;
}}
table.matrix-table {{
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  font-size: 13.5px;
  text-align: left;
}}
table.matrix-table th {{
  background: rgba(37, 99, 235, 0.1);
  color: var(--txt-main);
  padding: 14px 16px;
  font-weight: 700;
  border-bottom: 2px solid var(--border-card);
  white-space: nowrap;
}}
table.matrix-table td {{
  padding: 13px 16px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
  white-space: nowrap;
}}
table.matrix-table tr:hover td {{
  background: rgba(37, 99, 235, 0.05);
}}
.badge-pill {{
  display: inline-block;
  padding: 3px 9px;
  border-radius: 6px;
  font-size: 11px;
  font-weight: 600;
}}
.heat-cell {{
  font-weight: 600;
  font-variant-numeric: tabular-nums;
}}

/* Insights Grid */
.insights-grid {{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}}
.insight-card {{
  padding: 18px;
  border-radius: 14px;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid var(--border-card);
}}
.insight-icon {{
  font-size: 24px;
  margin-bottom: 8px;
}}
.insight-title {{
  font-size: 14px;
  font-weight: 700;
  color: var(--cyan);
  margin-bottom: 6px;
}}
.insight-body {{
  font-size: 12.5px;
  color: var(--txt-sub);
  line-height: 1.5;
}}

/* Footer */
.footer {{
  text-align: center;
  padding: 32px 0 20px;
  font-size: 13px;
  color: var(--txt-muted);
  border-top: 1px solid var(--border-card);
  margin-top: 32px;
}}
</style>
</head>
<body>

<!-- Navbar -->
<nav class="navbar">
  <div class="brand-wrapper">
    <div class="brand-icon">☕</div>
    <div>
      <div class="brand-title">CYBER COBALT BI · EXECUTIVE SALES HUB</div>
      <div class="brand-sub">Cafe &amp; Bakery Business Intelligence Analytics</div>
    </div>
  </div>

  <div class="student-badge">
    <span class="dot"></span>
    <span>นายภูริพัฒน์ เหมกุล (Phuriphat Hemakul) · 6752300313 · กลุ่ม 1.2-1</span>
  </div>

  <div class="nav-controls">
    <select id="branchFilter" class="filter-select">
      <option value="ALL">🏢 ทุกสาขา (All Branches)</option>
      <option value="มหาวิทยาลัย">🎓 สาขามหาวิทยาลัย</option>
      <option value="สำนักงาน">💼 สาขาสำนักงาน</option>
      <option value="ห้างสรรพสินค้า">🛍️ สาขาห้างสรรพสินค้า</option>
    </select>
    <select id="catFilter" class="filter-select">
      <option value="ALL">🏷️ ทุกหมวดหมู่ (All Categories)</option>
      <option value="เบเกอรี">🥐 เบเกอรี (Bakery)</option>
      <option value="กาแฟ">☕ กาแฟ (Coffee)</option>
      <option value="เครื่องดื่มอื่น">🍵 เครื่องดื่มอื่น (Beverages)</option>
    </select>
    <button id="themeToggle" class="btn-theme" title="สลับธีม สว่าง/มืด">🌓</button>
  </div>
</nav>

<div class="container">

  <!-- KPI Row -->
  <div class="kpi-row">
    <div class="kpi-card">
      <div class="kpi-header">
        <span class="kpi-title">รายได้รวม (Total Revenue)</span>
        <div class="kpi-icon-pill" style="background:rgba(37,99,235,0.15);color:var(--cyan)">฿</div>
      </div>
      <div class="kpi-num" id="kpiRevenue" style="color:var(--cyan)">฿72,530</div>
      <div class="kpi-meta">
        <span class="badge-up">เป้าหมาย 100%</span>
        <span>จากบิลขาย 100 รายการ</span>
      </div>
    </div>

    <div class="kpi-card">
      <div class="kpi-header">
        <span class="kpi-title">ยอดขายสะสม (Units Sold)</span>
        <div class="kpi-icon-pill" style="background:rgba(56,189,248,0.15);color:var(--cyan)">📦</div>
      </div>
      <div class="kpi-num" id="kpiVolume" style="color:var(--blue)">1,000</div>
      <div class="kpi-meta">
        <span class="badge-up">เฉลี่ย 32.3 ชิ้น/วัน</span>
        <span>ยอดคำสั่งซื้อทั้งหมด</span>
      </div>
    </div>

    <div class="kpi-card">
      <div class="kpi-header">
        <span class="kpi-title">กำไรขั้นต้น (Gross Profit)</span>
        <div class="kpi-icon-pill" style="background:rgba(245,158,11,0.15);color:var(--gold)">📈</div>
      </div>
      <div class="kpi-num" id="kpiProfit" style="color:var(--gold)">฿38,825</div>
      <div class="kpi-meta">
        <span class="badge-up" style="background:rgba(245,158,11,0.15);color:var(--gold)" id="kpiMargin">GP 53.53%</span>
        <span>ประสิทธิภาพกำไรยอดเยี่ยม</span>
      </div>
    </div>

    <div class="kpi-card">
      <div class="kpi-header">
        <span class="kpi-title">สินค้าแชมเปี้ยน (Top Driver)</span>
        <div class="kpi-icon-pill" style="background:rgba(244,63,94,0.15);color:var(--rose)">🏆</div>
      </div>
      <div class="kpi-num" style="font-size:24px;color:var(--rose);margin-top:4px;">ชีสเค้ก</div>
      <div class="kpi-meta">
        <span class="badge-up" style="background:rgba(244,63,94,0.15);color:var(--rose)">฿13,420 (18.5%)</span>
        <span>ขายได้ 122 ชิ้น</span>
      </div>
    </div>
  </div>

  <!-- Bento Section Grid -->
  <div class="bento-grid">
    <!-- Top 3 Champions -->
    <div class="card">
      <div class="card-header">
        <div class="card-heading">
          <span style="font-size:20px;">🥇</span>
          <div>
            <div class="card-title">Top 3 สินค้าสร้างรายได้สูงสุด (Revenue Drivers)</div>
            <div class="card-sub">วิเคราะห์สัดส่วนยอดขายจากสินค้าหลักตาม Prompt 1</div>
          </div>
        </div>
        <span class="badge-pill" style="background:rgba(37,99,235,0.15);color:var(--cyan)">ครอบคลุม 46.3% ของรายได้</span>
      </div>

      <div class="champion-list" id="championList">
        <!-- Generated by JS -->
      </div>
    </div>

    <!-- Category Contribution -->
    <div class="card">
      <div class="card-header">
        <div class="card-heading">
          <span style="font-size:20px;">🍰</span>
          <div>
            <div class="card-title">สัดส่วนรายได้แยกตามหมวดหมู่ (Category Share)</div>
            <div class="card-sub">การกระจายตัวของ 3 หมวดสินค้าหลัก</div>
          </div>
        </div>
      </div>

      <div class="cat-list" id="categoryList">
        <!-- Generated by JS -->
      </div>
    </div>
  </div>

  <!-- Second Grid: Branches & 31-Day Timeline -->
  <div class="second-grid">
    <!-- Branch Performance -->
    <div class="card">
      <div class="card-header">
        <div class="card-heading">
          <span style="font-size:20px;">🏪</span>
          <div>
            <div class="card-title">ผลการดำเนินงานรายสาขา (Branch Performance)</div>
            <div class="card-sub">เปรียบเทียบสัดส่วนยอดขาย กำไร และจำนวนบิล 3 สาขา</div>
          </div>
        </div>
      </div>

      <div class="branch-card" id="branchList">
        <!-- Generated by JS -->
      </div>
    </div>

    <!-- 31-Day Timeline Chart -->
    <div class="card">
      <div class="card-header">
        <div class="card-heading">
          <span style="font-size:20px;">📅</span>
          <div>
            <div class="card-title">แนวโน้มยอดขายรายวัน (31-Day Sales Trend)</div>
            <div class="card-sub">การกระจายตัวของรายได้ตลอด 31 วันในเดือนตุลาคม</div>
          </div>
        </div>
        <span class="badge-pill" style="background:rgba(56,189,248,0.15);color:var(--cyan)">Peak: วันที่ 15 และ 28</span>
      </div>

      <div class="chart-container">
        <svg class="timeline-chart" id="timelineChart" viewBox="0 0 540 180"></svg>
      </div>
    </div>
  </div>

  <!-- Cross-Tab Deep-Dive Matrix Table -->
  <div class="card table-card">
    <div class="card-header">
      <div class="card-heading">
        <span style="font-size:20px;">📊</span>
        <div>
          <div class="card-title">ตารางวิเคราะห์ไขว้ สินค้า × สาขา (Product × Branch Cross-Tab Matrix)</div>
          <div class="card-sub">รายงานตัวเลขยอดขายเชิงลึกและอัตรากำไรตาม Prompt 2</div>
        </div>
      </div>
      <span class="badge-pill" style="background:rgba(245,158,11,0.15);color:var(--gold)">Dynamic Pivot View</span>
    </div>

    <table class="matrix-table">
      <thead>
        <tr>
          <th>ชื่อสินค้า (Product)</th>
          <th>หมวดหมู่</th>
          <th>ราคาขาย/ต้นทุน</th>
          <th style="text-align:right;">มหาวิทยาลัย</th>
          <th style="text-align:right;">สำนักงาน</th>
          <th style="text-align:right;">ห้างสรรพสินค้า</th>
          <th style="text-align:right;">ยอดรวมทั้งหมด</th>
          <th style="text-align:center;">อัตรากำไร (GP%)</th>
        </tr>
      </thead>
      <tbody id="matrixTableBody">
        <!-- Generated by JS -->
      </tbody>
    </table>
  </div>

  <!-- Strategic Insights Panel -->
  <div class="card">
    <div class="card-header">
      <div class="card-heading">
        <span style="font-size:20px;">💡</span>
        <div>
          <div class="card-title">ข้อเสนอแนะเชิงกลยุทธ์ทางธุรกิจ (Executive Strategic Insights)</div>
          <div class="card-sub">การประยุกต์ใช้ข้อมูลสารสนเทศในการบริหารจัดการทางธุรกิจ (SC60107)</div>
        </div>
      </div>
    </div>

    <div class="insights-grid">
      <div class="insight-card">
        <div class="insight-icon">🎯</div>
        <div class="insight-title">1. กลยุทธ์ Menu Engineering &amp; High-Margin Bundling</div>
        <div class="insight-body">
          สินค้ากลุ่มเบเกอรี (ชีสเค้ก และครัวซองต์) สร้างรายได้สูงสุดถึง 40.7% ควรจับคู่ขาย (Bundle) ร่วมกับกาแฟอัตรากำไรสูง เช่น ลาเต้ (GP 62.7%) เพื่อเพิ่ม Average Order Value (AOV) ต่อบิลให้สูงขึ้น
        </div>
      </div>

      <div class="insight-card">
        <div class="insight-icon">🚚</div>
        <div class="insight-title">2. การจัดสรรสินค้าตามลักษณะสาขา (Branch Allocation)</div>
        <div class="insight-body">
          สาขามหาวิทยาลัยมียอดขายสูงสุด (฿29,865) โดดเด่นด้านเครื่องดื่มราคาประหยัดและชีสเค้ก ในขณะที่สาขาห้างสรรพสินค้าสร้างยอดขายครัวซองต์ได้สม่ำเสมอ ควรวางแผน Supply Chain กระจายสต็อกให้ตรงความต้องการ
        </div>
      </div>

      <div class="insight-card">
        <div class="insight-icon">⚡</div>
        <div class="insight-title">3. การจัดการชั่วโมงเร่งด่วนและระบบสต็อก Real-time</div>
        <div class="insight-body">
          ยอดขายมีพีคชัดเจนในช่วงกลางเดือนและปลายเดือน ควรนำระบบ Cloud POS และ AI Demand Forecasting มาแจ้งเตือนวัตถุดิบขาดแคลนล่วงหน้า 3 วัน เพื่อป้องกัน Lost Sales Opportunities
        </div>
      </div>
    </div>
  </div>

  <footer class="footer">
    <div>เอกสารส่งมอบงาน: Dashboard (10 คะแนน) · รายวิชา SC60107 การจัดการเทคโนโลยีสารสนเทศทางธุรกิจ · สถาบันการจัดการปัญญาภิวัฒน์</div>
    <div style="margin-top:6px;font-weight:600;color:var(--cyan);">ผู้จัดทำ: นายภูริพัฒน์ เหมกุล (Phuriphat Hemakul) · รหัสนักศึกษา: 6752300313 · สาขาวิศวกรรมคอมพิวเตอร์และปัญญาประดิษฐ์ (CAI)</div>
  </footer>

</div>

<script>
// Ground Truth Raw Dataset from 1Amazon_Quick_Workshop test.xlsx
const RAW_SALES = {raw_sales_json};

const PRODUCT_META = {{
  "ชีสเค้ก": {{ cat: "เบเกอรี", color: "#fbbf24", price: 110, cost: 72, img: "https://images.unsplash.com/photo-1533134242443-d4fd215305ad?w=300&auto=format&fit=crop&q=80" }},
  "ลาเต้": {{ cat: "กาแฟ", color: "#38bdf8", price: 75, cost: 28, img: "https://images.unsplash.com/photo-1570968915860-54d5c301fa9f?w=300&auto=format&fit=crop&q=80" }},
  "ครัวซองต์": {{ cat: "เบเกอรี", color: "#f97316", price: 85, cost: 60, img: "https://images.unsplash.com/photo-1555507036-ab1f4038808a?w=300&auto=format&fit=crop&q=80" }},
  "คาปูชิโน": {{ cat: "กาแฟ", color: "#818cf8", price: 75, cost: 27, img: "https://images.unsplash.com/photo-1572442388796-11668a67e53d?w=300&auto=format&fit=crop&q=80" }},
  "โกโก้": {{ cat: "เครื่องดื่มอื่น", color: "#10b981", price: 65, cost: 25, img: "https://images.unsplash.com/photo-1542990253-0d0f5be5f0ed?w=300&auto=format&fit=crop&q=80" }},
  "อเมริกาโน": {{ cat: "กาแฟ", color: "#06b6d4", price: 60, cost: 20, img: "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=300&auto=format&fit=crop&q=80" }},
  "ชาไทย": {{ cat: "เครื่องดื่มอื่น", color: "#ea580c", price: 55, cost: 18, img: "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=300&auto=format&fit=crop&q=80" }},
  "บราวนี": {{ cat: "เบเกอรี", color: "#a855f7", price: 55, cost: 33, img: "https://images.unsplash.com/photo-1606313564200-e75d5e30476c?w=300&auto=format&fit=crop&q=80" }}
}};

function filterAndCompute() {{
  const bFilter = document.getElementById('branchFilter').value;
  const cFilter = document.getElementById('catFilter').value;

  const filtered = RAW_SALES.filter(r => {{
    const matchB = (bFilter === 'ALL' || r[2] === bFilter);
    const matchC = (cFilter === 'ALL' || r[4] === cFilter);
    return matchB && matchC;
  }});

  const totalRev = filtered.reduce((acc, r) => acc + r[6], 0);
  const totalProfit = filtered.reduce((acc, r) => acc + r[7], 0);
  const totalVolume = filtered.reduce((acc, r) => acc + r[5], 0);
  const marginPct = totalRev > 0 ? ((totalProfit / totalRev) * 100).toFixed(2) + '%' : '0.00%';

  document.getElementById('kpiRevenue').textContent = '฿' + totalRev.toLocaleString('th-TH');
  document.getElementById('kpiVolume').textContent = totalVolume.toLocaleString('th-TH');
  document.getElementById('kpiProfit').textContent = '฿' + totalProfit.toLocaleString('th-TH');
  document.getElementById('kpiMargin').textContent = 'GP ' + marginPct;

  // Top 3 Products
  const prodTotals = {{}};
  filtered.forEach(r => {{
    const p = r[3];
    if (!prodTotals[p]) prodTotals[p] = {{ rev: 0, qty: 0, profit: 0 }};
    prodTotals[p].rev += r[6];
    prodTotals[p].qty += r[5];
    prodTotals[p].profit += r[7];
  }});

  const sortedProds = Object.keys(prodTotals).map(k => ({{
    name: k,
    rev: prodTotals[k].rev,
    qty: prodTotals[k].qty,
    profit: prodTotals[k].profit,
    meta: PRODUCT_META[k] || {{ color: '#2563eb', cat: '', img: '' }}
  }})).sort((a, b) => b.rev - a.rev);

  const top3 = sortedProds.slice(0, 3);
  const champList = document.getElementById('championList');
  champList.innerHTML = top3.map((item, idx) => {{
    const pct = totalRev > 0 ? ((item.rev / totalRev) * 100).toFixed(1) : 0;
    const rankClass = idx === 0 ? 'rank-1' : idx === 1 ? 'rank-2' : 'rank-3';
    return `
      <div class="champ-item">
        <div class="champ-rank ${{rankClass}}">#${{idx + 1}}</div>
        <img class="champ-thumb" src="${{item.meta.img}}" alt="${{item.name}}" onerror="this.src='https://images.unsplash.com/photo-1509440159596-0249088772ff?w=300'">
        <div class="champ-info">
          <div class="name">${{item.name}} <span style="font-size:11px;font-weight:500;color:var(--txt-muted);">(${{item.meta.cat}})</span></div>
          <div class="sub">ขายได้ ${{item.qty}} ชิ้น · กำไร ฿${{item.profit.toLocaleString('th-TH')}}</div>
          <div class="champ-bar">
            <div class="champ-fill" style="width:${{pct}}%;"></div>
          </div>
        </div>
        <div class="champ-val">
          <div class="rev">฿${{item.rev.toLocaleString('th-TH')}}</div>
          <div class="pct">${{pct}}% ของยอดรวม</div>
        </div>
      </div>
    `;
  }}).join('');

  // Category breakdown
  const catTotals = {{ "เบเกอรี": 0, "กาแฟ": 0, "เครื่องดื่มอื่น": 0 }};
  const catProfits = {{ "เบเกอรี": 0, "กาแฟ": 0, "เครื่องดื่มอื่น": 0 }};
  filtered.forEach(r => {{
    if (catTotals[r[4]] !== undefined) {{
      catTotals[r[4]] += r[6];
      catProfits[r[4]] += r[7];
    }}
  }});
  const catColors = {{ "เบเกอรี": "#fbbf24", "กาแฟ": "#38bdf8", "เครื่องดื่มอื่น": "#34d399" }};
  const catList = document.getElementById('categoryList');
  catList.innerHTML = Object.keys(catTotals).map(c => {{
    const cRev = catTotals[c];
    const cProf = catProfits[c];
    const cPct = totalRev > 0 ? ((cRev / totalRev) * 100).toFixed(1) : 0;
    const cMargin = cRev > 0 ? ((cProf / cRev) * 100).toFixed(1) + '%' : '0%';
    return `
      <div class="cat-item">
        <div class="cat-item-top">
          <span class="cat-name">
            <span class="cat-dot" style="background:${{catColors[c]}};"></span>
            ${{c}}
          </span>
          <span style="font-weight:700;color:${{catColors[c]}};">฿${{cRev.toLocaleString('th-TH')}} (${{cPct}}%)</span>
        </div>
        <div class="cat-bar-bg">
          <div class="cat-bar-fill" style="width:${{cPct}}%;background:${{catColors[c]}};"></div>
        </div>
        <div class="cat-footer">
          <span>กำไร: ฿${{cProf.toLocaleString('th-TH')}}</span>
          <span>อัตรากำไร (GP): ${{cMargin}}</span>
        </div>
      </div>
    `;
  }}).join('');

  // Branch Breakdown
  const branchTotals = {{ "มหาวิทยาลัย": {{ rev: 0, prof: 0, bills: 0 }}, "สำนักงาน": {{ rev: 0, prof: 0, bills: 0 }}, "ห้างสรรพสินค้า": {{ rev: 0, prof: 0, bills: 0 }} }};
  filtered.forEach(r => {{
    if (branchTotals[r[2]]) {{
      branchTotals[r[2]].rev += r[6];
      branchTotals[r[2]].prof += r[7];
      branchTotals[r[2]].bills += 1;
    }}
  }});
  const branchList = document.getElementById('branchList');
  branchList.innerHTML = Object.keys(branchTotals).map(b => {{
    const d = branchTotals[b];
    const bPct = totalRev > 0 ? ((d.rev / totalRev) * 100).toFixed(1) : 0;
    return `
      <div class="branch-row">
        <div>
          <div style="font-weight:700;">${{b}}</div>
          <div style="font-size:11.5px;color:var(--txt-muted);">${{d.bills}} บิลสั่งซื้อ</div>
        </div>
        <div>
          <div class="branch-track">
            <div class="branch-fill" style="width:${{bPct}}%;"></div>
          </div>
        </div>
        <div style="text-align:right;">
          <div style="font-weight:700;color:var(--cyan);">฿${{d.rev.toLocaleString('th-TH')}}</div>
          <div style="font-size:11.5px;color:var(--txt-muted);">${{bPct}}%</div>
        </div>
      </div>
    `;
  }}).join('');

  // 31-Day Timeline SVG
  renderTimeline(filtered);

  // Matrix Table
  renderMatrixTable(filtered);
}}

function renderTimeline(data) {{
  const daily = Array(32).fill(0);
  data.forEach(r => {{
    const d = r[1];
    if (d >= 1 && d <= 31) daily[d] += r[6];
  }});

  const maxVal = Math.max(...daily.slice(1), 1000);
  const w = 540;
  const h = 180;
  const padL = 30;
  const padR = 20;
  const padT = 20;
  const padB = 30;

  const points = [];
  for (let d = 1; d <= 31; d++) {{
    const x = padL + ((d - 1) / 30) * (w - padL - padR);
    const y = h - padB - (daily[d] / maxVal) * (h - padT - padB);
    points.push([x, y, d, daily[d]]);
  }}

  const pathD = points.map((p, i) => (i === 0 ? `M ${{p[0]}},${{p[1]}}` : `L ${{p[0]}},${{p[1]}}`)).join(' ');
  const areaD = `${{pathD}} L ${{points[points.length-1][0]}},${{h - padB}} L ${{points[0][0]}},${{h - padB}} Z`;

  let svgHtml = `
    <defs>
      <linearGradient id="areaGrad" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.38"/>
        <stop offset="100%" stop-color="#38bdf8" stop-opacity="0.0"/>
      </linearGradient>
    </defs>
    <!-- Axis lines -->
    <line x1="${{padL}}" y1="${{h-padB}}" x2="${{w-padR}}" y2="${{h-padB}}" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>
    <!-- Area & Line -->
    <path d="${{areaD}}" fill="url(#areaGrad)"/>
    <path d="${{pathD}}" fill="none" stroke="#38bdf8" stroke-width="2.5" stroke-linecap="round"/>
  `;

  // Plot peak markers
  points.forEach(p => {{
    if (p[2] === 15 || p[2] === 28 || p[3] > 4000) {{
      svgHtml += `
        <circle cx="${{p[0]}}" cy="${{p[1]}}" r="4.5" fill="#fbbf24" stroke="#070d1e" stroke-width="2"/>
        <text x="${{p[0]}}" y="${{p[1] - 8}}" fill="#fbbf24" font-size="10" font-weight="700" text-anchor="middle">฿${{p[3]}}</text>
      `;
    }}
  }});

  // X Labels
  [1, 5, 10, 15, 20, 25, 31].forEach(d => {{
    const x = padL + ((d - 1) / 30) * (w - padL - padR);
    svgHtml += `<text x="${{x}}" y="${{h - 10}}" fill="#94a3b8" font-size="10" text-anchor="middle">ว.${{d}}</text>`;
  }});

  document.getElementById('timelineChart').innerHTML = svgHtml;
}}

function renderMatrixTable(data) {{
  const matrix = {{}};
  const prodNames = Object.keys(PRODUCT_META);
  prodNames.forEach(p => {{
    matrix[p] = {{ "มหาวิทยาลัย": 0, "สำนักงาน": 0, "ห้างสรรพสินค้า": 0, total: 0, profit: 0 }};
  }});

  data.forEach(r => {{
    const b = r[2];
    const p = r[3];
    const rev = r[6];
    const prof = r[7];
    if (matrix[p]) {{
      if (matrix[p][b] !== undefined) matrix[p][b] += rev;
      matrix[p].total += rev;
      matrix[p].profit += prof;
    }}
  }});

  const tbody = document.getElementById('matrixTableBody');
  tbody.innerHTML = prodNames.map(p => {{
    const m = matrix[p];
    const meta = PRODUCT_META[p];
    const gpPct = m.total > 0 ? ((m.profit / m.total) * 100).toFixed(1) + '%' : '0.0%';
    return `
      <tr>
        <td style="font-weight:700;">${{p}}</td>
        <td><span class="badge-pill" style="background:rgba(255,255,255,0.06);color:var(--txt-sub);">${{meta.cat}}</span></td>
        <td style="color:var(--txt-muted);">฿${{meta.price}} / ฿${{meta.cost}}</td>
        <td style="text-align:right;" class="heat-cell">฿${{m["มหาวิทยาลัย"].toLocaleString('th-TH')}}</td>
        <td style="text-align:right;" class="heat-cell">฿${{m["สำนักงาน"].toLocaleString('th-TH')}}</td>
        <td style="text-align:right;" class="heat-cell">฿${{m["ห้างสรรพสินค้า"].toLocaleString('th-TH')}}</td>
        <td style="text-align:right;font-weight:800;color:var(--cyan);">฿${{m.total.toLocaleString('th-TH')}}</td>
        <td style="text-align:center;"><span class="badge-pill" style="background:rgba(56,189,248,0.15);color:var(--cyan);">${{gpPct}}</span></td>
      </tr>
    `;
  }}).join('');
}}

// Filter Listeners
document.getElementById('branchFilter').addEventListener('change', filterAndCompute);
document.getElementById('catFilter').addEventListener('change', filterAndCompute);

// Theme Toggle
const themeBtn = document.getElementById('themeToggle');
themeBtn.addEventListener('click', () => {{
  const cur = document.documentElement.getAttribute('data-theme');
  document.documentElement.setAttribute('data-theme', cur === 'dark' ? 'light' : 'dark');
}});

// Initial boot
window.addEventListener('DOMContentLoaded', filterAndCompute);
</script>
</body>
</html>
'''

dest1 = r'02_Labs_Assignments\Week5\Dashboard-6752300313.html'
dest2 = r'Dashboard-6752300313.html'
dest3 = r'dashboard.html'

for p in [dest1, dest2, dest3]:
    with open(p, 'w', encoding='utf-8') as f:
        f.write(html_template)

print("Generated upgraded Phuriphat Dashboard HTML!")
