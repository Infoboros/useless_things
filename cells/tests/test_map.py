import unittest
from random import randint
from typing import Callable

from cells.cell import Cell
from cells.map import Map, SlideDir

class TestMap(unittest.TestCase):
    height = 20
    width = 20

    def test_init(self):
        map = Map()
        self._check_map(map, lambda el: el == 0)

    def test_generate_new_cell(self):
        height = TestMap.height
        width = TestMap.width

        map = Map(height, width)
        for _ in range(height*width):
            map.generate_new_cell()

        self._check_map(map, lambda el: (el == 2) or (el == 4))

    def _check_map(self, map: Map, condition: Callable[[int], bool]):
        int_representation_map = map.to_int_lists()
        for row in int_representation_map:
            for el in row:
                self.assertTrue(condition(el))

    @staticmethod
    def _random_map_generate() -> Map:
        h = TestMap.height
        w = TestMap.width

        map = Map(h, w)
        for _ in range(randint(h, w*h/2)):
            map.generate_new_cell()
        return map

if __name__ == '__main__':
    unittest.main()
