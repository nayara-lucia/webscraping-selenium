# ⚙️ Webscraping com Selenium
O objetivo desse case é extrair os dados de todos os smartphones samsung no site da magalu e exportá-los para uma planilha do google sheets.

> Webscraping é uma técnica de coleta de dados de plataformas online, como sites, redes sociais etc.

### Tecnologias utilizadas:

![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white) 
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)

<hr>

### Etapas do Projeto:

1. Inicialização do WebDriver: Inicia-se uma instância do WebDriver do Chrome.

2. Acesso à Categoria de Celulares Samsung: Navega-se até a categoria de celulares da Samsung no site da Magazine Luiza usando o método get() do WebDriver.

3. Coleta de Produtos: Define-se uma função chamada coletar_produtos(pagina) para extrair os dados dos produtos da página atual. Dentro desta função, os produtos são coletados e seus nomes e preços são extraídos usando seletores de classe específicos.

4. Loop para Coleta de Dados: Inicia-se um loop while para coletar os dados de três páginas de produtos. Dentro do loop, os produtos da página atual são coletados usando a função coletar_produtos(). Os dados são então divididos em nomes e preços e adicionados a um DataFrame temporário. Este DataFrame temporário é então concatenado com um DataFrame principal que armazena todos os dados coletados.

5. Navegação para a Próxima Página: Dentro do loop, o WebDriver localiza e clica no botão para ir para a próxima página de produtos.

6. Integração com Google Sheets: Os dados coletados são então transferidos para uma planilha do Google Sheets usando a biblioteca gspread e a função set_with_dataframe().
   
### Resultado 🌟




https://github.com/nayara-lucia/webscraping-selenium/assets/126920974/bd4c2395-531f-4fb8-90dd-22a29e95ea90



