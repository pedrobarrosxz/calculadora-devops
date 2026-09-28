import unittest

from calculadora import soma
from calculadora import subtracao
from calculadora import multiplicacao
from calculadora import divisao


class TestCalculadora(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(soma(10, 5), 15)

    def test_subtracao(self):
        self.assertEqual(subtracao(10, 5), 5)

    def test_multiplicacao(self):
        self.assertEqual(multiplicacao(10, 5), 50)

    def test_divisao(self):
        self.assertEqual(divisao(10, 5), 2)

    def test_divisao_por_zero(self):
        with self.assertRaises(ValueError):
            divisao(10, 0)


if __name__ == "__main__":
    unittest.main()
