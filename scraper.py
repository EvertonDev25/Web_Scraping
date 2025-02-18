from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import psycopg2
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

def insert_into_db(clube, noticia, data_publicacao):
    try:
        conexao = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="senha",
            database="postgres"
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

##CONFIGURAÇÃO DO DRIVE PARA O GOOGLE CHROME
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://ge.globo.com/")
driver.maximize_window()
sleep(2)

def coletar_links_sp():
    driver.find_element(By.CLASS_NAME, "icons-escudo-header").click()
    sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/header/div[2]/div/div/span/div[2]/div[1]/div/div[17]/a").click()
    sleep(1)

    for i in range(1, 3):  # Pegando os 2 primeiros links de São Paulo
        link_element = driver.find_element(By.XPATH, "/html/body/div[2]/main[3]/div[2]/div/div/div/div/div[{0}]/div/a".format(i))
        link = link_element.get_attribute("href")
        print("São Paulo - Link {}: {}".format(i, link))

        data_publicacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        insert_into_db("São Paulo", link, data_publicacao)


def coletar_links_corinthians():
    driver.find_element(By.CLASS_NAME, "icons-escudo-header").click()
    sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/header/div[2]/div/div/span/span[2]/div[2]/div[1]/div/div[6]/a/img").click()
    sleep(1)

    for i in range(1, 3):
        link_element = driver.find_element(By.XPATH, "/html/body/div[2]/main[3]/div[2]/div/div/div/div/div[{0}]/div/a".format(i))
        link = link_element.get_attribute("href")
        print("Corinthians - Link {}: {}".format(i, link))

        data_publicacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        insert_into_db("Corinthians", link, data_publicacao)


def coletar_links_palmeiras():
    driver.find_element(By.CLASS_NAME, "icons-escudo-header").click()
    sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/header/div[2]/div/div/span/span[2]/div[2]/div[1]/div/div[15]/a/img").click()
    sleep(1)

    for i in range(1, 3):
        link_element = driver.find_element(By.XPATH, "/html/body/div[2]/main[3]/div[2]/div/div/div/div/div[{0}]/div/a".format(i))
        link = link_element.get_attribute("href")
        print("Palmeiras - Link {}: {}".format(i, link))

        data_publicacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        insert_into_db("Palmeiras", link, data_publicacao)


coletar_links_sp()
coletar_links_corinthians()
coletar_links_palmeiras()

driver.quit()
