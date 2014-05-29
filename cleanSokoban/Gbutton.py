# -- coding: utf-8 --

from tkinter import *

class Gbutton(Button):
    def __init__(self, row, column, n1, n2, n3):
        self.row = row
        self.column = column
        Button.__init__(self, n1, text=n2, command=lambda:
        n3.dostuff(row, column))
