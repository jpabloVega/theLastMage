from trinkets import locations
from inputFuntions import *
from battle import battle
from specialEvents import special_event

def movement(hero, night_time):
    clear_screen()
    options = get_opc_list("movement")
    has_not_moved = True
    passed = 1
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
                    return passed
                case _:
                    show_text(f"{direction} is not a valid direction")
                    direction = None
    input(f"You move {direction} ")
    passed = 1
    on_event_tile = chech_special_tiles(hero.position)
    if on_event_tile:
        special_event(hero)
    else:
        prob = get_random_num()
        if prob <= 30:
            budget = hero.level
            if night_time:
                budget += 2
                passed = battle(hero, budget)
    return passed

def chech_special_tiles(position):
    if position in locations:
        return True
    return False