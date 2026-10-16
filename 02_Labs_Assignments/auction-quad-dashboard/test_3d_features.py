import asyncio
import os
import sys
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding='utf-8')

test_file = r'C:\Users\iznamu\Downloads\Auction Quad Dashboard — Google Material Symbols.html'
file_url = 'file:///' + test_file.replace('\\', '/')

async def run_3d_tests():
    print("=== AUDITING 3D POP-UP MODAL & REALISTIC MODELS ===")
    async with async_playwright() as p:
        browser = await p.chromium.launch(channel='msedge', headless=True)
        page = await browser.new_page()

        console_errors = []
        page.on('console', lambda msg: console_errors.append(msg.text) if msg.type in ['error'] else None)
        page.on('pageerror', lambda err: console_errors.append(str(err)))

        await page.goto(file_url, wait_until='networkidle')
        await asyncio.sleep(1)

        # 1. Open 1st product: ชีสเค้ก
        await page.click('.bar-item:nth-child(1)')
        await asyncio.sleep(0.6)

        badge_text = await page.inner_text('#modelModeBadge')
        print(f"Badge Text: '{badge_text}'")
        assert "โมเดล 3D สมจริง" in badge_text, f"Badge unexpected: {badge_text}"

        import_btn_visible = await page.is_visible('#btnImportGLB')
        print(f"Import .GLB Button Visible: {import_btn_visible}")
        assert import_btn_visible, "Import button should be visible"

        # Verify 3D mesh has multiple children in mMeshGroup
        mesh_child_count = await page.evaluate("() => mMeshGroup ? mMeshGroup.children.length : 0")
        print(f"ชีสเค้ก mMeshGroup child count: {mesh_child_count} (Expect > 2)")
        assert mesh_child_count > 2, f"Expected mesh children > 2, got {mesh_child_count}"

        # Capture screenshot of 3D modal in Dark Mode
        modal_shot_dark = os.path.join(os.path.dirname(test_file), '3d_modal_cheesecake_dark.png')
        await page.locator('#modal3D .modal-card').screenshot(path=modal_shot_dark)
        print(f"Saved modal screenshot (Dark): {modal_shot_dark}")

        # Switch to Light Mode inside modal using applyTheme
        await page.evaluate("applyTheme('light')")
        await asyncio.sleep(0.4)

        modal_shot_light = os.path.join(os.path.dirname(test_file), '3d_modal_cheesecake_light.png')
        await page.locator('#modal3D .modal-card').screenshot(path=modal_shot_light)
        print(f"Saved modal screenshot (Light): {modal_shot_light}")

        # Switch back to Dark Mode
        await page.evaluate("applyTheme('dark')")
        await asyncio.sleep(0.3)

        # Test remaining 7 products to ensure all procedural models instantiate without errors
        products = ["ลาเต้", "ครัวซองต์", "คาปูชิโน", "โกโก้", "อเมริกาโน", "ชาไทย", "บราวนี"]
        for p_name in products:
            await page.evaluate(f"openProductModal('{p_name}')")
            await asyncio.sleep(0.3)
            p_badge = await page.inner_text('#modelModeBadge')
            p_title = await page.inner_text('#mTitle')
            p_count = await page.evaluate("() => mMeshGroup ? mMeshGroup.children.length : 0")
            print(f"-> Tested '{p_title}': badge='{p_badge.strip()}', children={p_count}")
            assert p_count > 2, f"Model for {p_name} failed to load mesh"

        # Capture modal screenshot for Latte
        await page.evaluate("openProductModal('ลาเต้')")
        await asyncio.sleep(0.4)
        latte_shot = os.path.join(os.path.dirname(test_file), '3d_modal_latte_dark.png')
        await page.locator('#modal3D .modal-card').screenshot(path=latte_shot)
        print(f"Saved modal screenshot for Latte: {latte_shot}")

        # Capture modal screenshot for Croissant
        await page.evaluate("openProductModal('ครัวซองต์')")
        await asyncio.sleep(0.4)
        croissant_shot = os.path.join(os.path.dirname(test_file), '3d_modal_croissant_dark.png')
        await page.locator('#modal3D .modal-card').screenshot(path=croissant_shot)
        print(f"Saved modal screenshot for Croissant: {croissant_shot}")

        # Capture modal screenshot for Thai Tea
        await page.evaluate("openProductModal('ชาไทย')")
        await asyncio.sleep(0.4)
        tea_shot = os.path.join(os.path.dirname(test_file), '3d_modal_thaitea_dark.png')
        await page.locator('#modal3D .modal-card').screenshot(path=tea_shot)
        print(f"Saved modal screenshot for Thai Tea: {tea_shot}")

        print(f"\nTotal Console Errors during all 8 3D model transitions: {len(console_errors)}")
        if console_errors:
            print("Errors:", console_errors)
        assert len(console_errors) == 0, f"Found console errors: {console_errors}"

        await browser.close()
        print("\nALL 8 REALISTIC 3D MODELS VERIFIED 100% SUCCESSFUL!")

asyncio.run(run_3d_tests())
