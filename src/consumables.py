## []
from constants import *

items = {
    "potion": 3,
    "mana crystal": 0,
    "bomb": 4,
}

def use_item(target, item_name):
    match (item_name):
        case "potion":
            target.heal(POTION_HEAL)
        case _:
            print("this should be possible")
    return