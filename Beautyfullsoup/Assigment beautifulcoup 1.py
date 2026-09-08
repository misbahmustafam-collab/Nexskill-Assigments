import requests
from bs4 import BeautifulSoup
import csv


URL="https://www.ebay.com/"
r=requests.get(URL)
soup=BeautifulSoup(r.content,'html5lib')

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        " (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
}

r = requests.get(URL, headers=headers)

soup=BeautifulSoup(r.content,"html.parser")
#sary product ki khali list
products=[]
#ebay mn har product li tag mn hota h jiski class itme s hoti h
items=soup.find_all("li",attrs={"class":"s-items"})


for row in items:
    title_elem=row.find("div",attrs={"class":"s-item_title"})
    price_elem=row.find("span",attrs={"class":"s-item_price"})
    link_elem=row.find("a",attrs={"class":"s-item-link"})

    if title_elem and price_elem and link_elem:
        title_text=title_elem.text.strip()
        # Pehla  header item skip karne ke liye
        if "Shop on eBay" in title_text:
            continue

        # Single product ki Dictionary (Teacher style)
        product = {}
        product["title"] = title_text
        product["price"] = price_elem.text.strip()
        product["url"] = link_elem["href"]

        # List mein add kar dein
        products.append(product)

print("Status Code:", r.status_code)
print("Total items found:", len(items))
filename = "ebay_laptops.csv"

with open(filename, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["title", "price", "url"])
    w.writeheader()
    for product in products:
        w.writerow(product)

print(f"Done! {len(products)} products save ho gaye hain.")

