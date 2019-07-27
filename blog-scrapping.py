from bs4 import BeautifulSoup
import requests
from csv import writer

response = requests.get('https://blog.scrapinghub.com/')

soup = BeautifulSoup(response.text, 'html.parser')

posts = soup.find_all(class_='post-header')

with open('posts.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    header = ['Title', 'Link', 'Date', 'Author']
    csv_writer.writerow(header)
    for post in posts:
        title = post.find('h2').get_text()
        link = post.find('a')['href']
        date = post.find(class_ = 'date').get_text().replace('\n', '')
        author = post.find(class_='author').get_text().replace('\n', '')
        csv_writer.writerow([title, link, date, author])


