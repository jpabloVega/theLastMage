## Equipment and items used in objects
## [0=in_possession, 1=type, 2=bonus_defence 3=bonus_attack 4=speed]
equipment = {
    "old hat": [0, "Headwear", 10, 0, 0],
    "battle helmet": [0, "Headwear", 30, 10, 0],
    "rabadon hat": [0, "Headwear", 10, 30, 10],
    "stitched robe": [0, "Robe", 10, 0, 5],
    "chainmail armor": [0, "Robe", 30, 10, 5],
    "bear robe": [0, "Robe", 20, 10, 15],
    "normal boots": [0, "Boots", 10, 0, 10],
    "hermes boots": [0, "Boots", 10, 10, 20],
    "boots boots": [0, "Boots", 20, 20, 15],
    "wood staff": [0, "Staff", 0, 30, 0],
    "oak staff": [0, "Staff", 20, 20, 0],
    "light staff": [0, "Staff", 0, 40, 20],
    "equilibrium grimoire": [1, "Grimoire", 20, 20, 10],
    "destruction grimoire": [0, "Grimoire", 0, 50, 0],
    "inmortal grimoire": [0, "Grimoire", 30, 10, 10],
    }

equipment_cost = {
    "old hat": 100,
    "battle helmet": 200,
    "rabadon hat": 320,
    "stitched robe": 100,
    "chainmail armor": 250,
    "bear robe": 400,
    "normal boots": 100,
    "hermes boots": 300,
    "boots boots": 350,
    "wood staff": 100,
    "oak staff": 200,
    "light staff": 200,
    "equilibrium grimoire": 242,
    "destruction grimoire": 420,
    "inmortal grimoire": 400,
}

items = {
    "potion": 2,
    "manalyx": 0,
    "bandages": 1,
    "antidote": 1,
    "ointment": 1
}

items_cost = {
    "potion": 10,
    "manalyx": 20,
    "bandages": 5,
    "antidote": 5,
    "ointment": 5
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
        "Name": "Starving wolf",
        "Health": (200, 250),
        "Defence": (10, 15),
        "Attack": (42, 50),
        "Speed": (25, 30),
        "Cost": 1
    },
    "Armor": {
        "Name": "Possesed soldier corpse",
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
        "Name": "Killer pupper",
        "Health": (280, 331),
        "Defence": (42, 50),
        "Attack": (100, 122),
        "Speed": (45, 58),
        "Cost": 5
    },
    "Harpy": {
        "Name": "Dragon harpy",
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
        "Name": "Death emyssary",
        "Health": (600, 700),
        "Defence": (50, 62),
        "Attack": (140, 149),
        "Speed": (50, 55),
        "Cost": 10
    },
    "Lord": {
        "Name": "Echo of the Dark Lord",
        "Health": (2000, 2300),
        "Defence": (60, 72),
        "Attack": (130, 141),
        "Speed": (50, 68),
        "Cost": 11
    },
}

monster_loot = {
    "Starving wolf": [
        "Ragged pelt", 
        "Sharp fangs"
        ],
    "Possesed soldier corpse": [
        "Rusted armor scraps", 
        "Faded royal emblem"
        ],
    "Cursed undead": [
        "Silver pendant",
        "Red eyeball"
    ],
    "Exiled traitor elf": [
        "Worn out bow",
        "Statue of the forgoten god"
    ],
    "Killer pupper": [
        "Limp puppet",
        "Ultra fine string"
    ],
    "Dragon harpy": [
        "Harpys feather",
        "Sharp talons"
    ],
    "Melted corpses mass": [
        "Incomplete phylosopher stone",
        "Tear of the dammed"
    ],
    "Torturer devil": [
        "Bag of skulls",
        "Orders from hell"
    ],
    "Vengeful great tree": [
        "Rotten bark",
        "Polluted core"
    ],
    "Death emyssary": [
        "Death book",
        "Goat skull"
    ],
    "Echo of the Dark Lord": [
        "Broken blade",
        "Cursed blade"
    ]
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
        "discovered": True
    },
    (7, 3): {
        "name": "store",
        "discovered": True
    },
    (7, 7): {
        "name": "store",
        "discovered": True
    },
    (2, 9): {
        "name": "fight",
        "discovered": False
    },
    (1,  1): {
        "name": "fight",
        "discovered": False
    },
    (9, 0): {
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

objectives = {
    "Treasure chests found": [2, 3],
    "Monster dens destroyed": [4, 4],
    "Magic trees healed": [4, 4]
}

## Menu options
opc = {
    "main": ["move", "book", "bag", "stats", "rest", "quit"],
    "bag": ["items", "equipment", "loot", "back"],
    "movement": ["up", "down", "left", "right", "cancel"],
    "battle": ["attack", "magic", "items", "stats"],
    "battle_status": ["self", "enemies"],
    "store": ["items", "equipment", "sell", "leave"],
    "book": ["map", "spells", "objectives","back"]
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

title_card = """
___________.__             .__                   __                                   
\__    ___/|  |__   ____   |  | _____    _______/  |_    _____ _____     ____   ____  
  |    |   |  |  \_/ __ \  |  | \__  \  /  ___/\   __\  /     \\__  \   / ___\_/ __ \ 
  |    |   |   Y  \  ___/  |  |__/ __ \_\___ \  |  |   |  Y Y  \/ __ \_/ /_/  >  ___/ 
  |____|   |___|  /\___  > |____(____  /____  > |__|   |__|_|  (____  /\___  / \___  >
                \/     \/            \/     \/               \/     \//_____/      \/ 
                                                                                Made by: pabloV"""