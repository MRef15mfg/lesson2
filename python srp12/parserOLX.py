import requests
from bs4 import BeautifulSoup
import csv
 
URL = "https://www.olx.ua/uk/transport/legkovye-avtomobili/"
HOST = "https://www.olx.ua/"
CSV = "cards.csv"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
}
 
def get_html(url, params=None):
    return requests.get(url, headers=HEADERS, params=params)
 
def get_content(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all('div', class_="css-1r93q13")
    cards = []
    for item in items:
        title_item = item.find_next('h4', class_="css-1g61gc2")
        title = title_item.get_text() if title_item else "No title"

        price_item = item.find_next('p', class_="css-uj7mm0")
        price = price_item.get_text() if price_item else "No price"

        info_item = item.find_next('span', class_="css-t4djs0")
        info = info_item.get_text() if info_item else "No info"

        link_item = item.find_next('a', class_="css-1tqlkj0")
        link = HOST + link_item.get('href') if link_item else "No link"

        image_item = item.find("img", class_="css-8wsg1m")
        image = image_item.get("src") if image_item else "No image"

 
        cards.append({
            "title": title,
            "price": price,
            "link": link,
            "image": image,
            "info" : info
            
        })
    return cards
 
def save_to_csv(cards, path):
    with open(path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        for card in cards:
            writer.writerow(["\nTITLE : ", card["title"], "\nPRICE : ", card["price"], "\nLINK : ", card["link"], "\nIMAGE : ", card["image"], "\nINFO : ", card["info"]])
 
def parser():
    pagination = int(input("Enter number of pages : "))
    html = get_html(URL)
    if html.status_code == 200:
        cards = []
        for page in range(1, pagination + 1):
            print(f"Parsing page {str(page)}")
            html = get_html(URL, params={"page": page})
            cards.extend(get_content(html.text))
            save_to_csv(cards, CSV)
    else:
        print("Error")
 
parser()
