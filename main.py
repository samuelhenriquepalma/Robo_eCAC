# from user_interface import obterDadosDoUsuario, exibirMenu
# from browser import inicializarChrome
from logger_config import logger
from interface import App

if __name__ == "__main__":
    app = App()
    app.mainloop()
#     json_cookies, cnpj = obterDadosDoUsuario()
#     urlDownload = "C:\\path\\to\\downloads"  # Ajuste conforme necessário

#     json_cookies = '''
# [
# {
#     "domain": ".sso.acesso.gov.br",
#     "expirationDate": 1753492051,
#     "hostOnly": false,
#     "httpOnly": false,
#     "name": "Govbrid",
#     "path": "/",
#     "sameSite": "no_restriction",
#     "secure": true,
#     "session": false,
#     "storeId": "0",
#     "value": "be041e2e-eb0f-4bab-a722-906fc27346dc",
#     "id": 1
# },
# {
#     "domain": ".sso.acesso.gov.br",
#     "hostOnly": false,
#     "httpOnly": true,
#     "name": "INGRESSCOOKIE",
#     "path": "/",
#     "sameSite": "no_restriction",
#     "secure": true,
#     "session": true,
#     "storeId": "0",
#     "value": "5306c1e670cbf319",
#     "id": 2
# },
# {
#     "domain": ".sso.acesso.gov.br",
#     "hostOnly": false,
#     "httpOnly": true,
#     "name": "Session_Gov_Br_Prod",
#     "path": "/",
#     "sameSite": "no_restriction",
#     "secure": true,
#     "session": true,
#     "storeId": "0",
#     "value": "ySQxwoRXb2949Z6t8TKsZ8g7PSHdAxFyEz_rVTJ6.scp-7695d5b4dd-rhfrq",
#     "id": 3
# },
# {
#     "domain": ".sso.acesso.gov.br",
#     "hostOnly": false,
#     "httpOnly": false,
#     "name": "TS01ecd73c",
#     "path": "/",
#     "sameSite": "unspecified",
#     "secure": false,
#     "session": true,
#     "storeId": "0",
#     "value": "01fef04d4ec37505aa38b5e52bfe0b80ddd82a406faeab9a60e295c3daeff5e3f98ac50bd36e79135d8fa1616781faffb3684d6dc2bd841cb85b97fe0b7c707872de5166a09d9d69b0491bb7f33222046b0409759b8210adb74bb21c1dd99ad2c66af52374",
#     "id": 4
# },
# {
#     "domain": "sso.acesso.gov.br",
#     "hostOnly": true,
#     "httpOnly": false,
#     "name": "Third-Party-Cookie-Support-Test",
#     "path": "/",
#     "sameSite": "no_restriction",
#     "secure": true,
#     "session": true,
#     "storeId": "0",
#     "value": "true",
#     "id": 5
# }
# ]
# '''
#     cnpj = '02129949000111'

# inicialização do browser.py
# vDrive = inicializarChrome(json_cookies, urlDownload, cnpj)
    
# inicialização do menu em user_interface
# exibirMenu(vDrive)
