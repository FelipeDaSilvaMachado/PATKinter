# Aqui estamos importando o módulo tkinter, 
# que é usado para criar interfaces gráficas em Python, 
# e também o ttk, que fornece widgets estilizados como 
# botões e caixas de entrada.
from tkinter import *
from tkinter import ttk

# Cria a janela principal do aplicativo
root = Tk()
# Define o título da janela
root.title("Pés para Metros")

# Função que faz a conversão de pés para metros
def calculate(*args):
    try:
        # Obtém o valor digitado no campo de entrada (em pés)
        value = float(feet.get())
        # Faz a conversão de pés para metros e arredonda o resultado
        result = int(0.3048 * value * 10000.0 + 0.5)/10000.0
        # Armazena o valor convertido na variável 'metros'
        metros.set(result)
    except ValueError:
        # Ignora se o valor digitado não for numérico
        pass

# Cria o container principal (frame) para organizar os widgets
mainframe = ttk.Frame(root, padding="3 3 12 12")
# Posiciona o frame na janela principal
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# Permite que a janela se redimensione corretamente
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Variável para armazenar o valor digitado em pés
feet = StringVar()
# Cria o campo de entrada (input) para digitar o valor em pés
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
# Posiciona o campo de entrada na grade (coluna 2, linha 1)
feet_entry.grid(column=2, row=1, sticky=(W, E))

# Variável para armazenar o valor convertido para metros
metros = StringVar()
# Cria um rótulo (label) que exibirá o valor em metros
ttk.Label(mainframe, textvariable=metros).grid(column=2, row=2, sticky=(W, E))

# Cria um botão "Calcular" que executa a função 'calculate' ao ser clicado
ttk.Button(mainframe, text="Calcular", command=calculate).grid(column=3, row=3, sticky=W)

# Cria os rótulos de texto estático na janela
ttk.Label(mainframe, text="Pés").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="é equivalente a").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="Metros").grid(column=3, row=2, sticky=W)

# Adiciona espaçamento ao redor dos widgets
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Define o foco inicial no campo de entrada de pés
feet_entry.focus()
# Associa a tecla "Enter" à função 'calculate'
root.bind("<Return>", calculate)

# Inicia o loop principal do Tkinter, mantendo a janela aberta
root.mainloop()