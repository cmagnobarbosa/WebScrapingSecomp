
# coding: utf-8

# In[ ]:


from bs4 import BeautifulSoup
import requests


# In[ ]:


site=requests.get("https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:Comunicado_sobre_o_Museu_Nacional")


# In[ ]:


soup=BeautifulSoup(site.content,"html.parser")


# In[ ]:


tags_p=soup.findAll("p")
print(tags_p[0].text)


# In[ ]:


print tags_p[1].text


# Agora vamos combinar o find para encontrar uma id especifica.

# In[ ]:


more_info= soup.find(id="Mais_informações")
print more_info

