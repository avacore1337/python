# -- coding: utf-8 --

# you need to install python tkinter
# sudo apt-get install python-tk
# sudo apt-get install python*3*-tk for python3
# sublimeREPL is needed for mac and windows. It's nice for linux
# it's tkinter on mac and in python3, not Tkinter

from tkinter import *
from Board import Board


class App:
            
    def __init__(self, master):
        self.master = master
        self.frame = Frame(master)
        self.buttons=[]
        self.board = Board()
        self.createButtonMatrix()
        self.update()

    def createButtonMatrix(self):
        for row in range(self.board.numberOfRows):
            buttonColumn = []
            for column in range(self.board.numberOfColumns):
                button = self.createButtonInMatrix(row,column)
                buttonColumn.append(button)
            self.buttons.append(buttonColumn)

    def createButtonInMatrix(self,row,column):
        buttonFunction = lambda row=row, column=column:self.click(row,column)
        button = Button(self.master, text="", command = buttonFunction)
        button.grid(row=row, column=column)
        button.config(height=1, width= 1)
        return button

    def click(self, row, column):
        self.board.dostuff(row,column)
        self.update()

    def update(self):
        for x in range(self.board.numberOfRows):
            for y in range(self.board.numberOfColumns):
                self.buttons[x][y].config(text=self.board.nodes[x][y].value)

def main():
    root = Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()


