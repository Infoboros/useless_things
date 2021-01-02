from typing import List
from random import choice, randint
from enum import Enum

from cells.cell import Cell


class SlideDir(Enum):
    UP = '_slide_up'
    DOWN = '_slide_down'
    LEFT = '_slide_left'
    RIGHT = '_slide_right'


class Map:
    _happen_step: bool
    _height: int
    _width: int
    _map: List[List[Cell]]

    def __init__(self, height: int = 4, width: int = 4):
        self._height = height
        self._width = width
        self._map = [[Cell() for _ in range(self._width)] for _ in range(self._height)]

    def __str__(self):
        int_repres = self.to_int_lists()
        str_repres = [["%5s" % el for el in row] for row in int_repres]
        return "\n".join([" ".join(row) for row in str_repres])

    def to_int_lists(self) -> List[List[int]]:
        return [[el.value for el in row] for row in self._map]

    def generate_new_cell(self):
        empty_list = []
        for i, row in enumerate(self._map):
            for j, cell in enumerate(row):
                if not cell:
                    empty_list.append((i, j))
        new_i, new_j = choice(empty_list)
        # шанс 4 - 10%
        #      2 - 90%
        self._map[new_i][new_j] = Cell(2) if randint(0, 9) else Cell(4)

    def _slide_up(self):
        for j in range(self._width):
            for i in range(self._height - 1):
                self._map[i][j], self._map[i + 1][j] = self._map[i][j] + self._map[i + 1][j]

    def _slide_down(self):
        for j in range(self._width - 1, -1, -1):
            for i in range(self._height - 1, 0, -1):
                self._map[i][j], self._map[i - 1][j] = self._map[i][j] + self._map[i - 1][j]

    def _slide_right(self):
        for i in range(self._height - 1, -1, -1):
            for j in range(self._width - 1, 0, -1):
                self._map[i][j], self._map[i][j - 1] = self._map[i][j] + self._map[i][j - 1]

    def _slide_left(self):
        for i in range(self._height):
            for j in range(self._width - 1):
                self._map[i][j], self._map[i][j + 1] = self._map[i][j] + self._map[i][j + 1]

    def step(self, direction: SlideDir):
        self._happen_step = True
        slide_func = getattr(self, direction.value)
        slide_func()
        if self._happen_step:
            self.generate_new_cell()
