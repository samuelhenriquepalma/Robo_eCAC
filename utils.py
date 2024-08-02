from selenium.webdriver.common.by import By
import os
import random
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

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

def gerar_intervalo_datas(data_inicio, data_fim):
    """
    Gera uma lista de strings no formato MM/YYYY representando todos os meses dentro do intervalo de datas fornecido.
    """
    inicio = datetime.strptime(data_inicio, "%m/%Y")
    fim = datetime.strptime(data_fim, "%m/%Y")
    intervalo = []

    #print(f'inicio: {inicio}, fim: {fim}')

    while inicio <= fim:
        intervalo.append(inicio.strftime("%m/%Y"))
        # Avançar para o próximo mês
        if inicio.month == 12:
            inicio = inicio.replace(year=inicio.year + 1, month=1)
        else:
            inicio = inicio.replace(month=inicio.month + 1)

    #print(f'intervalo: {intervalo}')

    return intervalo

