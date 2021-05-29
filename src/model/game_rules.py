__all__ = ['novo_jogo', 'gen_senha', 'compara_tentativa', 'testa_tentativa', 'get_valorDif']

from random import randint
import json
from model import game_state
from view import draw_canvas

m_resposta = []

# Dicionário com constantes relacionadas a cada dificuldade
valores_dif = {
    0: {"pedras": 4, "cores": 6, "limite": 8},
    1: {"pedras": 5, "cores": 7, "limite": 10},
    2: {"pedras": 6, "cores": 8, "limite": 12}
}

# Gera uma senha aleatoriamente, de acordo com a dificuldade definida
def gen_senha():
    """Gera uma senha com tamanho e cores de acordo com a atual dificuldade."""

    for i in range(valores_dif[game_state.estado["dificuldade"]]["pedras"]):
        game_state.estado["senha"].append(randint(0, valores_dif[game_state.estado["dificuldade"]]["cores"]-1))

# Compara a tentiva do jogador com a senha atual, retornando uma lista com as pedras resposta
def compara_tentativa(tentativa):
    """Compara a tentativa do jogador com a senha e cria uma resposta que será retornada."""

    senha = game_state.estado["senha"].copy()
    m_resposta = []

    game_state.estado["tentativas"].append(tentativa[:])

    for pos, pedra in enumerate(tentativa):
        if senha[pos] == pedra:
            m_resposta.append("*")
            senha[pos] = -1
            tentativa[pos] = -2

    for pos, pedra in enumerate(tentativa):
        if pedra in senha:
            m_resposta.append("#")
            senha[senha.index(pedra)] = -1
            tentativa[pos] = -2

    game_state.estado["respostas"].append(m_resposta[:])

    return m_resposta

# Checa o estado atual do jogo, se acabou (em vitória ou derrota) ou não
def testa_tentativa():
    """Testa se a partida acabou e, no caso, se o jogador perdeu ou ganhou."""

    if game_state.estado["resposta"] == ['*']*valores_dif[game_state.estado["dificuldade"]]["pedras"]:
        return 1

    if game_state.game_state.get_qtd_jogadas() > valores_dif[game_state.estado["dificuldade"]]["limite"]-1:
        return -1

    return 0

# 'Getters'

def get_valorDif(valor):
    """Retorna um dos valores de regra relacionados à dificuldade atual.

    Valores possíveis de argumento:
        "pedras" -- Retorna o número máximo de pedras da senha
        "cores"  -- Retorna o número de cores diferentes possíveis
        "limite" -- Retorna o número máximo de tentativas
    """
    global valores_dif
    if game_state.estado["dificuldade"] is None:
        return -1
    return valores_dif[game_state.estado["dificuldade"]][valor]

# Carregar/Salvar estado do jogo

def salvar():
    """Salva o atual estado de uma partida em um arquivo json que pode ser carregado
    para continuar de onde o jogador parou."""
    if not game_state.estado is None:
        fp = open("partida_mm.json", "w")
        json.dump(game_state.estado, fp)
        fp.close()


def carregar():
    """Carrega a partida salva em um arquivo json."""
    global m_resposta
    fp = open("partida_mm.json", "r")
    game_state.estado = json.load(fp)
    fp.close()

    game_state.estado["partida"] = True
    game_state.estado["cor_selecionada"] = -1
    game_state.estado["tentativa_tmp"] = [-1, -1, -1, -1, -1, -1]

    m_resposta = []


