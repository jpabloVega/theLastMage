from hero import Hero
from movement import movement
from bag import open_menu

print("starting...")

def main():
    hero = Hero("Pablo", 5, 5, 50, 100, 1, 1, 39, 50, 3)
    playing = True

    while playing :
        print(hero.health)
        actions = input("What to do: ")
        sep = actions.split(" ", 1)
        match (sep[0]):
            case "move":
                movement(sep[1], hero)
            case "open":
                open_menu(sep[1], hero)
            case "stats":
                hero.see_stats()
            case "quit":
                playing = False
            case _:
                print("unknown command")
        
if __name__ == "__main__":
    main()



