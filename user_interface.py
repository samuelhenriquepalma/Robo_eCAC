import time
import tkinter as tk
from actions import executar_acoes_sequenciais, verificar_paginas_e_baixar
import json
from tkinter import messagebox
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from logger_config import logger
from utils import gerar_intervalo_datas



def obterDadosDoUsuario():
    def on_submit():
        cookies_part = cookies_entry.get("1.0", tk.END).strip()
        cnpj_part = cnpj_entry.get().strip()
        cnpj_part = cnpj_part.replace('.','')
        cnpj_part = cnpj_part.replace('-','')
        cnpj_part = cnpj_part.replace('/','')

        try:
            cookies = json.loads(cookies_part)

            govbrid = next(item['value'] for item in cookies if item['name'] == 'Govbrid')
            ingresscookie = next(item['value'] for item in cookies if item['name'] == 'INGRESSCOOKIE')
            session_gov_br_prod = next(item['value'] for item in cookies if item['name'] == 'Session_Gov_Br_Prod')

            json_cookies = json.dumps([
                {"name": "Govbrid", "value": govbrid},
                {"name": "INGRESSCOOKIE", "value": ingresscookie},
                {"name": "Session_Gov_Br_Prod", "value": session_gov_br_prod}
            ])

            if not cnpj_part:
                raise ValueError("CNPJ não pode estar vazio!")
            
            messagebox.showinfo("Sucesso", "Cookies e CNPJ atualizados com sucesso!")
            root.result = (json_cookies, cnpj_part)
            root.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao processar os dados: {e}")
            root.result = (None, None)

    root = tk.Tk()
    root.title("Entrada de Dados")

    tk.Label(root, text="Cole o JSON dos cookies:").pack(pady=(10, 0))
    cookies_entry = tk.Text(root, height=10, width=50)
    cookies_entry.pack(pady=(0, 10))

    tk.Label(root, text="Digite o CNPJ da empresa:").pack(pady=(10, 0))
    cnpj_entry = tk.Entry(root, width=50)
    cnpj_entry.pack(pady=(0, 10))

    submit_button = tk.Button(root, text="Enviar", command=on_submit)
    submit_button.pack(pady=(10, 20))

    root.result = (None, None)
    root.mainloop()
    return root.result

def exibirMenu(vDrive):
    logger.info('iniciando menu de ações...')

    def iniciarDownload():
        data_inicio = data_inicio_entry.get().strip()
        data_fim = data_fim_entry.get().strip()

        if not data_inicio or not data_fim:
            messagebox.showerror("Erro", "Por favor, preencha as datas de início e fim.")
            return

        intervalo_datas = gerar_intervalo_datas(data_inicio, data_fim)
        pasta_downloads = r"C:\path\to\downloads"  # Ajuste conforme necessário

        # print(f'intervalor datas: {intervalo_datas}')
        for data in intervalo_datas:
            data_inicio, data_fim = data, data

            # Preencher os campos de data no site
            campo_data_inicio = vDrive.find_element(By.XPATH, '//input[@id="mes_ano_inicio"]')
            campo_data_fim = vDrive.find_element(By.XPATH, '//*[@id="mes_ano_fim"]')
            # Clicar no botão limpar
            botao_limpar = vDrive.find_element(By.CSS_SELECTOR, 'button[data-testid="botao_limpar"]')
            botao_limpar.click()
            # Enviar Periodos
            campo_data_inicio.send_keys(data_inicio)
            campo_data_fim.send_keys(data_fim)

            # Clicar no botão de busca
            botao_buscar = vDrive.find_element(By.XPATH, '/html/body/app-root/div/div[3]/app-evento2020-lista-pesquisa/fieldset/div[2]/button[1]')
            botao_buscar.click()

            try:
                vDrive.find_element(By.XPATH, '/html/body/app-root/div/div[3]/app-evento2020-lista-pesquisa/fieldset[2]/div/table/tr[2]/td[7]/button[1]').click()  # Seleciona o evento para voltar a pagina 1
                vDrive.find_element(By.XPATH, '/html/body/app-root/div/div[3]/app-evento2020-formulario/app-reinf-versao-leiaute/form/app-reinf-botoes-formulario/div/div/button[1]').click()  # Volta à tabela de eventos para voltar a pagina 1
                # Executar ações sequenciais
                executar_acoes_sequenciais(vDrive, pasta_downloads)
            except NoSuchElementException:
                logger.info(f"Não foi encontrado evento em {data_inicio}.")
                time.sleep(0.2)  # Espera entre as ações
            else:
                logger.info(f"Não há mais eventos em {data_inicio}.")


    def pararPrograma():
        if messagebox.askyesno("Confirmação", "Tem certeza que deseja parar o programa?"):
            logger.debug('Finalizando a aplicação...')
            vDrive.quit()
            root.destroy()

    root = tk.Tk()
    root.title("Navegador com Controle")

    # Frame para o navegador
    navegador_frame = tk.Frame(root, height=100, width=100)
    navegador_frame.pack(padx=10, pady=10)

    # Frame para os botões
    botoes_frame = tk.Frame(root)
    botoes_frame.pack(padx=10, pady=10)

    data_inicio_label = tk.Label(botoes_frame, text="Data Início (MM/YYYY):")
    data_inicio_label.pack(pady=(10, 0))
    data_inicio_entry = tk.Entry(botoes_frame, width=20)
    data_inicio_entry.pack(pady=(0, 10))

    data_fim_label = tk.Label(botoes_frame, text="Data Fim (MM/YYYY):")
    data_fim_label.pack(pady=(10, 0))
    data_fim_entry = tk.Entry(botoes_frame, width=20)
    data_fim_entry.pack(pady=(0, 10))

    iniciar_button = tk.Button(botoes_frame, text="Iniciar Download", command=iniciarDownload)
    iniciar_button.pack(side="left", padx=10)

    parar_button = tk.Button(botoes_frame, text="Parar Programa", command=pararPrograma)
    parar_button.pack(side="right", padx=10)

    root.mainloop()
