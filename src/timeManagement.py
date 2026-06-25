from inputFuntions import clear_screen, input_to_digit

def resting(hero, time):
    clear_screen()
    max_health = hero.max_health
    heal_per_hour = max_health / 20
    max_mana = hero.max_mana
    mana_per_hour = max_mana / 20
    amount = input_to_digit("Rest how many hours?: > ")
    if not isinstance(amount, int):
        return 0
    if amount <= 0:
        input("No rest for the wicked")
        return 0
    else:
        input(f"You rest {amount} hours")
        hero.heal(int(heal_per_hour * amount))
        hero.heal_mana(int(mana_per_hour * amount))
        time += amount
        while time > 24:
            time -= 24
        return time

def get_am_pm(hour):
    hour = hour % 24
    if hour < 12:
        print(f"{hour} a.m.")
    else:
        xhour = hour - 12
        print(f"{xhour} p.m.")
    return hour

def is_night(hour):
    if hour > 21 or hour < 5:
        return True
    return False

def add_hours(hours, amount):
    total = hours + amount
    if total > 24:
        return total - 24
    return total

