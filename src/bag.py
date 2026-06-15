from consumables import *
from objects import equipment, equip_item

def open_menu(selection: str, hero):
    match selection:
        case "consumables":
            for key, value in items.items():
                if value > 0 :
                    print(f"{key} in inventory {value}")
            chosen_item = input("which do you use?")
            if chosen_item in items:
                if items[chosen_item] > 0:
                    print(f"you use {chosen_item}")
                    use_item(hero, chosen_item)
                    items[chosen_item] -= 1
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
