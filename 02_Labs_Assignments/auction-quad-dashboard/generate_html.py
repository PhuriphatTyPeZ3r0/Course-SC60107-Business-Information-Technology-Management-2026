import json
import os

data_path = os.path.join('02_Labs_Assignments', 'auction-quad-dashboard', 'sales_data.json')
out_path = os.path.join('02_Labs_Assignments', 'auction-quad-dashboard', 'dashboard.html')

with open(data_path, 'r', encoding='utf-8') as f:
    sales = json.load(f)

json_data_str = json.dumps(sales, ensure_ascii=False)

html_template = """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Auction Quad — แดชบอร์ดยอดขายอัจฉริยะ (Sales Intelligence Dashboard)</title>
  
  <!-- Google Fonts: Prompt (Thai & Latin) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Prompt:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
  
  <!-- Google Material Symbols Rounded Icons -->
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
  
  <!-- Three.js & OrbitControls via CDN -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>

  <style>
    /* ==========================================================================
       Auction Quad Design System — Core Stylesheet
       ========================================================================== */
    :root {
      --bg-canvas: #060b18;
      --bg-surface: rgba(13, 23, 46, 0.75);
      --bg-surface-hover: rgba(19, 34, 68, 0.85);
      --bg-card: rgba(15, 27, 54, 0.65);
      --bg-card-elevated: rgba(22, 38, 77, 0.85);

      /* Primary Blue Spectrum */
      --blue-900: #0b1a3a;
      --blue-800: #1e3a8a;
      --blue-700: #1d4ed8;
      --blue-600: #2563eb;
      --blue-500: #3b82f6;
      --blue-400: #60a5fa;
      --blue-300: #38bdf8;
      --blue-glow: rgba(37, 99, 235, 0.35);

      /* Accent Orange Spectrum */
      --orange-700: #c2410c;
      --orange-600: #ea580c;
      --orange-500: #f97316;
      --orange-400: #fb923c;
      --orange-300: #fdba74;
      --orange-glow: rgba(249, 115, 22, 0.35);
      --amber-500: #f59e0b;

      /* Semantic Colors */
      --color-profit: #10b981;
      --color-profit-glow: rgba(16, 185, 129, 0.25);
      --color-cost: #ef4444;

      /* Typography & Borders */
      --text-primary: #f8fafc;
      --text-secondary: #cbd5e1;
      --text-muted: #94a3b8;
      --text-dim: #64748b;

      --border-subtle: rgba(255, 255, 255, 0.08);
      --border-focus: rgba(56, 189, 248, 0.45);
      --border-orange: rgba(249, 115, 22, 0.45);

      --radius-sm: 8px;
      --radius-md: 14px;
      --radius-lg: 20px;
      --radius-pill: 9999px;

      --shadow-glass: 0 8px 32px 0 rgba(0, 0, 0, 0.45);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: 'Prompt', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      -webkit-font-smoothing: antialiased;
    }

    body {
      background-color: var(--bg-canvas);
      background-image: 
        radial-gradient(circle at 15% 15%, rgba(37, 99, 235, 0.12) 0%, transparent 45%),
        radial-gradient(circle at 85% 25%, rgba(249, 115, 22, 0.10) 0%, transparent 45%),
        radial-gradient(circle at 50% 85%, rgba(16, 185, 129, 0.08) 0%, transparent 50%);
      color: var(--text-primary);
      min-height: 100vh;
      padding: 24px 20px 60px;
      overflow-x: hidden;
    }

    .tabular, .num, td.num-cell {
      font-variant-numeric: tabular-nums;
      letter-spacing: -0.02em;
    }

    .glass {
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      box-shadow: 
        inset 0 1px 0 0 rgba(255, 255, 255, 0.08),
        var(--shadow-glass);
      transition: border-color 0.2s, box-shadow 0.2s;
    }

    .glass:hover {
      border-color: rgba(56, 189, 248, 0.25);
    }

    .container {
      max-width: 1480px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 22px;
    }

    /* Header */
    .header {
      padding: 16px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 16px;
    }

    .header-left {
      display: flex;
      align-items: center;
      gap: 16px;
    }

    .brand-mark {
      width: 44px;
      height: 44px;
      border-radius: 12px;
      background: linear-gradient(135deg, var(--blue-600) 0%, var(--orange-500) 100%);
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 4px 18px var(--orange-glow);
    }

    .brand-mark span {
      color: #fff;
      font-size: 26px;
    }

    .brand-title h1 {
      font-size: 22px;
      font-weight: 700;
      letter-spacing: -0.02em;
      background: linear-gradient(90deg, #ffffff 40%, var(--blue-300) 80%, var(--orange-400) 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .badge-sim {
      font-size: 11px;
      font-weight: 600;
      padding: 4px 10px;
      border-radius: var(--radius-pill);
      background: rgba(245, 158, 11, 0.15);
      border: 1px solid rgba(245, 158, 11, 0.4);
      color: #fbbf24;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      letter-spacing: 0.02em;
    }

    .header-meta {
      font-size: 13px;
      color: var(--text-muted);
      margin-top: 2px;
    }

    .header-right {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 8px 16px;
      border-radius: var(--radius-sm);
      font-size: 13px;
      font-weight: 500;
      cursor: pointer;
      border: 1px solid transparent;
      transition: all 0.2s;
    }

    .btn-secondary {
      background: rgba(255, 255, 255, 0.06);
      border-color: var(--border-subtle);
      color: var(--text-secondary);
    }
    .btn-secondary:hover {
      background: rgba(255, 255, 255, 0.12);
      color: #fff;
    }

    .btn-orange {
      background: linear-gradient(135deg, var(--orange-500) 0%, var(--orange-600) 100%);
      color: #fff;
      box-shadow: 0 4px 14px var(--orange-glow);
    }
    .btn-orange:hover {
      transform: translateY(-1px);
    }

    /* Hero Split */
    .hero-split {
      display: grid;
      grid-template-columns: 1.15fr 1fr;
      gap: 20px;
    }

    @media (max-width: 1080px) {
      .hero-split {
        grid-template-columns: 1fr;
      }
    }

    .stage-3d-card {
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      height: 390px;
    }

    .stage-header {
      padding: 14px 18px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--border-subtle);
      z-index: 2;
    }

    .stage-title {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 14px;
      font-weight: 600;
      color: var(--text-primary);
    }

    .stage-title .material-symbols-rounded {
      color: var(--orange-400);
      font-size: 20px;
    }

    .stage-controls {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .pill-btn {
      font-size: 12px;
      padding: 4px 10px;
      border-radius: var(--radius-pill);
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid var(--border-subtle);
      color: var(--text-secondary);
      cursor: pointer;
      transition: all 0.2s;
    }

    .pill-btn.active {
      background: var(--blue-600);
      border-color: var(--blue-400);
      color: #fff;
      box-shadow: 0 0 10px var(--blue-glow);
    }

    .stage-canvas-container {
      flex: 1;
      width: 100%;
      position: relative;
      cursor: grab;
    }
    .stage-canvas-container:active {
      cursor: grabbing;
    }

    #threeCanvas {
      width: 100%;
      height: 100%;
      display: block;
    }

    .stage-hint {
      position: absolute;
      bottom: 12px;
      left: 18px;
      font-size: 11px;
      color: var(--text-muted);
      pointer-events: none;
      display: flex;
      align-items: center;
      gap: 5px;
      background: rgba(6, 11, 24, 0.65);
      padding: 4px 10px;
      border-radius: var(--radius-pill);
      border: 1px solid var(--border-subtle);
    }

    /* KPI Matrix Cards */
    .kpi-matrix {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 16px;
    }

    .kpi-card {
      padding: 20px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      position: relative;
      overflow: hidden;
    }

    .kpi-card::after {
      content: "";
      position: absolute;
      top: 0;
      right: 0;
      width: 90px;
      height: 90px;
      border-radius: 50%;
      filter: blur(40px);
      pointer-events: none;
      opacity: 0.35;
    }

    .kpi-revenue::after { background: var(--blue-500); }
    .kpi-qty::after { background: var(--orange-500); }
    .kpi-profit::after { background: var(--color-profit); }
    .kpi-margin::after { background: var(--blue-300); }

    .kpi-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 14px;
    }

    .kpi-title {
      font-size: 13px;
      color: var(--text-muted);
      font-weight: 500;
    }

    .kpi-icon-wrap {
      width: 36px;
      height: 36px;
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border-subtle);
    }

    .kpi-revenue .kpi-icon-wrap { color: var(--blue-400); border-color: rgba(59, 130, 246, 0.3); }
    .kpi-qty .kpi-icon-wrap { color: var(--orange-400); border-color: rgba(249, 115, 22, 0.3); }
    .kpi-profit .kpi-icon-wrap { color: var(--color-profit); border-color: rgba(16, 185, 129, 0.3); }
    .kpi-margin .kpi-icon-wrap { color: var(--blue-300); border-color: rgba(56, 189, 248, 0.3); }

    .kpi-val {
      font-size: 28px;
      font-weight: 700;
      color: #fff;
      line-height: 1.1;
      margin-bottom: 8px;
    }

    .kpi-footer {
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 12px;
      color: var(--text-secondary);
      border-top: 1px solid rgba(255, 255, 255, 0.05);
      padding-top: 10px;
      margin-top: 6px;
    }

    .kpi-badge {
      font-size: 11px;
      font-weight: 600;
      padding: 2px 7px;
      border-radius: 6px;
    }
    .badge-blue { background: rgba(37, 99, 235, 0.2); color: var(--blue-300); }
    .badge-orange { background: rgba(249, 115, 22, 0.2); color: var(--orange-300); }
    .badge-green { background: rgba(16, 185, 129, 0.2); color: #34d399; }

    /* Cross-Filter Bar */
    .filter-bar {
      padding: 14px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 14px;
    }

    .filter-group {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }

    .filter-label {
      font-size: 12px;
      font-weight: 600;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-right: 4px;
    }

    .chip {
      padding: 6px 14px;
      border-radius: var(--radius-pill);
      font-size: 13px;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border-subtle);
      color: var(--text-secondary);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }

    .chip:hover {
      background: rgba(255, 255, 255, 0.1);
      border-color: rgba(255, 255, 255, 0.2);
      color: #fff;
    }

    .chip.active {
      background: linear-gradient(135deg, var(--blue-600) 0%, var(--blue-700) 100%);
      border-color: var(--blue-400);
      color: #fff;
      font-weight: 500;
      box-shadow: 0 2px 10px var(--blue-glow);
    }

    .chip-orange.active {
      background: linear-gradient(135deg, var(--orange-500) 0%, var(--orange-600) 100%);
      border-color: var(--orange-300);
      box-shadow: 0 2px 10px var(--orange-glow);
    }

    .search-box {
      display: flex;
      align-items: center;
      gap: 8px;
      background: rgba(0, 0, 0, 0.35);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-pill);
      padding: 6px 14px;
      min-width: 240px;
    }

    .search-box input {
      background: transparent;
      border: none;
      outline: none;
      color: #fff;
      font-size: 13px;
      width: 100%;
    }

    .search-box .material-symbols-rounded {
      color: var(--text-muted);
      font-size: 18px;
    }

    /* Quad Grid */
    .quad-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 20px;
    }

    @media (max-width: 992px) {
      .quad-grid {
        grid-template-columns: 1fr;
      }
    }

    .quad-card {
      padding: 22px;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    .quad-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--border-subtle);
      padding-bottom: 12px;
    }

    .quad-title {
      font-size: 15px;
      font-weight: 600;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .quad-tag {
      font-size: 11px;
      font-weight: 600;
      padding: 2px 8px;
      border-radius: 4px;
      background: rgba(56, 189, 248, 0.12);
      color: var(--blue-300);
      border: 1px solid rgba(56, 189, 248, 0.25);
    }

    /* Quad 1 Bars */
    .product-bars {
      display: flex;
      flex-direction: column;
      gap: 12px;
    }

    .product-bar-row {
      display: flex;
      flex-direction: column;
      gap: 5px;
    }

    .p-bar-label {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 13px;
    }

    .p-bar-name {
      display: flex;
      align-items: center;
      gap: 8px;
      font-weight: 500;
    }

    .rank-medal {
      width: 22px;
      height: 22px;
      border-radius: 6px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 11px;
      font-weight: 700;
    }
    .rank-1 { background: linear-gradient(135deg, #fbbf24, #d97706); color: #000; box-shadow: 0 0 8px rgba(251, 191, 36, 0.4); }
    .rank-2 { background: linear-gradient(135deg, #94a3b8, #64748b); color: #fff; }
    .rank-3 { background: linear-gradient(135deg, #b45309, #78350f); color: #fed7aa; }
    .rank-other { background: rgba(255,255,255,0.08); color: var(--text-muted); }

    .p-bar-track {
      height: 28px;
      background: rgba(0, 0, 0, 0.35);
      border-radius: 6px;
      overflow: hidden;
      position: relative;
      display: flex;
      align-items: center;
      border: 1px solid rgba(255, 255, 255, 0.05);
    }

    .p-bar-fill {
      height: 100%;
      border-radius: 6px;
      display: flex;
      align-items: center;
      padding-left: 10px;
      font-size: 11px;
      font-weight: 600;
      color: #fff;
      transition: width 0.6s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .fill-blue {
      background: linear-gradient(90deg, var(--blue-700) 0%, var(--blue-500) 100%);
      box-shadow: 0 0 12px var(--blue-glow);
    }
    .fill-orange {
      background: linear-gradient(90deg, var(--orange-600) 0%, var(--orange-400) 100%);
      box-shadow: 0 0 12px var(--orange-glow);
    }
    .fill-amber {
      background: linear-gradient(90deg, #d97706 0%, #f59e0b 100%);
    }

    /* Quad 2 Table */
    .data-table-wrap {
      overflow-x: auto;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-subtle);
    }

    .data-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 13px;
      text-align: left;
    }

    .data-table th {
      background: rgba(255, 255, 255, 0.04);
      color: var(--text-muted);
      font-weight: 600;
      padding: 10px 14px;
      border-bottom: 1px solid var(--border-subtle);
      white-space: nowrap;
    }

    .data-table td {
      padding: 12px 14px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.04);
      color: var(--text-secondary);
      white-space: nowrap;
    }

    .data-table tbody tr:hover {
      background: rgba(255, 255, 255, 0.03);
    }

    .branch-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-weight: 600;
      color: #fff;
    }

    .share-bar-mini {
      height: 6px;
      background: rgba(255, 255, 255, 0.1);
      border-radius: 3px;
      overflow: hidden;
      width: 70px;
      display: inline-block;
      vertical-align: middle;
      margin-left: 6px;
    }

    .share-bar-fill {
      height: 100%;
      background: var(--blue-400);
      border-radius: 3px;
    }

    /* Quad 3 */
    .chart-container-svg {
      width: 100%;
      height: 190px;
      position: relative;
    }

    .timeline-summary {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 10px;
      margin-top: 10px;
    }

    .sub-stat-box {
      background: rgba(0, 0, 0, 0.25);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
      padding: 10px 12px;
      text-align: center;
    }
    .sub-stat-title {
      font-size: 11px;
      color: var(--text-muted);
      margin-bottom: 3px;
    }
    .sub-stat-val {
      font-size: 15px;
      font-weight: 600;
      color: #fff;
    }

    /* Quad 4 */
    .cat-mix-bar {
      height: 16px;
      border-radius: 8px;
      overflow: hidden;
      display: flex;
      margin-bottom: 14px;
      background: rgba(0, 0, 0, 0.3);
    }
    .cat-slice {
      height: 100%;
      transition: width 0.4s ease;
    }
    .slice-bakery { background: #f59e0b; }
    .slice-coffee { background: #3b82f6; }
    .slice-drinks { background: #10b981; }

    .matrix-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
    }

    .matrix-box {
      background: rgba(0, 0, 0, 0.25);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
      padding: 10px 12px;
    }

    .matrix-box-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 6px;
      font-size: 12px;
      font-weight: 600;
    }

    .matrix-items {
      font-size: 11px;
      color: var(--text-secondary);
      line-height: 1.5;
    }

    /* Transactions Explorer */
    .transactions-card {
      padding: 22px;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    .pagination-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 12px;
      color: var(--text-muted);
      padding-top: 12px;
    }

    .page-controls {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .page-btn {
      width: 32px;
      height: 32px;
      border-radius: 6px;
      display: flex;
      align-items: center;
      justify-content: center;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border-subtle);
      color: var(--text-secondary);
      cursor: pointer;
    }
    .page-btn:hover:not(:disabled) {
      background: var(--blue-600);
      color: #fff;
    }
    .page-btn:disabled {
      opacity: 0.3;
      cursor: not-allowed;
    }

    /* Footer */
    .footer {
      text-align: center;
      font-size: 12px;
      color: var(--text-dim);
      padding: 24px 0 10px;
    }
  </style>
</head>
<body>

  <div class="container">
    <!-- HEADER -->
    <header class="glass header">
      <div class="header-left">
        <div class="brand-mark">
          <span class="material-symbols-rounded">view_in_ar</span>
        </div>
        <div class="brand-title">
          <h1>
            Auction Quad Sales Dashboard
            <span class="badge-sim">
              <span class="material-symbols-rounded" style="font-size:14px;">science</span>
              ข้อมูลจำลองเพื่อการเรียนรู้
            </span>
          </h1>
          <div class="header-meta">
            ชุดข้อมูลการขายร้านกาแฟและเบเกอรี • วันที่ 1 - 31 สิงหาคม 2026 (รวม 100 รายการธุรกรรม 1,000 ชิ้น)
          </div>
        </div>
      </div>

      <div class="header-right">
        <button class="btn btn-secondary" id="resetFiltersBtn" title="ล้างตัวกรองทั้งหมด">
          <span class="material-symbols-rounded">restart_alt</span>
          รีเซ็ตตัวกรอง
        </button>
        <button class="btn btn-orange" id="exportCsvBtn" title="ส่งออกข้อมูลที่กำลังแสดงเป็น CSV">
          <span class="material-symbols-rounded">download</span>
          ส่งออก CSV
        </button>
      </div>
    </header>

    <!-- HERO SPLIT: 3D THREE.JS STAGE + 4 KPI CARDS -->
    <section class="hero-split">
      <!-- 3D Spatial Interactive Stage -->
      <div class="glass stage-3d-card">
        <div class="stage-header">
          <div class="stage-title">
            <span class="material-symbols-rounded">3d_rotation</span>
            <span>3D Spatial Stage — แท่นจัดอันดับสินค้าอัจฉริยะ (Top 3 Podium)</span>
          </div>
          <div class="stage-controls">
            <button class="pill-btn active" id="btnModeRev">ยอดขาย (Rev)</button>
            <button class="pill-btn" id="btnModeProfit">กำไร (Profit)</button>
            <button class="pill-btn" id="btnAutoRotate" title="สลับการหมุนอัตโนมัติ">
              <span class="material-symbols-rounded" style="font-size: 14px; vertical-align: middle;">sync</span>
            </button>
          </div>
        </div>

        <div class="stage-canvas-container" id="canvasContainer">
          <canvas id="threeCanvas"></canvas>
          <div class="stage-hint">
            <span class="material-symbols-rounded" style="font-size: 14px;">touch_app</span>
            คลิกลากเพื่อหมุน 360° | เลื่อนลูกกลิ้งเมาส์เพื่อซูม
          </div>
        </div>
      </div>

      <!-- 4 Executive KPI Matrix Cards -->
      <div class="kpi-matrix">
        <!-- KPI 1: รายได้รวม (Total Revenue) -->
        <div class="glass kpi-card kpi-revenue">
          <div class="kpi-header">
            <span class="kpi-title">รายได้รวม (Total Revenue)</span>
            <div class="kpi-icon-wrap">
              <span class="material-symbols-rounded">payments</span>
            </div>
          </div>
          <div class="kpi-val tabular" id="kpiRevenue">฿72,530.00</div>
          <div class="kpi-footer">
            <span>เฉลี่ย ฿72.53 / หน่วย</span>
            <span class="kpi-badge badge-blue">เป้าหมาย 100%</span>
          </div>
        </div>

        <!-- KPI 2: จำนวนหน่วยที่ขายรวม (Total Units Sold) -->
        <div class="glass kpi-card kpi-qty">
          <div class="kpi-header">
            <span class="kpi-title">จำนวนขายรวม (Units Sold)</span>
            <div class="kpi-icon-wrap">
              <span class="material-symbols-rounded">inventory_2</span>
            </div>
          </div>
          <div class="kpi-val tabular" id="kpiQty">1,000</div>
          <div class="kpi-footer">
            <span id="kpiOrderCount">100 บิลธุรกรรม</span>
            <span class="kpi-badge badge-orange">10.0 ชิ้น / บิล</span>
          </div>
        </div>

        <!-- KPI 3: กำไรขั้นต้นรวม (Total Gross Profit) -->
        <div class="glass kpi-card kpi-profit">
          <div class="kpi-header">
            <span class="kpi-title">กำไรขั้นต้นรวม (Gross Profit)</span>
            <div class="kpi-icon-wrap">
              <span class="material-symbols-rounded">trending_up</span>
            </div>
          </div>
          <div class="kpi-val tabular" id="kpiProfit">฿38,825.00</div>
          <div class="kpi-footer">
            <span id="kpiCostVal">ต้นทุน ฿33,705.00</span>
            <span class="kpi-badge badge-green">บวกสุทธิ</span>
          </div>
        </div>

        <!-- KPI 4: อัตรากำไรขั้นต้น (% Gross Profit Margin) -->
        <div class="glass kpi-card kpi-margin">
          <div class="kpi-header">
            <span class="kpi-title">อัตรากำไรขั้นต้น (GP Margin)</span>
            <div class="kpi-icon-wrap">
              <span class="material-symbols-rounded">percent</span>
            </div>
          </div>
          <div class="kpi-val tabular" id="kpiMargin">53.53%</div>
          <div class="kpi-footer">
            <span>ระดับสูง (Healthy Retail)</span>
            <span class="kpi-badge badge-blue">มาตรฐานดีเยี่ยม</span>
          </div>
        </div>
      </div>
    </section>

    <!-- GLOBAL CROSS-FILTER BAR -->
    <div class="glass filter-bar">
      <!-- Filter Branch -->
      <div class="filter-group">
        <span class="filter-label">สาขา:</span>
        <button class="chip active" data-filter="branch" data-val="ALL">ทั้งหมด (3 สาขา)</button>
        <button class="chip" data-filter="branch" data-val="มหาวิทยาลัย">มหาวิทยาลัย</button>
        <button class="chip" data-filter="branch" data-val="สำนักงาน">สำนักงาน</button>
        <button class="chip" data-filter="branch" data-val="ห้างสรรพสินค้า">ห้างสรรพสินค้า</button>
      </div>

      <!-- Filter Category -->
      <div class="filter-group">
        <span class="filter-label">หมวดหมู่:</span>
        <button class="chip chip-orange active" data-filter="cat" data-val="ALL">ทุกหมวดหมู่</button>
        <button class="chip chip-orange" data-filter="cat" data-val="กาแฟ">กาแฟ</button>
        <button class="chip chip-orange" data-filter="cat" data-val="เบเกอรี">เบเกอรี</button>
        <button class="chip chip-orange" data-filter="cat" data-val="เครื่องดื่มอื่น">เครื่องดื่มอื่น</button>
      </div>

      <!-- Search Box -->
      <div class="search-box">
        <span class="material-symbols-rounded">search</span>
        <input type="text" id="searchInput" placeholder="ค้นหาสินค้า, สาขา, รหัสบิล...">
      </div>
    </div>

    <!-- THE 4 ANALYTICAL QUADRANTS -->
    <main class="quad-grid">
      <!-- QUADRANT 1: สินค้าที่มีรายได้สูงสุด 3 อันดับแรก (Prompt Requirement #2) -->
      <div class="glass quad-card">
        <div class="quad-header">
          <div class="quad-title">
            <span class="material-symbols-rounded" style="color: var(--amber-500);">leaderboard</span>
            <span>Quad I: จัดอันดับสินค้าที่มีรายได้สูงสุด (Top Rankings)</span>
          </div>
          <div style="display: flex; gap: 6px;">
            <button class="pill-btn active" id="btnToggleTop3">Top 3</button>
            <button class="pill-btn" id="btnToggleAllProds">ทั้งหมด (8)</button>
          </div>
        </div>

        <div class="product-bars" id="productBarsContainer">
          <!-- Populated by JavaScript -->
        </div>
      </div>

      <!-- QUADRANT 2: ตารางเปรียบเทียบรายได้แต่ละสาขา (Prompt Requirement #3) -->
      <div class="glass quad-card">
        <div class="quad-header">
          <div class="quad-title">
            <span class="material-symbols-rounded" style="color: var(--blue-400);">storefront</span>
            <span>Quad II: เปรียบเทียบผลงานและรายได้รายสาขา (Branch Matrix)</span>
          </div>
          <span class="quad-tag">3 สาขาหลัก</span>
        </div>

        <div class="data-table-wrap">
          <table class="data-table">
            <thead>
              <tr>
                <th>สาขา</th>
                <th>จำนวนบิล</th>
                <th>หน่วยขาย</th>
                <th>รายได้รวม (บาท)</th>
                <th>สัดส่วน (%)</th>
                <th>กำไรขั้นต้น (บาท)</th>
                <th>% กำไร</th>
              </tr>
            </thead>
            <tbody id="branchTableBody">
              <!-- Populated by JavaScript -->
            </tbody>
          </table>
        </div>
      </div>

      <!-- QUADRANT 3: มิติเวลาและการกระจายรายวัน (Temporal Velocity) -->
      <div class="glass quad-card">
        <div class="quad-header">
          <div class="quad-title">
            <span class="material-symbols-rounded" style="color: var(--orange-400);">timeline</span>
            <span>Quad III: แนวโน้มยอดขายรายวัน สิงหาคม 2026 (Temporal Dynamics)</span>
          </div>
          <span class="quad-tag" id="peakDayTag">Peak: 21 ส.ค.</span>
        </div>

        <div class="chart-container-svg" id="dailyChartContainer">
          <!-- SVG Daily Line / Bar Chart generated by JS -->
        </div>

        <div class="timeline-summary">
          <div class="sub-stat-box">
            <div class="sub-stat-title">ยอดขายวันธรรมดา (จ.-ศ.)</div>
            <div class="sub-stat-val tabular" id="valWeekdayRev">฿53,680</div>
          </div>
          <div class="sub-stat-box">
            <div class="sub-stat-title">ยอดขายวันหยุด (ส.-อา.)</div>
            <div class="sub-stat-val tabular" id="valWeekendRev">฿18,850</div>
          </div>
          <div class="sub-stat-box">
            <div class="sub-stat-title">ยอดขายเฉลี่ยต่อวัน</div>
            <div class="sub-stat-val tabular" id="valAvgDailyRev">฿2,339.68</div>
          </div>
        </div>
      </div>

      <!-- QUADRANT 4: โครงสร้างหมวดหมู่ & BCG-Style Matrix -->
      <div class="glass quad-card">
        <div class="quad-header">
          <div class="quad-title">
            <span class="material-symbols-rounded" style="color: var(--color-profit);">category</span>
            <span>Quad IV: โครงสร้างหมวดหมู่ & กลยุทธ์สินค้า (Category & BCG Matrix)</span>
          </div>
          <span class="quad-tag">3 หมวดหมู่</span>
        </div>

        <div>
          <div style="font-size: 12px; color: var(--text-muted); margin-bottom: 6px; display: flex; justify-content: space-between;">
            <span>สัดส่วนยอดขายตามหมวดหมู่</span>
            <span id="catMixLegend">เบเกอรี 40.7% • กาแฟ 38.5% • เครื่องดื่มอื่น 20.9%</span>
          </div>
          <div class="cat-mix-bar" id="catMixBar">
            <div class="cat-slice slice-bakery" id="sliceBakery" style="width: 40.7%;" title="เบเกอรี"></div>
            <div class="cat-slice slice-coffee" id="sliceCoffee" style="width: 38.5%;" title="กาแฟ"></div>
            <div class="cat-slice slice-drinks" id="sliceDrinks" style="width: 20.9%;" title="เครื่องดื่มอื่น"></div>
          </div>
        </div>

        <!-- 4 Quadrants Matrix -->
        <div class="matrix-grid">
          <div class="matrix-box" style="border-left: 3px solid #10b981;">
            <div class="matrix-box-header" style="color: #34d399;">
              <span>🌟 สินค้าดาวเด่น (High Rev / High GP%)</span>
            </div>
            <div class="matrix-items">
              • ลาเต้ (กำไร 62.7% | ฿10,125)<br>
              • คาปูชิโน (กำไร 64.0% | ฿9,375)<br>
              • อเมริกาโน (กำไร 66.7% | ฿8,400)
            </div>
          </div>

          <div class="matrix-box" style="border-left: 3px solid #f59e0b;">
            <div class="matrix-box-header" style="color: #fbbf24;">
              <span>💰 เครื่องจักรเงินสด (High Rev / Moderate GP%)</span>
            </div>
            <div class="matrix-items">
              • ชีสเค้ก (ยอดขาย No.1 ฿13,420 | กำไร 34.5%)<br>
              • ครัวซองต์ (ยอดขาย No.3 ฿10,030 | กำไร 29.4%)
            </div>
          </div>

          <div class="matrix-box" style="border-left: 3px solid #38bdf8;">
            <div class="matrix-box-header" style="color: #38bdf8;">
              <span>🎯 โอกาสเติบโต (High GP% / Growth Potential)</span>
            </div>
            <div class="matrix-items">
              • ชาไทย (กำไรสูงสุด 67.3% | ยอดขาย ฿6,160)<br>
              • โกโก้ (กำไร 61.5% | ยอดขาย ฿8,970)
            </div>
          </div>

          <div class="matrix-box" style="border-left: 3px solid #94a3b8;">
            <div class="matrix-box-header" style="color: #cbd5e1;">
              <span>⚡ สินค้าเสริมทราฟฟิก (Standard Margin)</span>
            </div>
            <div class="matrix-items">
              • บราวนี (กำไร 60.0% | ยอดขาย ฿6,050)
            </div>
          </div>
        </div>
      </div>
    </main>

    <!-- DETAILED TRANSACTION EXPLORER -->
    <section class="glass transactions-card">
      <div class="quad-header">
        <div class="quad-title">
          <span class="material-symbols-rounded" style="color: var(--blue-400);">table_chart</span>
          <span>ตารางบันทึกธุรกรรมการขายรายบิล (Detailed Transaction Explorer)</span>
        </div>
        <div style="font-size: 13px; color: var(--text-muted);">
          แสดง <span id="rowCountLabel" class="tabular" style="color:#fff; font-weight:600;">100</span> รายการ
        </div>
      </div>

      <div class="data-table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th style="cursor:pointer;" onclick="handleSort('id')">รหัส ⬍</th>
              <th style="cursor:pointer;" onclick="handleSort('date')">วันที่ ⬍</th>
              <th style="cursor:pointer;" onclick="handleSort('branch')">สาขา ⬍</th>
              <th style="cursor:pointer;" onclick="handleSort('product')">สินค้า ⬍</th>
              <th style="cursor:pointer;" onclick="handleSort('category')">หมวดหมู่ ⬍</th>
              <th style="cursor:pointer; text-align:right;" onclick="handleSort('qty')">จำนวน (ชิ้น) ⬍</th>
              <th style="cursor:pointer; text-align:right;" onclick="handleSort('price')">ราคา/หน่วย ⬍</th>
              <th style="cursor:pointer; text-align:right;" onclick="handleSort('cost')">ต้นทุน/หน่วย ⬍</th>
              <th style="cursor:pointer; text-align:right;" onclick="handleSort('revenue')">รายได้รวม (บาท) ⬍</th>
              <th style="cursor:pointer; text-align:right;" onclick="handleSort('profit')">กำไรขั้นต้น (บาท) ⬍</th>
            </tr>
          </thead>
          <tbody id="transactionTableBody">
            <!-- Populated by JavaScript -->
          </tbody>
        </table>
      </div>

      <div class="pagination-bar">
        <div>
          หน้า <span id="currentPageSpan" class="tabular">1</span> จาก <span id="totalPagesSpan" class="tabular">10</span>
        </div>
        <div class="page-controls">
          <button class="page-btn" id="btnPrevPage" onclick="changePage(-1)">
            <span class="material-symbols-rounded" style="font-size: 18px;">chevron_left</span>
          </button>
          <button class="page-btn" id="btnNextPage" onclick="changePage(1)">
            <span class="material-symbols-rounded" style="font-size: 18px;">chevron_right</span>
          </button>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
      Auction Quad Design System • Business IT Management Workshop • ข้อมูลจำลองเพื่อการเรียนรู้ ห้ามใช้ในเชิงพาณิชย์
    </footer>
  </div>

  <!-- JAVASCRIPT APPLICATION ENGINE -->
  <script>
    // Embedded Data: Exact 100 sales records from Excel Sheet 'Sales'
    const RAW_DATA = """ + json_data_str + """;

    // State Management
    let currentFilterBranch = 'ALL';
    let currentFilterCat = 'ALL';
    let currentSearchTerm = '';
    let currentRankingMode = 'revenue'; // 'revenue' or 'profit'
    let showAllProducts = false;
    let sortColumn = 'id';
    let sortAsc = true;
    let currentPage = 1;
    const pageSize = 10;

    // Currency Formatter
    const fmtTHB = (val) => '฿' + Number(val).toLocaleString('th-TH', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
    const fmtInt = (val) => Number(val).toLocaleString('th-TH');

    // Filter Logic
    function getFilteredData() {
      return RAW_DATA.filter(item => {
        const matchBranch = (currentFilterBranch === 'ALL' || item.branch === currentFilterBranch);
        const matchCat = (currentFilterCat === 'ALL' || item.category === currentFilterCat);
        const matchSearch = (!currentSearchTerm || 
          item.id.toLowerCase().includes(currentSearchTerm) ||
          item.product.toLowerCase().includes(currentSearchTerm) ||
          item.branch.toLowerCase().includes(currentSearchTerm) ||
          item.category.toLowerCase().includes(currentSearchTerm)
        );
        return matchBranch && matchCat && matchSearch;
      });
    }

    // Update Everything
    function updateDashboard() {
      const data = getFilteredData();

      // 1. Calculate Executive KPIs
      let totalRev = 0;
      let totalQty = 0;
      let totalProfit = 0;
      let totalCost = 0;

      data.forEach(r => {
        totalRev += r.revenue;
        totalQty += r.qty;
        totalProfit += r.profit;
        totalCost += (r.qty * r.cost);
      });

      const gpMargin = totalRev > 0 ? (totalProfit / totalRev) * 100 : 0;

      // Update KPI DOM
      document.getElementById('kpiRevenue').textContent = fmtTHB(totalRev);
      document.getElementById('kpiQty').textContent = fmtInt(totalQty);
      document.getElementById('kpiOrderCount').textContent = data.length + ' บิลธุรกรรม';
      document.getElementById('kpiProfit').textContent = fmtTHB(totalProfit);
      document.getElementById('kpiCostVal').textContent = 'ต้นทุน ' + fmtTHB(totalCost);
      document.getElementById('kpiMargin').textContent = gpMargin.toFixed(2) + '%';

      // 2. Aggregate Products across branches
      const prodAgg = {};
      data.forEach(r => {
        if (!prodAgg[r.product]) {
          prodAgg[r.product] = {
            product: r.product,
            category: r.category,
            price: r.price,
            cost: r.cost,
            qty: 0,
            revenue: 0,
            profit: 0
          };
        }
        prodAgg[r.product].qty += r.qty;
        prodAgg[r.product].revenue += r.revenue;
        prodAgg[r.product].profit += r.profit;
      });

      const prodList = Object.values(prodAgg);
      prodList.sort((a, b) => b[currentRankingMode] - a[currentRankingMode]);

      // Render Product Bar Chart (Quad 1)
      renderProductBars(prodList);

      // Render Branch Matrix Table (Quad 2)
      renderBranchMatrix(data, totalRev);

      // Render Daily Timeline Chart (Quad 3)
      renderDailyTimeline(data);

      // Render Category Mix & BCG (Quad 4)
      renderCategoryMix(data, totalRev);

      // Render Transaction Explorer Table
      renderTransactionTable(data);

      // Update 3D Stage Pillars
      update3DScene(prodList);
    }

    // Quadrant 1: Product Bar Chart
    function renderProductBars(prodList) {
      const container = document.getElementById('productBarsContainer');
      container.innerHTML = '';

      const itemsToShow = showAllProducts ? prodList : prodList.slice(0, 3);
      if (itemsToShow.length === 0) {
        container.innerHTML = '<div style="color:var(--text-muted); padding:20px; text-align:center;">ไม่พบข้อมูลที่ตรงกับเงื่อนไข</div>';
        return;
      }

      const maxVal = Math.max(...itemsToShow.map(p => p[currentRankingMode]), 1);

      itemsToShow.forEach((p, idx) => {
        const val = p[currentRankingMode];
        const pct = Math.min(100, Math.max(8, (val / maxVal) * 100));
        const marginPct = p.revenue > 0 ? ((p.profit / p.revenue) * 100).toFixed(1) : 0;

        let rankClass = 'rank-other';
        if (idx === 0) rankClass = 'rank-1';
        else if (idx === 1) rankClass = 'rank-2';
        else if (idx === 2) rankClass = 'rank-3';

        const row = document.createElement('div');
        row.className = 'product-bar-row';
        row.innerHTML = `
          <div class="p-bar-label">
            <div class="p-bar-name">
              <span class="rank-medal ${rankClass}">${idx + 1}</span>
              <span>${p.product}</span>
              <span style="font-size:11px; color:var(--text-muted);">(${p.category})</span>
            </div>
            <div class="tabular" style="font-weight:600; color:#fff;">
              ${fmtTHB(val)}
              <span style="font-size:11px; font-weight:normal; color:var(--text-muted); margin-left:6px;">
                (ขาย ${fmtInt(p.qty)} ชิ้น • กำไร ${marginPct}%)
              </span>
            </div>
          </div>
          <div class="p-bar-track">
            <div class="p-bar-fill ${idx === 0 ? 'fill-amber' : (idx % 2 === 1 ? 'fill-blue' : 'fill-orange')}" style="width: ${pct}%;">
              <span>${p.product} • ${pct.toFixed(0)}%</span>
            </div>
          </div>
        `;
        container.appendChild(row);
      });
    }

    // Quadrant 2: Branch Comparison Matrix
    function renderBranchMatrix(data, totalRev) {
      const branchAgg = {
        'มหาวิทยาลัย': { name: 'มหาวิทยาลัย', orders: 0, qty: 0, revenue: 0, profit: 0 },
        'สำนักงาน': { name: 'สำนักงาน', orders: 0, qty: 0, revenue: 0, profit: 0 },
        'ห้างสรรพสินค้า': { name: 'ห้างสรรพสินค้า', orders: 0, qty: 0, revenue: 0, profit: 0 }
      };

      data.forEach(r => {
        if (branchAgg[r.branch]) {
          branchAgg[r.branch].orders += 1;
          branchAgg[r.branch].qty += r.qty;
          branchAgg[r.branch].revenue += r.revenue;
          branchAgg[r.branch].profit += r.profit;
        }
      });

      const tbody = document.getElementById('branchTableBody');
      tbody.innerHTML = '';

      const branches = Object.values(branchAgg).sort((a, b) => b.revenue - a.revenue);

      branches.forEach(b => {
        const sharePct = totalRev > 0 ? (b.revenue / totalRev) * 100 : 0;
        const marginPct = b.revenue > 0 ? (b.profit / b.revenue) * 100 : 0;

        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td>
            <div class="branch-badge">
              <span class="material-symbols-rounded" style="font-size: 18px; color:var(--blue-400);">store</span>
              <span>${b.name}</span>
            </div>
          </td>
          <td class="num-cell">${fmtInt(b.orders)}</td>
          <td class="num-cell">${fmtInt(b.qty)}</td>
          <td class="num-cell" style="font-weight:600; color:#fff;">${fmtTHB(b.revenue)}</td>
          <td class="num-cell">
            ${sharePct.toFixed(1)}%
            <span class="share-bar-mini"><span class="share-bar-fill" style="width:${sharePct}%;"></span></span>
          </td>
          <td class="num-cell" style="color:#34d399;">${fmtTHB(b.profit)}</td>
          <td class="num-cell">${marginPct.toFixed(1)}%</td>
        `;
        tbody.appendChild(tr);
      });
    }

    // Quadrant 3: Daily Timeline SVG Chart
    function renderDailyTimeline(data) {
      const dailyMap = {};
      for (let day = 1; day <= 31; day++) {
        const dayStr = '2026-08-' + String(day).padStart(2, '0');
        dailyMap[dayStr] = { rev: 0, qty: 0, day: day };
      }

      let weekdayRev = 0;
      let weekendRev = 0;

      data.forEach(r => {
        if (dailyMap[r.date]) {
          dailyMap[r.date].rev += r.revenue;
          dailyMap[r.date].qty += r.qty;
        }
        const d = new Date(r.date + 'T00:00:00');
        const dow = d.getDay();
        if (dow === 0 || dow === 6) {
          weekendRev += r.revenue;
        } else {
          weekdayRev += r.revenue;
        }
      });

      document.getElementById('valWeekdayRev').textContent = fmtTHB(weekdayRev);
      document.getElementById('valWeekendRev').textContent = fmtTHB(weekendRev);
      const activeDays = 31;
      const totalFilteredRev = data.reduce((s, r) => s + r.revenue, 0);
      document.getElementById('valAvgDailyRev').textContent = fmtTHB(totalFilteredRev / activeDays);

      let peakDay = '';
      let maxDailyRev = 0;
      Object.entries(dailyMap).forEach(([dt, val]) => {
        if (val.rev > maxDailyRev) {
          maxDailyRev = val.rev;
          peakDay = dt;
        }
      });
      if (peakDay) {
        const dayNum = parseInt(peakDay.split('-')[2], 10);
        document.getElementById('peakDayTag').textContent = `Peak: ${dayNum} ส.ค. (${fmtTHB(maxDailyRev)})`;
      }

      const container = document.getElementById('dailyChartContainer');
      const width = 640;
      const height = 180;
      const padLeft = 40;
      const padRight = 15;
      const padBottom = 25;
      const padTop = 15;

      const chartW = width - padLeft - padRight;
      const chartH = height - padTop - padBottom;

      const daysArr = Object.values(dailyMap);
      const maxVal = Math.max(maxDailyRev, 100);

      const barWidth = (chartW / 31) * 0.7;
      let barsSvg = '';
      let labelsSvg = '';

      daysArr.forEach((d, i) => {
        const x = padLeft + (i * (chartW / 31)) + 2;
        const h = (d.rev / maxVal) * chartH;
        const y = padTop + (chartH - h);

        const isPeak = (d.rev === maxDailyRev && maxDailyRev > 0);
        const fill = isPeak ? '#f97316' : (d.day % 2 === 0 ? '#3b82f6' : '#2563eb');

        barsSvg += `
          <rect x="${x}" y="${y}" width="${barWidth}" height="${h}" rx="3" fill="${fill}" opacity="0.85">
            <title>${d.day} ส.ค.: ${fmtTHB(d.rev)} (${d.qty} ชิ้น)</title>
          </rect>
        `;

        if (d.day === 1 || d.day === 10 || d.day === 20 || d.day === 31) {
          labelsSvg += `<text x="${x + barWidth/2}" y="${height - 6}" font-size="10" fill="#94a3b8" text-anchor="middle">${d.day}</text>`;
        }
      });

      container.innerHTML = `
        <svg viewBox="0 0 ${width} ${height}" style="width:100%; height:100%; overflow:visible;">
          <line x1="${padLeft}" y1="${padTop}" x2="${width - padRight}" y2="${padTop}" stroke="rgba(255,255,255,0.06)" stroke-dasharray="3,3" />
          <line x1="${padLeft}" y1="${padTop + chartH/2}" x2="${width - padRight}" y2="${padTop + chartH/2}" stroke="rgba(255,255,255,0.06)" stroke-dasharray="3,3" />
          <line x1="${padLeft}" y1="${padTop + chartH}" x2="${width - padRight}" y2="${padTop + chartH}" stroke="rgba(255,255,255,0.12)" />
          
          <text x="${padLeft - 6}" y="${padTop + 10}" font-size="9" fill="#64748b" text-anchor="end">${(maxVal/1000).toFixed(1)}k</text>
          <text x="${padLeft - 6}" y="${padTop + chartH}" font-size="9" fill="#64748b" text-anchor="end">0</text>
          
          ${barsSvg}
          ${labelsSvg}
        </svg>
      `;
    }

    // Quadrant 4: Category Mix
    function renderCategoryMix(data, totalRev) {
      let bakeryRev = 0;
      let coffeeRev = 0;
      let drinksRev = 0;

      data.forEach(r => {
        if (r.category === 'เบเกอรี') bakeryRev += r.revenue;
        else if (r.category === 'กาแฟ') coffeeRev += r.revenue;
        else if (r.category === 'เครื่องดื่มอื่น') drinksRev += r.revenue;
      });

      const bPct = totalRev > 0 ? ((bakeryRev / totalRev) * 100).toFixed(1) : 0;
      const cPct = totalRev > 0 ? ((coffeeRev / totalRev) * 100).toFixed(1) : 0;
      const dPct = totalRev > 0 ? ((drinksRev / totalRev) * 100).toFixed(1) : 0;

      document.getElementById('sliceBakery').style.width = bPct + '%';
      document.getElementById('sliceCoffee').style.width = cPct + '%';
      document.getElementById('sliceDrinks').style.width = dPct + '%';

      document.getElementById('catMixLegend').textContent = 
        `เบเกอรี ${bPct}% (${fmtTHB(bakeryRev)}) • กาแฟ ${cPct}% (${fmtTHB(coffeeRev)}) • เครื่องดื่มอื่น ${dPct}% (${fmtTHB(drinksRev)})`;
    }

    // Transaction Explorer Table
    function renderTransactionTable(data) {
      const sorted = [...data].sort((a, b) => {
        let vA = a[sortColumn];
        let vB = b[sortColumn];
        if (typeof vA === 'string') {
          return sortAsc ? vA.localeCompare(vB) : vB.localeCompare(vA);
        }
        return sortAsc ? vA - vB : vB - vA;
      });

      document.getElementById('rowCountLabel').textContent = sorted.length;

      const totalPages = Math.max(1, Math.ceil(sorted.length / pageSize));
      if (currentPage > totalPages) currentPage = totalPages;

      document.getElementById('currentPageSpan').textContent = currentPage;
      document.getElementById('totalPagesSpan').textContent = totalPages;
      document.getElementById('btnPrevPage').disabled = (currentPage === 1);
      document.getElementById('btnNextPage').disabled = (currentPage === totalPages);

      const startIndex = (currentPage - 1) * pageSize;
      const pageRows = sorted.slice(startIndex, startIndex + pageSize);

      const tbody = document.getElementById('transactionTableBody');
      tbody.innerHTML = '';

      if (pageRows.length === 0) {
        tbody.innerHTML = '<tr><td colspan="10" style="text-align:center; padding:20px; color:var(--text-muted);">ไม่พบรายการที่ค้นหา</td></tr>';
        return;
      }

      pageRows.forEach(r => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td style="font-weight:600; color:var(--blue-400);">${r.id}</td>
          <td class="num-cell">${r.date}</td>
          <td>${r.branch}</td>
          <td style="font-weight:500; color:#fff;">${r.product}</td>
          <td><span style="font-size:11px; padding:2px 6px; border-radius:4px; background:rgba(255,255,255,0.06);">${r.category}</span></td>
          <td class="num-cell" style="text-align:right;">${r.qty}</td>
          <td class="num-cell" style="text-align:right;">${fmtTHB(r.price)}</td>
          <td class="num-cell" style="text-align:right;">${fmtTHB(r.cost)}</td>
          <td class="num-cell" style="text-align:right; font-weight:600; color:#fff;">${fmtTHB(r.revenue)}</td>
          <td class="num-cell" style="text-align:right; font-weight:600; color:#34d399;">${fmtTHB(r.profit)}</td>
        `;
        tbody.appendChild(tr);
      });
    }

    function changePage(delta) {
      currentPage += delta;
      updateDashboard();
    }

    function handleSort(col) {
      if (sortColumn === col) {
        sortAsc = !sortAsc;
      } else {
        sortColumn = col;
        sortAsc = true;
      }
      updateDashboard();
    }

    // CSV Export
    function exportToCSV() {
      const data = getFilteredData();
      const headers = ['รหัสรายการ', 'วันที่', 'สาขา', 'สินค้า', 'หมวดหมู่', 'จำนวนขาย (หน่วย)', 'ราคาขายต่อหน่วย (บาท)', 'ต้นทุนต่อหน่วย (บาท)', 'รายได้รวม (บาท)', 'กำไรขั้นต้น (บาท)'];
      
      const rows = data.map(r => [
        r.id,
        r.date,
        '"' + r.branch + '"',
        '"' + r.product + '"',
        '"' + r.category + '"',
        r.qty,
        r.price,
        r.cost,
        r.revenue,
        r.profit
      ]);

      const csvContent = '\uFEFF' + [headers.join(','), ...rows.map(e => e.join(',')).join('\\n')].join('\\n');
      const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `auction_quad_sales_${currentFilterBranch}_${currentFilterCat}.csv`;
      a.click();
      URL.revokeObjectURL(url);
    }

    // ==========================================================================
    // THREE.JS 3D INTERACTIVE STAGE ENGINE
    // ==========================================================================
    let scene, camera, renderer, controls;
    let podiumGroup;
    let pillars = [];
    let isAutoRotating = true;

    function initThreeJS() {
      const container = document.getElementById('canvasContainer');
      const width = container.clientWidth;
      const height = container.clientHeight;

      if (!window.WebGLRenderingContext) {
        container.innerHTML = '<div style="padding:40px; text-align:center; color:var(--text-muted);">WebGL ไม่รองรับในเบราว์เซอร์นี้ — ระบบทำงานในโหมดมาตรฐาน 2D</div>';
        return;
      }

      scene = new THREE.Scene();
      scene.fog = new THREE.FogExp2(0x060b18, 0.04);

      camera = new THREE.PerspectiveCamera(40, width / height, 0.1, 100);
      camera.position.set(0, 5, 9.5);

      renderer = new THREE.WebGLRenderer({
        canvas: document.getElementById('threeCanvas'),
        antialias: true,
        alpha: true
      });
      renderer.setSize(width, height);
      renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
      renderer.toneMapping = THREE.ACESFilmicToneMapping;
      renderer.toneMappingExposure = 1.2;

      controls = new THREE.OrbitControls(camera, renderer.domElement);
      controls.enableDamping = true;
      controls.dampingFactor = 0.05;
      controls.enablePan = false;
      controls.minDistance = 6;
      controls.maxDistance = 14;
      controls.maxPolarAngle = Math.PI / 2 - 0.05;

      const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
      scene.add(ambientLight);

      const dirLight = new THREE.DirectionalLight(0xffffff, 1.2);
      dirLight.position.set(5, 10, 7);
      scene.add(dirLight);

      const bluePoint = new THREE.PointLight(0x3b82f6, 2.5, 20);
      bluePoint.position.set(-5, 4, 3);
      scene.add(bluePoint);

      const orangePoint = new THREE.PointLight(0xf97316, 2.5, 20);
      orangePoint.position.set(5, 4, 3);
      scene.add(orangePoint);

      podiumGroup = new THREE.Group();
      scene.add(podiumGroup);

      const baseGeo = new THREE.CylinderGeometry(4.2, 4.4, 0.2, 48);
      const baseMat = new THREE.MeshStandardMaterial({
        color: 0x0c1730,
        roughness: 0.3,
        metalness: 0.8
      });
      const baseDisc = new THREE.Mesh(baseGeo, baseMat);
      baseDisc.position.y = -0.1;
      podiumGroup.add(baseDisc);

      const ringGeo = new THREE.TorusGeometry(4.25, 0.04, 16, 64);
      const ringMat = new THREE.MeshBasicMaterial({ color: 0x38bdf8 });
      const ringMesh = new THREE.Mesh(ringGeo, ringMat);
      ringMesh.rotation.x = Math.PI / 2;
      ringMesh.position.y = 0.02;
      podiumGroup.add(ringMesh);

      const particleGeo = new THREE.BufferGeometry();
      const particleCount = 120;
      const posArray = new Float32Array(particleCount * 3);
      for (let i = 0; i < particleCount * 3; i += 3) {
        posArray[i] = (Math.random() - 0.5) * 12;
        posArray[i + 1] = Math.random() * 6;
        posArray[i + 2] = (Math.random() - 0.5) * 12;
      }
      particleGeo.setAttribute('position', new THREE.BufferAttribute(posArray, 3));
      const particleMat = new THREE.PointsMaterial({
        size: 0.07,
        color: 0x60a5fa,
        transparent: true,
        opacity: 0.7
      });
      const particleMesh = new THREE.Points(particleGeo, particleMat);
      scene.add(particleMesh);

      window.addEventListener('resize', onWindowResize);
      animate();
    }

    function update3DScene(sortedProds) {
      if (!podiumGroup) return;

      pillars.forEach(p => podiumGroup.remove(p.mesh));
      pillars = [];

      const top3 = sortedProds.slice(0, 3);
      if (top3.length === 0) return;

      const maxVal = top3[0][currentRankingMode] || 1;

      const configs = [
        { rank: 1, pos: [0, 0, 0.4], color: 0xf59e0b, emissive: 0x78350f, rad: 0.9 },
        { rank: 2, pos: [-2.1, 0, -0.4], color: 0x2563eb, emissive: 0x1e3a8a, rad: 0.75 },
        { rank: 3, pos: [2.1, 0, -0.4], color: 0xf97316, emissive: 0x9a3412, rad: 0.75 }
      ];

      top3.forEach((prod, i) => {
        const cfg = configs[i];
        const val = prod[currentRankingMode];
        const heightScale = Math.max(0.6, (val / maxVal) * 3.5);

        const geo = new THREE.CylinderGeometry(cfg.rad, cfg.rad, heightScale, 36);
        const mat = new THREE.MeshStandardMaterial({
          color: cfg.color,
          emissive: cfg.emissive,
          roughness: 0.25,
          metalness: 0.6
        });

        const mesh = new THREE.Mesh(geo, mat);
        mesh.position.set(cfg.pos[0], heightScale / 2, cfg.pos[2]);

        podiumGroup.add(mesh);
        pillars.push({ mesh, prod, targetH: heightScale });
      });
    }

    function animate() {
      requestAnimationFrame(animate);

      if (controls) {
        controls.update();
      }

      if (podiumGroup && isAutoRotating) {
        podiumGroup.rotation.y += 0.004;
      }

      if (renderer && scene && camera) {
        renderer.render(scene, camera);
      }
    }

    function onWindowResize() {
      const container = document.getElementById('canvasContainer');
      if (!container || !renderer || !camera) return;
      const width = container.clientWidth;
      const height = container.clientHeight;
      camera.aspect = width / height;
      camera.updateProjectionMatrix();
      renderer.setSize(width, height);
    }

    // INITIALIZATION & LISTENERS
    document.addEventListener('DOMContentLoaded', () => {
      try {
        initThreeJS();
      } catch (err) {
        console.warn('3D initialization failed, fallback active:', err);
      }

      updateDashboard();

      document.querySelectorAll('[data-filter="branch"]').forEach(btn => {
        btn.addEventListener('click', (e) => {
          document.querySelectorAll('[data-filter="branch"]').forEach(b => b.classList.remove('active'));
          e.currentTarget.classList.add('active');
          currentFilterBranch = e.currentTarget.dataset.val;
          currentPage = 1;
          updateDashboard();
        });
      });

      document.querySelectorAll('[data-filter="cat"]').forEach(btn => {
        btn.addEventListener('click', (e) => {
          document.querySelectorAll('[data-filter="cat"]').forEach(b => b.classList.remove('active'));
          e.currentTarget.classList.add('active');
          currentFilterCat = e.currentTarget.dataset.val;
          currentPage = 1;
          updateDashboard();
        });
      });

      document.getElementById('searchInput').addEventListener('input', (e) => {
        currentSearchTerm = e.target.value.trim().toLowerCase();
        currentPage = 1;
        updateDashboard();
      });

      document.getElementById('resetFiltersBtn').addEventListener('click', () => {
        currentFilterBranch = 'ALL';
        currentFilterCat = 'ALL';
        currentSearchTerm = '';
        currentPage = 1;
        document.getElementById('searchInput').value = '';

        document.querySelectorAll('[data-filter="branch"]').forEach(b => {
          b.classList.toggle('active', b.dataset.val === 'ALL');
        });
        document.querySelectorAll('[data-filter="cat"]').forEach(b => {
          b.classList.toggle('active', b.dataset.val === 'ALL');
        });

        updateDashboard();
      });

      document.getElementById('exportCsvBtn').addEventListener('click', exportToCSV);

      document.getElementById('btnModeRev').addEventListener('click', () => {
        currentRankingMode = 'revenue';
        document.getElementById('btnModeRev').classList.add('active');
        document.getElementById('btnModeProfit').classList.remove('active');
        updateDashboard();
      });

      document.getElementById('btnModeProfit').addEventListener('click', () => {
        currentRankingMode = 'profit';
        document.getElementById('btnModeProfit').classList.add('active');
        document.getElementById('btnModeRev').classList.remove('active');
        updateDashboard();
      });

      document.getElementById('btnAutoRotate').addEventListener('click', () => {
        isAutoRotating = !isAutoRotating;
        document.getElementById('btnAutoRotate').classList.toggle('active', isAutoRotating);
      });

      document.getElementById('btnToggleTop3').addEventListener('click', () => {
        showAllProducts = false;
        document.getElementById('btnToggleTop3').classList.add('active');
        document.getElementById('btnToggleAllProds').classList.remove('active');
        updateDashboard();
      });

      document.getElementById('btnToggleAllProds').addEventListener('click', () => {
        showAllProducts = true;
        document.getElementById('btnToggleAllProds').classList.add('active');
        document.getElementById('btnToggleTop3').classList.remove('active');
        updateDashboard();
      });
    });
  </script>
</body>
</html>
"""

with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html_template)

print('Generated dashboard.html successfully!')
