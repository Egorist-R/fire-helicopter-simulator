import random 
from map import EMPTY, TREE, FIRE

CLOUD = "☁️"
STORM = "⛈️"

class CloudManager:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[None for j in range(cols)] for i in range(rows)]

    def spawn_cloud(self):
        x = random.randint(0, self.rows - 1)
        y = random.randint(0, self.cols - 1)

        if random.random() < 0.30:
            self.grid[x][y] = STORM
        else:
            self.grid[x][y] = CLOUD

    def update_clouds(self, game_map, heli):
        new_grid = [[None for j in range(self.cols)] for i in range(self.rows)]

        dx, dy = random.choice([(0, 1), (1, 0), (0, 0)])

        for i in range(self.rows):
            for j in range(self.cols):
                cloud_type = self.grid[i][j]
                if cloud_type is not None:
                    nx = i + dx
                    ny = j + dy

                    if game_map.check_bounds(nx, ny):
                        new_grid[nx][ny] = cloud_type

                        if cloud_type == CLOUD and game_map.grid[nx][ny] == FIRE:
                            game_map.grid[nx][ny] = TREE

                        elif cloud_type == STORM and random.random() < 0.10:
                            if game_map.grid[nx][ny] == TREE:
                                game_map.grid[nx][ny] = FIRE

                            if nx == heli.x and ny == heli.y:
                                heli.hp = heli.hp - 20
                                if heli.hp < 0:
                                    heli.hp = 0

        self.grid = new_grid 