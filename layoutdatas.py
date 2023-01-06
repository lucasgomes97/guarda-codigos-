import tkinter as tk
from tkinter import *
import datetime
import pyautogui

app = tk.Tk()
app.geometry("750x100")
app.config(background="white")
app.title('Confirme a Data do relatório')

#lista de Entradas

dia_entrada = tk.Entry(app)
mes_entrada = tk.Entry(app)
ano_entrada = tk.Entry(app)

#textos

dia_text= tk.Label(app, text=("Dia/"), width=5)
mes_text = tk.Label(app, text=("Mês/"), width=5)
ano_text = tk.Label(app, text=("Ano"), width=5)
dia_text.pack(side=("left"))
mes_text.pack(side=("left"))
ano_text.pack(side=("left"))

#Funções

def callback():
    dia = dia_entrada.get()
    mes = mes_entrada.get()
    ano = ano_entrada.get()
    print(f"{dia}/{mes}/{ano}")
    

def sair():
    app.configure(bg='green') 
    pyautogui.alert("Data Confirmada") 
    app.destroy()
    app.quit()

    
def mudar_cor():
    app.configure(bg='green') 


#Fixar Entradas na Janela

dia_entrada.pack(side=("left"))
mes_entrada.pack(side=("left"))
ano_entrada.pack(side=("left"))

#Botão Confirma

comando_das_funçoes=lambda:(callback(), mudar_cor(), sair())
botao = tk.Button(app, text="Confirmar data", command=comando_das_funçoes)
botao.config(background=("white"),font=("times new romam", 10))
botao.pack(side=["left"])

app.mainloop()

