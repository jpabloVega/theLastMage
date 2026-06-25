from inputFuntions import *
from hero import Hero
from trinkets import title_card

intro_txt = """
The Dark Lord arose
The wizards fought
And they fell
...

Libraries were destroyed
Magic forests burned
Magicians persecuted
Magic was lost

Or was it..?
In the depst of an old forest
A hidden library remained
An inside of it
The last mage
An his prodigious student
"""



def intro():
    clear_screen()
    show_text(intro_txt)
    name = ""
    while name == "":
        clear_screen()
        print("And his name was")
        name = input(" >")
    good_bye = f"""
Thats it, you have mastered my last spell
You are one of a kind {name}
But you still lack experience

Prove your worth
Go into the forest
Destroy the dens inhabited by monsters
Restore the withered trees
And find the lost reliqs

Until you do so
You wont be able to leave this forest

Try to avoid traveling at night
The darkness atracts stronger beasts
Rest to recover your strength
But dont lose focus on your objectives

Now leave
I know you will bring order back into the world
Even if Im not there to see it
"""
    show_text(good_bye)
    hero = Hero(name, 287, 300, 4, 39, 4, 1, 3, 35, 39, 1, 50)
    hero.equipment["Headwear"] = "old hat"
    hero.equipment["Robe"] = "stitched robe"
    hero.equipment["Boots"] = "normal boots"
    hero.equipment["Staff"] = "wood staff"
    input("He pushes you through the door")
    input("When you turn around the library is nowhere to be found")
    input("You see your surroundings")
    input("An old forest grows in every direction")
    input("You feel lost and scared")
    input("But above all else you feel determined")
    input(f"Go {name}")
    input("SAVE THE WORLD!!!")
    clear_screen()
    input(title_card)
    return hero

