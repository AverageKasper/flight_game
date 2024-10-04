## TODO: MAKE FUNCTION FOR RULE LIST AND SHIT

from utilities import anim_print
from utilities import clear_window
from utilities import int_check

def rule_print():
    anim_print("""HOW TO PLAY
Your goal is to avoid the loanshark (aka The Shark), and gather money to pay back your debt to him.
You fly around to different airports using CP (Carbon Points) and do tasks at the ariports to gain money.
Every flight puts the Shark 1 step behind and every task you do makes the Shark come 1 step closer.
""", delay = 0)
    page_turn = input(anim_print("Type 1 to go to the next page or 2 to play the game: ",delay = 0))
    page_turn = int_check(page_turn)
    while page_turn != 1 and page_turn != 2:
        page_turn = input(anim_print("Invalid option, try again: "))
        page_turn = int_check(page_turn)
    clear_window()
    if page_turn == 2:
        return
    anim_print("""DIFFICULTIES
On normal difficulty you are 10000€ in debt and start out with 1000€ and 7000CP.
On hard difficulty you are 20000€ in debt and start out with 0€ and 4000CP.
Choosing a difficulty doesnt affect the game otherwise.
""",delay=0)
    page_turn = input(anim_print("Type 1 to go to the next page or 2 to play the game: ",delay = 0))
    page_turn = int_check(page_turn)
    while page_turn != 1 and page_turn != 2:
        page_turn = input(anim_print("Invalid option, try again: "))
        page_turn = int_check(page_turn)
    clear_window()
    if page_turn == 2:
        return
    anim_print("""MOVING AND GAMEPLAY PART 1
When you move you will choose between 3 different airports.

TYPE 1: Cheapest option to fly to, costing 100CP.
Tasks to do at Type 1 airports are: Dumpster diving, Pickpocketing.

TYPE 2: Medium airports, costing 200CP.
Tasks to do at Type 2 airports are: Trivia, Part-time work.
               
TYPE 3: Largest airports, costing 500CP.
Tasks to do at Type 3 airports are: Gambling, Smoking.
""",delay=0)
    page_turn = input(anim_print("Type 1 to go to the next page or 2 to play the game: ",delay = 0))
    page_turn = int_check(page_turn)
    while page_turn != 1 and page_turn != 2:
        page_turn = input(anim_print("Invalid option, try again: "))
        page_turn = int_check(page_turn)
    clear_window()
    if page_turn == 2:
        return
    anim_print("""MOVING AND GAMEPLAY PART 2
At airports you can do 2 task per airport before you need to move to the next one.

""")

