from constants import POTION_HEAL_AMOUNT
from trinkets import equipment, items

def add_item(item_name):
    if item_name not in equipment:
        return print(f"{item_name} is not a valid item")
    equipment[item_name][0] += 1
    return

def equip_item(target, item_name):
    if item_name not in equipment:
        return print("item name doesnt match item in inventory")
    in_possession = equipment[item_name][0]
    if in_possession < 1:
        return print("You dont possess this item")
    equipment[item_name][0] -= 1
    equip_type = equipment[item_name][1]
    unequiped_item = target.update_equipment(equip_type, item_name)
    if unequiped_item != None:
        print(f"Unequiped {unequiped_item} and placed in inventory")   
        add_item(unequiped_item)
    target.update_stats()
    return print(f"You equiped {item_name}")


def use_item(target, item_name):
    match (item_name):
        case "potion":
            target.heal(POTION_HEAL_AMOUNT)
        case _:
            print("this should be possible")
    return