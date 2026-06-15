def battle(self, enemy):
    print(f"{self.name} fights against {enemy.name}")
    while self.health > 0 or enemy.health > 0:
        if enemy.speed > self.speed:
            ##enemy turn
            self.take_damage(enemy.attack())
            
        