# Web Scraper de Notícias de Futebol
 Este repositório contém um scrip de web scraping para coletar links de notícias de três clubes de
 futebol: São Paulo, Corinthians e Palmeiras, diretamente do site Globo Esporte. As informações coletadas são armazenadas
 em um banco de dados PostgreSQL para posterior análise ou processamento.

 # O que está incluído neste repositório
  - Script principal: um script em python que utiliza biblioteca selenium para navegar no site,
    coletar links de notícias dos clubes e salvar essas informações no banco de dados.
  - Banco de dados PostgreSQL: O código cria automaticamente a tabela notícias no banco de dados para armazenar os dados
    das notícias, incluindo o clube, o link da notícia e a data da publicação
  - Instalação automática do driver do Edge: a biblioteca webdriver_manager é utilizada para gerenciar o driver
    do Microsoft Edge
  ### Módulos utilizados:
     - selenium: para automação da navegação na web e coleta de dados.
     - psycopg2: para integração com o banco de dados PostreSQL.
     - datetime: para registrar a data e hora da coleta das notícias.

 # Instalação
 ### Requisitos
   - Python 3.x
   - PostgreSQL configurado e rodando no seu sistema(ou use um serviço de banco de dados remoto).

### Passos para instalação

   - Clone o repositório
   - Navegue até o repostorio: cd Web_Scraping
   - Instale as dependências : pip install -r requirements.txt
   - Execute o script: pyhton scraper.py

   
 
