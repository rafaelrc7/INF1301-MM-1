#!/usr/bin/env python3

# Caio Coutinho Palmieri
# Gustavo Zalcman
# Rafael Ribeiro de Carvalho

import tkinter
from view import draw_canvas
from model import game_state
from controller import event_handler

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
partida.add_command(label="Salvar", command=game_state.salvar)
partida.add_command(label="Carregar", command=event_handler.load_event)

nova_partida=tkinter.Menu(menu)
nova_partida.add_command(label="Fácil", command=event_handler.njogo["facil"])
nova_partida.add_command(label="Médio", command=event_handler.njogo["medio"])
nova_partida.add_command(label="Difícil", command=event_handler.njogo["dificil"])

menu.add_cascade(label="Nova Partida...", menu=nova_partida)
menu.add_cascade(label="Partida...", menu=partida)
root.configure(menu=menu)

canvas.focus_set()
canvas.pack()
root.mainloop()
