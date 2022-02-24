import pygame
import tkinter as tk
from tkinter.filedialog import askdirectory
import os

musicPlayer = tk.Tk()
musicPlayer.title("Music Player")
musicPlayer.geometry("450 x 350")

directory = askdirectory()
os.chdir(directory)
songList = os.listdir()
playList = tk.Listbox(musicPlayer, font="Helvetica 12 bold",
                      bg="yellow", selectmode=tk.SINGLE)

for item in songList:
    pos = 0
    playList.insert(pos, item)
    pos = pos + 1

pygame.init()
pygame.mixer.init()
