from inputFuntions import *
from intro import intro
from movement import movement
from bag import open_bag
from timeManagement import *
from book import book_menu


def main():
    input("Press ENTER to start...")
    hero = intro()
    time = 8
    playing = True
    menu_options = get_opc_list("main")
    while playing :
        clear_screen()
        time = get_am_pm(time)
        list_options(menu_options)
        choice = clean_input()
        match (choice):
            case "move":
                time = movement(hero, time)
            case "bag":
                open_bag(hero)
            case "book":
                book_menu(hero)
            case "stats":
                hero.see_stats()
            case "rest":
                time = resting(hero, time)
            case "quit":
                playing = False
            case _:
                print("unknown command")
if __name__ == "__main__":
    main()



