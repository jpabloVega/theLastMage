from trinkets import locations
from inputFuntions import *

def movement(hero):
    clear_screen()
    options = get_opc_list("movement")
    has_not_moved = True
    while has_not_moved:
        print("Choose a direction to move: ")
        print(f"Current position {hero.position}")
        list_options(options)
        direction = clean_input()
        match direction:
                case "up":
                    hero.move_up(1)
                    has_not_moved = False
                case "down":
                    hero.move_down(1)
                    has_not_moved = False
                case "left":
                    hero.move_left(1)
                    has_not_moved = False
                case "right":
                    hero.move_right(1)
                    has_not_moved = False
                case "cancel":
                    return
                case _:
                    show_text(f"{direction} is not a valid direction")
                    direction = None
    input(f"You move {direction} ")
    chech_special_tiles(hero.position)
    return

def chech_special_tiles(position):
    if position in locations:
        show_text(locations[position])
    return