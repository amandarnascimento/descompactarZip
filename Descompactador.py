import tkinter as tk
from tkinter import filedialog, messagebox
import zipfile
import os

# Função para descompactar o arquivo zipado
def descompactar_arquivo():
    # Obtendo os caminhos e o nome da pasta
    caminho_origem = entrada_origem.get()
    caminho_destino = entrada_destino.get()
    nome_pasta = entrada_pasta.get()

    # Verificando se todos os campos foram preenchidos
    if not caminho_origem or not caminho_destino or not nome_pasta:
        label_status.config(text="Por favor, insira o caminho do arquivo, destino e nome da pasta", fg="red")
        return

    # Verificando se o arquivo de origem existe
    if not os.path.exists(caminho_origem):
        label_status.config(text="O arquivo de origem não existe", fg="red")
        return

    # Criando o caminho completo da pasta de destino
    pasta_destino = os.path.join(caminho_destino, nome_pasta)
    if os.path.exists(pasta_destino):
        messagebox.showwarning("Aviso", "A pasta de destino já existe")
        return

    try:
        # Criando a pasta de destino
        os.makedirs(pasta_destino)
        # Descompactando o arquivo zipado na pasta de destino
        with zipfile.ZipFile(caminho_origem, 'r') as zip_ref:
            zip_ref.extractall(pasta_destino)
        label_status.config(text="Arquivo descompactado com sucesso", fg="#00975C")
    except Exception as e:
        label_status.config(text=f"Erro ao descompactar o arquivo: {e}", fg="red")

# Função para limpar os campos de entrada
def limpar_campos():
    entrada_origem.delete(0, tk.END)
    entrada_destino.delete(0, tk.END)
    entrada_pasta.delete(0, tk.END)
    label_status.config(text="", fg="black")

# Função para sair do aplicativo
def sair_aplicativo():
    janela_principal.destroy()

# Criando a janela principal
janela_principal = tk.Tk()
janela_principal.title("Descompactador de Arquivo")

# Label e Entry para o caminho do arquivo zipado
label_origem = tk.Label(janela_principal, text="Caminho do arquivo zipado:")
label_origem.grid(row=0, column=0, padx=5, pady=5, sticky="w")
entrada_origem = tk.Entry(janela_principal, width=50)
entrada_origem.grid(row=0, column=1, padx=5, pady=5)

# Botão para selecionar o arquivo zipado
botao_origem = tk.Button(janela_principal, text="Selecionar Arquivo", command=lambda: entrada_origem.insert(tk.END, filedialog.askopenfilename()))
botao_origem.grid(row=0, column=2, padx=5, pady=5)

# Label e Entry para o caminho de destino
label_destino = tk.Label(janela_principal, text="Caminho de destino:")
label_destino.grid(row=1, column=0, padx=5, pady=5, sticky="w")
entrada_destino = tk.Entry(janela_principal, width=50)
entrada_destino.grid(row=1, column=1, padx=5, pady=5)

# Botão para selecionar o caminho de destino
botao_destino = tk.Button(janela_principal, text="Selecionar Destino", command=lambda: entrada_destino.insert(tk.END, filedialog.askdirectory()))
botao_destino.grid(row=1, column=2, padx=5, pady=5)

# Label e Entry para o nome da pasta
label_pasta = tk.Label(janela_principal, text="Nome da pasta a ser criada:")
label_pasta.grid(row=2, column=0, padx=5, pady=5, sticky="w")
entrada_pasta = tk.Entry(janela_principal, width=50)
entrada_pasta.grid(row=2, column=1, padx=5, pady=5)

# Botão para descompactar o arquivo
botao_descompactar = tk.Button(janela_principal, text="Descompactar", command=descompactar_arquivo, bg="#00975C", fg="white")
botao_descompactar.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

# Botão para limpar os campos
botao_limpar = tk.Button(janela_principal, text="Limpar Campos", command=limpar_campos)
botao_limpar.grid(row=4, column=0, padx=5, pady=5, sticky="ew")

# Botão para sair
botao_sair = tk.Button(janela_principal, text="Sair", command=sair_aplicativo)
botao_sair.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

# Label para exibir o status
label_status = tk.Label(janela_principal, text="", fg="black")
label_status.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

janela_principal.mainloop()
