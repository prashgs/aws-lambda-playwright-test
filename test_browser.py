from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    response = page.goto('https://joecoffeecompany.com/', wait_until='load')
    print(response.ok)
    