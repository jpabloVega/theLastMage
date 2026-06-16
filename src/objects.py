from constants import POTION_HEAL_AMOUNT

## [0=in_possession, 1=type, 2=bonus_defence 3=bonus_attack]
equipment = {
    "Normal Hat": [0, "Headwear", 10, 0],
    "Normal Staff": [1, "Staff", 0, 10],
    "Insane Staff": [1, "Staff", 10, 100],
    "Normal Robe": [3, "Robe", 10, 0],
    }

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
        print(f"Unequiped {unequiped_item} placed in inventory")    
        add_item(unequiped_item)
    target.update_stats()
    return print(f"You equiped {item_name}")

items = {
    "potion": 3,
    "mana crystal": 0,
    "bomb": 4,
}

def use_item(target, item_name):
    match (item_name):
        case "potion":
            target.heal(POTION_HEAL_AMOUNT)
        case _:
            print("this should be possible")
    return