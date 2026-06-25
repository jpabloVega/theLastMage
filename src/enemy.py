import random
from character import Character
from trinkets import monster_stats
from inputFuntions import clear_screen, get_random_num

class Enemy (Character):
    def __init__(self, name, health, max_health, defence, attack, speed, cost):
        super().__init__(name, health, max_health, defence, attack, speed)
        self.cost = cost

class Wolf (Enemy):
    def __init__(self, name, health, max_health, defence, attack, speed, cost):
        super().__init__(name, health, max_health, defence, attack, speed, cost)

    def attack_enemy(self, target):
        atk_prob = get_random_num()
        if atk_prob > 30:
            print(f"{self.name} bites {target.name}")
            target.take_dmg(self.attack)
            bleed_prob = get_random_num()
            if bleed_prob < 20:
                target.apply_debuff("bleed")
        else:
            self.apply_buff("attack")

class Armor (Enemy):
    def __init__(self, name, health, max_health, defence, attack, speed, cost):
        super().__init__(name, health, max_health, defence, attack, speed, cost)
    
    def attack_enemy(self, target):
        atk_prob = get_random_num()
        if atk_prob > 15:
            print(f"{self.name} swings at {target.name}")
            target.take_dmg(self.attack)
        else:
            print("A black liquid reinforces the soldiers armor")
            self.apply_buff("defence")

class Zombie (Enemy):
    def __init__(self, name, health, max_health, defence, attack, speed, cost):
        super().__init__(name, health, max_health, defence, attack, speed, cost)

    def attack_enemy(self, target):
        atk_prob = get_random_num()
        if atk_prob > 90:
            print(f"Zombie bites {target.name}")
            target.take_dmg(self.attack)
            target.apply_debuff("poison")
        elif atk_prob > 80:
            print(f"Zombie sharp nails attack {target.name}")
            target.apply_debuff("bleed")
        else:
            print(f"Zombie charges at {target.name}")
            target.take_dmg(self.attack)

class Elf (Enemy):
    def __init__(self, name, health, max_health, defence, attack, speed, cost):
        super().__init__(name, health, max_health, defence, attack, speed, cost)
    
    def attack_enemy(self, target):
        atk_prob = get_random_num()
        if atk_prob > 80:
            print("Elf moves like the wind")
            self.apply_buff("speed")
        else:
            print(f"The elf shoots an arrow at {target.name}")
            target.take_dmg(self.attack)
            arrow_prob = get_random_num(1, 10)
            if arrow_prob == 1:
                target.apply_debuff("poison")
            if arrow_prob == 2:
                target.apply_debuff("bleed")
            if arrow_prob == 3:
                target.apply_debuff("burn")
            
class Puppet (Enemy):
    def __init__(self, name, health, max_health, defence, attack, speed, cost):
        super().__init__(name, health, max_health, defence, attack, speed, cost)

    def attack_enemy(self, target):
        atk_prob = get_random_num()
        print(f"The puppet swings at {target.name}")
        target.take_dmg(self.attack)
        if atk_prob > 30:
            print("And again!")
            target.take_dmg(self.attack)
        if atk_prob > 90:
            print("And again!!")
            target.take_dmg(self.attack)

class Harpy (Enemy):
    def __init__(self, name, health, max_health, defence, attack, speed, cost):
        super().__init__(name, health, max_health, defence, attack, speed, cost)

    def attack_enemy(self, target):
        atk_prob = get_random_num()
        if atk_prob > 85:
            print("Harpy hones its claws")
            self.apply_buff("attack")
        else:
            print("Harpy descends in a tailspin")
            target.take_dmg(self.attack)
            if atk_prob < 15:
                target.apply_debuff("bleed")

class Mass (Enemy):
    def __init__(self, name, health, max_health, defence, attack, speed, cost):
        super().__init__(name, health, max_health, defence, attack, speed, cost)

    def attack_enemy(self, target):
        atk_prob = get_random_num()
        print(f"Flesh mass tries to take a chunk out of {target.name}")
        target.take_dmg(self.attack)
        if atk_prob > 80:
            print(f"Flesh mass eats {target.name} flesh")
            heal = self.max_health
            heal /= 10
            self.heal(heal)

class Devil (Enemy):
    def __init__(self, name, health, max_health, defence, attack, speed, cost):
        super().__init__(name, health, max_health, defence, attack, speed, cost)

    def attack_enemy(self, target):
        atk_prob = get_random_num()
        if atk_prob > 50:
            print("Devil chants a fiery spell")
            target.take_dmg(self.attack)
            if atk_prob > 80:
                target.apply_debuff("burn")
        else:
            print("Devil stabs you with its trident")
            target.take_dmg(self.attack)
            if atk_prob < 20:
                target.apply_debuff("bleed")

class Tree (Enemy):
    def __init__(self, name, health, max_health, defence, attack, speed, cost):
        super().__init__(name, health, max_health, defence, attack, speed, cost)

    def attack_enemy(self, target):
        atk_prob = get_random_num()
        if atk_prob < 15:
            print("The trees bark becomes hard like iron")
            self.apply_buff("defence")
        elif atk_prob < 30:
            print("Poison pollen covers the area")
            target.apply_debuff("poison")
        elif atk_prob < 40:
            print("Dark green leafs grow on the tree")
            heal = self.max_health
            heal -= self.health
            self.heal(int(heal / 10))
        else:
            print("The tree slams the ground")
            target.take_dmg(self.attack)

class Goat  (Enemy):
    def __init__(self, name, health, max_health, defence, attack, speed, cost):
        super().__init__(name, health, max_health, defence, attack, speed, cost)

    def attack_enemy(self, target):
        atk_prob = get_random_num()
        if atk_prob < 30:
            print("You hear the song of death")
            target.take_dmg(self.attack)
            target.apply_debuff("bleed")
            target.apply_debuff("burn")
            target.apply_debuff("poison")
        else:
            print("The goat is watching")

class Lord (Enemy):
    def __init__(self, name, health, max_health, defence, attack, speed, cost):
        super().__init__(name, health, max_health, defence, attack, speed, cost)
    
    def attack_enemy(self, target):
        atk_prob = get_random_num()
        if atk_prob < 10:
            print("You see a glimpse of the Dark Lords true power")
            self.apply_buff("attack")
            self.apply_buff("defence")
            self.apply_buff("speed")
        elif atk_prob < 50:
            print("The rotten blade pierces your skin")
            target.take_dmg(self.attack)
            if atk_prob < 40:
                target.apply_debuff("burn")
            if atk_prob < 30:
                target.apply_debuff("poison")
            if atk_prob < 20:
                target.apply_debuff("bleed")
        else:
            print("The dark lord strikes")
            target.take_dmg(self.attack)

def spawn_enemy(enemy_name: str) -> Character:
    enemy_stats = get_random_stats(enemy_name)
    name = enemy_stats["Name"]
    health = enemy_stats["Health"]
    defence = enemy_stats["Defence"]
    attack = enemy_stats["Attack"]
    speed = enemy_stats["Speed"]
    cost = enemy_stats["Cost"]
    match (enemy_name):
        case ("Wolf"):
            return Wolf(name, health, health, defence, attack, speed, cost)
        case ("Armor"):
            return Armor(name, health, health, defence, attack, speed, cost)
        case ("Zombie"):
            return Zombie(name, health, health, defence, attack, speed, cost)
        case ("Elf"):
            return Elf(name, health, health, defence, attack, speed, cost)
        case ("Puppet"):
            return Puppet(name, health, health, defence, attack, speed, cost)
        case ("Harpy"):
            return Harpy(name, health, health, defence, attack, speed, cost)
        case ("Mass"):
            return Mass(name, health, health, defence, attack, speed, cost)
        case ("Devil"):
            return Devil(name, health, health, defence, attack, speed, cost)
        case ("Tree"):
            return Tree(name, health, health, defence, attack, speed, cost)
        case ("Goat"):
            return Goat(name, health, health, defence, attack, speed, cost)
        case ("Lord"):
            return Lord(name, health, health, defence, attack, speed, cost)
        case _:
            return input("unknown monster")

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
        monster = all_mons[rand]
        x = spawn_enemy(monster)
        if x.cost <= temp_bud:
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