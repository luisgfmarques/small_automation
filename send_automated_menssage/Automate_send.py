import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import urllib
from math import *
df_Contatos = pd.read_csv('book.csv')
df_Contatos
contatos = df_Contatos[(df_Contatos['Numero de Telefone'].notna())]
contatos = contatos.reset_index()
contatos.pop('index')
for i in range(len(contatos)):
    numero = str(contatos.loc[i][0])
    numero = numero.replace('(','')
    numero = numero.replace(')','')
    numero = numero.replace('.','')
    numero = numero.replace(' ','')
    numero = numero.replace('-','')
    if(len(numero)== 10):
        number_list = list(numero)
        number_list.insert(2,"9")
        numero = ''.join(map(str,number_list))
    if(len(numero) != 11):
        print(f"O numero do contado {contatos.loc[i][1]} com ID numero {i} esta com erro {numero}.")
    else:
        contatos.loc[i][0] = ("+55" + numero)
    contatos.loc[i][1] = (contatos.loc[i][1].title())
file = open("mensage.txt")
Mensagem = file.read()
contatos['Mensagem'] = ' '
contatos['Link'] = ' '
for i in range(len(contatos)):
    Nome = contatos.loc[i][1]
    contatos.loc[i][2] = (Mensagem.format(Nome))
    texto = urllib.parse.quote(contatos.loc[i][2])
    contatos.loc[i][3] = f"https://web.whatsapp.com/send?phone=55{contatos.loc[i][0]}&text={texto}"
browser = webdriver.Safari()
try:
    for i in range(len(contatos)):
        browser.get(contatos.loc[i][3])
        while len(browser.find_elements(by=By.ID , value="side")) < 1:
            time.sleep(1)
        browser.implicitly_wait(30)
        browser.find_element(by=By.XPATH, value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ESCAPE)
        browser.find_element(by=By.XPATH, value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ENTER)
        time.sleep(2)
        print(f"enviado para o contado numero {i} -- {contatos.loc[i][1]}")
    browser.quit()
    print("Convites Enviados Corretamente")
except:
    print("Ocorreu algum erro de execucao e nem todos os convites foram enviados, por gentileza tente novamente ")
