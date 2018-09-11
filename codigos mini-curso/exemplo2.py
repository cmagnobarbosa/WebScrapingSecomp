
# coding: utf-8

# ***Coletando dados de Example.com usando métodos**
# Lembre-se o inspecionar elementos é um dos seus melhores amigos quando o assunto é coleta.

# In[ ]:


import requests
from bs4 import BeautifulSoup


# In[ ]:


site= requests.get("http://example.com")


# In[ ]:


soup=BeautifulSoup(site.content,"html.parser")


# Agora no lugar de navegar pela árvore vamos usar métodos para percorrer a árvore.

# In[ ]:


print (soup.find_all("h1")[0].text)


# **Também podemos usar a função select

# In[ ]:


print(soup.select("p"))


# **Que tal selecionarmos todos os links disponíveis nesta pagina?

# In[ ]:


links = soup.select("a")
print(links)


# In[ ]:


#acessando um atributo
for  link in links:
    print(link['href'])


# Podemos usar a função find para encontrar a primeira ocorrencia de determinada tag.

# In[ ]:


print(soup.find("p"))

