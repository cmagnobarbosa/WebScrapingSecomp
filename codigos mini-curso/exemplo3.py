
# coding: utf-8

# Coletando os dados dos professores do dcomp.
# Lembre-se de usar o inspecionar elementos...

# In[1]:



import requests
from bs4 import BeautifulSoup


# In[2]:


site= requests.get("http://dcomp.ufsj.edu.br/pessoas/professores/")


# In[3]:


print(site.encoding)


# In[4]:


soup=BeautifulSoup(site.text,"lxml")


# Aqui foi usado algo novo... combinamos o findAll com uma pesquisa personalizada por uma determinada classe.

# In[5]:


corpo=soup.find_all("div",{"class":"profile-entry"})
print("Total de Professores:",len(corpo))


# In[ ]:


print(corpo)


# Agora vamos melhorar a visualização.

# In[11]:


for i in corpo:
    print "Professor:",i.h1.text
    print "Área de pesquisa:",i.findAll("p")[2].text
    print "Lattes:",i.findAll("a")[-1]['href']
    print("-------")

