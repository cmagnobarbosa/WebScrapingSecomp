
# coding: utf-8

# ** Coletor de Preços do Mercado Livre
# Descubra a faixa de preço para vender o seu produto, entenda os seus concorrentes.

# In[ ]:


import time
from bs4 import BeautifulSoup


# In[ ]:


from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys


# In[ ]:


# é utilizado para fazer uma breve análise
import collections


# In[ ]:


site="https://www.mercadolivre.com.br/"


# In[ ]:


produto_alvo="ssd 120gb"


# In[ ]:


options = Options()
options.set_headless(headless=True)
navegador = webdriver.Firefox(firefox_options=options)
#navegador = webdriver.Firefox()
navegador.get(site)


# In[ ]:


time.sleep(5)


# In[ ]:


campo_busca=navegador.find_element_by_class_name("nav-search-input")


# In[ ]:


campo_busca.send_keys(produto_alvo)


# In[ ]:


campo_busca.send_keys(Keys.ENTER)


# In[ ]:


time.sleep(5)


# In[ ]:


lista_produtos=navegador.find_element_by_id("searchResults")


# In[ ]:


html = lista_produtos.get_attribute('innerHTML')


# In[ ]:


soup = BeautifulSoup(html,"html.parser")


# In[ ]:


lista_produtos= soup.findAll("div",{"class":"rowItem item item--grid item--has-row-logo new with-reviews "})
print len(lista_produtos)


# In[ ]:


lista_precos=[]
for produto in lista_produtos:
    reais=produto.findAll("span",{"class":"price__fraction"})
    centavos=produto.findAll("span",{"class":"price__decimals"})
    if(centavos):
        centavos=float(centavos[0].text)/100.0
        final=float(reais[0].text)+centavos
        #print final
        lista_precos.append(final)
    else:
        lista_precos.append(float(reais[0].text))


# In[ ]:


print "Maior Preço: R$",max(lista_precos)
print "Menor Preço: R$",min(lista_precos)
print "Preço Médio: R$",sum(lista_precos)/len(lista_precos)


# In[ ]:


produtos_vendidos=soup.findAll("div",{"class":"item__condition"})
total_vendidos=0
lista_origem=[]
for vendas in produtos_vendidos:
    venda=vendas.text.split("-")
    #print venda
    try:
        #ignora os produtos usados..
        total_vendidos+=int(venda[0].split(" ")[1])
        origem=venda[1]
        lista_origem.append(origem)
    except Exception as e:
        pass
    

counter=collections.Counter(lista_origem)
origens=counter.most_common(2)
print "Número de Vendas:",total_vendidos
print "Origem dos produtos:"
for i in origens:
    print "Origem:",i[0],"Número de vendedores:",i[1]

