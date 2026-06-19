from character import Character
from trinkets import equipment, spells, spell_costs
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
            "ghost": 0
        }

    def take_dmg(self, dmg):
        if self.shield > 0:
            shield = self.shield
            if shield > dmg:
                print(f"The shield protects {self.name}")
                self.shield -= dmg
                dmg = 0
            else:
                print("The shield breaks!")
                self.shield = 0
                dmg -= shield
        self.health -= dmg
        input(f"{self.name} recieves {dmg} damage")

    def heal(self, amount):
        self.health += amount
        missing_health = self.health - self.max_health
        if self.health > self.max_health:
            self.health = self.max_health
            return print(f"{self.name} recovers {missing_health} health")
        input(f"{self.name} recovers {amount} health.")
    
    def heal_mana(self, amount):
        self.mana += amount
        missing_mana = self.mana - self.max_mana
        if self.mana > self.max_mana:
            self.mana = self.max_mana
            return print(f"{self.name} recovers {missing_mana} mana")
        input(f"{self.name} recovers {amount} mana")

    def use_mana(self, amount):
        self.mana -= amount
        if self.mana < 0:
            self.mana = 0
        print(f"You use {amount} mana")

    def attack_enemy(self, target):
        print(f"{self.name} attacks {target.name}")
        target.take_dmg(self.total_attack)
        if self.active_spells["ghost"] > 1:
            atk = self.total_attack
            ghost_atk = int(atk / 5)
            print("And the ghost follows!")
            target.take_dmg(ghost_atk)

    def see_stats(self):
        clear_screen()
        self.update_stats()
        stats = f"""
{self.name} stats:
Level:   {self.level}
Health:  {self.health}/{self.max_health}
Mana:    {self.mana}/{self.max_mana}
Attack:  {self.total_attack}
Buffatk: {self.buff_attack}
Defence: {self.total_defence}
Shield:  {self.shield}
Speed:   {self.total_speed}
Equipment:
Headwear: {self.equipment["Headwear"]}
Robe:     {self.equipment["Robe"]}
Boots:    {self.equipment["Boots"]}
Staff:    {self.equipment["Staff"]}
Grimoire: {self.equipment["Grimoire"]}
buffs: {self.buffs}
debuffs: {self.debuffs}
active spells: {self.active_spells}
"""
        print(f"{stats}")

    def update_stats(self):
        self.bonus_attack = 0
        self.bonus_defence = 0
        self.bonus_speed = 0
        self.buff_attack = 0
        self.buff_defence = 0
        self.buff_speed = 0
        for buff in self.buffs:
            if self.buffs[buff] > 0:
                match (buff):
                    case "attack":
                        atk = self.attack
                        buff_atk = int(atk * 0.4)
                        self.buff_attack = buff_atk
                    case "defence":
                        defence = self.defence
                        buff_defence = int(defence * 0.4)
                        self.buff_defence = buff_defence
                    case "speed":
                        spd = self.speed
                        buff_spd = int(spd * 0.4)
                        self.buff_defence = buff_spd
        for equip_name in self.equipment.values():
            if equip_name != None:
                equip = equipment[equip_name]
                self.bonus_attack += equip[3]
                self.bonus_defence += equip[2]
                self.bonus_speed += equip[4]
        self.total_attack = self.attack + self.bonus_attack + self.buff_attack
        self.total_defence = self.defence + self.bonus_defence + self.buff_defence
        self.total_speed = self.speed + self.speed + self.buff_speed
    
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
                if choice[0] == "back":
                    return False
                if second_arg == None:
                    input("Incorrect syntaxis, Example: Flame ignite")
                    clear_screen()
                    continue
                if choice[0] in spells and choice[1] in spells[choice[0]]:
                    mana = self.mana
                    if mana < spell_costs[choice[1]]:
                        input("You dont have enough mana for that spell")
                        return False
                    match (choice[0]):
                        case "flame":
                            self.flame_menu(choice[1], alive_enemies, enemies)
                        case "earth":
                            self.earth_menu(choice[1], alive_enemies, enemies)
                        case "spirit":
                            self.spirit_menu(choice[1], alive_enemies, enemies)
                        case _:
                            input("error in use magic menu")
                    return True
                else:
                    input("Unknown spell, try again")
                clear_screen()
        
    def spell_countdown(self):
        for spell in self.active_spells:
            if self.active_spells[spell] < 0:
                self.active_spells[spell] = 0
            if self.active_spells[spell] > 0:
                self.active_spells[spell] -= 1
                if self.active_spells[spell] == 0:
                    input(f"{spell} efects end")

    def spell_duration_increase(self, amount):
        for spell in self.active_spells:
            if self.active_spells[spell] < 0:
                self.active_spells[spell] = 0
            if self.active_spells[spell] > 0:
                self.active_spells[spell] += amount
                input(f"{spell} effects duration increased")

    def active_spells_effects(self):
        for spell in self.active_spells:
            if self.active_spells[spell] < 0:
                self.active_spells[spell] = 0
            if self.active_spells[spell] > 0:
                match (spell):
                    case "warmth":
                        print("Warmth heals you")
                        max_health = self.max_health
                        curr_health = self.health
                        missing_health = max_health - curr_health
                        self.heal(int(missing_health / 10))
                        max_mana = self.max_mana
                        curr_mana = self.mana
                        missing_mana = max_mana - curr_mana
                        self.heal_mana(int(missing_mana / 10))
                    case "oasis":
                        print("Oasis alleviates your wounds")
                        self.countdown_buff_debuffs()
                    case "ghost":
                        print("The undead roam amoung us")
                    case _:
                        input("error in active spells effects")

    def spells_update(self):
        self.spell_countdown()
        self.active_spells_effects()

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
                melt_target = list_alive_enemies("Cast flame melt on: ", alive_enemies, enemies, self, False)
                self.flame_melt(melt_target)
            case _:
                input("error on flame menu")
        clean_input()
        return True

    def flame_ring(self, enemies):
        self.use_mana(3)
        atk_dmg = self.get_attack_percentage(70)
        atk_dmg = self.total_attack
        print("The enemies burn in a ring of fire")
        for enemy in enemies:
            enemy.take_dmg(atk_dmg)
            prob = get_random_num()
            if prob < 20:
                enemy.apply_debuff("burn")

    def flame_warmth(self):
        self.use_mana(5)
        if self.active_spells["warmth"] > 0:
            print("Warmth duration extended")
        else:
            print("You heal every turn")
        max_health = self.max_health
        curr_health = self.health
        missing_health = max_health - curr_health
        heal_amount = int(missing_health / 3)
        print("The warmth makes the pain go away")
        self.active_spells["warmth"] = 4
        self.heal(heal_amount)
    
    def flame_ignite(self, target):
        self.use_mana(2)
        if target.name == self.name:
            print(f"{self.name} is fired up!")
            self.apply_buff("attack")
        else:
            atk_dmg = self.get_attack_percentage(80)
            if target.debuffs["burn"] > 0:
                print("Ignite does extra damage!")
                atk_dmg += self.get_attack_percentage(100)
            print(f"{target.name} combust!")
            target.take_dmg(atk_dmg)

    def flame_melt(self, target):
        self.use_mana(1)
        lvl = self.level
        reduce_amount = lvl * 2
        print(f"Fire melts {target.name} armor")
        target.modify_defence(reduce_amount, False)
        target.apply_debuff("burn")
        

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
        clean_input()
        return True

    def earth_shield(self):
        self.use_mana(2)
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
        self.use_mana(5)
        if self.active_spells["oasis"] > 0:
            print("Oasis duration extended")
        self.active_spells["oasis"] = 4
        print("You heal faster from illness")

    def earth_swamp(self, target):
        self.use_mana(1)
        lvl = self.level
        reduce_amount = lvl * 2
        print(f"A swamp appears under {target.name}")
        target.apply_debuff("poison")
        target.modify_speed(reduce_amount, False)

    def earth_spike(self, target):
        self.use_mana(4)
        print(f"{self.name} shoots a stalactite at {target.name}")
        tar_max_hp = target.max_health
        tar_curr_hp = target.health
        missing_porc = int(((tar_curr_hp / tar_max_hp) -1) * -100)
        atk_dmg = self.get_attack_percentage(missing_porc + 80)
        target.take_dmg(atk_dmg)
        prob = get_random_num()
        if prob < 90:
            target.apply_debuff("bleed")

## Spirit spells

    def spirit_menu(self, choice, alive_enemies, enemies):
        clear_screen()
        match (choice):
            case "calm":
                calm_target = list_alive_enemies("Cast spirit calm on: ", alive_enemies, enemies, self, True)
                self.spirit_calm(calm_target)
            case "bond":
                orig_targ = list_alive_enemies("Cast spirit bond from: ", alive_enemies, enemies, self, True)
                dest_targ = list_alive_enemies("Bond to: ", alive_enemies, enemies, self, True)
                self.spirit_bond(orig_targ, dest_targ)
            case "steal":
                steal_target = list_alive_enemies("Cast flame ignite on: ", alive_enemies, enemies, self, False)
                self.spirit_steal(steal_target)
            case "ghost":
                self.spirit_ghost()
            case _:
                input("error on flame menu")
        clean_input()
        return True

    def spirit_calm(self, target):
        self.use_mana(2)
        max_mana = self.max_mana
        count = 0
        if target.name == self.name:
            self.spell_duration_increase(2)
            return True
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
        self.use_mana(4)
        count = 0
        if orig_target == dest_target:
            print(f"Origin and target are the same, no effect")
            return True
        print(f"Passing debuffs from {orig_target.name} to {dest_target.name}")
        for debuff in orig_target.debuffs:
            if orig_target.debuffs[debuff] > 0:
                dest_target.apply_debuff(debuff)
                count += 1
        if count == 0:
            input(f"{orig_target.name} has no debuffs to pass")
    
    def spirit_steal(self, target):
        self.use_mana(0)
        atk_dmg = self.get_attack_percentage(80)
        heal_amount = atk_dmg * 2
        print(f"{self.name} pulls {target.name} soul")
        target.take_dmg(atk_dmg)
        self.heal_mana(heal_amount)
        if target.health <= 0:
            print(f"{self.name} steals {target.name} soul!")
            self.apply_buff("speed")
            self.heal(heal_amount * 2)
        
    def spirit_ghost(self):
        self.use_mana(5)
        input(f"{self.name} summons the dead!")
        self.active_spells["ghost"] = 3



## Spells
'''
"flame": ["ring", "warmth", "ignite", "melt"],
"earth": ["shield", "oasis", "swamp", "spike"],
"spirit": ["clean", "bond", "steal", "berserk"]
'''
