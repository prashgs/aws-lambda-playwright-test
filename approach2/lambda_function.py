import json
from playwright.sync_api import sync_playwright


def handler(event, context):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('https://example.com')
        title = page.title()
        screenshot_path = '/tmp/screenshot.png'
        page.screenshot(path=screenshot_path)
        browser.close()

    return {
        'statusCode': 200,
        'body': json.dumps({'title': title, 'screenshot_path': screenshot_path})
    }
