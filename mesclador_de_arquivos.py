import os
import pandas as pd
import warnings
from tkinter.filedialog import askdirectory

warnings.simplefilter("ignore")
lista = []

#CRIA UMA JANELA DE DIALOGO PARA SELECIONAR O DIRETÓRIO E SALVA O SEU CAMINHO NA VARIAVEL 
caminho = askdirectory(title='Escolha o diretório')

#LISTA TODOS OS ARQUIVOS QUE ESTÃO NO DIRETORIO INDICADO
lista_de_arquivo = os.listdir(caminho)

#LAÇO PARA IDENTIFICAR OS ARQUIVOS E ADICIONALOS NA LISTA, UTILIZANDO PANDAS PARA LER OS ARQUIVOS
for file in lista_de_arquivo:
   if file.endswith('.xlsx'):
       lista.append(pd.read_excel(file))


#CONCATENANDO OS ARQUIVOS E GERANDO O ARQUIVO .csv
dado = pd.concat(lista)
dado.to_csv('caminho.csv')
