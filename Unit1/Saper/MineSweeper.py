from random import randint
from typing import List


class Cell:
    """Клетка игрового поля"""
    def __init__(self, around_mines: int = 0, mine: bool = False) -> None:
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole:
    """Игровое поле"""
    def __init__(self, N: int, M: int) -> None:
        self.pole = []
        self.N = N
        self.M = M
        self.init()

    def __make_game_pole(self) -> List[List[Cell]]:
        """Создаем поле с ячейками Cell"""
        board = [[Cell() for _ in range(self.N)] for _ in range(self.N)]
        return board

    def __plant_bombs(self) -> None:
        """Плантим бомбы"""
        bombs_planted = 0
        while bombs_planted < self.M:
            loc = randint(0, self.N ** 2 - 1)
            row = loc // self.N
            col = loc % self.N

            if self.pole[row][col].mine:
                continue
            self.pole[row][col].mine = True
            bombs_planted += 1

    def __plant_value_on_board(self) -> None:
        """Плантим значения вокруг бомб"""
        for row in range(self.N):
            for col in range(self.N):
                if self.pole[row][col].mine:
                    continue
                self.pole[row][col].around_mines = self.get_num_neighboring_bombs(row, col)

    def get_num_neighboring_bombs(self, row: int, col: int) -> int:
        """Вспомогательня функция для def __plant_value_on_board(self): возвращает числовое значение бомб в ячейку"""
        num_neighboring_bombs = 0
        for r in range(max(0, row - 1), min(self.N - 1, row + 1) + 1):
            for c in range(max(0, col - 1), min(self.N - 1, col + 1) + 1):
                if r == row and c == col:
                    continue
                if self.pole[r][c].mine:
                    num_neighboring_bombs += 1

        return num_neighboring_bombs

    def init(self) -> None:
        """Инициализируем поле, бомбы и значение ячеек вокруг бомб"""
        self.pole = self.__make_game_pole()
        self.__plant_bombs()
        self.__plant_value_on_board()

    def show(self) -> None:
        for i in range(self.N):
            for j in range(self.N):
                if self.pole[i][j].mine:
                    print('*', end=' ')
                else:
                    print(self.pole[i][j].around_mines, end=' ')
            print()


if __name__ == '__main__':
    game = GamePole(10, 12)
    game.show()
