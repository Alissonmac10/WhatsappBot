from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time
import requests


#API 
agent = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

#CHAVE    xgLNUFtZsAbhZZaxkRh5ofM6Z0YIXwwv
api = requests.get("https://editacodigo.com.br/index/api-whatsapp/HVttpuoF4LxnGGt4JSUrxItpT0wqooqF" ,  headers=agent)
time.sleep(1)
api = api.text
api = api.split(".n.")
bolinha_notificacao = api[3].strip()
contato_cliente = api[4].strip()
caixa_msg = api[5].strip()
msg_cliente = api[6].strip()
caixa_msg2 = api[7].strip()
caixa_pesquisa = api[8].strip()




dir_path = os.getcwd()
profile_path = os.path.join(dir_path, "profile", "zap")

options = Options()
options.add_argument("--user-data-dir=" + profile_path)

driver = webdriver.Chrome(options=options)
driver.get("https://web.whatsapp.com/")
time.sleep(10)

def bot():
    try:
        
        #CAPTURAR A BOLINHA
        bolinha = driver.find_element(By.CLASS_NAME,bolinha_notificacao)
        bolinha = driver.find_elements(By.CLASS_NAME,bolinha_notificacao)
        clica_bolinha = bolinha[-1]
        acao_bolinha = webdriver.common.action_chains.ActionChains(driver)
        acao_bolinha.move_to_element_with_offset(clica_bolinha,0,-20)
        acao_bolinha.click()
        acao_bolinha.perform()
        acao_bolinha.click()
        acao_bolinha.perform()
        time.sleep(1)

        #PEGAR O TELEFONE
        telefone_cliente = driver.find_element(By.XPATH,contato_cliente)
        telefone_final = telefone_cliente.text 
        print(telefone_final)
        time.sleep(2)

        #PEGAR A MSG DO CLIENTE
        todas_as_msg = driver.find_elements(By.CLASS_NAME,msg_cliente)
        todas_as_msg_texto = [e.text for e in todas_as_msg]
        msg = todas_as_msg_texto[-1]
        print(msg)
        time.sleep(2)

        #RESPONDENDO CLIENTE
        campo_de_texto = driver.find_element(By.XPATH,caixa_msg)
        campo_de_texto.click()
        time.sleep(1)
        campo_de_texto.send_keys('ME CAGUEI TODINHO!!!!!', Keys.ENTER)


        #FECHAR CONTATO

        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()


    except:
        print("AGUARDANDO NOVAS MENSAGENS")



















while True:
    bot()

