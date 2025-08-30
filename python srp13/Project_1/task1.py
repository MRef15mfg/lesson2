import requests
from bs4 import BeautifulSoup
import csv
import json
import os

URL = "https://books.toscrape.com/catalogue/page-{}.html"
HOST = "https://books.toscrape.com/"
CSV_FILE = "books.csv"
HTML_FILE = "books.html"
JSON_FILE = "books.json"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
}

def get_page(url):
    return requests.get(url, headers=HEADERS)

def parse_books(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all('li', class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
    books = []
    for item in items:


        title = item.find('h3').find('a')['title']
        price = item.find('p', class_="price_color").get_text()
        image = HOST + item.find('img')['src']



        books.append({
            "title": title,
            "price": price,
            "image": image
        })
    return books

def save_csv(books, path):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(["Title", "Price", "Image"])

        for book in books:
            writer.writerow([book["title"], book["price"], book["image"]])

def save_html(books, path):
    with open(path, "w", encoding="utf-8") as f:
        f.write("<html><body>\n")
        for book in books:
            f.write(f"<h3>{book['title']}</h3>\n")
            f.write(f"<p>{book['price']}</p>\n")
            f.write(f"<img src='{book['image']}'/><br>\n")
        f.write("</body></html>")

def save_json(books, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(books, f, indent=4, ensure_ascii=False)

def main():
    total_pages = int(input("Enter number of pages to parse : "))
    
    for page in range(1, total_pages + 1):
        url = URL.format(page)
        print(f"Parsing page {page}...")
        response = get_page(url)
        if response.status_code == 200:
            books = parse_books(response.text)
        else:
            print(f"Error: {response.status_code}")

    save_csv(books, CSV_FILE)
    save_html(books, HTML_FILE)
    save_json(books, JSON_FILE)
    print(f"Saved {len(books)} books to CSV, HTML, and JSON files.")

if __name__ == "__main__":
    main()
