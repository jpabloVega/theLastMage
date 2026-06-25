from trinkets import locations
from inputFuntions import *
from battle import battle
from specialEvents import special_event
from timeManagement import *
from book import see_map_ver2

def movement(hero, time):
    options = get_opc_list("movement")
    while True:
        clear_screen()
        print(see_map_ver2(hero))
        print(get_am_pm(time))
        night_time = is_night(time)
        print("Choose a direction to move: ")
        print(f"Current position {hero.position}")
        list_options(options)
        direction = clean_input()
        match direction:
                case "up":
                    hero.move_up(1)
                    time += 1
                case "down":
                    hero.move_down(1)
                    time += 1
                case "left":
                    hero.move_left(1)
                    time += 1
                case "right":
                    hero.move_right(1)
                    time += 1
                case "cancel":
                    return time
                case _:
                    show_text(f"{direction} is not a valid direction")
                    direction = None
        input(f"You move {direction} ")
        on_event_tile = chech_special_tiles(hero.position)
        if on_event_tile:
            time += special_event(hero)
        else:
            prob = get_random_num()
            if prob <= 35:
                input("Monster ambush!")
                budget = hero.level
                if night_time:
                    budget += 2
                time += battle(hero, budget)

def chech_special_tiles(position):
    if position in locations:
        return True
    return False