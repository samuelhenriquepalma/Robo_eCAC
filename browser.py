from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json
import time
import random

def inicializarChrome(json_cookies, urlDownload, cnpj):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36"
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--enable-javascript")
    options.add_argument("accept-cookies")
    options.add_argument(f"user-agent={user_agent}")
    options.add_experimental_option("prefs", {
        "download.default_directory": r"" + urlDownload,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

    vDrive = webdriver.Chrome(options=options)
    vDrive.implicitly_wait(1.5)

    vDrive.get("https://sso.acesso.gov.br/login?client_id=portal-logado.estaleiro.serpro.gov.br")
    #time.sleep(random.uniform(3, 5))

    vDrive.delete_all_cookies()
    #time.sleep(random.uniform(2, 4))

    data = json.loads(json_cookies)
    for cookie in data:
        vDrive.add_cookie({
            "name": cookie['name'],
            "value": cookie['value'],
            "domain": ".acesso.gov.br"
        })

    vDrive.get("https://cav.receita.fazenda.gov.br/ecac/")
    vDrive.find_element(By.XPATH, '//*[@id="login-dados-certificado"]/p[2]/input').click()
    vDrive.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(random.uniform(1, 2))

    vDrive.find_element(By.XPATH, '//*[@id="btnPerfil"]/span').click()
    time.sleep(random.uniform(0.5, 2))

    vDrive.find_element(By.XPATH, '//*[@id="txtNIPapel2"]').send_keys(cnpj)
    time.sleep(random.uniform(0.5, 2))

    vDrive.find_element(By.XPATH, '//*[@id="formPJ"]/input[4]').click()
    time.sleep(2)

    vDrive.get("https://www3.cav.receita.fazenda.gov.br/reinfweb/#/2020/lista")
    return vDrive
