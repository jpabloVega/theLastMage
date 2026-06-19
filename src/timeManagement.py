from inputFuntions import clear_screen, input_to_digit

def resting(hero):
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
        return amount

def get_am_pm(hour):
    if hour < 12 or hour == 24:
        if hour == 24:
            return "12 a.m."
        return f"{hour} a.m."
    hour -= 12
    return f"{hour} p.m."

def is_night(hour):
    if hour > 21 or hour < 5:
        return True
    return False

def add_hours(hours, amount):
    total = hours + amount
    if total > 24:
        return total - 24
    return total

