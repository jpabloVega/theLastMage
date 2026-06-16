from hero import Hero
from movement import movement
from bag import open_menu
from enemy import spawn_enemy, Wolf

print("starting...")

def main():
    hero = Hero("Pablo", 10, 10, 50, 37, 25, 10, 42, 100, 250)
    playing = True

    while playing :
        actions = input("What to do: ")
        sep = actions.split(" ", 1)
        match (sep[0]):
            case "move":
                movement(sep[1], hero)
            case "open":
                open_menu(sep[1], hero)
            case "stats":
                hero.see_stats()
            case "spawn":
                x = spawn_enemy(sep[1])
                x.see_stats()
            case "quit":
                playing = False
            case _:
                print("unknown command")
        
if __name__ == "__main__":
    main()



