"""
Módulo único do pacote view.
Responsável por desenhar a tela do jogo.
"""

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
        "*": "black", # pedras de resposta
        "#": "white"
}

def inicia(canvas):
    """
    Função simples que inicializa o pacote view. Recebe e guarda o canvas
    criado na inicialização do programa.
    """
    global cnv
    cnv = canvas


def draw():
    """
    Função que efetivamente desenha o tabuleiro e seus conteúdos na tela.
    Antes de desenhar, a função apaga a tela e redesenha o tabuleiro.
    """
    global cnv, m_cores

    cnv.delete("all") # limpa a tela

    # Loop responsável por desenhar as 13 fileiras de pedras do jogo.
    # A primeira fileira é a senha, que só é revelada no fim da partida.
    # Os retangulos que demarcam todas as fileiras sao desenhados. Porem, apenas
    # os circulos da fileira de senha de das tentativas possiveis de acordo com
    # a dificuldade sao desenhados.
    for i in range(13): # 'i' representa a linha atual
        # Marca a fileira da tentativa atual com um marro mais escuro
        if i == 12-game_state.get_qtd_jogadas() and game_state.estado["partida"] > 0:
            cor = '#92522e'
        else:
            cor = ''

        # Desenha os retangulos das pedras de tentativa e de resposta
        cnv.create_rectangle(65, (i*53)+6, 65+313, ((i+1)*53)+6, fill=cor)
        cnv.create_rectangle(65+315, (i*53)+6, 65+315+65, ((i+1)*53)+6, fill='')

        # Bloco que desenha as pedras. Apenas pedras de tentativas possiveis,
        # da senha e pedras resposta são desenhadas.

        if not game_state.estado["dificuldade"] is None: # Apenas desenhar se tiver uma dificuldade definida
            for j in range(game_rules.get_valorDif("pedras")): # 'j' seriam colunas, que tem a quantidade de pedras possiveis pela dificuldade
                # Apenas desenhamos pedras da primeira linha (senha) ou das linhas de tentativas possiveis (de acordo com dificuldade)
                if i == 0 or i > 12 - game_rules.get_valorDif("limite"):
                    if i == 0: # Linha da senha
                        # Senha eh revelada apenas se partida acabou
                        if game_state.estado["partida"] < 1:
                            cor = m_cores[game_state.estado["senha"][j]]
                        else:
                            cor = ''
                    # Tentativa ainda nao alcancada, pedras vazias
                    elif i < 12-game_state.get_qtd_jogadas():
                        cor = ''
                    # Tentativa atual, cor das pedras depende ta tentativa atual (dinamica)
                    elif i == 12-game_state.get_qtd_jogadas():
                        cor = m_cores[game_state.estado["tentativa_tmp"][j]]
                    # Tentativa passada, recuperamos as cores da tentativa passade e também desenhamos as pedras de resposta
                    else:
                        cor = m_cores[game_state.estado["tentativas"][abs(i-12)][j]]
                        for x in range(len(game_state.estado["respostas"][abs(i-12)])):
                            r_cor = m_cores[game_state.estado["respostas"][abs(i-12)][x]]
                            cnv.create_oval(65+317+(x%3)*20, i*53+12+(x//3)*20, 65+337+(x%3)*20, i*53+12+(x//3)*20+20, fill=r_cor)

                    cnv.create_oval((j*53)+65+8, (i*53)+6+10, (j*53)+65+53-10, (i*53)+6+53-10, fill=cor)

    # paleta de seleção
    for i in range(2): # coluna
        for j in range(4): # linha
            x = (i*87)+507
            y = (j*87)+42
            c = i*4 + j # cor
            cnv.create_rectangle( x, y, x+87, y+87, fill='')
            # Desenhamos o numero de cores da paleta de acordo com a dificuldade.
            if not game_state.estado["dificuldade"] is None:
                if c < game_rules.get_valorDif("cores"):
                    # Desenhamos um circulo preto atras da cor selecionada para marca-la
                    if c == game_state.estado["cor_selecionada"]:
                        cnv.create_oval(x, y, x+87, y+87, fill="black")
                    cnv.create_oval(x+5, y+5, x+82, y+82, fill=m_cores[c])

    # "ativa" o botao de proxima tentativa, caso cores suficientes forem selecionadas na tentativa
    if not -1 in game_state.estado["tentativa_tmp"][:game_rules.get_valorDif("pedras")]:
        cnv.create_rectangle(507, 348+42+10, 2*87+507, 348+42+87, fill='blue')
        cnv.create_text(507+87, 348+42+50, text="Próxima\ntentativa", fill="yellow",
                font="Times 15 bold")
    # se nao, botao fica "desativado"
    else:
        cnv.create_rectangle(507, 348+42+10, 2*87+507, 348+42+87, fill='black')

    # Mostra mensagens de vitoria/derrota de acordo com o estado da partida
    # Se nao tiver partida em progresso, mostra mensagem pedindo para o jogador começar
    if game_state.estado["partida"] < 1:
        if game_state.estado["partida"] == -1:
            cnv.create_text(507+87, 348+87+70, text="VOCÊ GANHOU!", fill="green",
                    font="Times 20 bold")
        elif game_state.estado["partida"] == -2:
            cnv.create_text(507+87, 348+87+70, text="VOCÊ PERDEU", fill="red",
                    font="Times 20 bold")

        cnv.create_text(507+87, 348+87+120, fill="black", font="Times 12 bold",
                text="Inicie uma partida nova ou carregue\n uma antiga na barra de menu do jogo.")

