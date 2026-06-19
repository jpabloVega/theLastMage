from constants import *
from inputFuntions import get_random_num

class Character():
    def __init__(self, name, health: float, max_health, defence: float, attack: float, speed: int):
        self.name = name
        self.max_health = max_health
        self.health = health
        self.defence = defence
        self.attack = attack
        self.speed = speed
        self.bonus_attack = 0
        self.buff_attack = 0
        self.total_attack = self.attack + self.bonus_attack + self.buff_attack
        self.buff_defence = 0
        self.bonus_defence = 0
        self.total_defence = self.defence + self.bonus_defence + self.buff_defence
        self.buff_speed = 0
        self.bonus_speed = 0
        self.total_speed = self.speed + self.bonus_speed + self.bonus_speed
        self.debuffs = {
            "burn": 0,
            "poison": 0,
            "bleed": 0
        }
        self.buffs = {
            "attack": 0,
            "speed": 0,
            "defence": 0
        }

    def attack_enemy(self, target: None):
        pass

    def take_dmg(self, dmg: float) -> bool:
        self.health -= dmg
        input(f"{self.name} recieves {dmg} damage!")
        if self.health <= 0:
            input(f"{self.name} dies!")

    def heal(self, amount):
        self.health += amount
        missing_health = self.health - self.max_health
        if self.health > self.max_health:
            self.health = self.max_health
            return input(f"{self.name} recovers {missing_health} health.")
        return input(f"{self.name} recovers {amount} health.")

    def move_up(self, speed):
        self.y += speed
        if self.y > Y_TOP:
            self.y = Y_BOT
        self.position = (self.x, self.y)
        return

    def move_down(self, speed):
        self.y -= speed
        if self.y < Y_BOT:
            self.y = Y_TOP
        self.position = (self.x, self.y)
        return
    
    def move_right(self, speed):
        self.x += speed
        if self.x > X_TOP:
            self.x = X_BOT
        self.position = (self.x, self.y)
        return
    
    def move_left(self, speed):
        self.x -= speed
        if self.x < X_BOT:
            self.x = X_TOP
        self.position = (self.x, self.y)

    def see_stats(self):
        stats = f"""
{self.name} stats:
Health:  {self.health}/{self.max_health}
Attack:  {self.attack}
Defence: {self.defence}
Speed:   {self.speed}
"""
        return print(stats)
    
    def modify_defence(self, amount: int, increase=True):
        curr = self.defence
        if increase:
            self.defence += curr
        else:  
            if curr - amount < 0:
                self.defence = 0
                print(f"{self.name} defence cant go lower")
                return curr
            else:
                self.defence -= amount
                print(f"{self.name} defence reduced by {amount}")
                return amount
            
    def modify_attack(self, amount: int, increase=True):
        curr = self.attack
        if increase:
            self.attack += amount
        else:  
            if curr - amount < 0:
                self.attack = 0
                print(f"{self.name} attack cant go lower")
                return curr
            else:
                self.attack -= amount
                print(f"{self.name} attack reduced by {amount}")
                return amount
            
    def modify_speed(self, amount: int, increase=True):
        curr = self.speed
        if increase:
            self.speed += curr
        else:  
            if curr - amount < 0:
                self.speed = 0
                print(f"{self.name} speed cant go lower")
                return curr
            else:
                self.speed -= amount
                print(f"{self.name} speed reduced by {amount}")
                return amount

    def update_stats(self):
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
                        defence = defence
                        buff_defence = int(defence * 0.4)
                        self.buff_defence = buff_defence
                    case "speed":
                        spd = self.speed
                        buff_spd = int(spd * 0.4)
                        self.buff_defence = buff_spd
                    case _:
                        input("error in update stats, character")
        self.total_attack = self.attack + self.buff_attack
        self.total_defence = self.defence + self.buff_defence
        self.total_speed = self.speed + self.buff_speed

    def apply_buff(self, buff):
        if self.buffs[buff] > 0:
            print(f"{buff} buff is refreshed!")
        else:
            print(f"{self.name} {buff} increases!")
        match (buff):
            case "attack":
                self.buffs[buff] = 5
                self.update_stats()
            case "defence":
                self.buffs[buff] = 5
                self.update_stats()
            case "speed":
                self.buffs[buff] = 5
                self.update_stats()
            case _:
                input("error in apply buffs")
        
    def apply_debuff(self, debuff):
        match (debuff):
            case "burn":
                if self.debuffs[debuff] == 0:
                    print(f"{self.name} is set ablaze!")
                    self.debuffs[debuff] = get_random_num(3,5)
                else:
                    print(f"Cant burn, {self.name} is on fire already!")
            case "poison":
                if self.debuffs[debuff] == 0:
                    print(f"{self.name} becomes poisoned!")
                    self.debuffs[debuff] = get_random_num(8,10)
                else:
                    print(f"Cant poison, {self.name} is on poisoned already!")
            case "bleed":
                if self.debuffs[debuff] == 0:
                    print(f"{self.name} start to bleed!")
                    self.debuffs[debuff] = get_random_num(2,3)
                else:
                    print(f"Cant bleed, {self.name} is bleeding already!")
            case _:
                input("error in apply debuffs")
    
    def apply_debuff_effect(self):
            curr_health = self.health
            max_health = self.max_health
            for debuff in self.debuffs:
                if self.debuffs[debuff] > 0:
                    match (debuff):
                        case "burn":
                            print(f"{self.name} is burning")
                            burn_dmg = curr_health / 10
                            self.take_dmg(int(burn_dmg))
                        case "poison":
                            print(f"{self.name} is poisoned")
                            poison_dmg =  max_health / 20
                            self.take_dmg(int(poison_dmg))
                        case "bleed":
                            print(f"{self.name} is bleeding")
                            bleed_dmg = (max_health - curr_health) / 4
                            self.take_dmg(int(bleed_dmg) + 1)
                        case _:
                            input("Error in apply debufs method")

    def countdown_buff_debuffs(self):
        for buff in self.buffs:
            if self.buffs[buff] < 0:
                self.buffs[buff] = 0
            if self.buffs[buff] == 0:
                continue
            elif self.buffs[buff] > 0:
                curr = self.buffs[buff]
                self.buffs[buff] = curr - 1
                if self.buffs[buff] == 0:
                    print(f"{self.name} {buff} up ends!")
            else:
                input("error in countdown buffs and debuffs")
        for debuff in self.debuffs:
            if self.debuffs[debuff] < 0:
                self.debuffs[debuff] = 0
            if self.debuffs[debuff] == 0:
                continue
            elif self.debuffs[debuff] > 0:
                curr = self.debuffs[debuff]
                self.debuffs[debuff] = curr - 1
                if self.debuffs[debuff] == 0:
                    print(f"{self.name} {debuff} ends!")
            else:
                input("error in countdown buffs and debuffs")
        self.update_stats()



    def battle_update(self):
        self.apply_debuff_effect()
        self.countdown_buff_debuffs()
        self.update_stats()
        