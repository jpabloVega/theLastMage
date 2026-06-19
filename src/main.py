from inputFuntions import *
from hero import Hero
from movement import movement
from bag import open_bag
from enemy import spawn_enemy, Wolf
from battle import battle

print("starting...")
test= """
Enter to start
"""

def main():
    hero = Hero("Pablo", 1900,2000, 0, 100, 23, 1, 2, 29, 39, 3)
    playing = True
    show_text(test)
    menu_options = get_opc_list("main")
    while playing :
        clear_screen()
        list_options(menu_options)
        choice = clean_input()
        match (choice):
            case "move":
                movement(hero)
            case "battle":
                print("you choose to fight")
                battle(hero)
            case "bag":
                open_bag(hero)
            case "status":
                hero.see_stats()
            case "spawn":
                get_magic_options()
                input("xd")
            case "quit":
                playing = False
            case _:
                print("unknown command")
        
if __name__ == "__main__":
    main()



