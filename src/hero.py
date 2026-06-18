from character import Character
from trinkets import equipment
from constants import base_atk, base_def
from objects import add_item

class Hero(Character):
    def __init__(self, name, health, max_health, defence, attack, speed, x, y, mana, max_mana):
        super().__init__(name, health, max_health, defence, attack, speed)
        self.x = x
        self.y = y
        self.position = (x, y)
        self.mana = mana
        self.max_mana = max_mana
        self.equipment = {
            "Headwear": None,
            "Robe": None,
            "Boots": None,
            "Staff": None,
            "Grimoire": None,
        }

    def attack_enemy(self, target):
        target.take_dmg(self.attack)
        print(f"{self.name} attacks {target.name}")
        input(f"Deals {self.attack} damage!")

    def see_stats(self):
        stats = f"""
{self.name} stats:
Health:  {self.health}/{self.max_health}
Mana:    {self.mana}/{self.max_mana}
Attack:  {self.attack}
Defence: {self.defence}
Speed:   {self.speed}
Equipment:
Headwear: {self.equipment["Headwear"]}
Robe:     {self.equipment["Robe"]}
Boots:    {self.equipment["Boots"]}
Staff:    {self.equipment["Staff"]}
Grimoire: {self.equipment["Grimoire"]}
"""
        print(stats)
        input("< go back")
    
    def test_equipment_values(self):
        for equip_name in self.equipment.values():
            print(equip_name)

    def update_stats(self):
        self.attack = 1
        self.speed = 1
        atk = 0
        defence = 0
        speed = 0
        for equip_name in self.equipment.values():
            if equip_name != None:
                equip = equipment[equip_name]
                atk += equip[3]
                defence += equip[2]
                speed += equip[4]
        self.attack = atk + 1
        self.defence = defence
        self.speed = speed 
    
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

    def update_equipment(self, equip_type, equip_name):
        removed_equip = self.equipment[equip_type]
        equip = equipment[equip_name]
        self.equipment[equip_type] = equip_name
        return removed_equip