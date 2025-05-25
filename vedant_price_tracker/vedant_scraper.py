import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import time

base_url = "https://www.vedantcomputers.com/graphics-cards"
headers = {
    "User-Agent": "Mozilla/5.0 (compatible; PriceTrackerBot/1.0)"
}

def scrape_page(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    products = []

    items = soup.select("div.product-layout")
    for item in items:
        try:
            name = item.select_one("div.caption a").text.strip()
            price = item.select_one(".price").text.strip()
            link = item.select_one("div.caption a")["href"]
            image = item.select_one("img")["src"]

            products.append({
                "Product Name": name,
                "Price": price,
                "Product URL": link,
                "Image URL": image
            })
        except Exception as e:
            print(f"Error parsing a product: {e}")
            continue

    return products

def main():
    all_products = []

    for page in range(1, 4):
        page_url = f"{base_url}?page={page}"
        print(f"Scraping {page_url}...")
        try:
            products = scrape_page(page_url)
            all_products.extend(products)
            time.sleep(1)
        except Exception as e:
            print(f"Error scraping page {page}: {e}")

    df = pd.DataFrame(all_products)
    df.to_csv("vedant_products.csv", index=False)
    print("Saved CSV: vedant_products.csv")

    with open("products.json", "w", encoding="utf-8") as f:
        json.dump(all_products, f, indent=2, ensure_ascii=False)
    print("Saved JSON: products.json")

if __name__ == "__main__":
    main()
