from character import Character

class Enemy (Character):
    def __init__(self, name, x, y, health, defence, attack):
        super().__init__(name, x, y, health, defence, attack)

    def attack(self):
        return self.attack