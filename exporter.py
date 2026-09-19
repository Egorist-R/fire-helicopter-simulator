import json

class GameExporter:
    def __init__(self, filename="savegame.json"):
        self.filename = filename

    def save_game(self, game_map, heli, clouds):
        save_data = {
            "map": {
                "rows": game_map.rows,
                "cols": game_map.cols,
                "grid": game_map.grid
            },
            "helicopter": {
                "x": heli.x,
                "y": heli.y,
                "water": heli.water,
                "max_water": heli.max_water,
                "hp": heli.hp,
                "score": heli.score
            },
            "clouds": {
                "grid": clouds.grid
            }
        }

        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(save_data, f, ensure_ascii=False, indent=4)
        
        print("\n💾 [ИГРА УСПЕШНО СОХРАНЕНА!]\n")
