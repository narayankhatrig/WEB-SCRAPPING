# python -m pip install requests
# => get data from web (html, json, xml)
#python -m pip install beautifulsoup4
# => parse html

import json
import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"

def scrape_books(url):
    response = requests.get(url)
    #print(response.status_code)
    #print(response.text)
    if response.status_code != 200:
        print("Failed to load the page")
        return []
    
    #set encoding explicitly to handle special characters correctly
    response.encoding = response.apparent_encoding
    #print(response.text)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    #print(books)
    all_books = []
    for book in books:
        title = book.h3.a['title']
        #print(title)
        price_string = book.find('p', class_='price_color').text
        #print(price_string, type(price_string))
        currency = price_string[0]
        price = float(price_string[1:])
        #print(title, currency, price)
        all_books.append(
            {
                "title": title,
                "currency": currency,
                "price": price,
            }
        )
    #print(all_books)
    return all_books
    

books = scrape_books(url)

with open("books.json", "w", encoding='utf-8') as f:
    json.dump(books, f, indent = 4, ensure_ascii=False)


