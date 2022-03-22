import tkinter as tk
import os 
import pygame
from tkinter import messagebox
from PIL import Image, ImageTk

pygame.mixer.init()
#Commands
def Pong():
 pipe=os.popen("pongint.py")
 mw.destroy()
 pygame.mixer.music.load("xeno.mp3") 
 pygame.mixer.music.Stop()
def TicTacToe():
 pipe=os.popen("tictactoe.py")
def Connect():
 pipe=os.popen("cinter.py")
 mw.destroy()
 pygame.mixer.music.load("xeno.mp3") 
 pygame.mixer.music.Stop()
def gibbonga():
    pipe=os.popen("gibbonga.py")
    pygame.mixer.music.load("xeno.mp3") 
    pygame.mixer.music.Stop()
def crd():
    messagebox.showinfo('Game launcher v 1.0.0','Written by Chamsi mouhib & Guessmi nesrine .')
def play():
    pygame.mixer.music.load("xeno.mp3") #Loading File Into Mixer
    pygame.mixer.music.play() #Playing It In The Whole Device
while pygame.mixer.music.get_busy() == True: #looping the music file
                continue
def stop():
    pygame.mixer.music.load("xeno.mp3") #Loading File Into Mixer
    pygame.mixer.music.Stop() #Stop It In The Whole Device

mw = tk.Tk()
mw.title('Game launcher')

back=tk.Frame(master=mw, width=900, height=600, bg='black')
back.pack_propagate(0) 
back.pack(fill=tk.BOTH, expand=1) #Adapts the size to the window

load = Image.open("Game.png")
render = ImageTk.PhotoImage(load)
img = tk.Label(mw, image=render, bg='black')
img.image = render
img.place(x=1, y=1, relwidth=1, relheight=0.5)

#Menu bar

menubar = tk.Menu(mw)
about = tk.Menu(menubar, tearoff=0)
about.add_command(label="Bonus", command =gibbonga)
about.add_command(label="Credits", command=crd)
about.add_separator()
about.add_command(label="Exit", command=mw.destroy)
menubar.add_cascade(label='About', menu=about)
mw.config(menu=menubar)


#Buttons and commands

Pong = tk.Button(master=back, text='Pong', command= Pong,width='100', borderwidth=3, bg='Light gray', activebackground='Lightblue')
Pong.pack()
Pong.place(relx=0.5, rely=0.5, anchor="n")
Tic = tk.Button(master=back, text='TicTacToe', command= TicTacToe,width='100', borderwidth=3, bg='gray', activebackground='lightblue')
Tic.pack()
Tic.place (relx =0.5, rely=0.6,anchor='center')
Connect = tk.Button(master=back, text='Connect4', command= Connect,width='100', borderwidth=3, bg='Light gray', activebackground='lightblue')
Connect.pack()
Connect.place (relx =0.5, rely=0.7,anchor='s')
close = tk.Button(master=back, text='Quit', command=mw.destroy,width='100', borderwidth=3, bg='gray', activebackground='lightblue')
close.pack()
close.place (relx =0.5, rely=0.8,anchor='s')
##PATCH 1.0.0
info = tk.Label(master=back, text='Game launcher version 1.0.0 ', bg='black', fg='white')
info.pack()
info.place (relx =0.0, rely=1,anchor='sw')
##
Music = tk.Button(mw,text="Enable music",command=play,borderwidth=2, bg='Gray', activebackground='lightgreen')
Music.pack()
Music.place (relx =0.4, rely=0.9,anchor='s')
Music = tk.Button(mw,text="Disable music",command=stop,borderwidth=2, bg='Light gray', activebackground='crimson')
Music.pack()
Music.place (relx =0.6, rely=0.9,anchor='s')

pygame.mixer.music.load("xeno.mp3") 
pygame.mixer.music.play()
mw.mainloop()
