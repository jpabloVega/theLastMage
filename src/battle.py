from enemy import *
from inputFuntions import *

def battle(hero):
    clear_screen()
    enemies = get_enemy_flock(30)
    print(f"{hero.name} VS")
    list_options(get_enemies_names(enemies))

    ##while len(enemies) > 0 or 
    show_text("end fight ")
            
