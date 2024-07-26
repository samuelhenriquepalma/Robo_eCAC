from selenium.webdriver.common.by import By
import random
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import os
from selenium.webdriver.common.keys import Keys
from logger_config import logger


# Lista de XPaths para ações sequenciais
lista_xpath = [
    '/html/body/app-root/div/div[3]/app-evento2020-lista-pesquisa/fieldset[2]/div/table/tr[2]/td[7]/button[1]',
    '/html/body/app-root/div/div[3]/app-evento2020-lista-pesquisa/fieldset[2]/div/table/tr[3]/td[7]/button[1]',
    '/html/body/app-root/div/div[3]/app-evento2020-lista-pesquisa/fieldset[2]/div/table/tr[4]/td[7]/button[1]',
    '/html/body/app-root/div/div[3]/app-evento2020-lista-pesquisa/fieldset[2]/div/table/tr[5]/td[7]/button[1]',
    '/html/body/app-root/div/div[3]/app-evento2020-lista-pesquisa/fieldset[2]/div/table/tr[6]/td[7]/button[1]',
    '/html/body/app-root/div/div[3]/app-evento2020-lista-pesquisa/fieldset[2]/div/table/tr[7]/td[7]/button[1]',
    '/html/body/app-root/div/div[3]/app-evento2020-lista-pesquisa/fieldset[2]/div/table/tr[8]/td[7]/button[1]',
    '/html/body/app-root/div/div[3]/app-evento2020-lista-pesquisa/fieldset[2]/div/table/tr[9]/td[7]/button[1]',
    '/html/body/app-root/div/div[3]/app-evento2020-lista-pesquisa/fieldset[2]/div/table/tr[10]/td[7]/button[1]',
    '/html/body/app-root/div/div[3]/app-evento2020-lista-pesquisa/fieldset[2]/div/table/tr[11]/td[7]/button[1]',
    '/html/body/app-root/div/div[3]/app-evento2020-lista-pesquisa/fieldset[2]/div/table/tr[12]/td[7]/button[1]'
]

def verificar_arquivo_download(path_pasta, timeout=30):
    """
    Verifica a presença de um novo arquivo na pasta de downloads.
    """
    tempo_inicial = time.time()
    arquivos_iniciais = set(os.listdir(path_pasta))

    while time.time() - tempo_inicial < timeout:
        arquivos_atuais = set(os.listdir(path_pasta))
        novos_arquivos = arquivos_atuais - arquivos_iniciais

        if novos_arquivos:
            return True

        time.sleep(0.3)

    return False

def executar_acoes_sequenciais(vDrive, pasta_downloads):
    pagina_atual = 1

    while True:
        for xpath in lista_xpath:
            try:
                btn = vDrive.find_element(By.XPATH, xpath)  # Seleciona o evento
                btn.click()
                logger.info('Abrindo o Evento...')
                time.sleep(0.3)  # Espera aleatória entre as ações
                
                tentativas = 0
                download_sucesso = False

                while tentativas < 3:
                    # Fazer o download do XML
                    btn_download = vDrive.find_element(By.XPATH, '/html/body/app-root/div/div[3]/app-evento2020-formulario/app-reinf-versao-leiaute/form/app-reinf-botoes-formulario/div/div/button[2]')
                    btn_download.click()
                    logger.info(f'Tentando download... tentativa: {tentativas + 1}')
                    
                    # Verifica se o arquivo foi baixado
                    if verificar_arquivo_download(pasta_downloads):
                        download_sucesso = True
                        break
                    
                    tentativas += 1
                    time.sleep(0.2)

                if not download_sucesso:
                    logger.error('Erro: Não foi possível realizar o download após 3 tentativas.')
                    continue
                
                logger.info('Download Concluido!!!')
                time.sleep(0.2)  # Espera aleatória entre as ações

                btn_voltar = vDrive.find_element(By.XPATH, '/html/body/app-root/div/div[3]/app-evento2020-formulario/app-reinf-versao-leiaute/form/app-reinf-botoes-formulario/div/div/button[1]')  # Volta à tabela de eventos
                btn_voltar.click()
                logger.info('Retornando à tabela de eventos...')
                time.sleep(0.2)  # Espera aleatória entre as ações

                # Clicar no botão "próxima página" até chegar na página atual
                for _ in range(pagina_atual - 1):
                    nextPage = vDrive.find_element(By.CSS_SELECTOR, 'li[class="pagination-next"] a:nth-child(1)')  # Vai para a próxima página
                    nextPage.click()

            except NoSuchElementException:
                try:
                    nextPage = vDrive.find_element(By.CSS_SELECTOR, 'li[class="pagination-next"] a:nth-child(1)')  # Vai para a próxima página
                    nextPage.click()
                    pagina_atual += 1  # Incrementa a página atual
                    logger.info('Próxima Página...')
                    time.sleep(0.3)  # Espera aleatória entre as ações

                except NoSuchElementException:
                    logger.info("Não há mais eventos.")
                    return

            

def verificar_paginas_e_baixar(vDrive):
    while True:
        try:
            botao_proxima_pagina = vDrive.find_element(By.XPATH, 'XPATH_DO_BOTAO_PROXIMA_PAGINA')
            baixar_arquivos(vDrive)
            botao_proxima_pagina.click()
            time.sleep(random.uniform(1, 3))
        except Exception as e:
            logger.error(f"Erro ao verificar ou mudar de página: {e}")
            break

def baixar_arquivos(vDrive):
    botoes_download = vDrive.find_elements(By.XPATH, 'XPATH_DOS_BOTOES_DE_DOWNLOAD')
    for botao in botoes_download:
        try:
            botao.click()
            time.sleep(random.uniform(1, 3))
        except Exception as e:
            logger.error(f"Erro ao baixar arquivo: {e}")
