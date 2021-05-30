__all__ = ['estado', 'nova_partida', 'get_qtd_jogadas']

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
