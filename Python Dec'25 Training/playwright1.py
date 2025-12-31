from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Set headless=False to see it run
    page = browser.new_page()

    # Set a realistic user agent
    page.set_extra_http_headers({"Accept-Language": "en-US,en;q=0.9"})
    page.emulate_media(color_scheme="light")

    page.goto(
        "https://www.flipkart.com/pomegranate/p/itm4d6d3c36d2563?pid=FRTFECZ8CSDKAPBZ&lid=LSTFRTFECZ8CSDKAPBZR2PXIN&marketplace=HYPERLOCAL&shopId=che_111_wh_hl_01&pageUID=1766686550092"
    )

    # Wait for product title to load
    page.wait_for_selector("span.B_NuCI")  # Flipkart's product title class (may change)

    title = page.text_content("span.B_NuCI")
    price = page.text_content("div._30jeq3._16Jk6d")  # Price selector

    print("Title:", title)
    print("Price:", price)

    browser.close()
