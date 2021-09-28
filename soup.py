<<<<<<< HEAD


import requests
from bs4 import BeautifulSoup

url = 'https://www2.correios.com.br/sistemas/rastreamento/ctrl/ctrlRastreamento.cfm?'

r = requests.post(url='https://www2.correios.com.br/sistemas/rastreamento/ctrl/ctrlRastreamento.cfm?', data={'objetos':'QH119857610BR'})
html_doc = r._content

soup = BeautifulSoup(html_doc, 'html.parser')
tag = soup.find(id="objetos")

print(tag)
=======

import html
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd



url= 'https://www.instagram.com/explore/tags/duckcute/'

r = requests.get(url)
html_doc = r.content 


soup = bs(html_doc, 'html.parser')
tags = soup.find_all('a')

>>>>>>> f238b564304ae1ce6052dfea88eb9134e2eab08b
