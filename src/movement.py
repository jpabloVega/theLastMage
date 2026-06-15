from constants import *

def movement(user_input: str, hero):
    direction = user_input
    mov_amount = input(f"You can move up to {hero.speed}, how many do you move?")
    if not mov_amount.isdigit():
        print("invalid amount try again")
        return
    mov_amount = int(mov_amount)
    if mov_amount > hero.speed:
        mov_amount = hero.speed
        print(f"you only move {hero.speed}")
    match direction:
            case "up":
                hero.move_up(mov_amount)
            case "down":
                hero.move_down(mov_amount)
            case "left":
                hero.move_left(mov_amount)
            case "right":
                hero.move_right(mov_amount)
            case _:
                print("unknown command")
    chech_special_tiles(hero.position)
    return

def chech_special_tiles(position):
    if position in locations:
        print(locations[position])
    return