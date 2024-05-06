from tkinter import*
from random import*
from EGN_Calculator import*
#This is the ENGLISH translation of the GUI "frontend". The actual calculations happen in the EGN_Calculator.py file.
tk = Tk()

tk.title("EGN GENERATOR - EN VERSION // ЕГН ГЕНЕРАТОР - АНГЛИЙСКА ВЕРСИЯ")
tk.geometry("400x400")

About = Label(tk, text = "EGN CALCULATOR \n MADE BY GAMELINE")
About.grid()

tk.mainloop()
