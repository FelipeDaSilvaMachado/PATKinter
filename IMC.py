# Importando a biblioteca tkinter
from tkinter import *
from tkinter import ttk

# Criando a janela raiz/root
root = Tk()

# Colocando um título no meu app
root.title("Calculadora de IMC")

# Criando a função para calcular o IMC


def calculaIMC(*args):
    try:
        valor1 = float(peso.get())
        valor2 = float(altura.get())
        calculo = valor1 / valor2**2
        imc.set(f"{calculo: .1f}")
        tabelIMC.set(tabelaIMC(calculo))
    except ValueError:
        return None


def tabelaIMC(calculaIMC):
    if calculaIMC < 18.5:
        return "Você esta abaixo do peso, procure um médico"
    elif calculaIMC >= 18.5 and calculaIMC <= 24.9:
        return "Você está em seu peso normal"
    elif calculaIMC >= 25 and calculaIMC <= 29.9:
        return "Você está com sobrepeso, procure um médico"
    elif calculaIMC >= 30 and calculaIMC <= 34.9:
        return "Você está com Obesidade grau I, procure um médico"
    elif calculaIMC >= 35 and calculaIMC <= 39.9:
        return "Você está com Obesidade grau II, procure um médico"
    elif calculaIMC >= 40:
        return "Você está com Obesidade grau III, procure um médico"

# Criando o conteiner da janela do app
mainframe = ttk.Frame(root, padding="3 3 10 10")

# Posicionando o frame na janela root
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

# Faz com que a parte interna se redimensione corretamente
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# Definindo o tipo da variavel do programa
peso = StringVar()

# Criando a entrada do tipo (input) para digitar o peso
pesoEntry = ttk.Entry(mainframe, width=12, textvariable=peso)
# Posiciona o campo de entrada na grade (coluna 1, linha 1)
pesoEntry.grid(column=1, row=2, sticky=W)

# Definindo o tipo da variavel do programa
altura = StringVar()

# Criando a entrada do tipo (input) para digitar a altura
alturaEntry = ttk.Entry(mainframe, width=12, textvariable=altura)
# Posiciona o campo de entrada na grade (coluna 1, linha 1)
alturaEntry.grid(column=1, row=4, sticky=W)

# Definindo o tipo da variavel do programa
tabelIMC = StringVar()

# Variável para armazenar o valor do IMC calculado
imc = IntVar()
# Cria um rótulo (label) que exibirá o valor do imc calculado
ttk.Label(mainframe, textvariable=imc).grid(column=2, row=4, sticky=W)

# Cria um botão "Calcular" que executa a função 'calculate' ao ser clicado ttk.Button
ttk.Button(mainframe, text="Calcular IMC").grid(column=3, row=4, sticky=W)

# Cria os rótulos de texto estático na janela do programa ttk.Label
ttk.Label(mainframe, text="Seu peso").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Sua altura em metros, ex: 1 metro e 70 digite 1.70").grid(
    column=1, row=3, sticky=W)
ttk.Label(mainframe, textvariable=tabelIMC).grid(column= 1, row= 5, sticky=(W, E))

# Adiciona espaçamento ao redor dos widgets
for child in mainframe.winfo_children():
    child.grid_configure(padx=3, pady=3)

# Define o foco inicial no campo de entrada de milhas
pesoEntry.focus()

# Função que muda o foco para alturaEntry
def mudar_foco(event):
    alturaEntry.focus_set()  # Define o foco em alturaEntry

# Associa a tecla "Enter" à função 'funcao'
pesoEntry.bind("<Return>", mudar_foco)
root.bind("<Return>", calculaIMC)
# Inicia o loop principal do Tkinter, mantendo a janela aberta
root.mainloop()