from selenium.webdriver.common.by import By
import os
import random
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def pagina_desejada(vDrive, xpath_tabela):
    try:
        # Esperar até que a tabela desejada esteja presente
        WebDriverWait(vDrive, 20).until(
            EC.presence_of_element_located((By.XPATH, xpath_tabela))
        )
        return True
    except Exception as e:
        print(f"Erro ao verificar página desejada: {e}")
        return False


def criar_pasta_e_baixar(vDrive, nome_pasta):
    if not os.path.exists(nome_pasta):
        os.makedirs(nome_pasta)
    
    prefs = {"download.default_directory": os.path.abspath(nome_pasta)}
    vDrive.execute_cdp_cmd("Page.setDownloadBehavior", {"behavior": "allow", "downloadPath": os.path.abspath(nome_pasta)})

    botoes_download = vDrive.find_elements(By.XPATH, 'XPATH_DOS_BOTOES_DE_DOWNLOAD')
    for botao in botoes_download:
        botao.click()
        time.sleep(random.uniform(1, 3))
