from character import Character
from objects import equipment
from constants import base_atk, base_def

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
        return print(stats)
    
    def update_stats(self):
        for equip_type, equip_name in self.equipment.items():
            if equip_name != None:
                self.attack = base_atk + equipment[equip_name][3]
                self.defence = base_def + equipment[equip_name][2]
        return
    
    def update_equipment(self, equip_type, equip_name):
        removed_equip = self.equipment[equip_type]
        self.equipment[equip_type] = equip_name
        return removed_equip