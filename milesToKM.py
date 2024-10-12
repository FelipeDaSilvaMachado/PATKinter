# Importando a biblioteca tkinter
from tkinter import *
from tkinter import ttk

# Criando a janela raiz/root
root = Tk()

# Colocando um título no meu app
root.title("Convertendo Milhas para KM")

# Criando a função para converter milhas em KM
def converteMilha(*args):
    try:
        # Obtém o valor digitado no campo de entrada (em milhas)
        valor = float(milhas.get())
        # Faz a conversão de pés para metros e arredonda o resultado
        conversao = float(valor / 0.6214)
        # Armazena o valor convertido na variável 'metros'
        km.set(f"{conversao: .2f}")
    except ValueError:
        # Ignora se o valor digitado não for numérico
        pass


# Criando o conteiner da janela do app
mainframe = ttk.Frame(root, padding="5 5 10 10")

# Posicionando o frame na janela root
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

# Faz com que a parte interna se redimensione corretamente
# mainframe.columnconfigure(0, weight=100)
# mainframe.rowconfigure(0, weight=100)

# Definindo o tipo da variavel do programa
milhas = StringVar()

# Criando a entrada do tipo (input) para digitar o valor em milhas
milhasEntry = ttk.Entry(mainframe, width=12, textvariable=milhas)
# Posiciona o campo de entrada na grade (coluna 1, linha 1)
milhasEntry.grid(column=2, row=1, sticky=(W, E))

# Variável para armazenar o valor convertido para KM
km = IntVar()
# Cria um rótulo (label) que exibirá o valor em metros
ttk.Label(mainframe, textvariable=km).grid(column=1, row=2, sticky=E)

# Cria um botão "Calcular" que executa a função 'calculate' ao ser clicado
ttk.Button(mainframe, text="Converter", command=converteMilha).grid(
    column=3, row=1, sticky=E)

# Cria os rótulos de texto estático na janela do programa
ttk.Label(mainframe, text="Valor em milhas: ").grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, text="km").grid(column=2, row=2, sticky=W)

# Adiciona espaçamento ao redor dos widgets
for child in mainframe.winfo_children():
    child.grid_configure(padx=3, pady=3)

# Define o foco inicial no campo de entrada de milhas
milhasEntry.focus()
# Associa a tecla "Enter" à função 'converteMilha'
root.bind("<Return>", converteMilha)
# Inicia o loop principal do Tkinter, mantendo a janela aberta
root.mainloop()