import time
import os
import random as r

def anim_print(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.0)

# Clearing console function
def clear_window():
    os.system('cls' if os.name=='nt' else 'clear')

def random_events():
    event_list = ["Pdiddy", "9/11", "Mother", "organ seller"]
    event_check = r.randint(1,4)
    if event_check == event_list.index(event_check):
        print("pdiddy")
    elif event_check == event_list.index(event_check):
        print("9/11")
    elif event_check == event_list.index(event_check):
        print("mother")
    elif event_check == event_list.index(event_check):
        print("Organ")
    




random_events()