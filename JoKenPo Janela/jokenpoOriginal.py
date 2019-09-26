#importando bibliotecas
from tkinter import *
from pygame import mixer
from random import randint

cliques = 0
Jogador1 = 0
Jogador2 = 0
regras = 0
solo = 0

def pagina_Solo():
  global solo
  if solo == 0:
    solo = Toplevel()
    solo.geometry('600x519+700+50')
    solo.title("Jo - Ken - Pô / Jogar Solo")

def pagina_regras():
  global regras
  if regras == 0:
    regras = Toplevel()
    regras.geometry('723x446+100+600')
    regras.title("Jo - Ken - Pô / Regras")

    imagemRegras = PhotoImage(file="regras.png")
    fundoRegras = Label(regras, image=imagemRegras)
    fundoRegras.place(x=0, y=0, relwidth=1, relheight=1)
    regras.mainloop()

principal = Tk()
principal.geometry('600x519+100+50')
principal.title("Jo - Ken - Pô")

imagemArquivo = PhotoImage(file="jokenpoChuck.png")
imagem = Label(principal, image=imagemArquivo)
imagem.place(x=0, y=0, relwidth=1, relheight=1)

botaoSolo = Button(principal,bg="black",activebackground="grey",fg="white",text="Jogar Solo",height=5,width=12,command=pagina_Solo)
botaoSolo.place(x = 130, y = 160)

botaoMultijogador = Button(principal,bg="black",activebackground="grey",fg="white",text="Jogador VS Jogador",height=5,width=14,command=pagina_regras)
botaoMultijogador.place(x = 340, y = 160)

botaoRegras = Button(principal,bg="black",activebackground="grey",fg="white",text="Regras",height=5,width=14,command=pagina_regras)
botaoRegras.place(x = 226, y = 270)

mixer.init()
mixer.music.load("8bit.mp3")
mixer.music.play(-1)
principal.mainloop()