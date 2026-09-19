import random
import os
import time

EMPTY = "⬜"   # Пустая земля
WATER = "🟦"   # Вода / Река
TREE = "🟩"    # Живое дерево
FIRE = "🟥"    # Горящее дерево
ASH = "⬛"     # Сгоревшее дерево (зола)

class Map:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[EMPTY for j in range(cols)] for i in range(rows)]

    def get_random_cell(self):
        x = random.randint(0, self.rows -1)
        y = random.randint(0, self.cols -1)
        return x, y

    def check_bounds(self, x, y):
        if 0 <= x < self.rows and 0 <= y < self.cols:
            return True
        else:
            return False

    def generate_rivers(self, count):
        for _ in range(count):
            x, y = self.get_random_cell()
            length = random.randint(3, 7)

            for _ in range(length):
                if self.check_bounds(x, y):
                    self.grid[x][y] = WATER
                direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
                x = x + direction[0]
                y = y + direction[1]

    def generate_trees(self, count):
        for _ in range(count):
            x, y = self.get_random_cell()
            if self.grid[x][y] == EMPTY:
                self.grid[x][y] = TREE

    def draw(self, heli, clouds):
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(self.rows):
            row_to_print = []
            for j in range(self.cols):
                if clouds.grid[i][j] is not None:
                    row_to_print.append(clouds.grid[i][j])
                elif i == heli.x and j == heli.y:
                    row_to_print.append("🛸")
                else:
                    row_to_print.append(self.grid[i][j])
            print("".join(row_to_print))
        print(f"🎒 Вода: {heli.water}/{heli.max_water} | ❤️ Жизни: {heli.hp} | 🏆 Очки: {heli.score}")

    def grow_trees(self):
        x, y = self.get_random_cell()
        if self.grid[x][y] == EMPTY:
            self.grid[x][y] = TREE




        