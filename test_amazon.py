from playwright.sync_api import sync_playwright

def search_and_add(product_name):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.amazon.in")
        page.wait_for_timeout(3000)

        # Search
        page.fill("#twotabsearchtextbox", product_name)
        page.press("#twotabsearchtextbox", "Enter")

        page.wait_for_selector(".s-result-item[data-component-type='s-search-result']")

        # Get valid product (skip ads)
        products = page.locator(".s-result-item[data-component-type='s-search-result']")
        count = products.count()

        selected = None
        price = None

        for i in range(count):
            item = products.nth(i)
            price_locator = item.locator(".a-price-whole")
            if price_locator.count() > 0:
                price = price_locator.first.text_content()
                selected = item
                break

        if not selected:
            print(f"No valid product found for {product_name}")
            browser.close()
            return

        print(f"{product_name} Price: ₹{price}")

        # Click product (same tab OR new tab)
        selected.click()
        page.wait_for_load_state()

        # Add to cart
        try:
            page.click("#add-to-cart-button", timeout=5000)
        except:
            print("Add to cart button not found")

        browser.close()


def test_iphone():
    search_and_add("iPhone")


def test_galaxy():
    search_and_add("Samsung Galaxy")