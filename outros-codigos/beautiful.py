from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang='pt' dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Título</title>
  </head>
  <body>
	<div id= 'msg_1' class= 'mensagens'>
        <p>Meu nome é Thrawn</p>
    <div>
<div id= 'msg_2' class= 'mensagens' >
	<p>Olá meu nome é Vader</p>
	<a href="https://ufsj.edu.br">UFSJ</a>
  </body>
</html>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.text)
print("Titulo:",soup.title)
# <title>The Dormouse's story</title>
print("Tag P:",soup.p)
#print("Div",soup.div)
print(soup.find_all("div",class_='mensa'))
