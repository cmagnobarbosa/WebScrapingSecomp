# coding:utf8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
"""
Monitora novas postagens
no pastbin

"""

site_alvo="https://pastebin.com/archive"

#selenium
options = Options()
options.set_headless(headless=True)
#webdriver
navegador = webdriver.Firefox(firefox_options=options)
navegador.get(site_alvo)
#Retorna uma lista de elementos de acordo com o nome da classe.
codigos = navegador.find_element_by_class_name('maintable')
html=codigos.get_attribute('innerHTML')
parser=BeautifulSoup(html,"lxml")
lista_codigos=parser.findAll("tr")
lista_codigos.pop()
for codigo in lista_codigos:
    try:
        detalhes=codigo.findAll("td")
        cod=codigo.findAll("a")[0]['href']
        link="https://pastebin.com/raw"+str(cod)
        print("Link para baixar:",link)
        print("Postado a:",detalhes[1].text)
        print("Sintaxe:",detalhes[2].text)
    except Exception as e:
        pass

navegador.close()
