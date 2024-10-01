import time
import os


# Animated print function
def anim_print(text, delay=0.00):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    return ""

# Clearing console function
def clear_window():
    os.system('cls' if os.name=='nt' else 'clear')

# Checks if value can be changed to int, used when need for number
def int_check(player_input):
    while player_input is not int:
        try:
            player_input = int(player_input)
        except:
           player_input =  input("Invalid option, try again: ")
        else:
           player_input = int(player_input)
           break 
    return player_input