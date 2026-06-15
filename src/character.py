from constants import *

class Character():
    def __init__(self, name: str, x: int, y: int, health: float, max_health:float, defence: float, attack: float):
        self.name = name
        self.x = x
        self.y = y
        self.position = (x, y)
        self.health = health
        self.max_health = max_health
        self.defence = defence
        self.attack = attack

    def take_dmg(self, dmg):
        self.health -= (dmg - self.defence)
        if self.health < 0:
            self.die()
        return
    
    def heal(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health
        return

    
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
        return
    
    def die(self):
        pass
    
