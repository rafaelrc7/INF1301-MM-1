__all__ = ['def_dificuldade', 'gen_senha', 'compara_tentativa', 'testa_tentativa', 'get_dif', 'get_sen', 'get_valorDif', 'get_tentativas']

from random import randint

valores_dif = {
        0: {"pedras": 4, "cores": 6, "limite": 8},
        1: {"pedras": 5, "cores": 7, "limite": 10},
        2: {"pedras": 6, "cores": 8, "limite": 12}
        }

def def_dificuldade(dificuldade):
    global m_dificuldade, m_quantidade_jogadas, m_senha, m_resposta

    m_dificuldade = dificuldade
    m_quantidade_jogadas = 0
    m_senha = []
    m_resposta = []

def gen_senha():
    global m_dificuldade, m_senha

    for i in range(valores_dif[m_dificuldade]["pedras"]):
        m_senha.append(randint(0, valores_dif[m_dificuldade]["cores"]-1))

def compara_tentativa(tentativa):
    global m_quantidade_jogadas, m_senha, m_resposta

    senha = m_senha.copy()
    m_resposta = []

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

    return m_resposta

def testa_tentativa():
    global m_dificuldade, m_quantidade_jogadas, m_resposta

    if (m_resposta == ['*']*valores_dif[m_dificuldade]["pedras"]):
        return 1

    if (m_quantidade_jogadas > valores_dif[m_dificuldade]["limite"]-1):
        return -1

    return 0;

# 'Getters'

def get_tentativas():
    global m_quantidade_jogadas
    return m_quantidade_jogadas

def get_dif():
    global m_dificuldade
    return m_dificuldade

def get_sen():
    global m_senha
    return m_senha

def get_valorDif(valor):
    global m_dificuldade
    return valores_dif[m_dificuldade][valor]

