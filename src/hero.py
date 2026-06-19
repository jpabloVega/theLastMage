from character import Character
from trinkets import equipment, spells
from objects import add_item
from inputFuntions import *
from battle import list_alive_enemies

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
        self.shield = 0
        self.equipment = {
            "Headwear": None,
            "Robe": None,
            "Boots": None,
            "Staff": None,
            "Grimoire": None,
        }
        self.active_spells = {
            "warmth": 0,
            "oasis": 0, 
            "berserk": 0
        }

    def take_dmg(self, dmg):
        if self.shield > 0:
            shield = self.shield
            dmg -= shield
            if shield > dmg:
                print(f"The shield protects {self.name}")
                self.shield -= dmg
            else:
                print("The shield breaks!")
                self.shield = 0
            if dmg < 0:
                dmg = 0
        self.health -= dmg
        print(f"{self.name} recieves {dmg} damage")

    def heal(self, amount):
        if self.active_spells["oasis"] > 0:
            amount = int(amount * 1.4)
            print(f"Oasis improves healing")
        self.health += amount
        missing_health = self.health - self.max_health
        if self.health > self.max_health:
            self.health = self.max_health
            return print(f"{self.name} recovers {missing_health} health")
        print(f"{self.name} recovers {amount} health.")
    
    def heal_mana(self, amount):
        if self.active_spells["oasis"] > 0:
            amount = int(amount * 1.5)
            print(f"Oasis improves mana regen")
        self.mana += amount
        missing_mana = self.mana - self.max_mana
        if self.mana > self.max_mana:
            self.mana = self.max_mana
            return print(f"{self.name} recovers {missing_mana} mana")
        print(f"{self.name} recovers {amount} mana")

    def attack_enemy(self, target):
        target.take_dmg(self.total_attack)
        print(f"{self.name} attacks {target.name}")
        input(f"Deals {self.attack} damage!")

    def see_stats(self):
        clear_screen()
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
        print(f"{stats}")

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

    def get_attack_percentage(self, percentage: int) -> int:
        total_attack = self.total_attack
        result = total_attack * percentage / 100
        return int(result)

## magic menu

    def use_magic(self, alive_enemies, enemies):
        while True:
            clear_screen()
            second_arg = None
            while second_arg == None:
                print("Choose a spell")
                get_magic_options()
                choice = clean_and_split_input()
                second_arg = choice[1]
                if second_arg == None:
                    input("Incorrect syntaxis, Example: Flame ignite")
                    clear_screen()
                    continue
                if choice[0] in spells and choice[1] in spells[choice[0]]:
                    match (choice[0]):
                        case "flame":
                            self.flame_menu(choice[1], alive_enemies, enemies)
                        case "earth":
                            self.earth_menu(choice[1], alive_enemies, enemies)
                        case "spirit":
                            self.spirit_menu(choice[1], alive_enemies, enemies)
                        case "staff":
                            self.staff_menu(choice[1], alive_enemies, enemies)
                        case _:
                            input("error in use magic menu")
                    return
                else:
                    input("Unknown spell, try again")
                clear_screen()
        

##Flame spells

    def flame_menu(self, choice, alive_enemies, enemies):
        clear_screen()
        match (choice):
            case "ring":
                print("You cast flame ring")
                self.flame_ring(enemies)
            case "warmth":
                print("You cast flame warmth")
                self.flame_warmth()
            case "ignite":
                ignite_target = list_alive_enemies("Cast flame ignite on: ", alive_enemies, enemies, self, True)
                self.flame_ignite(ignite_target)
            case "melt":
                melt_target = list_alive_enemies("Cast flame melt on: ", alive_enemies, enemies, self)
                self.flame_melt(melt_target)
            case _:
                input("error on flame menu")
        input()
        clean_input()
        return

    def flame_ring(self, enemies):
        atk_dmg = self.get_attack_percentage(70)
        print("The enemies burn in a ring of fire")
        for enemy in enemies:
            enemy.take_dmg(atk_dmg)
            prob = get_random_num()
            if prob < 20:
                enemy.apply_debuff("burn")

    def flame_warmth(self):
        if self.active_spells["oasis"] > 0:
            return print("Oasis is already active")
        defence = self.defence
        max_health = self.max_health
        curr_health = self.health
        missing_health = max_health - curr_health
        heal_amount = defence + (missing_health / 5)
        print("The warmth makes the pain go away")
        self.active_spells["oasis"] = 4
        self.heal(heal_amount)
    
    def flame_ignite(self, target):
        if target.name == self.name:
            print(f"{self.name} is fired up!")
            self.apply_buff("attack")
        else:
            atk_dmg = self.get_attack_percentage(120)
            print(f"{target.name} combust!")
            target.take_dmg(atk_dmg)
        target.apply_debuff("burn")

    def flame_melt(self, target):
        lvl = self.level
        reduce_amount = lvl * 2
        print(f"Fire melts {target.name} armor")
        target.modify_defence(reduce_amount, False)

## Earth spells

    def earth_menu(self, choice, alive_enemies, enemies):
        match (choice):
            case "shield":
                print("You cast earth shield")
                self.earth_shield()
            case "oasis":
                print("You cast earth oasis")
                self.earth_oasis()
            case "swamp":
                swamp_target = list_alive_enemies("Cast earth swamp on: ", alive_enemies, enemies, self)
                self.earth_swamp(swamp_target)
            case "spike":
                spike_target = list_alive_enemies("Cast earth spike on: ", alive_enemies, enemies, self)
                self.earth_spike(spike_target)
            case _:
                input("error on flame menu")

    def earth_shield(self):
        max_health = self.max_health
        max_shield = int(max_health / 5)
        if self.shield < max_shield:
            if self.shield == 0:
                print("A shield has been erected")
            else:
                print("The shield is rebuild")
            self.shield = max_shield
        else:
            print("Cannot have more shield")

    def earth_oasis(self):
        if self.active_spells["oasis"] > 0:
            return print("Oasis is already active")
        self.active_spells["oasis"] = 4
        print("Healing has been increased")

    def earth_swamp(self, target):
        lvl = self.level
        reduce_amount = lvl * 2
        print("A swamp appears under {target.name}")
        target.modify_speed(reduce_amount, False)

    def earth_spike(self, target):
        print(f"{self.name} shoots a stalactite at {target.name}")
        atk_dmg = self.get_attack_percentage(150)
        target.take_dmg(atk_dmg)
        prob = get_random_num()
        if prob < 90:
            target.apply_debuff("bleed")

## Spirit spells

    def spirit_menu(self, choice, alive_enemies, enemies):
        pass

    def spirit_calm(self, target):
        max_mana = self.max_mana
        count = 0
        for buff in target.buffs:
            if target.buffs[buff] > 0:
                target.buffs[buff] = 0
                print(f"{buff} up removed!")
                count += 1
                self.heal_mana(max_mana/10)
        target.buff_attack = 0
        target.buff_defence = 0
        target.buff_speed = 0
        if count == 0:
            print("No buffs to remove")

    def spirit_bond(self, orig_target, dest_target):
        count = 0
        print(f"Passing debuffs from {orig_target.name} to {dest_target.name}")
        for debuff in orig_target.debuffs:
            if orig_target.debuffs[debuff] > 0:
                dest_target.apply_debuff(debuff)
                count += 1
        if count == 0:
            print(f"{orig_target.name} has no debuffs to pass")
    
    def spirit_steal(self, target):
        atk_dmg = self.get_attack_percentage(80)
        heal_amount = atk_dmg * 2
        print(f"{self.name} pulls {target.name} soul")
        target.take_dmg(atk_dmg)
        self.heal(heal_amount)
        if target.health <= 0:
            print(f"{self.name} steals {target.name} soul!")
            self.apply_buff("speed")
            self.heal(heal_amount * 2)
        
    def spirit_berserk(self):
        print(f"{self.name} heart is filled with rage!")
        self.apply_buff("attack")
        self.apply_buff("defence")
        self.active_spells["berserk"] = 3

## Staff spells
    def staff_menu(self, choice, alive_enemies, enemies):
        pass

## Spells
'''
"flame": ["ring", "warmth", "ignite", "melt"],
"earth": ["shield", "oasis", "swamp", "spike"],
"spirit": ["clean", "bond", "steal", "berserk"],
"staff": ["bash", "swipe", "vampire", "empower"]
'''
