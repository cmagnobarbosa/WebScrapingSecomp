
import requests
from bs4 import BeautifulSoup
"""
Descricao:
Crawler simples que retorna o nome, área
e o lates dos professores do dcomp.

MiniCurso: WebScrapping
Secomp 2018

Carlos Magno
Lucas Félix
UFSJ

Requisitos:
* python3
* requests, BeautifulSoup
"""
# Endereço do site a ser "crawleado".
site= requests.get("http://dcomp.ufsj.edu.br/pessoas/professores/")
#extrai o html
html=site.text
#parser utilizando para varrer o html
parser=BeautifulSoup(html,"lxml")

# a classe que contém os dados dos professores
#Utilize o inspecionar elementos em um navegador web a sua escolha
corpo=parser.findAll("div",{"class":"profile-entry"})
print("Total de Professores:",len(corpo))
for i in corpo:
    print("Nome:",i.find("h1").text)
    print("Área de pesquisa:",i.findAll("p")[2].text)
    print("Lattes:",i.findAll("a")[-1]['href'])
    print("-------")
