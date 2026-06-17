from inputFuntions import  *
from objects import *

def open_bag(user_input: str, hero):
    in_menu = True
    selection = user_input
    while in_menu:
        clear_screen()
        options = get_opc_list("bag")
        if selection == None:
            list_options(options)
            selection = clean_input("  >  ")
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
                equip_item(hero, chosen_equip)
        elif chosen_equip == "back":
            return
        else:
            show_text(f"{chosen_equip} is not a valid equipment")

def see_items(hero):
    while True:
        clear_screen()
        print("Choose item to use: \n")
        for key, value in items.items():
            if value > 0 :
                print(f"+ {key} ({value})")
        print("+ back")
        chosen_item = clean_input("  >  ")
        if chosen_item in items:
            if items[chosen_item] > 0:
                print(f"you use {chosen_item}")
                use_item(hero, chosen_item)
                items[chosen_item] -= 1
        elif chosen_item == "back":
            return
        else:
            show_text(f"{chosen_item} is not an available item")