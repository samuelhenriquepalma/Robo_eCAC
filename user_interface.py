import time
import tkinter as tk
from actions import executar_acoes_sequenciais, verificar_paginas_e_baixar
import json
from tkinter import messagebox
from selenium.webdriver.common.by import By


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


    def iniciarAcoes():
        # Chama as ações sequenciais
        pasta_downloads = r"C:\path\to\downloads"  # Ajuste conforme necessário
        executar_acoes_sequenciais(vDrive, pasta_downloads)
        
        # Executa o loop de verificação de páginas e download
        # verificar_paginas_e_baixar(vDrive)

    def pararPrograma():
        if messagebox.askyesno("Confirmação", "Tem certeza que deseja parar o programa?"):
            vDrive.quit()
            root.destroy()

    root = tk.Tk()
    root.title("Navegador com Controle")

    # Frame para o navegador
    navegador_frame = tk.Frame(root, height=600, width=800)
    navegador_frame.pack(padx=10, pady=10)

    # Frame para os botões
    botoes_frame = tk.Frame(root)
    botoes_frame.pack(padx=10, pady=10)

    iniciar_button = tk.Button(botoes_frame, text="Iniciar Download", command=iniciarAcoes)
    iniciar_button.pack(side="left", padx=10)

    parar_button = tk.Button(botoes_frame, text="Parar Programa", command=pararPrograma)
    parar_button.pack(side="right", padx=10)

    root.mainloop()
