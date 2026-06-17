import random
from character import Character
from trinkets import monster_stats

class Wolf (Character):
    def __init__(self, name, health, max_health, defence, attack, speed, cost):
        super().__init__(name, health, max_health, defence, attack, speed)
        self.cost = cost

class Armor (Character):
    def __init__(self, name, health, max_health, defence, attack, speed, cost):
        super().__init__(name, health, max_health, defence, attack, speed)
        self.cost = cost

def spawn_enemy(enemy_name: str) -> Character:
    enemy_stats = get_random_stats(enemy_name)
    match (enemy_name):
        case ("Wolf"):
            return Wolf(enemy_stats["Name"], enemy_stats["Health"], enemy_stats["Health"], enemy_stats["Defence"], enemy_stats["Attack"], enemy_stats["Speed"], enemy_stats["Cost"])
        case ("Armor"):
            return Armor(enemy_stats["Name"], enemy_stats["Health"], enemy_stats["Health"], enemy_stats["Defence"], enemy_stats["Attack"], enemy_stats["Speed"], enemy_stats["Cost"])
        case _:
            return print("unknown monster")

def get_random_stats(enemy_name) -> list:
    name = monster_stats[enemy_name]["Name"]
    atk = random.randint(monster_stats[enemy_name]["Attack"][0], monster_stats[enemy_name]["Attack"][1])
    defence = random.randint(monster_stats[enemy_name]["Defence"][0], monster_stats[enemy_name]["Defence"][1])
    health = random.randint(monster_stats[enemy_name]["Health"][0], monster_stats[enemy_name]["Health"][1])
    speed = random.randint(monster_stats[enemy_name]["Speed"][0], monster_stats[enemy_name]["Speed"][1])
    cost = monster_stats[enemy_name]["Cost"]
    return {"Name": name, "Health": health, "Defence": defence, "Attack": atk, "Speed": speed, "Cost": cost}

def get_enemy_flock(budget: int) -> list[Character]:
    temp_bud = budget
    all_mons = list(monster_stats.keys())
    selected_mons = []
    while temp_bud > 0:
        rand = random.randint(0, len(all_mons) -1)
        x = spawn_enemy(all_mons[rand])
        temp_bud -= x.cost
        selected_mons.append(x)
    return selected_mons

def get_enemies_names(enemies: list) -> list[str]:
    if not enemies:
        raise ValueError("No enemies")
    enemies_names = []
    for enemy in enemies:
        enemies_names.append(enemy.name)
    return enemies_names