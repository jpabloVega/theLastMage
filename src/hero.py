from character import Character
from trinkets import equipment
from constants import base_atk, base_def
from objects import add_item

class Hero(Character):
    def __init__(self, name, health, max_health, defence, attack, speed, x, y, mana, max_mana, level):
        super().__init__(name, health, max_health, defence, attack, speed)
        self.x = x
        self.y = y
        self.position = (x, y)
        self.mana = mana
        self.max_mana = max_mana
        self.bonus_attack = 0
        self.total_attack = self.attack + self.bonus_attack
        self.bonus_defence = 0
        self.total_defence = self.defence + self.bonus_defence
        self.bonus_speed = 0
        self.total_speed = self.speed + self.bonus_speed
        self.level = level
        self.equipment = {
            "Headwear": None,
            "Robe": None,
            "Boots": None,
            "Staff": None,
            "Grimoire": None,
        }

    def attack_enemy(self, target):
        target.take_dmg(self.total_attack)
        print(f"{self.name} attacks {target.name}")
        input(f"Deals {self.attack} damage!")

    def see_stats(self):
        stats = f"""
{self.name} stats:
Level:   {self.level}
Health:  {self.health}/{self.max_health}
Mana:    {self.mana}/{self.max_mana}
Attack:  {self.total_attack}
Defence: {self.total_defence}
Speed:   {self.total_speed}
Equipment:
Headwear: {self.equipment["Headwear"]}
Robe:     {self.equipment["Robe"]}
Boots:    {self.equipment["Boots"]}
Staff:    {self.equipment["Staff"]}
Grimoire: {self.equipment["Grimoire"]}
"""
        input(f"{stats}\n< back")

    def update_stats(self):
        self.bonus_attack = 0
        self.bonus_defence = 0
        self.bonus_speed = 0
        for equip_name in self.equipment.values():
            if equip_name != None:
                equip = equipment[equip_name]
                self.bonus_attack += equip[3]
                self.bonus_defence += equip[2]
                self.bonus_speed += equip[4]
        self.total_attack = self.attack + self.bonus_attack
        self.total_defence = self.defence + self.bonus_defence
        self.total_speed = self.speed + self.speed
    
    def equip_item(self, item_name):
        if item_name not in equipment:
            return print("item name doesnt match item in inventory")
        in_possession = equipment[item_name][0]
        if in_possession < 1:
            return print("You dont possess this item")
        equipment[item_name][0] -= 1
        equip_type = equipment[item_name][1]
        unequiped_item = self.equipment[equip_type]
        if unequiped_item != None:
            input(f"Unequiped {unequiped_item} and placed in inventory")   
            add_item(unequiped_item)
        self.equipment[equip_type] = item_name
        self.update_stats()
        return input(f"You equiped {item_name}")

    def level_increase(self):
        self.level += 1

    def max_health_increase(self, amount: int):
        curr_max = self.max_health
        self.max_health = curr_max + amount
    
    def max_mana_increase(self, amount: int):
        curr_max = self.max_mana
        self.max_mana = curr_max + amount

    def modify_defence(self, amount: int, increase=True):
        curr = self.defence
        if increase:
            self.defence = amount + curr
        else:  
            if curr - amount < 0:
                self.defence = 0
                return curr
            else:
                self.defence = curr - amount
                return amount
            
    def modify_attack(self, amount: int, increase=True):
        curr = self.attack
        if increase:
            self.attack = amount + curr
        else:  
            if curr - amount < 0:
                self.attack = 0
                return curr
            else:
                self.attack = curr - amount
                return amount
            
    def modify_speed(self, amount: int, increase=True):
        curr = self.speed
        if increase:
            self.speed = amount + curr
        else:  
            if curr - amount < 0:
                self.speed = 0
                return curr
            else:
                self.speed = curr - amount
                return amount
            
    def use_magic(self, target):
        pass