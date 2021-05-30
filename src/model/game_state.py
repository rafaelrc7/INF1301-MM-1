__all__ = ['estado', 'nova_partida', 'get_qtd_jogadas', 'carregar', 'salvar']

import json
from model import game_rules

estado = {
    "partida": 0,
    "cor_selecionada": -1,
    "tentativa_tmp": [-1, -1, -1, -1, -1, -1],
    "dificuldade": None,
    "tentativas": [],
    "respostas": [],
    "senha": []
}

def nova_partida(dificuldade):
    """Define a dificuldade atual de acordo com o argumento recebido e inicia
    uma partida nova"""
    global estado

    estado.update (
        partida = 1,
        cor_selecionada = -1,
        tentativa_tmp = [-1, -1, -1, -1, -1, -1],
        dificuldade = dificuldade,
        tentativas = [],
        respostas = [],
        senha = []
    )

    game_rules.gen_senha()

def get_qtd_jogadas():
    global estado
    return len(estado["tentativas"])

# Carregar/Salvar estado do jogo

def salvar():
    """Salva o atual estado de uma partida em um arquivo json que pode ser carregado
    para continuar de onde o jogador parou."""
    global estado
    if not estado is None:
        fp = open("partida_mm.json", "w")
        json.dump(estado, fp)
        fp.close()


def carregar():
    """Carrega a partida salva em um arquivo json."""
    global estado
    fp = open("partida_mm.json", "r")
    estado = json.load(fp)
    fp.close()

