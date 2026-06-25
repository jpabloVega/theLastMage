from trinkets import locations, objectives
from inputFuntions import clean_input, clear_screen
from store import store_menu, get_item
from battle import battle
from win import you_win

def special_event(hero):
    position = hero.position
    event_name = locations[position]["name"]
    match event_name:
        case "chest":
            if not locations[position]["discovered"]:
                find_chest(hero)
                locations[position]["discovered"] = True
                objectives["Treasure chests found"][0] += 1
                check_win(hero)
                return 0
            else:
                input("You see a chest, its empty")
                return 0
        case "store":
            store_menu(hero)
            return 0
        case "fight":
            if not locations[position]["discovered"]:
                budget = hero.level
                budget += 3
                input("You run into a monster den, an intense battle approaches")
                turns = battle(hero, budget)
                clear_screen
                input("After overcoming such a challenge, you have proven your might")
                hero.level_up()
                locations[position]["discovered"] = True
                objectives["Monster dens destroyed"][0] += 1
                check_win(hero)
                return turns
            else:
                input("You see the remains of a monster den")
                return 0
        case "tree":
            if not locations[position]["discovered"]:
                find_tree(hero)
                locations[position]["discovered"] = True
                objectives["Magic trees healed"][0] += 1
                check_win(hero)
                return 0
            else:
                input("This magic tree blossoms with manalyx flowers!")
                hero.heal_mana(10)
                return 0
        case _:
            input("Error in special event")
            return 0
    
def check_win(hero):
    for obj in objectives:
        if objectives[obj][0] != objectives[obj][1]:
            return
    you_win(hero)

def find_tree(hero):
    input("Before you a dead tree")
    input("You use the Earth Oasis spell to bring it back to life")
    input("The tree blossoms")
    input("The trees magic flows through your body")
    hero.level_up()

def find_chest(hero):
    input("You find an ancient chest")
    input("Inside of it lies an ancient relic")
    input("When you grab it a light blinds you!")
    input("The relic disapears")
    input("But you feel different")
    hero.level_up()
    

    