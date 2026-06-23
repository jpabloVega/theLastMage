## Equipment and items used in objects
## [0=in_possession, 1=type, 2=bonus_defence 3=bonus_attack 4=speed]
equipment = {
    "Old hat": [0, "Headwear", 10, 0, 0],
    "Battle helmet": [0, "Headwear", 30, 10, 0],
    "Rabadon hat": [0, "Headwear", 10, 30, 10],
    "Stitched robe": [0, "Robe", 10, 0, 5],
    "Chainmail armor": [0, "Robe", 30, 10, 5],
    "Bear robe": [0, "Robe", 20, 10, 15],
    "Normal boots": [0, "Boots", 10, 0, 10],
    "Hermes boots": [0, "Boots", 10, 10, 20],
    "Boots boots": [0, "Boots", 20, 20, 15],
    "Wood staff": [0, "Staff", 0, 30, 0],
    "Oak staff": [0, "Staff", 20, 20, 0],
    "Light staff": [0, "Staff", 0, 40, 20],
    "Equilibrium grimoire": [0, "Grimoire", 20, 20, 10],
    "Destruction grimoire": [0, "Grimoire", 0, 50, 0],
    "Inmortal grimoire": [0, "Grimoire", 30, 10, 10],
    }

equipment_cost = {
    "Old hat": 100,
    "Battle helmet": 200,
    "Rabadon hat": 320,
    "Stitched robe": 100,
    "Chainmail armor": 250,
    "Bear robe": 400,
    "Normal boots": 100,
    "Hermes boots": 300,
    "Boots boots": 350,
    "Wood staff": 100,
    "Oak staff": 200,
    "Light staff": 200,
    "Equilibrium grimoire": 242,
    "Destruction grimoire": 420,
    "Inmortal grimoire": 400,
}

items = {
    "potion": 0,
    "manalyx": 0,
    "bandages": 0,
    "antidote": 0,
    "ointment": 0
}

items_cost = {
    "potion": 10,
    "manalyx": 20,
    "bandages": 5,
    "antidote": 5,
    "ointment": 5,
    "relic":  0
}

loot = {
        "Ragged pelt": {"inventory": 0, "cost": 10},
        "Sharp fangs": {"inventory": 0, "cost": 5},
        "Rusted armor scraps": {"inventory": 0, "cost": 10},
        "Faded royal emblem": {"inventory": 0, "cost": 15},
        "Silver pendant": {"inventory": 0, "cost": 25},
        "Red eyeball": {"inventory": 0, "cost": 10},
        "Worn out bow": {"inventory": 0, "cost": 20},
        "Statue of the forgoten god": {"inventory": 0, "cost": 200},
        "Limp puppet": {"inventory": 0, "cost": 30},
        "Ultra fine string": {"inventory": 0, "cost": 20},
        "Harpys feather": {"inventory": 0, "cost": 25},
        "Sharp talons": {"inventory": 0, "cost": 20},
        "Incomplete phylosopher stone": {"inventory": 0, "cost": 30},
        "Tear of the dammed": {"inventory": 0, "cost": 35},
        "Bag of skulls": {"inventory": 0, "cost": 50},
        "Letter from hell": {"inventory": 0, "cost": 200},
        "Rotten bark": {"inventory": 0, "cost": 40},
        "Polluted core": {"inventory": 0, "cost": 70},
        "Death book": {"inventory": 0, "cost": 100},
        "Hell bell": {"inventory": 0, "cost": 80},
        "Broken blade": {"inventory": 0, "cost": 10},
        "Cursed blade": {"inventory": 0, "cost": 300}
}



## Monster info
monster_stats = {
    "Wolf": {
        "Name": "Weak wolf",
        "Health": (200, 250),
        "Defence": (10, 15),
        "Attack": (42, 50),
        "Speed": (25, 30),
        "Cost": 1
    },
    "Armor": {
        "Name": "Rusted enchanted armor",
        "Health": (500, 580),
        "Defence": (30, 39),
        "Attack": (17, 21),
        "Speed": (5, 8),
        "Cost": 2
    },
    "Zombie": {
        "Name": "Cursed undead",
        "Health": (350, 420),
        "Defence": (17, 21),
        "Attack": (70, 91),
        "Speed": (18, 25),
        "Cost": 3
    },
    "Elf": {
        "Name": "Exiled traitor elf",
        "Health": (300, 320),
        "Defence": (23, 35),
        "Attack": (80, 91),
        "Speed": (35, 42),
        "Cost": 4
    },
    "Puppet": {
        "Name": "Devil puppet",
        "Health": (200, 223),
        "Defence": (42, 50),
        "Attack": (35, 42),
        "Speed": (45, 58),
        "Cost": 5
    },
    "Harpy": {
        "Name": "Winged dragon priestess",
        "Health": (380, 412),
        "Defence": (38, 48),
        "Attack": (72, 84),
        "Speed": (45, 48),
        "Cost": 6
    },
    "Mass": {
        "Name": "Melted corpses mass",
        "Health": (900, 1000),
        "Defence": (52, 62),
        "Attack": (70, 81),
        "Speed": (5, 8),
        "Cost": 7
    },
    "Devil": {
        "Name": "Torturer devil",
        "Health": (400, 435),
        "Defence": (40, 52),
        "Attack": (90, 95),
        "Speed": (39, 46),
        "Cost": 8
    },
    "Tree": {
        "Name": "Vengeful great tree",
        "Health": (1200, 1400),
        "Defence": (50, 62),
        "Attack": (80, 91),
        "Speed": (5, 8),
        "Cost": 9
    },
    "Goat": {
        "Name": "Goat shaped creature",
        "Health": (600, 700),
        "Defence": (50, 62),
        "Attack": (80, 91),
        "Speed": (50, 55),
        "Cost": 10
    },
    "Lord": {
        "Name": "Dark Lord Echo",
        "Health": (2000, 2300),
        "Defence": (60, 72),
        "Attack": (100, 121),
        "Speed": (50, 68),
        "Cost": 11
    },
}

monster_loot = {
    "Wolf": {
        "Ragged pelt": 10,
        "Sharp fangs": 5,
    },
    "Armor": {
        "Rusted armor scraps": 10,
        "Faded royal emblem": 15,
    },
    "Zombie": {
        "Silver pendant": 25,
        "Red eyeball": 10,
    },
    "Elf": {
        "Worn out bow": 20,
        "Statue of the forgoten god": 200
    },
    "Puppet": {
        "Limp puppet": 30,
        "Ultra fine string": 20
    },
    "Harpy": {
        "Harpys feather": 25,
        "Sharp talons": 20
    },
    "Mass": {
        "Incomplete phylosopher stone": 30,
        "Tear of the dammed": 35
    },
    "Devil": {
        "Bag of skulls": 50,
        "Letter from hell": 200
    },
    "Tree": {
        "Rotten bark": 40,
        "Polluted core": 70
    },
    "Goat": {
        "Death book": 100,
        "Hell bell": 80
    },
    "Lord": {
        "Broken blade": 10,
        "Cursed blade": 300
    }
}

## Important locations
locations = {
    (0, 8): {
        "name": "chest",
        "discovered": False,
    },
    (1, 4): {
        "name": "chest",
        "discovered": False,
    },
    (1, 2): {
        "name": "chest",
        "discovered": False,
    },
    (3, 7): {
        "name": "store",
        "discovered": False
    },
    (7, 3): {
        "name": "store",
        "discovered": False
    },
    (7, 7): {
        "name": "store",
        "discovered": False
    },
    (10, 7): {
        "name": "store",
        "discovered": False
    },
    (7, 10): {
        "name": "store",
        "discovered": False
    },
    (7, 0): {
        "name": "store",
        "discovered": False
    },
    (0, 7): {
        "name": "store",
        "discovered": False
    },
    (2, 9): {
        "name": "fight",
        "discovered": False
    },
    (1,  1): {
        "name": "fight",
        "discovered": False
    },
    (10, 0): {
        "name": "fight",
        "discovered": False
    },
    (8, 7): {
        "name": "fight",
        "discovered": False
    },
    (5, 9): {
        "name": "tree",
        "discovered": False
    },
    (9, 5): {
        "name": "tree",
        "discovered": False
    },
    (2, 5): {
        "name": "tree",
        "discovered": False
    },
    (5, 1): {
        "name": "tree",
        "discovered": False
    }
}

## Menu options
opc = {
    "main": ["move", "book", "bag", "stats", "rest", "quit"],
    "bag": ["items", "equipment", "back"],
    "movement": ["up", "down", "left", "right", "cancel"],
    "battle": ["attack", "magic", "items", "stats"],
    "battle_status": ["self", "enemies"],
    "store": ["items", "equipment", "sell", "leave"]
}

## Magic
spells = {
    "flame": ["ring", "warmth", "ignite", "melt"],
    "earth": ["shield", "oasis", "swamp", "spike"],
    "spirit": ["calm", "bond", "steal", "ghost"]
}

spell_costs = {
    "ring": 3,
    "warmth": 5,
    "ignite": 2,
    "melt": 1,
    "shield": 2,
    "oasis": 5,
    "swamp": 1,
    "spike": 4,
    "calm": 2,
    "bond": 4,
    "steal": 0,
    "ghost": 5,
}