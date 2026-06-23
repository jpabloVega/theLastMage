from constants import POTION_HEAL_AMOUNT, MANALYX_HEAL
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
        case "manalyx":
            target.heal_mana(MANALYX_HEAL)
        case "bandages":
            target.debuffs["bleed"] = 0
        case "antidote":
            target.debuffs["poison"] = 0
        case "ointment":
            target.debuffs["burn"] = 0
        case _:
            print("this should be possible")
    return