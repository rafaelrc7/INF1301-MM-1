from controller import event_handler
from model import game_rules
from model import game_state

cnv = None

m_cores = {
        -1: "",
        0: "red",
        1: "blue",
        2: "green",
        3: "yellow",
        4: "magenta",
        5: "cyan",
        6: "#ff872b", # laranja
        7: "#3d1500", # marrom
        }

def inicia(canvas):
    global cnv
    cnv = canvas
    return

def draw():
    global cnv, m_cores
    cnv.delete("all")
    for i in range(13):
        if i == 12-game_rules.get_tentativas():
            cor = '#92522e'
        else:
            cor = ''
        cnv.create_rectangle(65, (i*53)+6, 65+313, ((i+1)*53)+6, fill=cor)
        cnv.create_rectangle(65+315, (i*53)+6, 65+315+65, ((i+1)*53)+6, fill='')
        if not game_rules.get_dif() is None:
            for j in range(game_rules.get_valorDif("pedras")):
                if i == 0 or i > 12 - game_rules.get_valorDif("limite"):
                    if i < 12-game_rules.get_tentativas():
                        cor = ''
                    elif i == 12-game_rules.get_tentativas():
                        cor = m_cores[game_state.get_estado()["tentativa_tmp"][j]]
                    else:
                        cor = m_cores[game_rules.m_dados["tentativas"][abs(i-12)][j]]

                    cnv.create_oval((j*53)+65+8, (i*53)+6+10, (j*53)+65+53-10, (i*53)+6+53-10, fill=cor)

    # paleta de seleção
    for i in range(2): # coluna
        for j in range(4): # linha
            x = (i*87)+507
            y = (j*87)+42
            c = i*4 + j
            cnv.create_rectangle( x, y, x+87, y+87, fill='')
            if not game_rules.get_dif() is None:
                if c < game_rules.get_valorDif("cores"):
                    if c == game_state.get_estado()["cor_selecionada"]:
                        cnv.create_oval(x, y, x+87, y+87, fill="black")
                    cnv.create_oval(x+5, y+5, x+82, y+82, fill=m_cores[c])

    if not -1 in game_state.get_estado()["tentativa_tmp"][:game_rules.get_valorDif("pedras")]:
        cnv.create_rectangle(507, 348+42+10, 2*87+507, 348+42+87, fill='blue')
    else:
        cnv.create_rectangle(507, 348+42+10, 2*87+507, 348+42+87, fill='black')

    return
