from inputFuntions import *
from hero import Hero
from movement import movement
from bag import open_bag
from enemy import spawn_enemy, Wolf
from battle import battle
from timeManagement import *

print("starting...")
test= """
Enter to start
"""

def main():
    hero = Hero("Pablo", 1900,2000, 0, 100, 23, 1, 2, 29, 39, 3)
    time = 8
    playing = True
    show_text(test)
    menu_options = get_opc_list("main")
    while playing :
        clear_screen()
        passed = 0
        print(get_am_pm(time))
        night_time = is_night(time)
        list_options(menu_options)
        choice = clean_input()
        match (choice):
            case "move":
                passed = movement(hero, night_time)
            case "bag":
                open_bag(hero)
            case "book":
                print("you choose to fight")
                passed = battle(hero, 6)
            case "stats":
                hero.see_stats()
                clear_screen()
            case "rest":
                passed = resting(hero)
            case "quit":
                playing = False
            case _:
                print("unknown command")
        time = add_hours(time, passed)
if __name__ == "__main__":
    main()



