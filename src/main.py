from inputFuntions import *
from hero import Hero
from movement import movement
from bag import open_bag
from enemy import spawn_enemy, Wolf
from battle import battle

print("starting...")
test= """
Bienvenido
al legendario
pais
del peru
"""

def main():
    hero = Hero("Pablo", 40, 100, 5, 10, 4, 1, 2, 29, 39)
    playing = True
    show_text(test)
    menu_options = get_opc_list("main")
    while playing :
        clear_screen()
        list_options(menu_options)
        choice = clean_and_split_input("  >  ")
        match (choice[0]):
            case "move" | "ir":
                movement(choice[1], hero)
            case "battle":
                print("you choose to fight")
                battle(hero)
            case "bag":
                open_bag(choice[1], hero)
            case "see":
                hero.see_stats()
                show_text(str(hero.position))
            case "spawn":
                x = spawn_enemy(choice[1])
                x.see_stats()
            case "quit":
                playing = False
            case _:
                print("unknown command")
        
if __name__ == "__main__":
    main()



