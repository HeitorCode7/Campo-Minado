import tkinter as tk

class MeuBotao(tk.Button):
    def __init__(self, master, x, y, number=0, *args, **kwargs):
        super(MeuBotao, self).__init__(
                master, *args, **kwargs, width=3, font='Calibri 15 bold')
        self.x = x
        self.y = y
        self.numero = number
        self.e_bomba = False
        self.contagem_bomba = 0
        self.foi_aberto = False
    
    def __repr__(self):
        return f'MeuBotao{self.x} {self.y} {self.numero} {self.e_bomba}'
