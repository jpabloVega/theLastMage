from constants import POTION_HEAL_AMOUNT
from trinkets import equipment, items

def add_item(item_name):
    if item_name not in equipment:
        return print(f"{item_name} is not a valid item")
    equipment[item_name][0] += 1
    return

def use_item(target, item_name):
    match (item_name):
        case "potion":
            target.heal(POTION_HEAL_AMOUNT)
        case _:
            print("this should be possible")
    return