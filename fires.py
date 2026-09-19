import random
from map import TREE, FIRE, ASH

class FireManager:
    def __init__(self):
        pass

    def spawn_fire(self, game_map):
        x, y = game_map.get_random_cell()
        if game_map.grid[x][y] == TREE:
            game_map.grid[x][y] = FIRE

    def update_fires(self, game_map, heli):
        fire_cells = []
        for i in range(game_map.rows):
            for j in range(game_map.cols):
                if game_map.grid[i][j] == FIRE:
                    fire_cells.append((i, j))

        for x, y in fire_cells:
            if random.random() < 0.15:
                game_map.grid[x][y] = ASH
                heli.score = heli.score - 5
                continue

            neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            for nx, ny in neighbors:
                if game_map.check_bounds(nx, ny):
                    if game_map.grid[nx][ny] == TREE and random.random() < 0.20:
                        game_map.grid[nx][ny] = FIRE