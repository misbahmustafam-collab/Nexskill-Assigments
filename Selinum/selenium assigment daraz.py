from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

# Daraz Search URL
url = "https://www.daraz.pk/catalog/?q=laptop"
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)
products = []

items = driver.find_elements(By.XPATH, "//div[@data-qa-locator='product-item']")
for item in items:
    title = item.find_element(By.XPATH, ".//a").text
    link = item.find_element(By.XPATH, ".//a").get_attribute("href")
    products.append({"title": title, "url": link})

with open("daraz_products.csv", "w", newline='', encoding='utf-8') as csvfile:
    fieldnames = ["title", "url"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(products)

print("Data saved successfully")
driver.quit()
    


