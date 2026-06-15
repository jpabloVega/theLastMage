from consumables import *

def open_menu(selection: str, hero):
    match selection:
        case "consumables":
            for key, value in items.items():
                if value > 0 :
                    print(f"{value} - {key}")
            chosen_item = input("which do you use?")
            if chosen_item in items:
                if items[chosen_item] > 0:
                    print(f"you use {chosen_item}")
                    use_item(hero, chosen_item)
                    items[chosen_item] -= 1
        case "equipment":
            print("you see your equipment")
        case _:
            print("unknown command")
    return