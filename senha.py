# Aqui estamos importando o módulo tkinter,
# que é usado para criar interfaces gráficas em Python,
# e também o ttk, que fornece widgets estilizados como
# botões e caixas de entrada.
from tkinter import *
from tkinter import ttk
import random

# Cria a janela principal do aplicativo
# root == raiz
root = Tk()
# Define o título da janela
root.title("Gerador de Senhas Aleatórias")

# Função que gera uma senha aleatória com caracteres especiais, letras e numeros


def geraSenha(*args):
    listToPassword = []

    strAleat = ""
    for i in range(3):
        numsAleatorios = random.randint(0, 2)
        strAleat += str(numsAleatorios)
        listToPassword.append(strAleat)

    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    alpha = list(alfabeto)
    alphaSorteado = random.sample(alpha, 3)
    listToPassword.extend(alphaSorteado)

    specialsChars = r"!@#$%^&*()_-+=[]{}|;:'\",.<>?/`~\\"
 
    caracteresEspeciais = list(specialsChars)
    specialChrasSamp = random.sample(caracteresEspeciais, 3)
    listToPassword.extend(specialChrasSamp)

    random.shuffle(listToPassword)
    senhaAleatoria = "".join(listToPassword)
    senha.set(senhaAleatoria)


# Cria o container principal (frame) para organizar os widgets
mainframe = ttk.Frame(root, padding="5 5 15 15")
# Posiciona o frame na janela principal
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# Permite que a janela se redimensione corretamente
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Variável para armazenar o valor convertido para metros
senha = StringVar()
# Cria um rótulo (label) que exibirá o valor em metros
ttk.Label(mainframe, textvariable=senha).grid(
    column=2, row=1, sticky=(W, E))

# Cria um botão "Calcular" que executa a função 'calculate' ao ser clicado
ttk.Button(mainframe, text="Gerar Senha", command=geraSenha).grid(
    column=2, row=2, sticky=E)

# Cria os rótulos de texto estático na janela
ttk.Label(mainframe, text="Senha Aleatória: ").grid(column=1, row=1, sticky=W)

# Adiciona espaçamento ao redor dos widgets
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Inicia o loop principal do Tkinter, mantendo a janela aberta
root.mainloop()
