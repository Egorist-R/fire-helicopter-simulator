import time
import msvcrt
from map import Map
from helicopter import Helicopter
from fires import FireManager
from clouds import CloudManager
from shop import UpgradeShop 
from exporter import GameExporter
from importer import GameImporter

width = 10
height = 10

game_map = Map(width, height)
game_map.generate_rivers(2)
game_map.generate_trees(20)

copter = Helicopter(width // 2, height // 2)
fire_manager = FireManager()
cloud_manager = CloudManager(width, height)
shop_manager = UpgradeShop() 
exporter = GameExporter()
importer = GameImporter()

print("Игра запускается! Управление W, A, S, D. Выход: Q.")
print("🏥 Нажмите H для Госпиталя | 🛒 Нажмите U для Магазина улучшений | Выход: Q.")
time.sleep(2.0)

tick = 0

while True:
    tick = tick + 1

    if tick % 30 == 0:
        fire_manager.spawn_fire(game_map)

    if tick % 15 == 0:
        fire_manager.update_fires(game_map, copter)

    if tick % 40 == 0:
        cloud_manager.spawn_cloud()

    if tick % 10 == 0:
        cloud_manager.update_clouds(game_map, copter)

    if tick % 50 == 0:
        game_map.grow_trees()

    game_map.draw(copter, cloud_manager)

    if msvcrt.kbhit():
        key = msvcrt.getch().decode('utf-8').lower()

        if key == 'q':
            print("Игра завершена.")
            break
        elif key == 'w':
            copter.move(-1, 0, game_map)
        elif key == 's':
            copter.move(1, 0, game_map)
        elif key == 'a':
            copter.move(0, -1, game_map)
        elif key == 'd':
            copter.move(0, 1, game_map)

        elif key == 'h': 
            shop_manager.visit_hospital(copter)
            time.sleep(1.5) 
        elif key == 'u': 
            shop_manager.visit_shop(copter)
            time.sleep(1.5)

        elif key == 'k': 
            exporter.save_game(game_map, copter, cloud_manager)
            time.sleep(1.5)
        elif key == 'l': 
            importer.load_game(game_map, copter, cloud_manager)
            time.sleep(1.5)

    time.sleep(0.05)

