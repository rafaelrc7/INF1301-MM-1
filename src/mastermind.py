#!/usr/bin/env python3

import tkinter
from view import draw_canvas
from model import game_rules
from controller import event_handler

def njogo_facil():
    game_rules.def_dificuldade(0)
    draw_canvas.draw(canvas)

def njogo_medio():
    game_rules.def_dificuldade(1)
    draw_canvas.draw(canvas)

def njogo_dificil():
    game_rules.def_dificuldade(2)
    draw_canvas.draw(canvas)


root = tkinter.Tk(className="Mastermind")
root.geometry("745x700")
root.resizable(False, False)

game_rules.novo_jogo()

canvas = tkinter.Canvas(root, bg="#c58561", width=745, height=700)
canvas.bind('<ButtonRelease-1>', event_handler.click)
draw_canvas.inicia()
draw_canvas.draw(canvas)

menu=tkinter.Menu(root)

partida=tkinter.Menu(menu)
partida.add_command(label="Salvar", command=game_rules.salvar)
partida.add_command(label="Carregar", command=game_rules.carregar)

nova_partida=tkinter.Menu(menu)
nova_partida.add_command(label="Fácil", command=njogo_facil)
nova_partida.add_command(label="Médio", command=njogo_medio)
nova_partida.add_command(label="Difícil", command=njogo_dificil)

menu.add_cascade(label="Nova Partida...", menu=nova_partida)
menu.add_cascade(label="Partida...", menu=partida)
root.configure(menu=menu)

canvas.pack()
root.mainloop()
