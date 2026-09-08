from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

driver = webdriver.Chrome()

driver.get("https://www.ebay.com/")
time.sleep(5)

print(driver.title)

product = []
items = driver.find_elements(By.CSS_SELECTOR, "li.s-item")
for item in items:
    try:
        title_element = item.find_element(By.CSS_SELECTOR, "h3.s-item__title")
        price_element = item.find_element(By.CSS_SELECTOR, "span.s-item__price")
        product.append({
            "title": title_element.text,
            "price": price_element.text,
        })
    except Exception:
        continue

with open("products.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["title", "price"])
    writer.writeheader()
    writer.writerows(product)

driver.quit()