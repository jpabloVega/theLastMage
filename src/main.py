from inputFuntions import *
from hero import Hero
from movement import movement
from bag import open_menu
from enemy import spawn_enemy, Wolf
from battle import battle

print("starting...")
test= """
Welcome to the land of magic.
In this place you die.
"""


def main():
    hero = Hero(50, 100, 5, 5, 5, "Pablo", 10, 10, 39, 50)
    playing = True
    show_text(test)
    menu_options = get_opc_list("main")
    while playing :
        ##clear_screen()
        list_options(menu_options)
        choice = clean_and_split_input("What do you do")
        match (choice[0]):
            case "move":
                movement(choice[1], hero)
            case "battle":
                print("you choose to fight")
                battle(hero)
            case "open":
                open_menu(choice[1], hero)
            case "see":
                hero.see_stats()
            case "spawn":
                x = spawn_enemy(choice[1])
                x.see_stats()
            case "quit":
                playing = False
            case _:
                print("unknown command")
        
if __name__ == "__main__":
    main()



