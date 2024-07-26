import logging

# Configuração básica do logger
logging.basicConfig(level=logging.DEBUG, filename='my_app.log', filemode='w')
logger = logging.getLogger(__name__)

# Configuração do manipulador para exibir logs no console
console_handler = logging.StreamHandler()

# Configurando niveis de log
console_handler.setLevel(logging.DEBUG)  # Exibir todos os níveis de log

# Formatando os logs
formatter = logging.Formatter('Robo de automação eCAC: %(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# utilize no codigo: 
    # logger.debug('')
    # logger.inf('')
    # logger.error('')