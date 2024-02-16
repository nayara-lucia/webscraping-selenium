from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui as pa
import pandas as pd
from selenium.webdriver.common.by import By
import gspread
from gspread_dataframe import set_with_dataframe

navegador = webdriver.Chrome()
#Entra na categoria celulares da samsung
navegador.get("https://www.magazineluiza.com.br/smartphone/celulares-e-smartphones/s/te/tcsp/brand---samsung/")
# Abre o site
pagina = navegador.current_url

pa.sleep(4) # Carrega pagina

def coletar_produtos(pagina):

    lista_produtos = navegador.find_elements(By.CLASS_NAME, "#")
    df_lista = []

    for item in lista_produtos:
        nome_produto = ""
        preco_produto = ""
        url_produto = ""

        try:
            nome_produto = item.find_element(By.CLASS_NAME, "#").text
        except Exception:
            pass

        try:
            preco_produto = item.find_element(By.CLASS_NAME, "#").text
        except Exception:
            pass

        dados_linha = f"{nome_produto};{preco_produto}"
        print(dados_linha)
        df_lista.append(dados_linha)

    return df_lista


cont = 0
df = pd.DataFrame(columns=['Produto', 'Preço'])
while cont < 3:
    # Coleta os produtos da página atual
    produtos_pagina_atual = coletar_produtos(pagina)
    produtos = []
    precos = []

    for item in produtos_pagina_atual:
        produto, preco = item.split(';')
        produtos.append(produto)
        precos.append(preco)

    df_temporario = pd.DataFrame({'Produto': produtos, 'Preço': precos})

    # Adiciona os dados do DataFrame temporário ao DataFrame principal
    df = pd.concat([df, df_temporario], ignore_index=True)

    # Verifica se há uma próxima página
    try:
        proxima_pagina = navegador.find_element(By.CLASS_NAME, '#')
        proxima_pagina.click()
        pa.sleep(4)
        cont += 1
    except:
        # Se não houver mais páginas, saia do loop
        break


# Planilha
from senha import code_
CODE = code_

gc = gspread.service_account(filename='#.json')
sh = gc.open_by_key(CODE)

DICT = {}
WSS = sh.worksheets()

set_with_dataframe(worksheet=WSS[0], dataframe=df, include_index=False,
                    include_column_header=True, resize=True)



