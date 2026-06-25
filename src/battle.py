from enemy import *
from inputFuntions import *
from bag import see_items
from trinkets import monster_loot, loot

def battle(hero, budget):
    clear_screen()
    turn = 0
    enemies = spawn_enemies(budget)
    print(f"{hero.name} VS")
    list_options(get_enemies_names(enemies))
    hero_name = hero.name
    show_text()
    battle_ongoing = True
    alive_enemies = get_enemies_names(enemies)
    looted = get_loot(enemies)
    while battle_ongoing:
        for participant in participants:
            if participant.health > 0:
                participant.battle_update()
        clear_screen()
        apt = get_apt(hero)
        turn += 1
        participants = turn_order(hero, enemies, turn)
        for participant in participants:
            if participant.name == hero_name:
                while apt > 0:
                    alive_enemies = get_enemies_names(enemies)
                    battle_menu(alive_enemies, enemies, hero, apt)
                    enemies = remove_dead(enemies)
                    if not enemies:
                        apt = 0
                    apt -= 1
            elif participant.health > 0:
                participant.attack_enemy(hero)
                if hero.health <= 0:
                    input("You died!")
                    quit("Better luck next time!")
        hero.spells_update()
        enemies = remove_dead(enemies)
        participant = enemies + [hero]
        if hero.health <= 0:
                    input("You died!")
                    input("You can retry by running the game again")
                    quit("See you in the win screen!")
        enemies = remove_dead(enemies)
        if enemies:
            alive_enemies = get_enemies_names(enemies)
        else:
            battle_ongoing = False
    input("Victory!")
    hero.remove_spells_buffs_debuffs()
    clear_screen()
    if len(looted) > 0:
        print("You obtained")
        list_options(looted)
        clean_input("Take all")
        for item in looted:
            loot[item]["inventory"] += 1
    return turn

def battle_menu(alive_enemies, enemies, hero, apt):
    while True:
        clear_screen()
        print(f"{hero.name} turn")
        print(f"Actions left: {apt}")
        print("What do you do?: ")
        list_options(get_opc_list("battle"))
        selection = clean_input()
        match (selection):
            case "attack":
                hero_attacks(alive_enemies, enemies, hero)
                return
            case "magic":
                used_magic = hero.use_magic(alive_enemies, enemies)
                if used_magic:
                    return
            case "items":
                used_item = see_items(hero)
                if used_item:
                    return
            case "stats":
                status_menu(hero, enemies)
            case _:
                input("unknown command")

def get_apt(hero):
    apt = 2
    speed = hero.total_speed
    apt += int(speed/30)
    return apt


def list_alive_enemies(message, alive_enemies, enemies, hero, include_hero=False):
    if include_hero:
        name_list = alive_enemies + ["self"]
    else:
        name_list = alive_enemies
    while True:
        clear_screen()
        print(message)
        list_options(name_list)
        x = clean_input().upper()
        if x == "SELF" and include_hero:
            return hero
        for i in range(len(enemies)):
            if enemies[i].name[0] == x:
                target = enemies[i]
                return target
        input(f"{x} invalid target")
        target = None
        clear_screen()

def hero_attacks(alive_enemies, enemies, hero):
    target = list_alive_enemies("Who do you attack?: ",alive_enemies, enemies, hero)
    hero.attack_enemy(target)

def hero_magic(alive_enemies, enemies, hero):
    while True:
        clear_screen()
        print("Who do you attack?:")
        list_options(alive_enemies)
        x = input("> ").upper()
        for i in range(len(enemies)):
            if enemies[i].name[0] == x:
                target = enemies[i]
                hero.attack_enemy(target)
                return    
        input(f"{x} invalid target")
        target = None
        clear_screen()

def status_menu(hero, enemies):
    while True:
        clear_screen()
        print("Whose stats do you want to see?: ")
        list_options(get_opc_list("battle_status"))
        selection = clean_input()
        match (selection):
            case "self":
                hero.see_stats()
                clean_input("< go back ")
                return
            case "enemies":
                for enemy in enemies:
                    enemy.see_stats()
                clean_input("< go back ")
                return
            case _:
                clean_input("invalid option try again")

def spawn_enemies(budget: int) -> list:
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"]
    enemies = get_enemy_flock(budget)
    for i in range(len(enemies)):
        enemies[i].name = alphabet[i] + "> " + enemies[i].name
    return enemies

def get_loot(enemies):
    result = []
    for enemy in enemies:
        name = enemy.name
        name = name[3::]
        rdm_amount = get_random_num(0, 4)
        while rdm_amount > 0:
            rdm_reward = get_random_num(0,1)
            result.append(monster_loot[name][rdm_reward])
            rdm_amount -= 1
    return result

def remove_dead(enemies):
    alive_enemies = []
    for enemy in enemies:
        if enemy.health > 0:
            alive_enemies.append(enemy)
    return alive_enemies

def turn_order(hero, enemies, turn):
    clear_screen()
    participants = [hero] + enemies
    participants.sort(key=lambda x: x.total_speed, reverse=True)
    result = f"Turn {turn} order\n"
    for part in participants:
        result += f"+ {part.name}\n"
    input(result)
    return participants

