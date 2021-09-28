from time import sleep
import requests as req
from bs4 import BeautifulSoup
from cookie import COOKIES

url = 'https://www.instagram.com/explore/tags/alanzoka/'
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'

headers = {
    'User-Agent': (USER_AGENT),
}


r = req.get(url, headers = headers, cookies=(COOKIES))
html_doc = r.text

soup = BeautifulSoup(html_doc, 'html.parser')
for link in soup.find_all('link'):
    print(link.get('href'))

