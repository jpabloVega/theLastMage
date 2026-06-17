import os 
from trinkets import opc

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

def clean_input(description_text: str) -> str:
    input_text = input(description_text)
    return input_text.lower()

def clean_and_split_input(description_text: str):
    text = clean_input(description_text)
    x = text.split(" ", 1) 
    if len(x) < 2:
        x.append(None)
    return x

def list_options(options: list[str]):
    print("\n")
    for option in options:
        print(f"+ {option}")
    print("\n")

def turn_to_digit(str_to_int: str) -> int:
    if str_to_int.isdigit():
        return int(str_to_int)
    return print(f"{str_to_int} is not a number")

def get_opc_list(list_name: str) -> list[str]:
    return opc[list_name]