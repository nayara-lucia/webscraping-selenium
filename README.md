# ⚙️ Webscraping com Selenium
O objetivo desse case é extrair os dados de todos os itens da primeira página da categoria de Consoles no site da Magalu e exporta-los para uma planilha do Excel.

> Webscraping é uma técnica de coleta de dados de plataformas online, como sites, redes sociais etc.

### Tecnologias utilizadas:

![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white) 
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)

<hr>

### Etapas do Projeto:

1- Abrir o Chrome e direcionar p/ o site da Magalu

2- No search com <strong>Pyautogui</strong> procurar por console e dar "enter"

3- Identificar a class name das caixinhas de produto inspencionando a página

3- Para cada caixinha de produto identificar sua class name e extrair nome, preco e url

4- Armazenar os dados em um Dataframe

5- Criar um arquivo Excel com a engine <strong>xlsxwriter</strong>

6- Pegar os dados armazenados no Dataframe e armazenar na planilha criada

7- Salvar

<strong>BONUS</strong>: Na planilha Excel editar os delimitadores
### Resultado 🌟




https://github.com/nayara-lucia/webscraping-selenium/assets/126920974/bd4c2395-531f-4fb8-90dd-22a29e95ea90



