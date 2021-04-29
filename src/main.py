#!/usr/bin/env python3

from model import game_rules
import random

header = """
 __  __           _                      _           _
|  \/  | __ _ ___| |_ ___ _ __ _ __ ___ (_)_ __   __| |
| |\/| |/ _` / __| __/ _ \ '__| '_ ` _ \| | '_ \ / _` |
| |  | | (_| \__ \ ||  __/ |  | | | | | | | | | | (_| |
|_|  |_|\__,_|___/\__\___|_|  |_| |_| |_|_|_| |_|\__,_|

Para iniciar o jogo escolha uma dificuldade (0, 1 ou 2) ou digite -1 para sair.
"""

while True:
    print(header)
    inp = int(input("> "))
    if (inp < 0):
        break

    game_rules.def_dificuldade(inp)
    game_rules.gen_senha()

    n = game_rules.get_valorDif("pedras")
    status = 0

    while (status == 0):
        tentativa = list(map(int,input("\nEntre sua tentativa: ").strip().split()))[:n]
        print(game_rules.compara_tentativa(tentativa))
        status = game_rules.testa_tentativa()

    if (status == 1):
        print("\nParabens! Voce descobriu a senha, em %d tentativas!" % game_rules.get_tentativas())
    else:
        print("\nVoce falhou! Mais sorte na proxima vez!")
 
    print("Senha: ", game_rules.get_sen(), "\n")
