## Equipment and items used in objects
## [0=in_possession, 1=type, 2=bonus_defence 3=bonus_attack 4=speed]
equipment = {
    "normal hat": [1, "Headwear", 10, 0, 0],
    "normal staff": [1, "Staff", 0, 10, 0],
    "insane staff": [1, "Staff", 10, 100, 0],
    "normal robe": [1, "Robe", 10, 0, 5],
    }

items = {
    "potion": 3,
    "mana crystal": 0,
    "bomb": 4,
}

## Monster info
monster_stats = {
    "Wolf": {
        "Name": "Weak wolf",
        "Health": (900, 1000),
        "Defence": (28, 35),
        "Attack": (42, 50),
        "Speed": (20, 30),
        "Cost": 1
    },
    "Armor": {
        "Name": "Rusted enchanted armor",
        "Health": (2000, 2300),
        "Defence": (50, 72),
        "Attack": (17, 21),
        "Speed": (5, 8),
        "Cost": 2
    }
}

## Important locations
locations = {
    (2, 2): "magic tree",
    (5, 5): "exit",
}

## Menu options
opc = {
    "main": ["move", "battle", "bag", "status", "spawn", "quit"],
    "bag": ["items", "equipment", "back"],
    "movement": ["up", "down", "left", "right", "cancel"],
    "battle": ["attack", "magic", "items", "stats"],
    "battle_status": ["myself", "enemies"]
}

## Magic
spells = {
    "flame": ["ring", "warmth", "ignite", "melt"],
    "earth": ["shield", "oasis", "swamp", "spike"],
    "spirit": ["clean", "bond", "steal", "berserk"],
    "staff": ["bash", "swipe", "vampire", "empower"]
}