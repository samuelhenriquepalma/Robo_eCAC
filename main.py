from user_interface import obterDadosDoUsuario, exibirMenu
from browser import inicializarChrome
from logger_config import logger

if __name__ == "__main__":
    # json_cookies, cnpj = obterDadosDoUsuario()
    urlDownload = "C:\\path\\to\\downloads"  # Ajuste conforme necessário

    json_cookies = '''
[
{
    "domain": ".sso.acesso.gov.br",
    "expirationDate": 1753492051,
    "hostOnly": false,
    "httpOnly": false,
    "name": "Govbrid",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": true,
    "session": false,
    "storeId": "0",
    "value": "be041e2e-eb0f-4bab-a722-906fc27346dc",
    "id": 1
},
{
    "domain": ".sso.acesso.gov.br",
    "hostOnly": false,
    "httpOnly": true,
    "name": "INGRESSCOOKIE",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": true,
    "session": true,
    "storeId": "0",
    "value": "2859780680a91241",
    "id": 2
},
{
    "domain": ".sso.acesso.gov.br",
    "hostOnly": false,
    "httpOnly": true,
    "name": "Session_Gov_Br_Prod",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": true,
    "session": true,
    "storeId": "0",
    "value": "-uK58VebxJpokt2TvTfXiY0F75bU9isrTNWs4wNN.scp-7695d5b4dd-jckl2",
    "id": 3
},
{
    "domain": ".sso.acesso.gov.br",
    "hostOnly": false,
    "httpOnly": false,
    "name": "TS01ecd73c",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "01fef04d4e161ec9fdeb405f6d3f8c9e5e2ca10b5c1fef78a3daa278910780e247511cd3129af9aeace1f892f62d95895a5bdd1a9e810c4720cb06fd21759c0879e98fec7a361f3028ef335484a25ca796ef734d62d240e15900e842d0546d193b13059ab6",
    "id": 4
},
{
    "domain": "sso.acesso.gov.br",
    "hostOnly": true,
    "httpOnly": false,
    "name": "Third-Party-Cookie-Support-Test",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": true,
    "session": true,
    "storeId": "0",
    "value": "true",
    "id": 5
}
]
'''
    cnpj = '02129949000111'

    #inicialização do browser.py
    vDrive = inicializarChrome(json_cookies, urlDownload, cnpj)
    
    # inicialização do menu em user_interface
    exibirMenu(vDrive)
