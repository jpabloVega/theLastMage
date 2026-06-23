from trinkets import locations
from inputFuntions import clean_input, clear_screen
from store import store_menu, get_item
from battle import battle

def special_event(hero):
    position = hero.position
    event_name = locations[position]["name"]
    discovered = locations[position]["discovered"]
    match event_name:
        case "chest":
            find_chest(discovered)
            locations[position]["discovered"] = True
        case "store":
            store_menu(hero)
        case "fight":
            if not locations[position]["discovered"]:
                budget = hero.level
                budget += 3
                input("You run into a monster den, an intense battle approaches")
                battle(hero, budget)
                hero.level_up()
            locations[position]["discovered"] = True
        case "tree":
            find_tree(hero, discovered)
            locations[position]["discovered"] = True
        case _:
            input("Error in special event")

def find_tree(hero, found):
    clear_screen()
    if found:
        input("The tree is dead")
        return
    input("You find a magic tree")
    hero.level_up()

def find_chest(found):
    if found:
        return
    print("You find a chest")
    get_item("relic")
    

    