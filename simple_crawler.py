#coding: utf-8

import requests
from bs4 import BeautifulSoup
"""
Apresenta os recursos basicos do BeautifulSoup
"""


# requisicao basica
site= requests.get("http://example.com")
#retorno do codigo 200, indicando que o conteúdo foi coletado.
print("Status:",site.status_code)
print("Encoding:",site.encogit
