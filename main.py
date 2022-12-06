
import requests
from bs4 import BeautifulSoup
import pandas as pd

listanome = []
listapreco = []



abaUm = requests.get('http://127.0.0.1:5500/lima_aula5/lima_aula5/index.html')
soup = BeautifulSoup(abaUm.content, 'html.parser')

nome = soup.find_all("p")
prec = soup.find_all("h3")

print(nome)
for c in nome:
    c = c.text
    listanome.append(c)

for c in prec:
    c = c.text
    listapreco.append(c)

listalegal = {"Tenis": listanome, "Preço": listapreco}
plam = pd.DataFrame(listalegal)



plam.to_excel("pi.xls")



