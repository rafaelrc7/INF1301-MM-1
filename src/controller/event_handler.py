from model import game_rules
from model import game_state
from view import draw_canvas

def click_event(event):
    click(event)
    draw_canvas.draw()

def load_event():
    game_rules.carregar()
    draw_canvas.draw()

def click(event):
    x=event.x
    y=event.y

    if (game_state.get_estado()["partida"]):
        if x > 507 and x < 507+2*87 and y > 42 and y < 42 + 87*4:
            for i in range(2): # coluna
                for j in range(4): # linha
                    xc = (i*87)+507
                    yc = (j*87)+42
                    c = i*4 + j
                    if x > xc and x < xc+87 and y > yc and y < yc+87 and c < game_rules.get_valorDif("cores"):
                        game_state.get_estado()["cor_selecionada"] = c
                        return
        yf = (11-game_rules.get_tentativas()) * 53 + 65+8
        if game_state.get_estado()["cor_selecionada"] != -1 and y > yf and y < yf+87:
            for i in range(game_rules.get_valorDif("pedras")):
                xf = i*53 + 65+8
                if x > xf and x < xf+53:
                    game_state.get_estado()["tentativa_tmp"][i] = game_state.get_estado()["cor_selecionada"]
                    break


        if game_state.get_estado()["cor_selecionada"] != -1:
            game_state.get_estado()["cor_selecionada"] = -1

