import random
from character import Character

moster_stats = {
    "Wolf": {
        "Health": (900, 1000),
        "Defence": (28, 35),
        "Attack": (42, 50),
        "Speed": (20, 30),
        "Cost": 5
    },
    "Armor": {
        "Health": (2000, 2300),
        "Defence": (50, 72),
        "Attack": (17, 21),
        "Speed": (5, 8),
        "Cost": 8
    }
}

class Wolf (Character):
    def __init__(self, health, max_health, defence, attack, speed, cost):
        super().__init__(health, max_health, defence, attack, speed)
        self.name = "Man Eater Wolf"
        self.cost = cost

class Armor (Character):
    def __init__(self,health, max_health, defence, attack, speed, cost):
        super().__init__(health, max_health, defence, attack, speed)
        self.name = "Possesed Armor"
        self.cost = cost

def spawn_enemy(enemy_name: str) -> Character:
    enemy_stats = get_random_stats(enemy_name)
    match (enemy_name):
        case ("Wolf"):
            return Wolf(enemy_stats["Health"], enemy_stats["Health"], enemy_stats["Defence"], enemy_stats["Attack"], enemy_stats["Speed"], enemy_stats["Cost"])
        case ("Armor"):
            return Armor(enemy_stats["Health"], enemy_stats["Health"], enemy_stats["Defence"], enemy_stats["Attack"], enemy_stats["Speed"], enemy_stats["Cost"])
        case _:
            return print("unknown monster")

def get_random_stats(enemy_name) -> list:
    atk = random.randint(moster_stats[enemy_name]["Attack"][0], moster_stats[enemy_name]["Attack"][1])
    defence = random.randint(moster_stats[enemy_name]["Defence"][0], moster_stats[enemy_name]["Defence"][1])
    health = random.randint(moster_stats[enemy_name]["Health"][0], moster_stats[enemy_name]["Health"][1])
    speed = random.randint(moster_stats[enemy_name]["Speed"][0], moster_stats[enemy_name]["Speed"][1])
    cost = moster_stats[enemy_name]["Cost"]
    return {"Health": health, "Defence": defence, "Attack": atk, "Speed": speed, "Cost": cost}

def get_enemy_flock(budget: int) -> list[Character]:
    temp_bud = budget
    all_mons = list(moster_stats.keys())
    selected_mons = []
    while temp_bud > 0:
        rand = random.randint(0, len(all_mons) -1)
        x = spawn_enemy(all_mons[rand])
        temp_bud -= x.cost
        selected_mons.append(x)
    return selected_mons