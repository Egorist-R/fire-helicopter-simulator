class Helicopter:
    def __init__ (self, start_x, start_y):
        self.x = start_x
        self.y = start_y
        self.water = 0
        self.max_water = 1
        self.hp = 100
        self.score = 0

    def move(self, dx, dy, game_map):
        new_x = self.x + dx
        new_y = self.y + dy

        if game_map.check_bounds(new_x, new_y):
            self.x = new_x
            self.y = new_y

            if game_map.grid[self.x][self.y] == "🟦": # WATER
                self.water = self.max_water

            elif game_map.grid[self.x][self.y] == "🟥" and self.water > 0: # FIRE
                game_map.grid[self.x][self.y] = "🟩" # TREE
                self.water = self.water - 1
                self.score = self.score + 10