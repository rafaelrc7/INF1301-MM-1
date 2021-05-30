#!/usr/bin/env python3

import tkinter
from view import draw_canvas
from model import game_rules
from model import game_state
from controller import event_handler

def njogo_facil():
    game_state.nova_partida(0)
    draw_canvas.draw()

def njogo_medio():
    game_state.nova_partida(1)
    draw_canvas.draw()

def njogo_dificil():
    game_state.nova_partida(2)
    draw_canvas.draw()


root = tkinter.Tk(className="Mastermind")
root.geometry("745x700")
root.resizable(False, False)

canvas = tkinter.Canvas(root, bg="#c58561", width=745, height=700)
canvas.bind('<ButtonRelease-1>', event_handler.click_event)
canvas.bind('<Escape>', event_handler.esc_event)
draw_canvas.inicia(canvas)
draw_canvas.draw()

menu=tkinter.Menu(root)

partida=tkinter.Menu(menu)
partida.add_command(label="Salvar", command=game_rules.salvar)
partida.add_command(label="Carregar", command=event_handler.load_event)

nova_partida=tkinter.Menu(menu)
nova_partida.add_command(label="Fácil", command=njogo_facil)
nova_partida.add_command(label="Médio", command=njogo_medio)
nova_partida.add_command(label="Difícil", command=njogo_dificil)

menu.add_cascade(label="Nova Partida...", menu=nova_partida)
menu.add_cascade(label="Partida...", menu=partida)
root.configure(menu=menu)

canvas.focus_set()
canvas.pack()
root.mainloop()
