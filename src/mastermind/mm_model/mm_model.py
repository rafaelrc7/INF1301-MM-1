__all__ = ['def_dificuldade', 'gen_senha', 'turno']

from random import randint

m_dificuldade = 0 # 0- facil; 1- medio; 2- dificil
m_quantidade_jogadas = 0
m_senha = []

valores_dif = {
        0: {"pedras": 4, "cores": 6, "limite": 3},
        1: {"pedras": 5, "cores": 7, "limite": 10},
        2: {"pedras": 6, "cores": 8, "limite": 12}
        }

def def_dificuldade(dificuldade):
    global m_dificuldade
    m_dificuldade = dificuldade


def gen_senha():
    for i in range(valores_dif[m_dificuldade]["pedras"]):
        m_senha.append(randint(0, valores_dif[m_dificuldade]["cores"]-1))


def compara_tentativa(tentativa):
    global m_senha
    senha = m_senha
    resposta = []
    ret = 0

    for pos, pedra in enumerate(tentativa):
            if senha[pos] == pedra:
                resposta.append("*")
                senha[pos] = -1
                tentativa[pos] = -2

    for pos, pedra in enumerate(tentativa):
            if pedra in senha:
                resposta.append("#")
                senha[senha.index(pedra)] = -1
                tentativa[pos] = -2

    return resposta


def turno(tentativa):
    global m_quantidade_jogadas

    ret = compara_tentativa(tentativa)
    esta_correto = (ret == ['*']*valores_dif[m_dificuldade]["pedras"])

    if esta_correto:
        return ret, 1

    if (m_quantidade_jogadas >= valores_dif[m_dificuldade]["limite"]-1):
        return [], -1

    m_quantidade_jogadas += 1

    return ret, esta_correto
