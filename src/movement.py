from constants import *
from inputFuntions import *

def movement(user_input: str, hero):
    clear_screen()
    direction = user_input
    options = get_opc_list["movement"]
    if direction == None:
        list_options(options)
        direction = clean_input("Where do you move")
    match direction:
            case "up":
                print("up")
                hero.move_up(1)
            case "down":
                print("down")
                hero.move_down(1)
            case "left":
                print("left")
                hero.move_left(1)
            case "right":
                print("right")
                hero.move_right(1)
            case _:
                print("unknown command")
    chech_special_tiles(hero.position)
    return

def chech_special_tiles(position):
    if position in locations:
        print(locations[position])
    return