
from utilities import anim_print
from utilities import clear_window
from utilities import int_check
import random as r
choice = 0

def dialogue_1():
    anim_print("Random traveller: Oh... I didn't notice you there. Anything I can help you with? UwU:3")
    choice = input(anim_print("select an option:\n    1. Never mind...\n    2. Yes, I need to borrow some cash!\n   3. (explain ur situation)")).upper
    CP = 0
    while True:
        if choice == 1:
            anim_print("Random traveller: ???")
            break
        elif choice == 2:
            anim_print("hmm... I'm afraid I can't help you with that, but I have some CP I don't need. Here, take these 1000 CP")
            CP += 1000
            break
        elif choice == 3:
            anim_print("Really? Sounds bad! Perhaps these CP can help you out on your journey. I don't have any use for them anyway...")
            CP += 1000
            break
        else:
            anim_print("Invalid choice, please select 1, 2, or 3.")
        
        
dialogue_1()