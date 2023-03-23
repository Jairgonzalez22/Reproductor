#Import libreria 
from tkinter import *
import pygame, sys
from pygame.locals import*
from tkinter import filedialog
from PIL import ImageTk, Image


pygame.init() #Este metodo inicia libreria pygame

def OpenSong():
    cancion = filedialog.askopenfilename()
    print(cancion)
    pygame.mixer.music.load(cancion)
    pygame.mixer.music.play()

def PlaySong():
    pygame.mixer.music.play()

def StopSong():
    pygame.mixer.music.stop()


def PauseSong():
    pygame.mixer.music.pause()

def ResumeSong():
    pygame.mixer.music.song()

def VolumenUpper():
    nivelVolumen = pygame.mixer.music.get_volume() + 0.5
    pygame.mixer_music.set_volume(nivelVolumen)

def VolumenLower():
   nivelVolumen  = pygame.mixer.music.get_volume() - 0.7
   pygame.mixer_music.set_volume(nivelVolumen) 



raiz =Tk()
raiz.title("SPOTIFY2.0 MP3 - GUI")
#raiz.iconbintamp() 
raiz.geometry("600x400")
raiz.resizable(0,0)

#Frame - marco
framePrincipal = Frame(raiz,bg="#4d4d4d", width=600, height=400)
framePrincipal.pack(fill="both", expand=1)

tituloReproductor = Label(framePrincipal, text="REPRODUCTOR GUI", bg="#4d4d4d", fg="#f4f4f4", font=("PowerMax", 14))
tituloReproductor.pack()

imagenChida = Image.open("canncion-python.ico")
imagenReproductor = imagenChida.resize((200,150))
img = ImageTk.PhotoImage(imagenReproductor)

tituloImagen = Label(framePrincipal, image=img)
tituloImagen.pack()


#BotonOpenFile
botonOpen = Button((framePrincipal), text="Open", font=("Roboto", 10, "bold"), bg="#E7D40A",fg="#f4f4f4",width=7, height=2, bd=0, command=OpenSong)
botonOpen.place(relx=0.04, rely=0.5)


#BotonPlay
botonPlay = Button((framePrincipal), text="Play", font=("Roboto", 10, "bold"), bg="#42ab49",fg="#f4f4f4",width=7, height=2, bd=0, command=PlaySong )
botonPlay.place(relx=0.23, rely=0.5)


#BotonStop
botonStop = Button((framePrincipal), text="Stop", font=("Roboto", 10, "bold"), bg="#e2504c",fg="#f4f4f4",width=7, height=2, bd=0, highlightthickness=0, command=StopSong)
botonStop.place(relx=0.42 , rely=0.5)

#BotonPause 
botonPause = Button((framePrincipal), text="Pause", font=("Roboto", 10, "bold"), bg="#23BAC4",fg="#f4f4f4",width=7, height=2, bd=0, highlightthickness=0, command=PauseSong)
botonPause.place(relx=0.61, rely=0.5)

#BotonContinue
botonResume = Button((framePrincipal), text="Resume", font=("Roboto", 10, "bold"), bg="#024A86",fg="#f4f4f4",width=7, height=2, bd=0, highlightthickness=0, command=ResumeSong)
botonResume.place(relx=0.8, rely=0.5)

#BotonVolumen+
botonResume = Button((framePrincipal), text="Volumen +", font=("Roboto", 10, "bold"), bg="#024A86",fg="#f4f4f4",width=10, height=2, bd=0, highlightthickness=0, command=VolumenUpper)
botonResume.place(relx=0.1, rely=0.7)

#BotonVolumen-
botonResume = Button((framePrincipal), text="Volumen -", font=("Roboto", 10, "bold"), bg="#024A86",fg="#f4f4f4",width=10, height=2, bd=0, highlightthickness=0, command=VolumenLower)
botonResume.place(relx=0.7, rely=0.7)



raiz.mainloop()


