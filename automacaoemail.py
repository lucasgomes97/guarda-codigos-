# Automação de Sistemas e Processos com Python

import time  # controla o tempo do código

# 1° entrar no sistema
import pyautogui  # automatiza seu mouse e teclado
import pyperclip  # habilita a opção de  copiar e colar com o python

pyautogui.alert("Atenção!!! A automação vai iniciar, selecione a data do relatório e não meixa em nada até o código esteja finalizado.  "
                " Precione ok para iniciar")
pyautogui.press("win")  #aciona a tecla windows automaticamente
pyautogui.sleep(1)
pyautogui.write("google chrome") #realiza a pesquisa na barra do windows/ use seu browser de preferência
pyautogui.press("backspace")
pyautogui.press("enter")  #aperta/aciona a tecla enter
pyautogui.sleep(1)        #adiciona um deley em segundos apartir do valor indicado
link = "https://drive.google.com/drive/folders/1mhXZ3JPAnekXP_4vX7Z_sJj35VWqayaR"     # link do diretorio de onde fica seus dados
pyperclip.copy(link)              #comando para copiar o link( ctrl c) usando o pyperclip
pyautogui.hotkey("ctrl", "v")     #comando para colar o link (ctrl v) usando pyautogui
pyautogui.press("enter") #aperta/aciona a tecla enter
# 2° acessar a pasta de dados
"""import pyautogui
pyautogui.sleep(5)  #adiciona um deley em segundos apartir do valor indicado, para que tenhamos tempo para colocar o mouse onde queremos saber a coordenada
print(pyautogui.size())     #informa a resolução da tela em x, y
print(pyautogui.position()) #comando para informar as coordenadas da tela (x, y)""" #Grupo de comandos para localizar coordenadas na tela, cada caso tem suas coordenadas diferentes
pyautogui.sleep(3)      #adiciona um deley em segundos apartir do valor indicado
pyautogui.doubleClick(x=1265, y=354, button="left") #realiza um duplo click na coordenada indicada

# 3° download da base de dados
pyautogui.sleep(2)   #adiciona um deley em segundos apartir do valor indicado
pyautogui.click(x=1033, y=490)      #realiza um  click na coordenada indicada
pyautogui.sleep(2)   #adiciona um deley em segundos apartir do valor indicado
pyautogui.click(x=1675, y=229)      #realiza um click na coordenada indicada
pyautogui.sleep(2)   #adiciona um deley em segundos apartir do valor indicado
pyautogui.click(x=1438, y=758)
pyautogui.sleep(2)
pyautogui.click(x=1005, y=686)
pyautogui.sleep(2)   #adiciona um deley em segundos apartir do valor indicado
pyautogui.click(x=1675, y=229)      #realiza um click na coordenada indicada
pyautogui.sleep(2)   #adiciona um deley em segundos apartir do valor indicado
pyautogui.click(x=1438, y=758)
pyautogui.sleep(5)     #adiciona um deley em segundos apartir do valor indicado para esperar concluir o download

# 4° calcular indicadores / faturamento, quantidade de produtos
import pandas as pd  #biblioteca de linguagem para analise de dados / as pd é apelida para pandas
import numpy
import normalize
import unicodedata
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
pyautogui.click(x=98, y=252)
pyautogui.sleep(2)
pyautogui.click(x=1222, y=450)
time.sleep(1.5)
pyautogui.write("lucasceo22+codigos@gmail.com")    #email/ o + é para indicar qual pasta o email irá ficar
pyautogui.press("Tab")  #confirmar o email
pyautogui.click(x=1294, y=496)
time.sleep(1)
assunto = "Relatório de Vendas"  #macete para inserir caracteres especiais
pyperclip.copy(assunto)  #copiar o o texto acima
pyautogui.hotkey("ctrl", "v")     #comando para colar o link (ctrl v) usando pyautogui

#7 Preencher o email
pyautogui.press("tab")
texto_email = f'''Bom dia Sr istrudan, estou encaminhando um relatório sobre as vendas
   O faturamento foi de : R${faturamento:,.2f}
   A quantidade vendida foi de: {qtdprodutos:,}
   Abs.
   Eng. Lucas Gomes 
   CREA:9856976265'''  #seu texto de email
pyperclip.copy(texto_email)
pyautogui.hotkey("ctrl", "v")

# 8° enviar o email

time.sleep(1)
pyautogui.hotkey("ctrl", "enter") #atalho para enviar o email
pyautogui.alert("Email enviado com sucesso")
