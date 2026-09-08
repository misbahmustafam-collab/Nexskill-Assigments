from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time
url = "https://www.ebay.com/sch/i.html?_nkw=laptop"
driver = webdriver.Chrome()
driver.get(url)

time.sleep(3)

products = []

items = driver.find_elements(By.CLASS_NAME, "s-item")

for item in items:
    try:
        title = item.find_element(By.CLASS_NAME, "s-item__title").text
        price = item.find_element(By.CLASS_NAME, "s-item__price").text
        link = item.find_element(By.CLASS_NAME, "s-item__link").get_attribute("href")

        product = {
            "Title": title,
            "Price": price,
            "Link": link
        }
        products.append(product)
    except Exception:
        continue

with open("products.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["Title", "Price", "Link"])
    writer.writeheader()
    writer.writerows(products)

driver.quit()