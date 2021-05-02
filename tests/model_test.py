import unittest
from src.model import game_rules
from random import seed

class Test_def_dificuldade(unittest.TestCase):
    def test_valores(self):
        game_rules.def_dificuldade(0)

        self.assertEqual(game_rules.get_tentativas(), 0)
        self.assertEqual(game_rules.get_sen(), [])

    def test_facil(self):
        game_rules.def_dificuldade(0)

        self.assertEqual(game_rules.get_dif(), 0)

        self.assertEqual(game_rules.get_valorDif("pedras"), 4)
        self.assertEqual(game_rules.get_valorDif("cores"), 6)
        self.assertEqual(game_rules.get_valorDif("limite"), 8)

    def test_medio(self):
        game_rules.def_dificuldade(1)

        self.assertEqual(game_rules.get_dif(), 1)

        self.assertEqual(game_rules.get_valorDif("pedras"), 5)
        self.assertEqual(game_rules.get_valorDif("cores"), 7)
        self.assertEqual(game_rules.get_valorDif("limite"), 10)

    def test_dificil(self):
        game_rules.def_dificuldade(2)

        self.assertEqual(game_rules.get_dif(), 2)

        self.assertEqual(game_rules.get_valorDif("pedras"), 6)
        self.assertEqual(game_rules.get_valorDif("cores"), 8)
        self.assertEqual(game_rules.get_valorDif("limite"), 12)


class Test_gen_senha(unittest.TestCase):
    def setUp(self):
        seed(0)

    def test_facil(self):
        game_rules.def_dificuldade(0);
        game_rules.gen_senha()

        self.assertEqual(len(game_rules.get_sen()), 4)
        self.assertEqual(game_rules.get_sen(), [3, 3, 0, 2])

        game_rules.def_dificuldade(0);
        game_rules.gen_senha()

        self.assertEqual(len(game_rules.get_sen()), 4)
        self.assertEqual(game_rules.get_sen(), [4, 3, 3, 2])

    def test_medio(self):
        game_rules.def_dificuldade(1);
        game_rules.gen_senha()

        self.assertEqual(len(game_rules.get_sen()), 5)
        self.assertEqual(game_rules.get_sen(), [6, 3, 6, 3, 0])

        game_rules.def_dificuldade(1);
        game_rules.gen_senha()

        self.assertEqual(len(game_rules.get_sen()), 5)
        self.assertEqual(game_rules.get_sen(), [2, 4, 3, 3, 6])

    def test_dificil(self):
        game_rules.def_dificuldade(2);
        game_rules.gen_senha()

        self.assertEqual(len(game_rules.get_sen()), 6)
        self.assertEqual(game_rules.get_sen(), [6, 6, 0, 4, 7, 6])

        game_rules.def_dificuldade(2);
        game_rules.gen_senha()

        self.assertEqual(len(game_rules.get_sen()), 6)
        self.assertEqual(game_rules.get_sen(), [4, 7, 5, 3, 2, 4])


class Test_compara_tentativa(unittest.TestCase):
    def setUp(self):
        seed(0)
        game_rules.def_dificuldade(2);
        game_rules.gen_senha()

    def test_tentativa_errada(self):
        self.assertEqual(game_rules.compara_tentativa([5, 5, 5, 5, 5, 5]), [])
        self.assertEqual(game_rules.get_tentativas(), 1)

        self.assertEqual(game_rules.compara_tentativa([1, 1, 1, 1, 1, 1]), [])
        self.assertEqual(game_rules.get_tentativas(), 2)

    def test_tentativa_lugares_errado(self):
        self.assertEqual(game_rules.compara_tentativa([5, 5, 6, 6, 6, 4]), ['#', '#', '#', '#'])
        self.assertEqual(game_rules.get_tentativas(), 1)

        self.assertEqual(game_rules.compara_tentativa([4, 1, 1, 0, 1, 4]), ['#', '#'])
        self.assertEqual(game_rules.get_tentativas(), 2)

    def test_tentativa_lugares_errados_e_certos(self):
        self.assertEqual(game_rules.compara_tentativa([6, 5, 6, 6, 6, 6]), ['*', '*', '#'])
        self.assertEqual(game_rules.get_tentativas(), 1)

        self.assertEqual(game_rules.compara_tentativa([4, 6, 6, 4, 6, 4]), ['*', '*', '#', '#'])
        self.assertEqual(game_rules.get_tentativas(), 2)

    def test_tentativa_correta(self):
        self.assertEqual(game_rules.compara_tentativa([6, 6, 0, 4, 7, 6]), ['*', '*', '*', '*', '*', '*'])
        game_rules.def_dificuldade(2);
        game_rules.gen_senha()
        self.assertEqual(game_rules.compara_tentativa([4, 7, 5, 3, 2, 4]), ['*', '*', '*', '*', '*', '*'])


class Test_testa_tentativa(unittest.TestCase):
    def setUp(self):
        seed(0)
        game_rules.def_dificuldade(2);
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

if __name__ == '__main__':
    unittest.main()