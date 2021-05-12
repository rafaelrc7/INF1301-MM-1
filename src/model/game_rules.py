__all__ = ['def_dificuldade', 'gen_senha', 'compara_tentativa', 'testa_tentativa', 'get_dif', 'get_sen', 'get_valorDif', 'get_tentativas']

from random import randint
import json

# Dicionário com constantes relacionadas a cada dificuldade
valores_dif = {
    0: {"pedras": 4, "cores": 6, "limite": 8},
    1: {"pedras": 5, "cores": 7, "limite": 10},
    2: {"pedras": 6, "cores": 8, "limite": 12}
}

# Define, usando globais do módulo, a dificuldade da partida e reinicia valores relacionados.
def def_dificuldade(dificuldade):
    """Define a dificuldade atual de acordo com o argumento recebido e inicia
    uma partida nova"""
    global m_dificuldade, m_quantidade_jogadas, m_senha, m_resposta, m_dados

    m_dificuldade = dificuldade
    m_quantidade_jogadas = 0
    m_senha = []
    m_resposta = []

    m_dados = {
        "dificuldade": dificuldade,
        "tentativas": [],
        "respostas": [],
        "senha": []
    }


# Gera uma senha aleatoriamente, de acordo com a dificuldade definida
def gen_senha():
    """Gera uma senha com tamanho e cores de acordo com a atual dificuldade."""
    global m_dificuldade, m_senha, m_dados

    for i in range(valores_dif[m_dificuldade]["pedras"]):
        m_senha.append(randint(0, valores_dif[m_dificuldade]["cores"]-1))

    m_dados["senha"] = m_senha

# Compara a tentiva do jogador com a senha atual, retornando uma lista com as pedras resposta
def compara_tentativa(tentativa):
    """Compara a tentativa do jogador com a senha e cria uma resposta que será retornada."""
    global m_quantidade_jogadas, m_senha, m_resposta, m_dados

    senha = m_senha.copy()
    m_resposta = []

    m_dados["tentativas"].append(tentativa[:])

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

    m_quantidade_jogadas += 1

    m_dados["respostas"].append(m_resposta[:])

    return m_resposta

# Checa o estado atual do jogo, se acabbou (em vitória ou derrota) ou não
def testa_tentativa():
    """Testa se a partida acabou e, no caso, se o jogador perdeu ou ganhou."""
    global m_dificuldade, m_quantidade_jogadas, m_resposta

    if m_resposta == ['*']*valores_dif[m_dificuldade]["pedras"]:
        return 1

    if m_quantidade_jogadas > valores_dif[m_dificuldade]["limite"]-1:
        return -1

    return 0

# 'Getters'

def get_tentativas():
    """Retorna o número de tentativas já feitas."""
    global m_quantidade_jogadas
    return m_quantidade_jogadas

def get_dif():
    """Retorna o nível de dificuldade atual."""
    global m_dificuldade
    return m_dificuldade

def get_sen():
    """Retorna a senha atual."""
    global m_senha
    return m_senha

def get_valorDif(valor):
    """Retorna um dos valores de regra relacionados à dificuldade atual.

    Valores possíveis de argumento:
        "pedras" -- Retorna o número máximo de pedras da senha
        "cores"  -- Retorna o número de cores diferentes possíveis
        "limite" -- Retorna o número máximo de tentativas
    """
    global m_dificuldade
    return valores_dif[m_dificuldade][valor]

# Carregar/Salvar estado do jogo

def salvar (arq):
    """Salva o atual estado de uma partida em um arquivo json que pode ser carregado
    para continuar de onde o jogador parou."""
    global m_dados
    fp = open(arq+".json", "w")
    json.dump(m_dados, fp)
    fp.close()


def carregar (arq):
    """Carrega a partida salva em um arquivo json."""
    global m_dados, m_senha, m_dificuldade, m_quantidade_jogadas
    fp = open(arq+".json", "r")
    m_dados = json.load(fp)
    fp.close()

    m_senha = m_dados["senha"]
    m_dificuldade = m_dados["dificuldade"]
    m_quantidade_jogadas = len(m_dados["tentativas"])

