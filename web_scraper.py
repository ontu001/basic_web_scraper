import requests
from bs4 import BeautifulSoup
import sqlite3

def scrape_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extract the data from the website using BeautifulSoup
    # For example, if the website has a list of articles, you could extract the title and content of each article
    articles = soup.find_all('article')
    data = []
    for article in articles:
        title = article.find('h2').text
        content = article.find('p').text
        data.append((title, content))
    return data

def store_data(data):
    conn = sqlite3.connect('scraped_data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS articles (title text, content text)''')
    c.executemany('INSERT INTO articles VALUES (?,?)', data)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    url = 'https://www.github.com.com/articles'
    data = scrape_data(url)
    store_data(data)

#md rohanur rahman ontu