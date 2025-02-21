"""
 Autores: Pedro Arthur, Emanuel Rodrigues, Miguel Sthevão
 Documentação de Referência utilizada: https://tkdocs.com/
 OBS.: Optei por não utilizar a https://docs.python.org/3/library/tk.html, pois aparentemente está desatualizada
"""
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename # pra poder abrir um arquivo
from tkinter.filedialog import asksaveasfilename # pra poder salvar um arquivo
from tkinter import messagebox
from datetime import datetime
import os

# classe para excecao da altura e peso
class NegativeValueError(Exception): # semelhante a "class ValueError(Exception): ..."
    """Classe de excecao personalizada para valores negativos ou zero."""
    pass

# formata o nome para quando salvar, o nome do arquivo ficar certinho (acabou que nem usei porque deve ser salvo tudo em um arquivo só e não em arquivo separados por usuarios)
# def formatar_nome(nome:str) -> str:
    # return nome.replace(" ","_")
    
    
# ---------------- Foncoes ----------------

# calcula imc
def calcular_imc():
    try:
        # converte peso e altura pra float
        peso_valor = float(peso.get())
        altura_valor = float(altura.get())/100
        print(altura_valor)

        # verifica se o peso eh positivo
        if peso_valor <= 0:
            raise NegativeValueError("O valor do peso deve ser maior que zero")
        
        # verifica se a altura eh positivp
        if altura_valor <= 0:
            raise NegativeValueError("O valor da altura deve ser maior que zero")

        # calcula o IMC
        resultado = peso_valor / (altura_valor ** 2)
        
        # seta o StringVar com o resultado formatado com 2 casas decimais
        imc.set(f"{resultado:.2f}")
        mensagemImc.set(f"Seu Imc é de {resultado:.2f} ({classificar_imc(float(imc.get()))}) ")
        # salva as informações no arquivo
        
        
    except ValueError:
        # exceçao caso a altura ou o peso não sejam numéricos
        mensagemImc.set("Erro: Peso e altura devem ser números válidos")
    except NegativeValueError as e:
        mensagemImc.set(f"Erro: {str(e)}")

                
def classificar_imc(imc):
    if imc < 18.5:
        return "Peso Baixo"
    elif 18.5 <= imc <= 24.9:
        return "Peso normal"
    elif 25 <= imc <= 29.9:
        return "Sobrepeso"
    elif 30 <= imc <= 34.9:
        return "Obesidade Grau I"
    elif 35 <= imc <= 39.9:
        return "Obesidade Severa Grau II"
    else:
        return "Obesidade Mórbida Grau III"

def open_calculadora():
    start_page.withdraw()
    window.deiconify()
    
def sobre():
    messagebox.showinfo("Sobre", "Calculadora de IMC\nAutores: Pedro Arthur Maciel Albuquerque (Lindo), Emanuel Rodrigues, Miguel Sthevão\nDisciplina: Programação Orientada a Objetos\nProfessor: Michel da Silva\n\nEste aplicativo tem como objetivo calcular e classificar seu imc, determinando seu estado físico.\n\nA Classificação é feita com base na seguinte tabela:\n\n<18.5 -> Peso baixo\n18.5 - 24.9 -> Peso Normal\n25.0 - 29.9 -> Sobrepeso\n30.0 - 34.9 -> Obesidade Grau I\n35.0 - 39.9 -> Obesidade Severa Grau II\n>=40.0 -> Obesidade Mórbida Grau III")
    
def voltar_inicio():
    window.withdraw() # esconde a janela
    start_page.deiconify()    # mostra a janela
    
def save_info():
    
    try:
        conteudo = (f"Nome: {nome.get()}\n" # usa o get pq o nome eh da classe StringVar qyue tem essa funcao pra pegar o valor
                f"Peso: {peso.get()} Kg\n"
                f"Altura: {float(altura.get())/100} metros\n"
                f"Data: {data.get()}\n"
                f"IMC: {imc.get()} ({classificar_imc(float(imc.get()))})\n\n")
        with open(f"info.txt", 'a') as arquivo1:
            arquivo1.write(conteudo)
            
        messagebox.showinfo("Salvo", "Dados salvos com sucesso!")
    except:
        messagebox.showinfo("Erro", "Dados Inválidos!")
            
# ---------------- Window inicial ----------------
start_page = tk.Tk()
start_page.title("Calculadora de IMC - Tela Inicial")
start_page.geometry("400x550")

first_frame = ttk.Frame(start_page,padding="10 10 12 12")
first_frame.grid(column=0,row=0)
start_page.columnconfigure(0,weight=1)
start_page.rowconfigure(0,weight=1)

# Adicione os botões ao first_frame em vez de start_page
bttn_calculator = ttk.Button(first_frame, text="Abrir Calculadora de IMC", command=open_calculadora)
bttn_calculator.grid(row=1, column=0, pady=20)

bttn_creditos = ttk.Button(first_frame, text="Sobre", command=sobre)    
bttn_creditos.grid(row=2, column=0, pady=10)

# ---------------- Window da calculadora ----------------

window = tk.Toplevel()
window.title("Calculadora de IMC")
window.geometry("400x550") # com o geometry posso redimensionar a window usando o mouse
window.minsize(width=370, height=420)
# a linha a seguir eh importante pra nao deixar aparecer logo de cara as duas janelas
window.withdraw()

main_frame = ttk.Frame(window,padding="10 10 12 12")
main_frame.grid(column=0,row=0)
window.columnconfigure(0,weight=1)
window.rowconfigure(0,weight=1)



# ---------------- Variaveis ----------------

nome = StringVar()
peso = StringVar()
altura = StringVar()
data = StringVar()
imc = StringVar()
mensagemImc = StringVar()

# ---------------- Entrys ----------------

ttk.Label(main_frame, text="Nome:").grid(row=1, column=0, sticky="W")
ttk.Entry(main_frame, textvariable=nome).grid(row=1, column=1)

ttk.Label(main_frame, text="Peso (kg):").grid(row=2, column=0, sticky="W")
ttk.Entry(main_frame, textvariable=peso).grid(row=2, column=1)

ttk.Label(main_frame, text="Altura (cm):").grid(row=3, column=0, sticky="W")
ttk.Entry(main_frame, textvariable=altura).grid(row=3, column=1)

# Observação: Optei por nao colocar limitação na maneira de dar o input da data, pois assim o usuário fica mais livre para usar o modelo de data que ele desejar (ex: brasileiro (dd/mm/yyyy), americano (mm/dd/yyyy), china e coreia (yyyy-mm-dd))
ttk.Label(main_frame, text="Data:").grid(row=4, column=0, sticky="W")
ttk.Entry(main_frame, textvariable=data).grid(row=4, column=1)

# ---------------- Botoes ----------------
ttk.Button(main_frame, text="Calcular IMC", command=calcular_imc).grid(row=5, column=0, columnspan=2, pady=10)

ttk.Label(main_frame, textvariable=mensagemImc, foreground="blue").grid(row=6, column=0, columnspan=2) # coloquei em azul porque fica mais bonito

ttk.Button(main_frame, text="Salvar Dados", command=save_info).grid(row=7, column=0, columnspan=2, pady=10)

# back
ttk.Button(main_frame, text="Voltar", command=voltar_inicio).grid(row=8, column=0, columnspan=2, pady=10)

# ---------------- Titulo da pagina da culculadora ----------------
titulo_label = ttk.Label(window,text="Calculadora de IMC")
titulo_label.grid(column=0, row=0,  sticky="N",pady=5)
titulo_label.config(font=("Helvetica", 24, "bold"))

# dar start na primeira pagina
start_page.mainloop()
