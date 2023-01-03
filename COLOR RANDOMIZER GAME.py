# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 13:01:14 2023

@author: Swasti
"""

from tkinter import *
import random

root = Tk()
root.title("Encapsulation")
root.geometry("400x300")
root.config(bg = "White")

lbl_color = Label(root, font = ("Comic Sans MS", 20, "bold"), bg = "White")
lbl_color.place(relx = 0.5, rely = 0.4, anchor = CENTER)

class Score():
    
    def __init__(self):
        self.__score = 0
        
    def updateScore(self):
        self.text = ["BLUE", "TEAL", "GREEN", "ORANGE", "PINK", "RED", "YELLOW", "PURPLE", "BROWN", "GREY", "BLACK"]
        self.random_no_text = random.randint(0, 10)
        
        self.color = ["blue", "teal", "green", "orange", "pink", "red", "yellow", "purple", "brown", "grey", "black"]
        self.random_no_color = random.randint(0, 10)
        
        lbl_color["text"] = self.text[self.random_no_text]
        lbl_color["fg"] = self.color[self.random_no_color]

obj = Score()
        
btn = Button(root, text = "Start", command = obj.updateScore, relief = FLAT, bg = "#C39BD3", fg = "White", padx = 10, pady = 1, font = ("Arial", 15))
btn.place(relx = 0.6, rely = 0.8, anchor = CENTER)

root.mainloop()