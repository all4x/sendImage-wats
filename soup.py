
import html
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd



url= 'https://www.instagram.com/explore/tags/duckcute/'

r = requests.get(url)
html_doc = r.content 


soup = bs(html_doc, 'html.parser')
tags = soup.find_all('a')

