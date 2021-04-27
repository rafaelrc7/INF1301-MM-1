from mm_model.mm_model import *
import random

random.seed(0) # 0 - [6, 6, 0, 4, 7, 6]

def_dificuldade(0)
gen_senha()

tent = [6, 4, 6, 4]

print(tent)

resp, status = turno(tent)
print(status)

resp, status = turno(tent)
print(status)

resp, status = turno(tent)
print(status)

tent = [3, 3, 0, 2]
resp, status = turno(tent)
print(status)

