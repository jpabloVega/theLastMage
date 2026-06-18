from constants import *

class Character():
    def __init__(self, name, health: float, max_health, defence: float, attack: float, speed: int):
        self.name = name
        self.max_health = max_health
        self.health = health
        self.defence = defence
        self.attack = attack
        self.speed = speed

    def attack_enemy(self, target: None):
        pass

    def take_dmg(self, dmg: float) -> bool:
        self.health -= dmg
    
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
    
