#coding: utf-8

import requests
from bs4 import BeautifulSoup
"""
Apresenta os recursos basicos do BeautifulSoup
"""


# requisicao basica
site= requests.get("http://example.com")
#retorno do coidgo 200, indicando que o conteúdo foi coletado.
print("Status:",site.status_code)
print("Encoding:",site.encoding)
print("Cabeçalho",site.headers)
soup=BeautifulSoup(site.content,"html.parser")
#acessar a tag
print(soup.title)
#acessa o conteúdo da tag html
print(soup.html)

print("----")
print(soup.div.h1.text)

#pesquisa usando os métodos
print("First",soup.find("a"))
for i in soup.findAll("a"):
    print(i['href'])

#Fazendo um select
print(soup.select("p"))
#print(soup.link('href'))

#extrai o texto da pagina
# print("Extrai o texto da pagina")
# print(soup.get_text())
