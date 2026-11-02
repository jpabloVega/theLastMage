#### The last mage
### Console RPG

Explore a forest filled with horrible monsters, discover its secrets and become a powerfull wizard.

Game made as part of the course Boot.dev

## Requisites

- Python installed

## How to start

- Run main.py in the src folder

### Features

## Explore the forest

- Move in a tile based world
- Each time you move an enemy might ambush you
- Time passes during certain actions, monsters become stronger at night
- A map shows you places you have been to and places you are yet to explore

## Items and equipment

- Find the stores in the forest, there you can buy items and equipment, and also sell the loot dropped by monsters
- Open your bag to use items or change your equipment

## Stats

- Health: When your health gets to 0 you lose
- Mana: You need this to cast most of your spells
- Attack: Increase the damage you deal
- Defence: Decrease the damage your recieve
- Speed: In battle the faster combatants move first, you will also get extra turns if you are really fast

## Combat

- Random encounters that become harder as you level up
- Monster variety, each monster has its own set of moves
- Get loot from defeating monsters

## Spells

# Flame Spells

- Ring: Deal damage to all enemies, with a low chance of burn
- Warmth: Recover some of your missing hp for a few turns
- Ignite: Deal damage to an enemy increased if the target is burned, or cast on self to get an attack buff and burn yourdelf
- Melt: Reduce enemy defence and set it on fire

# Earth spells

- Shield: Summon a shield that protects you from damage
- Oasis: Recover faster from status aliments for a few turns
- Swamp: Reduce enemy's speed and poison them
- Spike: Deal damage based on missing health may cause bleed

#Spirit spells

- Calm: Remove enemy buffs, or self cast to extend the duration of multiturn spells
- Bond: Pass status aliments from one target to another
- Steal: Deal damage and recover mana if it kills the enemy recover health and get a speed buff
- Ghost: Summon a ghost that follows your attacks

# Status

- Increase your stats using spells or lower the enemys
- Burn enemies, the more health they have the more damage they will recieve
- Bleed damage increases as they get low on health
- Poison does fixed damage, but last longer that any other status

## Why a game

I like videogames, specially RPG's.
While studying through the python course I kept getting ideas on how I could use what I learn this lesson to build a game.

## Challenges

I had to much fun working on this project, had to forbid myself from adding more stuff.
The bigger it got the harder it became to debbug, and sometimes fixing something breaks other part.
The equipment took me a while, and some of the spells were hard to implement to the point I almost removed them.
I should have planned ahead more, when I reached certain point I realized how much I complicated my life by not drawing a diagram of how everything should work.

## What I Learned

When the project gets bigger is so easy for it to become a mess.
I now know how important is to plan ahead so you dont have to change everything later on.
I also became more comfortable using objects in python, inheritance and polymorphism were key on this project.
I made a Character that had two childs Enemy and Hero, the Character made everything from recieving damage to applying buffs, I just had to add the magic spells to the hero and the special attacks to each monster, saving a lot of work.

## Final message

I had a ton of fun making this game, I hope you do playing it!
I tried my best to keep this experience free of bugs, but some might have sliped in, so sorry in advance.
