# Caio Coutinho Palmieri
# Gustavo Zalcman
# Rafael Ribeiro de Carvalho
"""
Módulo do pacote controller que recebe e trata dos eventos do jogo, principalmente
cliques na tela.
"""
__all__ = ['click_event', 'esc_event', 'load_event', 'njogo']

from model import game_rules
from model import game_state
from view import draw_canvas

def click_event(event):
    """Recebe evento de click e chama a função que trata dos cliques, depois
    redesenha a tela."""
    click(event)
    draw_canvas.draw()


def esc_event(event):
    """Recebe e trata o evento de quando o jogador apertar esc e então redesenha
    a tela."""
    game_state.estado["cor_selecionada"] = -1
    draw_canvas.draw()


def load_event():
    """Recebe e trata o evento de quando o jogador quer carregar uma partida
    e então redesenha a tela."""
    game_state.carregar()
    draw_canvas.draw()


def click(event):
    """Função principal do módulo que trata dos eventos de clique na tela,
    tratando de acordo com o lugar do clique e estado atual do jogo."""
    x=event.x
    y=event.y

    if (game_state.estado["partida"] > 0): # Checa se partida esta em progresso
        # Checa se click aconteceu na paleta, se sim muda a cor selecionada para
        # qual foi clicada. Apenas cores disponiveis na dificuldade sao selecionaveis
        if x > 507 and x < 507+2*87 and y > 42 and y < 42 + 87*4:
            for i in range(2): # coluna
                for j in range(4): # linha
                    xc = (i*87)+507
                    yc = (j*87)+42
                    c = i*4 + j
                    if x > xc and x < xc+87 and y > yc and y < yc+87 and c < game_rules.get_valorDif("cores"):
                        game_state.estado["cor_selecionada"] = c
                        return

        # Se uma cor estiver selecionada e o jogador clicar numa posicao da
        # tentativa atual, atualiza.
        yf = (11-game_state.get_qtd_jogadas()) * 53 + 65+8
        if game_state.estado["cor_selecionada"] != -1 and y > yf and y < yf+87:
            for i in range(game_rules.get_valorDif("pedras")):
                xf = i*53 + 65+8
                if x > xf and x < xf+53:
                    game_state.estado["tentativa_tmp"][i] = game_state.estado["cor_selecionada"]
                    break

        # Se todas as cores suficientes para a tentativa forem selecionadas, o
        # botao para a avançar o jogo eh ativado. Aqui checa se o player clicou
        # nele. Se sim, a tentativa atual é testada, o jogo avança e a tentativa
        # é zerada novamente.
        if not -1 in game_state.estado["tentativa_tmp"][:game_rules.get_valorDif("pedras")]:
            if x > 507 and x < 2*87+507 and y > 348+42+10 and 348+42+87:
                game_rules.compara_tentativa(game_state.estado["tentativa_tmp"][:game_rules.get_valorDif("pedras")])
                game_state.estado["tentativa_tmp"] = [-1] * 6
                game_state.estado["partida"] = game_rules.testa_tentativa()


        # Reseta a cor selecionada para nenhuma.
        if game_state.estado["cor_selecionada"] != -1:
            game_state.estado["cor_selecionada"] = -1


def njogo_facil():
    game_state.nova_partida(0)
    draw_canvas.draw()


def njogo_medio():
    game_state.nova_partida(1)
    draw_canvas.draw()


def njogo_dificil():
    game_state.nova_partida(2)
    draw_canvas.draw()


njogo = {
    "facil": njogo_facil,
    "medio": njogo_medio,
    "dificil": njogo_dificil
}

