import unittest
from random import randint
from cells.cell import Cell
class TestCell(unittest.TestCase):

    def test_equal(self):
        rand_value = randint(0, 123)

        a = Cell(rand_value)
        b = Cell(rand_value)
        self.assertTrue(a == b, "Сравнение клеток на равенство не верно.")

        b = Cell(randint(1234,4352))
        self.assertTrue(a != b, "Сравнение клеток на равенство не верно.")

    def test_sum_emp(self):
        a = Cell(8)
        b = Cell()

        retA, retB = a+b
        self.assertTrue((retA == a) and (retB == b))

        retA, retB = b+a
        self.assertTrue((retA == a) and (retB == b))

    def test_sum_eq(self):
        a = Cell(8)
        b = Cell(8)

        retA, retB = a + b
        self.assertTrue((retA == Cell(16)) and (retB == Cell()))

    def test_sum_dif(self):
        a = Cell(8)
        b = Cell(4)

        retA, retB = a + b
        self.assertTrue((retA == a) and (retB == b))

        retA, retB = b + a
        self.assertTrue((retA == b) and (retB == a))
