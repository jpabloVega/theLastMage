from character import Character

class Hero(Character):
    def __init__(self, name, x, y, health, max_health, defence, attack, mana, speed):
        super().__init__(name, x, y, health, max_health, defence, attack)
        self.mana = mana
        self.speed = speed
    