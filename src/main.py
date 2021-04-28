#!/usr/bin/env python3

from model import game_rules
import random

random.seed(0) # 0 - [6, 6, 0, 4, 7, 6]

game_rules.def_dificuldade(0)
game_rules.gen_senha()

tent = [6, 4, 6, 4]

print(tent)

resp, status = game_rules.turno(tent)
print(status)

resp, status = game_rules.turno(tent)
print(status)

resp, status = game_rules.turno(tent)
print(status)

tent = [3, 3, 0, 2]
resp, status = game_rules.turno(tent)
print(status)

