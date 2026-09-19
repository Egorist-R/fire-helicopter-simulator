class UpgradeShop:
    def __init__(self):
        self.heal_cost = 20       
        self.upgrade_cost = 50     

    def visit_hospital(self, heli):
        print("\n🏥 [Добро пожаловать в Госпиталь]")
        
        if heli.hp >= 100:
            print("У вертолёта уже максимальное здоровье! Лечение не требуется.\n")
            return

        if heli.score >= self.heal_cost:
            heli.score = heli.score - self.heal_cost
            heli.hp = 100
            print("❤️ Вертолёт полностью отремонтирован! Здоровье: 100 HP.\n")
        else:
            print(f"❌ Недостаточно очков! Лечение стоит {self.heal_cost} очков (у вас: {heli.score}).\n")

    def visit_shop(self, heli):
        print("\n🛒 [Добро пожаловать в Магазин улучшений]")
        print(f"Текущий объём бака: {heli.max_water}")
        
        if heli.score >= self.upgrade_cost:
            heli.score = heli.score - self.upgrade_cost
            heli.max_water = heli.max_water + 1
            print(f"🚀 Улучшение успешно куплено! Новый объём бака: {heli.max_water}\n")
        else:
            print(f"❌ Недостаточно очков! Улучшение стоит {self.upgrade_cost} очков (у вас: {heli.score}).\n")
