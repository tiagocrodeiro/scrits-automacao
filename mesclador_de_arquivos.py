import os
import pandas as pd
import warnings
from tkinter.filedialog import askdirectory

warnings.simplefilter("ignore")
caminho = askdirectory(title='Escolha o diretório')

lista_de_arquivo = os.listdir(caminho)

lista = []
#print(lista_de_arquivo)
for file in lista_de_arquivo:
   if file.endswith('.xlsx'):
       lista.append(pd.read_excel(file))



dado = pd.concat(lista)
dado.to_csv('caminho')