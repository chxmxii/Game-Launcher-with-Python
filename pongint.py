import tkinter as tk
import os 
import pygame
from tkinter import messagebox
from PIL import Image, ImageTk

#Commands
pygame.mixer.init()
def playovso():
 pipe=os.popen("Pong.py")
 pipe=os.popen("Compteur.py")

def playvsb():
 pipe=os.popen("pongai.py")
 pipe=os.popen("Compteur.py")

def quitc():
    pipe=os.popen("Glauncher.py")
    mw.destroy()
    pygame.mixer.music.load("uni.mp3") #Loading File Into Mixer
    pygame.mixer.music.Stop()
def play():
    pygame.mixer.music.load("uni.mp3") #Loading File Into Mixer
    pygame.mixer.music.play() #Playing It In The Whole Device
while pygame.mixer.music.get_busy() == True: #looping the music file
                continue
def stop():
    pygame.mixer.music.load("uni.mp3") #Loading File Into Mixer
    pygame.mixer.music.Stop() #Stop It In The Whole Device
    
mw = tk.Tk()
mw.title('Pong')

back=tk.Frame(master=mw, width=900, height=600, bg='black')
back.pack_propagate(0) 
back.pack(fill=tk.BOTH, expand=1) #Adapts the size to the window

#Image logo mt3 game launcher

#filename = tk.PhotoImage(file = "Game.png")
#background_label = tk.Label(mw, image=filename)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)

load = Image.open("ponglog.png")
render = ImageTk.PhotoImage(load)
img = tk.Label(mw, image=render, bg='black')
img.image = render
img.place(x=1, y=1, relwidth=1, relheight=0.5)

#Adding music




#Menu bar

menubar = tk.Menu(mw)
about = tk.Menu(menubar, tearoff=0)
about.add_command(label="Exit", command=mw.destroy)
menubar.add_cascade(label='Exit', menu=about)
mw.config(menu=menubar)


#Buttons and commands

Playovo = tk.Button(master=back, text='Play one vs one', command= playovso,width='100', borderwidth=3, bg='Ivory', activebackground='Light gray')
Playovo.pack()
Playovo.place(relx=0.5, rely=0.5, anchor="n")
Playovb = tk.Button(master=back, text='Play vs BOT ', command= playvsb,width='100', borderwidth=3, bg='Light gray', activebackground='Ivory')
Playovb.pack()
Playovb.place (relx =0.5, rely=0.6,anchor='center')
close = tk.Button(master=back, text='Back to menu', command= quitc,width='100', borderwidth=3, bg='Ivory', activebackground='Light gray')
close.pack()
close.place (relx =0.5, rely=0.7,anchor='s')

Music = tk.Button(mw,text="Enable music",command=play,borderwidth=2, bg='Light gray', activebackground='Ivory')
Music.pack()
Music.place (relx =0.4, rely=0.8,anchor='s')
Music = tk.Button(mw,text="Disable music",command=stop,borderwidth=2, bg='Ivory', activebackground='crimson')
Music.pack()
Music.place (relx =0.6, rely=0.8,anchor='s')

pygame.mixer.music.load("uni.mp3") 
pygame.mixer.music.play() 



mw.mainloop()
