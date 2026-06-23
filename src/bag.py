from inputFuntions import  *
from objects import *

def open_bag(hero):
    in_menu = True
    while in_menu:
        clear_screen()
        options = get_opc_list("bag")
        list_options(options)
        selection = clean_input()
        match selection:
            case "items":
                see_items(hero)
                selection = None
            case "equipment":
                change_equipment(hero)
                selection = None
            case "back":
                in_menu = False
            case _:
                print("unknown command")
    return

def change_equipment(hero):
    while True:
        clear_screen()
        print("Choose your equipment: \n")
        for key, value in equipment.items():
            if value[0] > 0 :
                print(f"+ {key}")
        print("+ back")
        chosen_equip = clean_input("  >  ")
        if chosen_equip in equipment:
            if equipment[chosen_equip][0] > 0:
                print(f"equiping {chosen_equip}...")
                hero.equip_item(chosen_equip)
        elif chosen_equip == "back":
            return
        else:
            input(f"{chosen_equip} is not a valid equipment")

def see_items(hero):
    while True:
        clear_screen()
        print("Choose item to use: \n")
        for key, value in items.items():
            if value > 0 :
                print(f"+ {key} ({value})")
        print("+ back")
        chosen_item = clean_input()
        if chosen_item in items:
            if items[chosen_item] > 0:
                input(f"you use {chosen_item}")
                use_item(hero, chosen_item)
                items[chosen_item] -= 1
                return True
        elif chosen_item == "back":
            return False
        else:
            input(f"{chosen_item} is not an available item")