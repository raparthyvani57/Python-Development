import requests
from bs4 import BeautifulSoup
import json

URL = "https://quotes.toscrape.com/"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; SimpleWebScraper/1.0)"
}


def scrape_quotes(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()

    except requests.exceptions.RequestException as error:
        print(f"Error while fetching the webpage: {error}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    quotes = []

    for quote in soup.find_all("div", class_="quote"):
        text = quote.find("span", class_="text")
        author = quote.find("small", class_="author")
        tags = quote.find_all("a", class_="tag")

        if text and author:
            quote_data = {
                "quote": text.get_text(strip=True),
                "author": author.get_text(strip=True),
                "tags": [tag.get_text(strip=True) for tag in tags]
            }

            quotes.append(quote_data)

    return quotes


def save_as_text(quotes, filename):
    with open(filename, "w", encoding="utf-8") as file:
        for number, item in enumerate(quotes, start=1):
            file.write(f"{number}. {item['quote']}\n")
            file.write(f"   Author: {item['author']}\n")
            file.write(f"   Tags: {', '.join(item['tags'])}\n\n")


def save_as_json(quotes, filename):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(quotes, file, indent=4, ensure_ascii=False)


def main():
    print("Starting web scraper...")

    quotes = scrape_quotes(URL)

    if not quotes:
        print("No data was extracted.")
        return

    save_as_text(quotes, "headlines.txt")
    save_as_json(quotes, "headlines.json")

    print(f"Successfully scraped {len(quotes)} quotes.")
    print("Data saved to headlines.txt and headlines.json")


if __name__ == "__main__":
    main()