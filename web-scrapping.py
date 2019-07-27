from bs4 import BeautifulSoup
import requests

response = requests.get('https://blog.scrapinghub.com/')

soup = BeautifulSoup(response.text, 'html.parser')

posts = soup.find_all(class_='post-header')

for post in posts:
    title = post.find('h2').get_text()
    link = post.find('a')['href']
    date = post.find(class_ = 'date').get_text().replace('\n', '')
    author = post.find(class_='author').get_text().replace('\n', '')


