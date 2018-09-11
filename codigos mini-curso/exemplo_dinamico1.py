
# coding: utf-8

# Agora vamos combinar o BeautifulSoup com o Selenium para coletar dados de sites que utilizam javascript.

# In[ ]:


import time
from bs4 import BeautifulSoup


# In[ ]:


from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys


# In[ ]:


site_alvo="http://g1.globo.com"


# In[ ]:


options = Options()
options.set_headless(headless=True)


# In[ ]:


#acessa o navegador, caso queira ver o navega
#navegador = webdriver.Firefox(firefox_options=options)
navegador = webdriver.Firefox()
navegador.get(site_alvo)


# In[ ]:


#aguardando o site carregar..
time.sleep(10)


# In[ ]:


search=navegador.find_element_by_id("busca-campo")


# In[ ]:


#enviamos dados para o campo de pesquisa...
search.send_keys("eleicoes 2018")


# In[ ]:


search.send_keys(Keys.ENTER)


# In[ ]:


time.sleep(5)


# In[ ]:


noticias=navegador.find_elements_by_class_name("results__content")


# In[ ]:


print len(noticias)


# In[ ]:


html = noticias[0].get_attribute('innerHTML')


# In[ ]:


soup = BeautifulSoup(html,"html.parser")


# In[ ]:


lista_noticias= soup.findAll("li")


# In[ ]:


for noticia in lista_noticias:
    titulo=noticia.find("div",{"class":"widget--info__title product-color "})
    if(titulo):
        print "Titulo:",titulo.text
    #print new.div.text
    descricao=noticia.find("p",{"class":"widget--info__description"})
    if(descricao):
        print "Descrição:",descricao.text
    print("----")


# In[ ]:


navegador.stop_client()
navegador.close()

