from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page =browser.new_page()
    page.goto('https://www.soriana.com/?srsltid=AfmBOoqHzwxXhEwdnegMmiJ7UHiHUvADrHYaJWcRlwQEhzmpGLk8N6xd')
    page.screenshot(path='imagen.png')
    browser.close()
