# Automação de Sistemas e Processos com Python

# 1° entrar no sistema
import pyautogui  #automatiza seu mouse e teclado
import time      #controla o tempo do código
import pyperclip   # habilita a opção de  copiar e colar com o python
import tkinter as tk # Habilita a bibioteca para cria janelas
from tkinter import *
import datetime # Habilita a biblioteca de datas e Horas 
import pandas as pd  #biblioteca de linguagem para analise de dados / as pd é apelida para pandas
import numpy    #biblioteca de codigos matemáticos
import matplotlip # biblioteca para plantar gráficos
from unicodedata import normalize #biblioteca  para padronização de caracteres

#ALERTA INFORMANDO QUE A AUTOMAÇÃO VAI INICIAR

pyautogui.alert("Atenção!!! A automação vai iniciar, selecione a data do relatório e não meixa em nada até o código ""está finalizado.  "
                " Precione ok para iniciar")

breakpoint

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

#Após selecionar a data começara a etapa de baixar o arquivo, analisar e enviar o relatório 

pyautogui.press("win")  #aciona a tecla windows automaticamente
pyautogui.sleep(1)
pyautogui.write("google chrome") #realiza a pesquisa na barra do windows/ use seu browser de preferência
pyautogui.press("enter")  #aperta/aciona a tecla enter
pyautogui.sleep(1)        #adiciona um deley em segundos apartir do valor indicado
link = "https://drive.google.com/drive/folders/1mhXZ3JPAnekXP_4vX7Z_sJj35VWqayaR"     # link do diretorio de onde fica seus dados
pyperclip.copy(link)              #comando para copiar o link( ctrl c) usando o pyperclip
pyautogui.hotkey("ctrl", "v")     #comando para colar o link (ctrl v) usando pyautogui
pyautogui.press("enter") #aperta/aciona a tecla enter

# 2° acessar a pasta de dados

pyautogui.sleep(3)      #adiciona um deley em segundos apartir do valor indicado
pyautogui.doubleClick(x=1115, y=310, button="left") #realiza um duplo click na coordenada indicada

# 3° download da base de dados
pyautogui.sleep(1.5)   #adiciona um deley em segundos apartir do valor indicado
pyautogui.click(x=906, y=487)      #realiza um  click na coordenada indicada
pyautogui.sleep(1)   #adiciona um deley em segundos apartir do valor indicado
pyautogui.click(x=1713, y=176)      #realiza um click na coordenada indicada
pyautogui.sleep(1)   #adiciona um deley em segundos apartir do valor indicado
pyautogui.click(x=1475, y=618)
pyautogui.sleep(5)     #adiciona um deley em segundos apartir do valor indicado para esperar concluir o download

# 4° calcular indicadores / faturamento, quantidade de produtos

tabela = pd.read_excel(r"E:\Downloads\Vendas - Dez.xlsx")  # localizar o arquivo no sistema e ler/ r’ indica que o texto é uma raw string. Ou seja, sem caracteres especiais.
print(tabela) #mostrar a variavel tabela
faturamento = tabela["Valor Final"].sum()       #calcular faturamento dentro da tabela
qtdprodutos = tabela["Quantidade"].sum()        #calcular quantidade dentro da tabela

# 5° entrar no meu email

pyautogui.hotkey("ctrl", "t")
link ="https://mail.google.com"  #inbox  #link de seu email/gmail/hotmail/yahoo/etc
pyperclip.copy(link)    #copiar o link acima
pyautogui.hotkey("ctrl", "v")     #comando para colar o link (ctrl v) usando pyautogui
pyautogui.press("enter")    #aperta/aciona a tecla enter
pyautogui.sleep(5)          #adiciona um deley em segundos apartir do valor indicado

# 6° criar o email
pyautogui.click(x=111, y=202)
pyautogui.sleep(2)
pyautogui.write("lucasceo22@gmail.com")    #email/ o + é para indicar qual pasta o email irá ficar
pyautogui.press("Tab")  #confirmar o email
time.sleep(1)
assunto = "Relatório de Vendas"  #macete para inserir caracteres especiais
pyperclip.copy(assunto)  #copiar o o texto acima
pyautogui.hotkey("ctrl", "v")     #comando para colar o link (ctrl v) usando pyautogui

#7 Preencher o email

pyautogui.press("tab")
texto_email =  f'''Bom dia Sr/Sra fulano de tal, estou encaminhando um relatório sobre as vendas do dia.
   O faturamento foi de : R${faturamento:,.2f}
   A quantidade vendida foi de: {qtdprodutos:,}
   Abs.
   Eng. Lucas Gomes 
   CREA:9856976265'''   #seu texto de email

pyperclip.copy(texto_email)
pyautogui.hotkey("ctrl", "v")

# 8° enviar o email

time.sleep(1)
pyautogui.hotkey("ctrl", "enter") #atalho para enviar o email
pyautogui.alert("Email enviado com sucesso")