import os 
from random import randint
from trinkets import opc, spells

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def show_text(text=""):
    lines = text.split("\n")
    for line in lines:
        if line == "":
            continue
        input(line)
    input("<continue>")
    clear_screen()

def clean_input(description_text="> ") -> str:
    input_text = input(description_text)
    input_text.strip()
    return input_text.lower()

def clean_and_split_input(description_text="> "):
    text = clean_input(description_text)
    x = text.split(" ", 1) 
    if len(x) < 2:
        x.append(None)
    return x

def list_options(options: list[str], symbol="+ "):
    for option in options:
        print(f"{symbol} {option}")
    print("\n")

def input_to_digit(description_text="> ") -> int:
    user_input = input(description_text)
    if user_input.isdigit():
        num = int(user_input)
        if num < 0:
            return 0
        else:
            return num
    return print(f"{user_input} is not a number")

def get_opc_list(list_name: str) -> list[str]:
    return opc[list_name]

def get_names(list_of_names):
    names = []
    for item in list_of_names:
        names.append(item.name)
    return names

def get_random_num(low=0, high=100):
    return randint(low, high)

def get_magic_options():
    result = ""
    for element, spell in spells.items():
        result += f"+ {element}\n"
        for item in spell:
            result += f"--{item}\n"
        result += "\n"
    print(result)
    print("back")