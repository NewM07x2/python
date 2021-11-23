from bs4 import BeautifulSoup
import requests

html = requests.get('https://www.python.org/')
# print(html.text)
soup = BeautifulSoup(html.text, 'html.parser')
title = soup.find_all('title')
print(title)

intro = soup.find_all('div', {'class': 'introduction'})
print(intro[0].text)
