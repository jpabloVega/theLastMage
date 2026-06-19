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
        print(f"{self.name} recieves {dmg}")
    
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
        curr = self.total_defence
        if increase:
            self.total_defence = amount + curr
        else:  
            if curr - amount < 0:
                self.total_defence = 0
                print(f"{self.name} defence cant go lower")
                return curr
            else:
                self.total_defence = curr - amount
                print(f"{self.name} defence reduced by {amount}")
                return amount
            
    def modify_attack(self, amount: int, increase=True):
        curr = self.total_attack
        if increase:
            self.total_attack = amount + curr
        else:  
            if curr - amount < 0:
                self.total_attack = 0
                print(f"{self.name} attack cant go lower")
                return curr
            else:
                self.total_attack = curr - amount
                print(f"{self.name} attack reduced by {amount}")
                return amount
            
    def modify_speed(self, amount: int, increase=True):
        curr = self.total_speed
        if increase:
            self.total_speed = amount + curr
        else:  
            if curr - amount < 0:
                self.total_speed = 0
                print(f"{self.name} speed cant go lower")
                return curr
            else:
                self.total_speed = curr - amount
                print(f"{self.name} speed reduced by {amount}")
                return amount

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

    def update_stats(self):
        self.total_attack = self.attack + self.bonus_attack + self.buff_attack
        self.total_defence = self.defence + self.bonus_defence + self.buff_defence
        self.total_speed = self.speed + self.bonus_speed + self.bonus_speed

    def apply_buff(self, buff):
        atk = self.total_attack
        defence = self.total_defence
        speed = self.total_speed
        if self.buffs[buff] == 0:
            match (buff):
                case "attack":
                    print(f"{self.name} attack increases!")
                    self.buff_attack = 0
                    self.buffs[buff] = 4
                    self.buff_attack = int(atk * 1.5)
                case "defence":
                    print(f"{self.name} defence increases!")
                    self.buff_defence = 0
                    self.buffs[buff] = 4
                    self.buff_defence = int(defence * 1.5)
                case "speed":
                    print(f"{self.name} speed increases!")
                    self.buff_speed = 0
                    self.buffs[buff] = 4
                    self.buff_speed = int(speed * 1.5)
                case _:
                    input("error in apply buffs")
        else:
            print(F"{buff} is already active")
        self.update_stats()

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
    
    def countdown_buff_debuffs(self):
        for buff in self.buffs:
            if self.buffs[buff] == 0:
                pass
            elif self.buffs[buff] > 0:
                curr = self.buffs[buff]
                self.buffs[buff] = curr - 1
                if self.buffs[buff] == 0:
                    print(f"{self.name} {buff} up ends!")
                    match (buff):
                        case "attack":
                            self.buff_attack = 0
                        case "defence":
                            self.buff_defence = 0
                        case "speed":
                            self.buff_speed = 0
                        case _:
                            print("error in coundown buff debuffs -> buffs")
            else:
                input("error in countdown buffs and debuffs")
        for debuff in self.debuffs:
            if self.debuffs[debuff] == 0:
                pass
            elif self.debuffs[debuff] > 0:
                curr = self.debuffs[debuff]
                self.debuffs[debuff] = curr - 1
                if self.debuffs[debuff] == 0:
                    print(f"{self.name} {debuff} ends!")
            else:
                input("error in countdown buffs and debuffs")
        self.update_stats()

    def battle_update(self):
        self.countdown_buff_debuffs()
        self.apply_debuff_effect()