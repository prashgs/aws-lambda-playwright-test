import sys
from playwright.sync_api import sync_playwright

import os

os.environ['PLAYWRIGHT_BROWSERS_PATH'] = '/function/ms-playwright'
os.chmod(os.environ.get('PLAYWRIGHT_BROWSERS_PATH'), 0o777)


def handler(event, context):
    response = 'No response'
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        response = page.goto('https://joecoffeecompany.com/', wait_until='load')
        return str(response.ok)
