""""
Módulo do pacote Model responsável pelas regras do jogo. Aqui é implementado
a parte lógica do funcionamento do jogo.
"""
__all__ = ['gen_senha', 'compara_tentativa', 'testa_tentativa', 'get_valorDif']

from random import randint
from model import game_state

# Dicionário com constantes relacionadas a cada dificuldade
valores_dif = {
    0: {"pedras": 4, "cores": 6, "limite": 8},
    1: {"pedras": 5, "cores": 7, "limite": 10},
    2: {"pedras": 6, "cores": 8, "limite": 12}
}

def gen_senha():
    """Gera uma senha com tamanho e cores de acordo com a atual dificuldade."""

    for i in range(valores_dif[game_state.estado["dificuldade"]]["pedras"]):
        game_state.estado["senha"].append(randint(0, valores_dif[game_state.estado["dificuldade"]]["cores"]-1))


def compara_tentativa(tentativa):
    """Compara a tentativa do jogador, recebida como parâmetro, com a senha e
    cria uma resposta que será retornada e guardada no estado do jogo."""

    # Copia a senha, para poder editar sem afetar a senha do jogo
    senha = game_state.estado["senha"].copy()
    resposta = []

    # Salva a tentativa atual para poder ser acessada posteriormente
    game_state.estado["tentativas"].append(tentativa[:])

    # Procura por pedras de cor certa na posicao certa
    for pos, pedra in enumerate(tentativa):
        if senha[pos] == pedra:
            resposta.append("*")
            # Marca cores da senha e tentativa casadas
            senha[pos] = -1
            tentativa[pos] = -2

    # Procura por pedras de cor certa na posicao errada
    for pos, pedra in enumerate(tentativa):
        if pedra in senha:
            resposta.append("#")
            # Marca cores da senha e tentativa casadas
            senha[senha.index(pedra)] = -1
            tentativa[pos] = -2

    # Salva a resposta para tambem ser acessada posteriormente e retorna
    game_state.estado["respostas"].append(resposta[:])

    return resposta


def testa_tentativa():
    """Testa se a partida acabou e, no caso, se o jogador perdeu ou ganhou e
    então atualiza o estado do jogo.

    Retornos possíveis:
        -1 -> vitória
        -2 -> derrota
         1 -> partida continua em progresso
    """

    if game_state.estado["respostas"][-1] == ['*']*valores_dif[game_state.estado["dificuldade"]]["pedras"]:
        return -1

    if game_state.get_qtd_jogadas() > valores_dif[game_state.estado["dificuldade"]]["limite"]-1:
        return -2

    return 1


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

