import json
import os

class GameImporter:
    def __init__(self, filename="savegame.json"):
        self.filename = filename

    def load_game(self, game_map, heli, clouds):
        if not os.path.exists(self.filename):
            print("\n❌ [ФАЙЛ СОХРАНЕНИЯ НЕ НАЙДЕН!]\n")
            return False

        with open(self.filename, "r", encoding="utf-8") as f:
            save_data = json.load(f)
            
        game_map.rows = save_data["map"]["rows"]
        game_map.cols = save_data["map"]["cols"]
        game_map.grid = save_data["map"]["grid"]
        
        heli.x = save_data["helicopter"]["x"]
        heli.y = save_data["helicopter"]["y"]
        heli.water = save_data["helicopter"]["water"]
        heli.max_water = save_data["helicopter"]["max_water"]
        heli.hp = save_data["helicopter"]["hp"]
        heli.score = save_data["helicopter"]["score"]
        
        clouds.grid = save_data["clouds"]["grid"]
        
        print("\n📂 [ИГРА УСПЕШНО ЗАГРУЖЕНА!]\n")
        return True
