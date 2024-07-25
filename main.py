from user_interface import obterDadosDoUsuario, exibirMenu
from browser import inicializarChrome

if __name__ == "__main__":
    # json_cookies, cnpj = obterDadosDoUsuario()
    urlDownload = "C:\\path\\to\\downloads"  # Ajuste conforme necessário

    json_cookies = '''
[
{
    "domain": ".sso.acesso.gov.br",
    "expirationDate": 1751323671.616482,
    "hostOnly": false,
    "httpOnly": true,
    "name": "Govbrid",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": true,
    "session": false,
    "storeId": "0",
    "value": "dd1a0d07-8772-46d9-a4b9-c329422ee6ff",
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
    "value": "ee053434b6582505",
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
    "value": "Nr63WWFbXqpprRYLQUKeAmEijG2stlhOdyIoalhy.scp-7695d5b4dd-c4tvt",
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
    "value": "01fef04d4e2fb0d5138a1290411cecdc2b31309df33d2a0386c0aa51d4a41adf4606a7f52cf5dcf9d6096bcbaa17be21c235f55c47f022edaa749f01de638e4d85ca298e061f420475c8bd244c117e01b4fbfb23da16973a4faf9989267b223ace85348953",
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
    cnpj = '33285255000105'

    vDrive = inicializarChrome(json_cookies, urlDownload, cnpj)
    
    # Exibir a moldura com o navegador e botões
    exibirMenu(vDrive)
