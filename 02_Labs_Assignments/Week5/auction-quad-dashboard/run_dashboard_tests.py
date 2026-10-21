import asyncio
import os
import sys
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding='utf-8')

test_file = r'C:\Users\iznamu\Downloads\Auction Quad Dashboard — Google Material Symbols.html'
file_url = 'file:///' + test_file.replace('\\', '/')

async def run_tests():
    print(f"=== RUNNING AUTOMATED AUDIT FOR AUCTION QUAD DASHBOARD ===")
    print(f"Target: {test_file}\n")

    results = []
    console_logs = []
    console_errors = []

    def record_result(category, name, passed, details=""):
        status = "✅ PASS" if passed else "❌ FAIL"
        results.append((category, name, passed, details))
        print(f"[{status}] {category} -> {name}: {details}")

    async with async_playwright() as p:
        browser = await p.chromium.launch(channel='msedge', headless=True)
        page = await browser.new_page()

        page.on('console', lambda msg: (
            console_errors.append(msg.text) if msg.type in ['error'] else console_logs.append(msg.text)
        ))
        page.on('pageerror', lambda err: console_errors.append(str(err)))

        # 1. Page Load
        await page.goto(file_url, wait_until='networkidle')
        await asyncio.sleep(1)

        title = await page.title()
        record_result("Page Setup", "Title Check", "Auction Quad" in title, f"Title = '{title}'")
        record_result("Page Setup", "Console Errors", len(console_errors) == 0, 
                      f"Found {len(console_errors)} error(s): {console_errors if console_errors else 'None'}")

        # 2. Executive KPIs Verification
        kpi_vals = await page.eval_on_selector_all('.kpi-val', 'elements => elements.map(e => e.textContent.trim())')
        record_result("Financial KPIs", "Total Revenue", "72,530" in kpi_vals[0], f"Expected 72,530, got '{kpi_vals[0]}'")
        record_result("Financial KPIs", "Total Units Sold", "1,000" in kpi_vals[1], f"Expected 1,000, got '{kpi_vals[1]}'")
        record_result("Financial KPIs", "Total Gross Profit", "38,825" in kpi_vals[2], f"Expected 38,825, got '{kpi_vals[2]}'")
        record_result("Financial KPIs", "GP Margin %", "53.53" in kpi_vals[3], f"Expected 53.53%, got '{kpi_vals[3]}'")

        # 3. Quad I Top Products
        bar_names = await page.eval_on_selector_all('.bar-item .bar-name', 'elements => elements.map(e => e.textContent.trim())')
        bar_vals = await page.eval_on_selector_all('.bar-item .bar-num', 'elements => elements.map(e => e.textContent.trim())')
        
        top3_correct = (
            len(bar_names) >= 3 and 
            "ชีสเค้ก" in bar_names[0] and "฿13,420" in bar_vals[0] and
            "ลาเต้" in bar_names[1] and "฿10,125" in bar_vals[1] and
            "ครัวซองต์" in bar_names[2] and "฿10,030" in bar_vals[2]
        )
        record_result("Quad I Products", "Top 3 Ranking & Values", top3_correct, 
                      f"1st: {bar_names[0]} {bar_vals[0]}, 2nd: {bar_names[1]} {bar_vals[1]}, 3rd: {bar_names[2]} {bar_vals[2]}")

        # 4. Quad II Branches Table
        branch_rows = await page.eval_on_selector_all('.bt tbody tr', '''elements => elements.slice(0, 3).map(r => {
            const cells = Array.from(r.querySelectorAll('td')).map(td => td.textContent.trim());
            return { name: cells[0], orders: cells[1], qty: cells[2], rev: cells[3], profit: cells[5], gp: cells[6] };
        })''')
        
        uni_match = branch_rows[0]['rev'] == '฿33,395' and branch_rows[0]['qty'] == '465'
        off_match = branch_rows[1]['rev'] == '฿21,245' and branch_rows[1]['qty'] == '290'
        mall_match = branch_rows[2]['rev'] == '฿17,890' and branch_rows[2]['qty'] == '245'
        record_result("Quad II Branches", "Branch Table Accuracy", uni_match and off_match and mall_match,
                      f"Uni: {branch_rows[0]['rev']}, Off: {branch_rows[1]['rev']}, Mall: {branch_rows[2]['rev']}")

        # 5. Quad III & IV
        peak_text = await page.inner_text('.daily-stats .ds-p')
        record_result("Quad III Timeline", "Peak Day Identification", "4 ส.ค." in peak_text and "3,690" in peak_text, f"Peak = '{peak_text}'")

        cat_names = await page.eval_on_selector_all('.cat-card .cat-name', 'elements => elements.map(e => e.textContent.trim())')
        cat_pcts = await page.eval_on_selector_all('.cat-card .cat-pct', 'elements => elements.map(e => e.textContent.trim())')
        record_result("Quad IV Categories", "Category Breakdown", 
                      "40.7%" in cat_pcts[0] and "38.5%" in cat_pcts[1] and "20.9%" in cat_pcts[2],
                      f"Bakery: {cat_pcts[0]}, Coffee: {cat_pcts[1]}, Drinks: {cat_pcts[2]}")

        # 6. FEATURE TEST: Light/Dark Mode Switcher
        init_theme = await page.get_attribute('html', 'data-theme')
        theme_icon_1 = await page.inner_text('#themeIcon')
        
        # Click toggle to Light Mode
        await page.click('#themeToggle')
        await asyncio.sleep(0.3)
        theme_after_1 = await page.get_attribute('html', 'data-theme')
        theme_icon_2 = await page.inner_text('#themeIcon')
        ls_theme_1 = await page.evaluate("() => localStorage.getItem('aq_theme')")
        
        light_mode_ok = (theme_after_1 == 'light' and theme_icon_2 == 'dark_mode' and ls_theme_1 == 'light')
        record_result("Theme Switcher", "Toggle Dark -> Light", light_mode_ok, 
                      f"HTML[data-theme]={theme_after_1}, Icon={theme_icon_2}, localStorage={ls_theme_1}")

        # Click toggle back to Dark Mode
        await page.click('#themeToggle')
        await asyncio.sleep(0.3)
        theme_after_2 = await page.get_attribute('html', 'data-theme')
        theme_icon_3 = await page.inner_text('#themeIcon')
        ls_theme_2 = await page.evaluate("() => localStorage.getItem('aq_theme')")
        
        dark_mode_ok = (theme_after_2 == 'dark' and theme_icon_3 == 'light_mode' and ls_theme_2 == 'dark')
        record_result("Theme Switcher", "Toggle Light -> Dark", dark_mode_ok, 
                      f"HTML[data-theme]={theme_after_2}, Icon={theme_icon_3}, localStorage={ls_theme_2}")

        # 7. FEATURE TEST: 3D Card Pop-Up (Product Click -> Modal)
        modal_visible_0 = await page.is_visible('#modal3D')
        record_result("3D Pop-Up", "Initial Modal State Hidden", not modal_visible_0, f"Visible = {modal_visible_0}")

        # Click on 1st product bar: ชีสเค้ก
        await page.click('.bar-item:nth-child(1)')
        await asyncio.sleep(0.5)

        modal_visible_1 = await page.is_visible('#modal3D')
        m_title = await page.inner_text('#mTitle')
        m_cat = await page.inner_text('#mCat')
        m_price = await page.inner_text('#mPrice')
        m_rev = await page.inner_text('#mTotalRev')
        m_profit = await page.inner_text('#mTotalProfit')
        m_canvas_box = await page.eval_on_selector('#modal3DCanvas', 'c => ({ w: c.clientWidth, h: c.clientHeight })')

        cheesecake_modal_ok = (
            modal_visible_1 and 
            "ชีสเค้ก" in m_title and 
            "เบเกอรี" in m_cat and 
            "฿110.00" in m_price and 
            "฿13,420.00" in m_rev and
            "฿4,636.00" in m_profit and
            m_canvas_box['w'] > 0 and m_canvas_box['h'] > 0
        )
        record_result("3D Pop-Up", "Open Modal for 'ชีสเค้ก'", cheesecake_modal_ok,
                      f"Title: {m_title}, Price: {m_price}, Rev: {m_rev}, 3D Canvas: {m_canvas_box['w']}x{m_canvas_box['h']}px")

        # Test Close Button
        await page.click('.modal-close')
        await asyncio.sleep(0.3)
        modal_visible_closed_btn = await page.is_visible('#modal3D')
        record_result("3D Pop-Up", "Close via Close Button", not modal_visible_closed_btn, f"Visible = {modal_visible_closed_btn}")

        # Test Open for 'ลาเต้' & Close via Escape Key
        await page.click('.bar-item:nth-child(2)')
        await asyncio.sleep(0.5)
        m_title_latte = await page.inner_text('#mTitle')
        m_rev_latte = await page.inner_text('#mTotalRev')
        m_margin_latte = await page.inner_text('#mMargin')

        latte_modal_ok = ("ลาเต้" in m_title_latte and "฿10,125.00" in m_rev_latte and "62.7%" in m_margin_latte)
        record_result("3D Pop-Up", "Open Modal for 'ลาเต้'", latte_modal_ok,
                      f"Title: {m_title_latte}, Rev: {m_rev_latte}, Margin: {m_margin_latte}")

        await page.keyboard.press('Escape')
        await asyncio.sleep(0.3)
        modal_visible_closed_esc = await page.is_visible('#modal3D')
        record_result("3D Pop-Up", "Close via Escape Key", not modal_visible_closed_esc, f"Visible = {modal_visible_closed_esc}")

        # Test Open from KPI Card
        await page.click('.kpi:nth-child(1)')
        await asyncio.sleep(0.5)
        modal_visible_kpi = await page.is_visible('#modal3D')
        record_result("3D Pop-Up", "Open Modal from KPI Card", modal_visible_kpi, f"Visible = {modal_visible_kpi}")

        # Close via Backdrop click (click outside modal card)
        await page.mouse.click(10, 10)
        await asyncio.sleep(0.3)
        modal_visible_closed_backdrop = await page.is_visible('#modal3D')
        record_result("3D Pop-Up", "Close via Backdrop Click", not modal_visible_closed_backdrop, f"Visible = {modal_visible_closed_backdrop}")

        # Screenshot of Final State
        screenshot_path = os.path.join(os.path.dirname(test_file), 'test_verified_dashboard.png')
        await page.screenshot(path=screenshot_path, full_page=True)
        print(f"\nCaptured full-page screenshot: {screenshot_path}")

        await browser.close()

    total_tests = len(results)
    passed_tests = sum(1 for r in results if r[2])
    print(f"\n==========================================")
    print(f"AUDIT SUMMARY: {passed_tests} / {total_tests} TESTS PASSED")
    print(f"PASS RATE: {(passed_tests / total_tests) * 100:.1f}%")
    print(f"==========================================")

asyncio.run(run_tests())
