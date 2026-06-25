from inputFuntions import clear_screen, clean_input, get_opc_list, list_options
from trinkets import items_cost, items, loot, equipment_cost, equipment, opc

def store_menu(hero):
    clear_screen()
    input("You find a store inside the stump of a big tree")
    while True:
        print("Hello visitor what can I do for you?")
        opc = get_opc_list("store")
        list_options(opc)
        choice = clean_input()
        match choice:
            case "items":
                store_buy_items(hero)
            case "equipment":
                store_buy_equip(hero)
            case "sell":
                store_sell(hero)
            case "leave":
                return
            case _:
                input(f"unknown command: {choice}")
        clear_screen()

def store_sell(hero):
    while True:
        total = 0
        for name in loot.keys():
            total += loot[name]["inventory"] * loot[name]["cost"]
        if total <= 0:
            input("Sorry come back when you find some treasure")
            return
        print(f"I can pay you {total} for all of your loot")
        print("Do you accept? y/n")
        choice = clean_input()
        if choice == "y":
            hero.obtain_money(total)
            for name in loot.keys():
                loot[name]["inventory"] = 0
            return
        elif choice == "n":
            input("You dont accept the deal")
            return
        else:
            input("invalid option")
        
def store_buy_equip(hero):
    while True:
        clear_screen()
        print(f"Your money: {hero.money}")
        print("What are you buying?")
        list_store_items(equipment_cost)
        print("back")
        choice = clean_input()
        if choice == "back":
            return
        if choice in equipment_cost:
            buy = hero.spend_money(equipment_cost[choice])
            if buy:
                get_equipment(choice)
        else:
            print("invalid option")
        
def store_buy_items(hero):
    while True:
        clear_screen()
        print(f"Your money: {hero.money}")
        print("What are you buying?")
        list_store_items(items_cost)
        print("back")
        choice = clean_input()
        if choice == "back":
            return
        if choice in items_cost:
            buy = hero.spend_money(items_cost[choice])
        else:
            print("invalid option")
        if buy:
            get_item(choice)

def get_item(item):
    if item in items:
        items[item] += 1
        input(f"You get {item}")

def get_equipment(equip):
    if equip in equipment:
        equipment[equip][0] += 1
        input(f"{equip} added to equipment inventory")

def list_store_items(items):
    for item, value in items.items():
        print(f"{item} -> {value} gold")