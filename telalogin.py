
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_script = sys.argv[0]
_location = os.path.dirname(_script)

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40' # X11 color: #666666
_ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
_ana2color = 'beige' # X11 color: #f5f5dc
_tabfg1 = 'black' 
_tabfg2 = 'black' 
_tabbg1 = 'grey75' 
_tabbg2 = 'grey89' 
_bgmode = 'light' 




class Toplevel1:
    def __init__(self, top=None):
        top = tk.Tk()
        top.geometry("600x450+435+194")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Toplevel 0")
        top.configure(background="#000000")

        self.top = top

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.133, rely=0.067, relheight=0.789, relwidth=0.725)
        self.Frame1.configure(relief='solid')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="solid")
        self.Frame1.configure(background="#ff8000")
        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.391, rely=0.028, height=41, width=164)
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#ff8000")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Georgia} -size 21 -weight bold")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(text='''Login''')

        self.Entry1_1 = tk.Entry(self.Frame1)
        self.Entry1_1.place(relx=0.23, rely=0.563, height=30, relwidth=0.538)
        self.Entry1_1.configure(background="white")
        self.Entry1_1.configure(disabledforeground="#a3a3a3")
        self.Entry1_1.configure(font="TkFixedFont")
        self.Entry1_1.configure(foreground="#000000")
        self.Entry1_1.configure(highlightbackground="#d9d9d9")
        self.Entry1_1.configure(highlightcolor="black")
        self.Entry1_1.configure(insertbackground="black")
        self.Entry1_1.configure(selectbackground="#c4c4c4")
        self.Entry1_1.configure(selectforeground="black")


        self.Label1_1 = tk.Label(self.Frame1)
        self.Label1_1.place(relx=0.23, rely=0.225, height=41, width=164)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(anchor='w')
        self.Label1_1.configure(background="#ff8000")
        self.Label1_1.configure(compound='left')
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(font="-family {Georgia} -size 20")
        self.Label1_1.configure(foreground="#ffffff")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''Usuário''')

        self.Label1_1_1 = tk.Label(self.Frame1)
        self.Label1_1_1.place(relx=0.23, rely=0.451, height=41, width=164)
        self.Label1_1_1.configure(activebackground="#f9f9f9")
        self.Label1_1_1.configure(anchor='w')
        self.Label1_1_1.configure(background="#ff8000")
        self.Label1_1_1.configure(compound='left')
        self.Label1_1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1_1.configure(font="-family {Georgia} -size 20")
        self.Label1_1_1.configure(foreground="#ffffff")
        self.Label1_1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1_1.configure(highlightcolor="black")
        self.Label1_1_1.configure(text='''Senha''')

        self.Entryusuario = tk.Entry(self.Frame1)
        self.Entryusuario.place(relx=0.222, rely=0.329, height=30, relwidth=0.601)
        self.Entryusuario.configure(background="white")
        self.Entryusuario.configure(disabledforeground="#a3a3a3")
        self.Entryusuario.configure(font="TkFixedFont")
        self.Entryusuario.configure(foreground="#000000")
        self.Entryusuario.configure(highlightbackground="#d9d9d9")
        self.Entryusuario.configure(highlightcolor="black")
        self.Entryusuario.configure(insertbackground="black")
        self.Entryusuario.configure(selectbackground="#c4c4c4")
        self.Entryusuario.configure(selectforeground="black")

        

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.23, rely=0.732, height=34, width=107)
        self.Button1.configure(activebackground="beige")
        self.Button1.configure(activeforeground="black")
        self.Button1.configure(background="#008000")
        self.Button1.configure(compound='left')
        self.Button1.configure(cursor="fleur")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Georgia} -size 12")
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Login''')

        self.Button1_1 = tk.Button(self.Frame1)
        self.Button1_1.place(relx=0.552, rely=0.732, height=34, width=97)
        self.Button1_1.configure(activebackground="beige")
        self.Button1_1.configure(activeforeground="black")
        self.Button1_1.configure(background="#008000")
        self.Button1_1.configure(compound='left')
        self.Button1_1.configure(cursor="fleur")
        self.Button1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1.configure(font="-family {Georgia} -size 12")
        self.Button1_1.configure(foreground="#ffffff")
        self.Button1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1.configure(highlightcolor="black")
        self.Button1_1.configure(pady="0")
        self.Button1_1.configure(text='''Cadastrar''')

        self.TSeparator1 = ttk.Separator(self.Frame1)
        self.TSeparator1.place(relx=0.506, rely=0.732,  relheight=0.101)
        self.TSeparator1.configure(orient="vertical")
        top.mainloop()

    '''def verificaCadastro(self):
         usuarioCorreto = "admin"
         senhaCorreta = "1234"
      
         if self.Entry1.get() == "admin" and self.Entry2.get() == "1234":
            print("Usuário logado")
         else:
            print("Usuário/Senha incorretos")'''


Toplevel1()   





