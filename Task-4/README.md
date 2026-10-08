Web Scraper for Quotes
Objective

The objective of this project is to build a web scraper using Python, Requests, and BeautifulSoup to collect quotes from a website and save the extracted information into text and JSON files.

Technologies Used
Python
Requests
BeautifulSoup
JSON
Features
Sends HTTP requests to a webpage.
Handles HTTP request errors.
Parses HTML using BeautifulSoup.
Extracts quotes, authors, and tags.
Cleans the extracted data.
Saves the results as a text file.
Saves the results as a JSON file.
Output

The scraper successfully extracted 10 quotes.

The extracted data is saved in:

headlines.txt
headlines.json
How to Run

Install the required packages:

pip install requests beautifulsoup4


Run the program:

python Webscraper.py

Conclusion

This project demonstrates the basic process of web scraping, including sending HTTP requests, inspecting HTML structure, extracting information, cleaning data, and storing the collected information in different formats.