

import requests
from bs4 import BeautifulSoup

url = 'https://www2.correios.com.br/sistemas/rastreamento/ctrl/ctrlRastreamento.cfm?'

r = requests.post(url='https://www2.correios.com.br/sistemas/rastreamento/ctrl/ctrlRastreamento.cfm?', data={'objetos':'QH119857610BR'})
html_doc = r._content

soup = BeautifulSoup(html_doc, 'html.parser')
tag = soup.find(id="objetos")

print(tag)