from inputFuntions import  *
from objects import *

def open_menu(user_input: str, hero):
    clear_screen()
    selection = user_input
    options = get_opc_list("bag")
    if selection == None:
        list_options(options)
        selection = clean_input("What do you choose > ")
    match selection:
        case "items":
            for key, value in items.items():
                if value > 0 :
                    print(f"{key} in inventory {value}")
            chosen_item = input("which do you use?")
            if chosen_item in items:
                if items[chosen_item] > 0:
                    print(f"you use {chosen_item}")
                    use_item(hero, chosen_item)
                    items[chosen_item] -= 1
            else:
                return print(f"{chosen_item} is not an availeble item")
        case "equipment":
            for key, value in equipment.items():
                if value[0] > 0 :
                    print(f"{key} you have {value[0]}")
            chosen_equip = input("What do you equip")
            if chosen_equip in equipment:
                if equipment[chosen_equip][0] > 0:
                    print(f"equiping {chosen_equip}...")
            equip_item(hero, chosen_equip)
        case _:
            print("unknown command")
    return

