from enemy import *
from trinkets import equipment
from hero import Hero

x = equipment["normal hat"][2]
y = equipment["normal hat"][3]

print(x, y)

hero = Hero("Pablo", 298, 300, 5, 300, 4, 1, 2, 29, 39)

hero.test_equipment_values()
