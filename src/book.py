from inputFuntions import show_text
from spellDescription import spell_description
from trinkets import locations, objectives
from inputFuntions import *

def book_menu(hero):
    while True:
        clear_screen()
        book_opc = get_opc_list("book")
        list_options(book_opc)
        choice = clean_input()
        match choice:
            case "map":
                input(see_map_ver2(hero))
            case "spells":
                check_spells()
            case "objectives":
                see_objectives()
            case "back":
                return
            case _:
                input(f"Invalid option {choice}")

def see_objectives():
    result = ""
    for key, item in objectives.items():
        result += f"{key}: {item[0]} / {item[1]}\n"
    input(result)

def see_map(hero):
    result = f"Current position {hero.position}\n"
    stores = "Stores: \n"
    for location in locations:
        if locations[location]["name"] == "store":
            stores += f"{location} -> store\n"
        elif locations[location]["discovered"]:
            result += f"{location} -> {locations[location]["name"]} (Completed)\n"
        else:
            result += f"{location} -> ????\n"
    result += stores
    return result

def see_map_ver2(hero):
    result = "Forest map: \n"
    for y in range(9, -1, -1):
        for x in range(0, 10):
            if (x, y) == hero.position:
                result += " O"
            elif (x, y) in locations:
                if locations[(x, y)]["discovered"]:
                    result += f" {locations[(x, y)]["name"][0]}"
                else:
                    result += " ?"
            else:
                result += " +"
            if x == 9:
                result += "\n"
    return result

test = """y
1  + + + + + + + + + +
9  + + + + + + + + + +
8  + + + + + + + + + +
7  + + + + + + + + + +
6  + + + + + + + + + +
5  + + + + + + + + + +
4  + + + + + + + + + +
3  + + + + + + + + + +
2  + + + + + + + + + +
1  + + + + + + + + + +
  1 2 3 4 5 6 7 8 9 10 x"""


def check_spells():
    show_text(spell_description)