from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO
import time


def fetch_daily_data():
    # Set up headless browser
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Auto-install ChromeDriver
    service = Service(ChromeDriverManager().install())

    # Start driver
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://e2necc.com/home/eggprice")

    # Wait for JavaScript to load the content
    time.sleep(5)

    # Parse page source after JS loads
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    # Try printing all tables
    tables = soup.find_all("table")
    print(f"Found {len(tables)} tables.")

    if len(tables) == 0:
        print("❌ No tables found.")
        return None
    else:
        # Use the first one
        for i, t in enumerate(tables):
            try:
                df = pd.read_html(StringIO(str(t)))[0]
            except Exception:
                continue
        df.to_csv("egg_prices_today.csv", index=False)
        return df