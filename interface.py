import customtkinter
import tkinter as tk
import time
from tkinter import messagebox, filedialog
import json
from tkinter import scrolledtext
from logger_config import logger
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from browser import inicializarChrome
from utils import gerar_intervalo_datas
from actions import executar_acoes_sequenciais
import logging

# Redireciona as saídas de logging para o widget de texto
class TextHandler(logging.Handler):
    def __init__(self, text_widget):
        super().__init__()
        self.text_widget = text_widget

    def emit(self, record):
        msg = self.format(record)
        def append():
            self.text_widget.configure(state='normal')
            self.text_widget.insert(tk.END, msg + '\n')
            self.text_widget.configure(state='disabled')
            self.text_widget.yview(tk.END)
        self.text_widget.after(0, append)

# Classe para criar um frame com múltiplos checkboxes
class MyCheckboxFrame(customtkinter.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.checkboxes = []

        # Adiciona um título ao frame
        self.title_label = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6, font=("Arial", 14))
        self.title_label.grid(row=0, column=0, padx=10, pady=(10, 20), sticky="ew")

        # Adiciona os checkboxes ao frame
        for i, value in enumerate(self.values):
            checkbox = customtkinter.CTkCheckBox(self, text=value, font=("Arial", 14))
            checkbox.grid(row=i+1, column=0, padx=10, pady=(10, 5), sticky="w")
            self.checkboxes.append(checkbox)

    # Função para obter os valores selecionados dos checkboxes
    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes

# Classe principal do aplicativo
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("REINF AutoDownloader")
        self.geometry("800x600")  # Aumenta o tamanho da janela principal
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 1), weight=1)

        # Adiciona um frame para os campos de entrada
        self.input_frame = customtkinter.CTkFrame(self)
        self.input_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 0), sticky="nsew")
        self.input_frame.grid_columnconfigure((0, 1), weight=1)

        # Adiciona um label e uma entry para entrada do CNPJ
        self.cnpj_label = customtkinter.CTkLabel(self.input_frame, text="Digite o CNPJ da empresa:", font=("Arial", 14))
        self.cnpj_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.cnpj_entry = customtkinter.CTkEntry(self.input_frame, font=("Arial", 14), height=30)
        self.cnpj_entry.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="ew")

        # Adiciona um label e uma textbox para entrada dos cookies
        self.cookies_label = customtkinter.CTkLabel(self.input_frame, text="Cole o JSON dos cookies:", font=("Arial", 14))
        self.cookies_label.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="w")
        self.cookies_entry = customtkinter.CTkTextbox(self.input_frame, height=30, font=("Arial", 14))
        self.cookies_entry.grid(row=1, column=1, padx=10, pady=(0, 10), sticky="ew")

        # Adiciona o frame de checkboxes
        self.checkbox_frame = MyCheckboxFrame(self, "EFD-REINF", values=["R-2020", "R-2060"])
        self.checkbox_frame.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="nsew")

        # Widget Text para exibir os logs
        self.log_widget = scrolledtext.ScrolledText(self, wrap='word', height=10, width=50, font=("Arial", 14))
        self.log_widget.grid(row=3, column=0, columnspan=2, padx=10, pady=(10, 10), sticky="nsew")
        self.log_widget.configure(state='disabled')

        # Configura o logger para usar o TextHandler
        text_handler = TextHandler(self.log_widget)
        text_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))
        logger.addHandler(text_handler)

        # Adiciona um frame para os campos de entrada date
        self.input_frame_date = customtkinter.CTkFrame(self)
        self.input_frame_date.grid(row=1, column=1, padx=10, pady=(10, 0), sticky="nsew")
        self.input_frame_date.grid_columnconfigure(0, weight=1)
        self.input_frame_date.grid_columnconfigure(1, weight=1)
        # self.input_frame_date.grid_rowconfigure(0, weight=1)
        # self.input_frame_date.grid_rowconfigure(1, weight=1)
        # self.input_frame_date.grid_rowconfigure(2, weight=1)

        # Adiciona um título ao frame
        self.title_label = customtkinter.CTkLabel(self.input_frame_date, text='Período de Download', fg_color="gray30", corner_radius=6, font=("Arial", 14))
        self.title_label.grid(row=0, column=0, padx=10, pady=(10, 10), columnspan=2, sticky="ew")

        # Adiciona os labels e entries para as datas
        data_inicio_label = customtkinter.CTkLabel(self.input_frame_date, text="Data Início (MM/YYYY):", font=("Arial", 14))
        data_inicio_label.grid(row=1, column=0, padx=10, pady=(10, 15), sticky="w")
        self.data_inicio_entry = customtkinter.CTkEntry(self.input_frame_date, font=("Arial", 14), height=30)
        self.data_inicio_entry.grid(row=1, column=1, padx=10, pady=(10, 10), sticky="ew")

        data_fim_label = customtkinter.CTkLabel(self.input_frame_date, text="Data Fim (MM/YYYY):", font=("Arial", 14))
        data_fim_label.grid(row=2, column=0, padx=10, pady=(10, 15), sticky="w")
        self.data_fim_entry = customtkinter.CTkEntry(self.input_frame_date, font=("Arial", 14), height=30)
        self.data_fim_entry.grid(row=2, column=1, padx=10, pady=(10, 10), sticky="ew")


        # Adiciona os botões iniciar e parar
        iniciar_button = customtkinter.CTkButton(self, text="Iniciar Download", command=self.iniciar_autenticacao, font=("Arial", 16), height=30)
        iniciar_button.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        parar_button = customtkinter.CTkButton(self, text="Parar Programa", command=self.parar_programa, font=("Arial", 16), height=30)
        parar_button.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        # Adiciona um botão para escolher o diretório de download
        self.download_dir_button = customtkinter.CTkButton(self, text="Escolher Diretório de Download", command=self.escolher_diretorio_download, font=("Arial", 16), height=30)
        self.download_dir_button.grid(row=2, column=1, padx=10, pady=10, sticky="we")

        # Variável para armazenar o caminho do diretório de download
        self.pasta_downloads = None

    # Função para escolher o diretório de download
    def escolher_diretorio_download(self):
        self.pasta_downloads = filedialog.askdirectory()
        self.pasta_downloads = self.pasta_downloads.replace("/","\\")
        if self.pasta_downloads:
            messagebox.showinfo("Diretório Selecionado", f"Diretório de download selecionado: {self.pasta_downloads}")
            logger.info(f"Diretório de download selecionado: {self.pasta_downloads}")

    # Função para iniciar o download
    # def iniciar_download(self):
    #     if not self.pasta_downloads:
    #         messagebox.showwarning("Diretório não selecionado", "Por favor, escolha um diretório de download antes de iniciar.")
    #         return
        #logger.info('Iniciando Download')
        # Lógica para iniciar o download aqui
    


    # Função para parar o programa
    def parar_programa(self):
        logger.info('Parando Aplicação')
        # Lógica para parar o programa aqui

    # Função chamada quando o botão é pressionado
    def iniciar_autenticacao(self):

        if not self.pasta_downloads:
            messagebox.showwarning("Diretório não selecionado", "Por favor, escolha um diretório de download antes de iniciar.")
            return
        
        cookies_part = self.cookies_entry.get("1.0", tk.END).strip()
        cnpj_part = self.cnpj_entry.get().strip().replace('.', '').replace('-', '').replace('/', '')

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
            logger.info("Dados obtidos: %s, %s", json_cookies, cnpj_part)
            cnpj = cnpj_part
            urlDownload = self.pasta_downloads
            self.result = (json_cookies, cnpj_part)

            #inicializando o browser
            vDrive = inicializarChrome(json_cookies, urlDownload, cnpj)

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao processar os dados: {e}")
            logger.error("Erro ao processar os dados: %s", e)

        # Função para adicionar a barra nas datas automaticamente
        self.data_inicio_entry.bind('<KeyRelease>', self.add_slash)
        self.data_fim_entry.bind('<KeyRelease>', self.add_slash)

        #-------------------------------------------------------------------------------------------------

        data_inicio = self.data_inicio_entry.get().strip()
        data_fim = self.data_fim_entry.get().strip()

        if not data_inicio or not data_fim:
            messagebox.showerror("Erro", "Por favor, preencha as datas de início e fim.")
            return

        intervalo_datas = gerar_intervalo_datas(data_inicio, data_fim)
        pasta_downloads = self.pasta_downloads  # Ajuste conforme necessário
        
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
                time.sleep(1.5)  # Espera entre as ações
                vDrive.find_element(By.XPATH, '/html/body/app-root/div/div[3]/app-evento2020-formulario/app-reinf-versao-leiaute/form/app-reinf-botoes-formulario/div/div/button[1]').click()  # Volta à tabela de eventos para voltar a pagina 1
                time.sleep(1.5)  # Espera entre as ações
                # Executar ações sequenciais
                executar_acoes_sequenciais(vDrive, pasta_downloads)
            except NoSuchElementException:
                    logger.info(f"Não foi encontrado evento em {data_inicio}.")
                    time.sleep(0.2)  # Espera entre as ações
            else:
                logger.info(f"Não há mais eventos em {data_inicio}.")

    # Função para adicionar a barra nas datas automaticamente
    def add_slash(self, event):
        widget = event.widget
        text = widget.get()
        if len(text) == 2 and '/' not in text:
            widget.insert(tk.END, '/')

# app = App()
# app.mainloop()