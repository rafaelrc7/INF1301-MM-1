__all__ = ["estado", 'nova_partida', 'get_qtd_jogadas']

from model import game_rules

estado = {
    "partida": False,
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
    estado["partida"] = True
    estado["cor_selecionada"] = -1
    estado["tentativa_tmp"] = [-1, -1, -1, -1, -1, -1]
    estado["dificuldade"] = dificuldade
    game_rules.gen_senha()

def get_qtd_jogadas():
    return len(estado["tentativas"])
