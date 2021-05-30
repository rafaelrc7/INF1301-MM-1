__all__ = ['inicia', 'draw']

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
        "*": "black",
        "#": "white"
}

def inicia(canvas):
    global cnv
    cnv = canvas
    return

def draw():
    global cnv, m_cores

    cnv.delete("all")

    for i in range(13):
        if i == 12-game_state.get_qtd_jogadas() and game_state.estado["partida"] > 0:
            cor = '#92522e'
        else:
            cor = ''

        cnv.create_rectangle(65, (i*53)+6, 65+313, ((i+1)*53)+6, fill=cor)
        cnv.create_rectangle(65+315, (i*53)+6, 65+315+65, ((i+1)*53)+6, fill='')

        if not game_state.estado["dificuldade"] is None:
            for j in range(game_rules.get_valorDif("pedras")):
                if i == 0 or i > 12 - game_rules.get_valorDif("limite"):
                    if i == 0:
                        if game_state.estado["partida"] < 1:
                            cor = m_cores[game_state.estado["senha"][j]]
                        else:
                            cor = ''
                    elif i < 12-game_state.get_qtd_jogadas():
                        cor = ''
                    elif i == 12-game_state.get_qtd_jogadas():
                        cor = m_cores[game_state.estado["tentativa_tmp"][j]]
                    else:
                        cor = m_cores[game_state.estado["tentativas"][abs(i-12)][j]]
                        for x in range(len(game_state.estado["respostas"][abs(i-12)])):
                            r_cor = m_cores[game_state.estado["respostas"][abs(i-12)][x]]
                            cnv.create_oval(65+315+(x%3)*20, i*53+6+(x//3)*20, 65+335+(x%3)*20, i*53+6+(x//3)*20+20, fill=r_cor)

                    cnv.create_oval((j*53)+65+8, (i*53)+6+10, (j*53)+65+53-10, (i*53)+6+53-10, fill=cor)

    # paleta de seleção
    for i in range(2): # coluna
        for j in range(4): # linha
            x = (i*87)+507
            y = (j*87)+42
            c = i*4 + j
            cnv.create_rectangle( x, y, x+87, y+87, fill='')
            if not game_state.estado["dificuldade"] is None:
                if c < game_rules.get_valorDif("cores"):
                    if c == game_state.estado["cor_selecionada"]:
                        cnv.create_oval(x, y, x+87, y+87, fill="black")
                    cnv.create_oval(x+5, y+5, x+82, y+82, fill=m_cores[c])

    if not -1 in game_state.estado["tentativa_tmp"][:game_rules.get_valorDif("pedras")]:
        cnv.create_rectangle(507, 348+42+10, 2*87+507, 348+42+87, fill='blue')
        cnv.create_text(507+87, 348+42+50, text="Próxima\ntentativa", fill="yellow",
                font="Times 15 bold")
    else:
        cnv.create_rectangle(507, 348+42+10, 2*87+507, 348+42+87, fill='black')

    if game_state.estado["partida"] < 1:
        if game_state.estado["partida"] == -1:
            cnv.create_text(507+87, 348+87+70, text="VOCÊ GANHOU!", fill="green",
                    font="Times 20 bold")
        elif game_state.estado["partida"] == -2:
            cnv.create_text(507+87, 348+87+70, text="VOCÊ PERDEU", fill="red",
                    font="Times 20 bold")

        cnv.create_text(507+87, 348+87+120, fill="black", font="Times 12 bold",
                text="Inicie uma partida nova ou carregue\n uma antiga na barra de menu do jogo.")

