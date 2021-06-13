import unittest
from src.model import game_rules
from src.model import game_state
from random import seed
import pathlib as pl

class Test_nova_partida(unittest.TestCase):
    def test_valores(self):
        game_state.nova_partida(0)

        self.assertEqual(game_state.get_qtd_jogadas(), 0)
        self.assertEqual(game_state.estado["senha"], [])

    def test_facil(self):
        game_state.nova_partida(0)

        self.assertEqual(game_state.estado["dificuldade"], 0)

        self.assertEqual(game_rules.get_valorDif("pedras"), 4)
        self.assertEqual(game_rules.get_valorDif("cores"), 6)
        self.assertEqual(game_rules.get_valorDif("limite"), 8)

    def test_medio(self):
        game_state.nova_partida(1)

        self.assertEqual(game_state.estado["dificuldade"], 1)

        self.assertEqual(game_rules.get_valorDif("pedras"), 5)
        self.assertEqual(game_rules.get_valorDif("cores"), 7)
        self.assertEqual(game_rules.get_valorDif("limite"), 10)

    def test_dificil(self):
        game_state.nova_partida(2)

        self.assertEqual(game_state.estado["dificuldade"], 2)

        self.assertEqual(game_rules.get_valorDif("pedras"), 6)
        self.assertEqual(game_rules.get_valorDif("cores"), 8)
        self.assertEqual(game_rules.get_valorDif("limite"), 12)


class Test_gen_senha(unittest.TestCase):
    def setUp(self):
        seed(0)

    def test_facil(self):
        game_state.nova_partida(0)
        game_rules.gen_senha()

        self.assertEqual(len(game_state.estado["senha"]), 4)
        self.assertEqual(game_state.estado["senha"], [3, 3, 0, 2])

        game_state.nova_partida(0)
        game_rules.gen_senha()

        self.assertEqual(len(game_state.estado["senha"]), 4)
        self.assertEqual(game_state.estado["senha"], [4, 3, 3, 2])

    def test_medio(self):
        game_state.nova_partida(1)
        game_rules.gen_senha()

        self.assertEqual(len(game_state.estado["senha"]), 5)
        self.assertEqual(game_state.estado["senha"], [6, 3, 6, 3, 0])

        game_state.nova_partida(1)
        game_rules.gen_senha()

        self.assertEqual(len(game_state.estado["senha"]), 5)
        self.assertEqual(game_state.estado["senha"], [2, 4, 3, 3, 6])

    def test_dificil(self):
        game_state.nova_partida(2)
        game_rules.gen_senha()

        self.assertEqual(len(game_state.estado["senha"]), 6)
        self.assertEqual(game_state.estado["senha"], [6, 6, 0, 4, 7, 6])

        game_state.nova_partida(2)
        game_rules.gen_senha()

        self.assertEqual(len(game_state.estado["senha"]), 6)
        self.assertEqual(game_state.estado["senha"], [4, 7, 5, 3, 2, 4])


class Test_compara_tentativa(unittest.TestCase):
    def setUp(self):
        seed(0)
        game_state.nova_partida(2)
        game_rules.gen_senha()

    def test_tentativa_errada(self):
        self.assertEqual(game_rules.compara_tentativa([5, 5, 5, 5, 5, 5]), [])
        self.assertEqual(game_state.get_qtd_jogadas(), 1)

        self.assertEqual(game_rules.compara_tentativa([1, 1, 1, 1, 1, 1]), [])
        self.assertEqual(game_state.get_qtd_jogadas(), 2)

    def test_tentativa_lugares_errado(self):
        self.assertEqual(game_rules.compara_tentativa([5, 5, 6, 6, 6, 4]), ['#', '#', '#', '#'])
        self.assertEqual(game_state.get_qtd_jogadas(), 1)

        self.assertEqual(game_rules.compara_tentativa([4, 1, 1, 0, 1, 4]), ['#', '#'])
        self.assertEqual(game_state.get_qtd_jogadas(), 2)

    def test_tentativa_lugares_errados_e_certos(self):
        self.assertEqual(game_rules.compara_tentativa([6, 5, 6, 6, 6, 6]), ['*', '*', '#'])
        self.assertEqual(game_state.get_qtd_jogadas(), 1)

        self.assertEqual(game_rules.compara_tentativa([4, 6, 6, 4, 6, 4]), ['*', '*', '#', '#'])
        self.assertEqual(game_state.get_qtd_jogadas(), 2)

    def test_tentativa_correta(self):
        self.assertEqual(game_rules.compara_tentativa([6, 6, 0, 4, 7, 6]), ['*', '*', '*', '*', '*', '*'])
        game_state.nova_partida(2)
        game_rules.gen_senha()
        self.assertEqual(game_rules.compara_tentativa([4, 7, 5, 3, 2, 4]), ['*', '*', '*', '*', '*', '*'])


class Test_testa_tentativa(unittest.TestCase):
    def setUp(self):
        seed(0)
        game_state.nova_partida(2)
        game_rules.gen_senha()

    def test_vitoria_primeiro_turno(self):
        game_rules.compara_tentativa([6, 6, 0, 4, 7, 6])
        self.assertEqual(game_rules.testa_tentativa(), 1)

    def test_vitoria_terceiro_turno(self):
        for i in range(0, 2):
            game_rules.compara_tentativa([i, i, i, i, i, i])
            self.assertEqual(game_rules.testa_tentativa(), 0)

        game_rules.compara_tentativa([6, 6, 0, 4, 7, 6])
        self.assertEqual(game_rules.testa_tentativa(), 1)

    def test_ultimo_turno(self):
        for i in range(0, 11):
            game_rules.compara_tentativa([i, i, i, i, i, i])
            self.assertEqual(game_rules.testa_tentativa(), 0)

        game_rules.compara_tentativa([6, 6, 0, 4, 7, 6])
        self.assertEqual(game_rules.testa_tentativa(), 1)

    def test_derrota(self):
        for i in range(0, 11):
            game_rules.compara_tentativa([2, 2, 2, 2, 2, 2])
            self.assertEqual(game_rules.testa_tentativa(), 0)

        game_rules.compara_tentativa([0, 0, 0, 4, 7, 6])
        self.assertEqual(game_rules.testa_tentativa(), -1)


class Test_get_valorDif(unittest.TestCase):
    def test_Inicializacao(self):
        self.assertEqual(game_rules.get_valorDif("pedras"), -1)
    
    def test_valorDif_facil(self):
        game_state.nova_partida(0)
        self.assertEqual(game_rules.get_valorDif("pedras"), 4)
        self.assertEqual(game_rules.get_valorDif("cores"), 6)
        self.assertEqual(game_rules.get_valorDif("limite"), 8)
    
    def test_valorDif_medio(self):
        game_state.nova_partida(1)
        self.assertEqual(game_rules.get_valorDif("pedras"), 5)
        self.assertEqual(game_rules.get_valorDif("cores"), 7)
        self.assertEqual(game_rules.get_valorDif("limite"), 10)

    def test_valorDif_dificil(self):
        game_state.nova_partida(2)
        self.assertEqual(game_rules.get_valorDif("pedras"), 6)
        self.assertEqual(game_rules.get_valorDif("cores"), 8)
        self.assertEqual(game_rules.get_valorDif("limite"), 12)

class Test_nova_partida(unittest.TestCase):
    def test_nova_partida_partida(self):
        game_state.nova_partida(0)
        self.assertEqual(game_state.estado["partida"], 1)

    def test_nova_partida_facil(self):
        game_state.nova_partida(0)
        self.assertEqual(game_state.estado["dificuldade"], 0)

    def test_nova_partida_medio(self):
        game_state.nova_partida(1)
        self.assertEqual(game_state.estado["dificuldade"], 1)

    def test_nova_partida_dificil(self):
        game_state.nova_partida(2)
        self.assertEqual(game_state.estado["dificuldade"], 2)

class Test_get_qtd_jogadas(unittest.TestCase):
    def setUp(self):
        game_state.nova_partida(0)

    def test_sem_jogadas(self):
        self.assertEqual(game_state.get_qtd_jogadas(), 0)
    
    def test_uma_jogada(self):
        game_rules.compara_tentativa([-1,-1,-1,-1])
        self.assertEqual(game_state.get_qtd_jogadas(), 1)
    
    def test_tres_jogada(self):
        for i in range(0, 3):
            game_rules.compara_tentativa([-1,-1,-1,-1])
        self.assertEqual(game_state.get_qtd_jogadas(), 3)
    
    def test_oito_jogada(self):
        for i in range(0, 8):
            game_rules.compara_tentativa([-1,-1,-1,-1])
        self.assertEqual(game_state.get_qtd_jogadas(), 8)

class Test_salvar_E_carregar(unittest.TestCase):
    def setUp(self):
        seed(0)
        game_state.nova_partida(0)
    
    def test_salvar_facil_na_Partida(self):
        game_rules.compara_tentativa([0,0,0,0])
        game_state.salvar()
        fp = open("partida_mm.json", "r")
        arqSalvo = json.load(fp)
        self.assertEqual(arqSalvo, game_state.estado)
    
    def test_salvar_cria_json(self):
        path = pl.Path("INF1301-MM-1/partida_mm.json")
        self.assertTrue(path.exists)
    
    def test_salvar_facil_fora_Partida(self):
        game_rules.compara_tentativa([-1,-1,-1,-1])
        game_state.salvar()
        game_state.nova_partida(0)
        fp = open("partida_mm.json", "r")
        arqSalvo = json.load(fp)
        tentativa = {
            "partida": 1, 
            "cor_selecionada": -1, 
            "tentativa_tmp": [-1, -1, -1, -1, -1, -1], 
            "dificuldade": 0, 
            "tentativas": [[-1,-1,-1,-1]], 
            "respostas": [[]], 
            "senha": [3, 3, 0, 2]}
        self.assertEqual(arqSalvo, tentativa)
    
    def test_salvar_medio_na_Partida(self):
        game_state.nova_partida(1)
        game_rules.compara_tentativa([0,0,0,0,0])
        game_state.salvar()
        fp = open("partida_mm.json", "r")
        arqSalvo = json.load(fp)
        self.assertEqual(arqSalvo, game_state.estado)
    
    def test_salvar_medio_fora_Partida(self):
        game_state.nova_partida(1)
        game_rules.compara_tentativa([-1,-1,-1,-1,-1])
        game_state.salvar()
        game_state.nova_partida(0)
        fp = open("partida_mm.json", "r")
        arqSalvo = json.load(fp)
        tentativa = {
            "partida": 1, 
            "cor_selecionada": -1, 
            "tentativa_tmp": [-1, -1, -1, -1, -1, -1], 
            "dificuldade": 1, 
            "tentativas": [[-1,-1,-1,-1,-1]], 
            "respostas": [[]], 
            "senha": [3, 3, 0, 2]}
        self.assertEqual(arqSalvo, tentativa)
    
    def test_salvar_dificil_na_Partida(self):
        game_state.nova_partida(2)
        game_rules.compara_tentativa([0,0,0,0,0,0])
        game_state.salvar()
        fp = open("partida_mm.json", "r")
        arqSalvo = json.load(fp)
        self.assertEqual(arqSalvo, game_state.estado)
    
    def test_salvar_dificil_fora_Partida(self):
        game_state.nova_partida(1)
        game_rules.compara_tentativa([-1,-1,-1,-1,-1,-1])
        game_state.salvar()
        game_state.nova_partida(0)
        fp = open("partida_mm.json", "r")
        arqSalvo = json.load(fp)
        tentativa = {
            "partida": 1, 
            "cor_selecionada": -1, 
            "tentativa_tmp": [-1, -1, -1, -1, -1, -1], 
            "dificuldade": 1, 
            "tentativas": [[-1,-1,-1,-1,-1,-1]], 
            "respostas": [[]], 
            "senha": [3, 3, 0, 2]}
        self.assertEqual(arqSalvo, tentativa)
#Fazer unittest de carregar no game_state, depois fazer de event_handler, draw_canvas, e mastermind

if __name__ == '__main__':
    unittest.main()
