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
    "value": "4f3cf45260304f9d",
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
    "value": "EfErmCGTn1pggsg16mf8DHrKpy0glXVAHl7j4pzr.scp-7695d5b4dd-8rp8b",
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
    "value": "01fef04d4e418d1d25af855a4f2f8e120ac43fe0c73b3113f7c10e20fb2d09e6384eaf138a79b0142c7f04435b385869f28ea56fcf593002e2ed5bf0d9601f34accc1a74cfcab863e878abff666c956c08f37d7dedf1777190f8c96e79d0324b7ac8df8b90",
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
