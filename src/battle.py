from enemy import *
from inputFuntions import *
##replace me
temp_budget = 5

def battle(hero):
    clear_screen()
    enemies = spawn_enemies(temp_budget)
    print(f"{hero.name} VS")
    list_options(get_enemies_names(enemies))
    hero_name = hero.name
    show_text()
    battle_ongoing = True
    alive_enemies = get_enemies_names(enemies)
    while battle_ongoing:
        clear_screen()
        participants = turn_order(hero, enemies)
        for participant in participants:
            if participant.name == hero_name:
                hero_attacks(alive_enemies, enemies, hero)
            else:
                participant.attack_enemy(hero)
        enemies = remove_dead(enemies)
        if enemies:
            alive_enemies = get_enemies_names(enemies)
        else:
            battle_ongoing = False
    input("Victory")
    return

def hero_attacks(alive_enemies, enemies, hero):
    while True:
        print("Who do you attack?:")
        list_options(alive_enemies)
        x = input("> ").upper()
        for i in range(len(enemies)):
            if enemies[i].name[0] == x:
                target = enemies[i]
                hero.attack_enemy(target)
                return    
        input(f"{x} invalid target")
        clear_screen()

def spawn_enemies(budget: int) -> list:
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
    enemies = get_enemy_flock(budget)
    for i in range(len(enemies)):
        enemies[i].name = alphabet[i] + "> " + enemies[i].name
    return enemies

def remove_dead(enemies):
    alive_enemies = []
    for enemy in enemies:
        if enemy.health <= 0:
            input(f"{enemy.name} died!")
        else:
            alive_enemies.append(enemy)
    return alive_enemies

def turn_order(hero, enemies):
    clear_screen()
    participants = [hero] + enemies
    participants.sort(key=lambda x: x.speed, reverse=True)
    print("Turn order \n")
    for part in participants:
        print(f"+ {part.name}")
    show_text()
    return participants

