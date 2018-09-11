
# coding: utf-8

# **O seu primeiro crawler.**

# In[2]:


import requests


# In[1]:


from bs4 import BeautifulSoup


# In[ ]:


#Requisição usando o request.
site= requests.get("http://example.com")


# In[ ]:


# se estiver tudo ok, você verá o código 200.
print(site.status_code)


# In[ ]:


#imprime a codificação.
print(site.encoding)


# In[ ]:


# O conteúdo da pagina.
print(site.content)


# In[ ]:


soup=BeautifulSoup(site.content,"html.parser")


# **Navegando pelas tags**

# In[ ]:


# titulo dentro da tag had
print(soup.head.title)


# In[ ]:


#Acessando o texto em h1
print(soup.div.h1.text)

