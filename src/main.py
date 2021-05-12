#!/usr/bin/env python3

import sys
from model import game_rules

def sair_partida():
    if input("Deseja salvar a partida atual? [S/n] ") != "n":
        arq = input("Digite o nome da partida (Default: mastermind): ")
        if len(arq) == 0:
            arq = "mastermind"
        game_rules.salvar(arq)

    sys.exit(0)


header = """
 __  __           _                      _           _
|  \\/  | __ _ ___| |_ ___ _ __ _ __ ___ (_)_ __   __| |
| |\\/| |/ _` / __| __/ _ \\ '__| '_ ` _ \\| | '_ \\ / _` |
| |  | | (_| \\__ \\ ||  __/ |  | | | | | | | | | | (_| |
|_|  |_|\\__,_|___/\\__\\___|_|  |_| |_| |_|_|_| |_|\\__,_|

Para iniciar o jogo escolha uma dificuldade (0, 1 ou 2) ou digite -1 para sair.
Para carregar uma partida digite 3.
Você também pode sair durante uma partida (Nesse caso será perguntado se deseja salvar).
"""

while True:
    print(header)
    inp = int(input("> "))
    if inp < 0:
        break

    if inp != 3:
        game_rules.def_dificuldade(inp)
        game_rules.gen_senha()

    else:
        arq = input("Digite o nome da partida (Default: mastermind): ")
        if len(arq) == 0:
            arq = "mastermind"
        game_rules.carregar(arq)

    n = game_rules.get_valorDif("pedras")
    status = 0

    while status == 0:
        tentativa = list(map(int,input("\nEntre sua tentativa: ").strip().split()))[:n]

        if tentativa[0] == -1:
            sair_partida()

        print(game_rules.compara_tentativa(tentativa))
        status = game_rules.testa_tentativa()

    if status == 1:
        print("\nParabens! Voce descobriu a senha, em %d tentativas!" % game_rules.get_tentativas())
    else:
        print("\nVoce falhou! Mais sorte na proxima vez!")

    print("Senha: ", game_rules.get_sen(), "\n")
