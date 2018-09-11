
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
"""
Descricao:
Crawler Simples para listar as últimas legendas do legendas.tv

MiniCurso: WebScrapping
Secomp 2018

Carlos Magno
Lucas Félix
UFSJ

Requisitos:
* python3
* requests, BeautifulSoup, selenium, geckodriver

"""
# Endereço do site a ser "crawleado".
site_alvo="http://legendas.tv/legendas/-/d/1"


#selenium
options = Options()
options.set_headless(headless=True)
#webdriver
navegador = webdriver.Firefox(firefox_options=options)
navegador.get(site_alvo)
#Retorna uma lista de elementos de acordo com o nome da classe.
destaques = navegador.find_elements_by_class_name('destaque')

for destaque in destaques:
    #extrai o html
    html= destaque.get_attribute('innerHTML')
    parser=BeautifulSoup(html,"html.parser")
    print("Legenda:",parser.find("a").text)
    print("Detalhes:",parser.find("p",{"class":"data"}).text)
    print("-----------")
