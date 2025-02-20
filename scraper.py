import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import psycopg2
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from datetime import datetime

def create_table_if_not_exists():
    try:
        db_host = os.getenv('DB_HOST')
        db_user = os.getenv('DB_USER')
        db_password = os.getenv('DB_PASSWORD')
        db_name = os.getenv('DB_NAME')

        conexao = psycopg2.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )
        cursor = conexao.cursor()
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS noticias (
            id SERIAL PRIMARY KEY,
            clube VARCHAR(50) NOT NULL,
            noticias TEXT NOT NULL,
            data_publicacao TIMESTAMP NOT NULL
        );
        '''
        cursor.execute(create_table_query)
        conexao.commit()
        cursor.close()
        conexao.close()
        print("Tabela 'noticias' verificada/criada com sucesso!")
    except psycopg2.Error as err:
        print("Erro ao criar/verificar a tabela: {}".format(err))

def insert_into_db(clube, noticia, data_publicacao):
    try:

        db_host = os.getenv('DB_HOST')
        db_user = os.getenv('DB_USER')
        db_password = os.getenv('DB_PASSWORD')
        db_name = os.getenv('DB_NAME')

        conexao = psycopg2.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )
        cursor = conexao.cursor()
        query = "INSERT INTO noticias (clube, noticias, data_publicacao) VALUES (%s, %s, %s)"
        cursor.execute(query, (clube, noticia, data_publicacao))
        conexao.commit()
        cursor.close()
        conexao.close()
        print("Notícia do {} inserida com sucesso!".format(clube))
    except psycopg2.Error as err:
        print("Erro ao inserir dados no banco de dados: {}".format(err))

edge_options = webdriver.EdgeOptions()
edge_options.add_argument('--headless')
edge_options.add_argument('--no-sandbox')
edge_options.add_argument('--disable-dev-shm-usage')
edge_options.add_argument('--disable-gpu')
edge_options.add_argument('--window-size=1920x1080')

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()),options=edge_options)
driver.get("https://ge.globo.com/")
driver.maximize_window()
sleep(2)

def coletar_links_sp():
    driver.find_element(By.CLASS_NAME, "icons-escudo-header").click()
    sleep(2)
    driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/header/div[2]/div/div/span/div[2]/div[1]/div/div[17]/a").click()
    sleep(2)

    for i in range(1, 3):
        link_element = driver.find_element(By.XPATH, "/html/body/div[2]/main[3]/div[2]/div/div/div/div/div[{0}]/div/a".format(i))
        link = link_element.get_attribute("href")
        print("São Paulo - Link {}: {}".format(i, link))

        data_publicacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        insert_into_db("São Paulo", link, data_publicacao)


def coletar_links_corinthians():
    driver.find_element(By.CLASS_NAME, "icons-escudo-header").click()
    sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/header/div[2]/div/div/span/span[2]/div[2]/div[1]/div/div[6]/a/img").click()
    sleep(2)

    for i in range(1, 3):
        link_element = driver.find_element(By.XPATH, "/html/body/div[2]/main[3]/div[2]/div/div/div/div/div[{0}]/div/a".format(i))
        link = link_element.get_attribute("href")
        print("Corinthians - Link {}: {}".format(i, link))

        data_publicacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        insert_into_db("Corinthians", link, data_publicacao)


def coletar_links_palmeiras():
    driver.find_element(By.CLASS_NAME, "icons-escudo-header").click()
    sleep(2)
    driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/header/div[2]/div/div/span/span[2]/div[2]/div[1]/div/div[15]/a/img").click()
    sleep(2)

    for i in range(1,2):
        link_element = driver.find_element(By.XPATH, "/html/body/div[2]/main[3]/div[2]/div/div/div/div/div[{0}]/div/a".format(i))
        link = link_element.get_attribute("href")
        print("Palmeiras - Link {}: {}".format(i, link))

        data_publicacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        insert_into_db("Palmeiras", link, data_publicacao)

        driver.quit()

create_table_if_not_exists()
coletar_links_sp()
coletar_links_corinthians()
coletar_links_palmeiras()
