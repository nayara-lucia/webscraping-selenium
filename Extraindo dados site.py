from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui as pa
import pandas as pd

navegador = webdriver.Chrome()


navegador.get("https://www.magazineluiza.com.br") # Abre o site

navegador.find_element(By.ID, "input-search").send_keys("console") # Procura

pa.sleep(2)
pa.press("enter")
pa.sleep(10)


listaProdutos = navegador.find_elements(By.CLASS_NAME, "eJDyHN")

df_lista = []

for item in listaProdutos:

    nomeProduto = ""
    precoProduto = ""
    urlProduto = ""

    if nomeProduto == "":

        try:
            nomeProduto = item.find_element(By.CLASS_NAME, "uaEbk").text

        except Exception:
            pass
 #---------------------------------------------------------------------------------
    if precoProduto == "":

        try:
            precoProduto = item.find_element(By.CLASS_NAME, "kXWuGr").text

        except Exception:
            pass
# ---------------------------------------------------------------------------------
    if urlProduto == "":

        try:
            urlProduto = item.find_element(By.TAG_NAME, "a").get_attribute("href")

        except Exception:
            pass
# ---------------------------------------------------------------------------------

    print(nomeProduto, precoProduto, urlProduto)

    dadosLinha = nomeProduto + ";" + precoProduto + ";" + urlProduto
    df_lista.append(dadosLinha) # Populando o DF


# Cria a planilha e Prepara o arquivo do Excel usando xlsxwriter com mecanismo
arquivoExcel = pd.ExcelWriter('consoles_magazine.xlsx', engine='xlsxwriter')

# Puxando os dados pra planilha
planilha_dados = pd.DataFrame(df_lista, columns=['Nome;Preco;URL'])

# Joga nossos dados dentro do Arquivo excel criado e salva
planilha_dados.to_excel(arquivoExcel,sheet_name='Sheet1', index=False)

arquivoExcel.close() #Salva os dados no arquivos




