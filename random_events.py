import time
import os
import random as r

def anim_print(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.03)

# Clearing console function
def clear_window():
    os.system('cls' if os.name=='nt' else 'clear')

# Russian roulette function
def russian_roulette():
    bullet = 1
    player_death = False
    shark_death = False
    player_turn = False
    anim_print("Bonk\n")
    time.sleep(2)
    anim_print(f"""You wake up in a dark cellar with 2 chairs and a table.          
You see a 6 chamber revolver on the table.          
The loanshark is across the table from you.         
A rough voice speaks at you.            
"Its time to start the game now"            
"There is 1 bullet loaded into the revolver in front of you"            
"You will take turns firing the gun at your head"           
"Whoever survives gets to walk away"            
"Lets flip a coin for who goes first"           
""")
    coin_flip = input("Heads or tails: ").upper()
    coin_flip_result = r.randint(1,2)
    if (coin_flip_result == 1 and coin_flip == "HEADS") or (coin_flip_result == 2 and coin_flip == "TAILS"):
        anim_print("""Player goes first.\n""")
        player_turn = True
    else:
        anim_print("""Shark goes first\n""")
        player_turn = False
    time.sleep(1)
    while player_death == False and shark_death == False:
        if player_turn == True:
            anim_print("""You spin the chamber\n""")
            time.sleep(1)
            chamber_spin = r.randint(1,6)
            if chamber_spin == bullet:
                anim_print("""BANG!         \n""")
                player_death = True
                break
            else:
                anim_print("""CLICK             
You live for a moment longer.
""")
                player_turn = False
        elif player_turn == False:
            anim_print("""Shark spins the chamber\n""")
            time.sleep(1)
            chamber_spin = r.randint(1,6)
            if chamber_spin == bullet:
                anim_print("""BANG!             
""")

                shark_death = True
                break
            else:
                anim_print("""CLICK             
Shark stares you in the eyes.
""")
                player_turn = True
    return player_death
def random_event():
    event_list = ["Sausage",
                    "9/11",
                    "Mother",
                    "organ seller",
                    "Loanshark",
                    "Celebrity"]
    event_money = 0
    event_cp = 0
    player_death = False
    roulette_played = False
    kidney = 2
    event_check = r.randint(0,len(event_list)-1)
    if len(event_list) == 0:
        return
    if "Sausage" == event_list[event_check] :
        anim_print("""You found a person digging through the trash for a sausage.
Strange people these days.
""")
        
        event_list.remove("Sausage")
    elif "9/11" == event_list[event_check]:
        print("9/11")
        event_list.remove("9/11")
    elif "Mother" == event_list[event_check]:
        anim_print("""Your mother is calling you, do you wish to pick up?\n""")
        call_answer = input("Yes/No: ").upper()
        if call_answer == "YES":
            mother_money = r.randint(100,300)
            anim_print(f"""You picked up the phone.              
You hear your mothers voice.                
"Hello my child, i hear you are in a bit of a tight spot."              
"I will send you some money"                
You got {mother_money}€ from your mother.
""")
            event_money = mother_money
        else: 
            anim_print("You chose to not pick up.")
        event_list.remove("Mother")
    # Organ seller event
    elif "organ seller" == event_list[event_check]:
        anim_print(f"""You meet an black market organ seller.
He offers to buy your kidney
Do you accept?
""")
        kidney_sold = input("Yes/no: ").upper()
        if kidney_sold == "YES":
            kidney_money = r.randint(1500,3500)
            kidney = 1
            anim_print(f"You sold your kidney for {kidney_money}€")
            event_money = kidney_money
        event_list.remove("organ seller")
    elif "Loanshark" == event_list[event_check]:
        anim_print("The loanshark is calling you, do you wish to pick up?\n")
        call_answer = input("Yes/No: ").upper()
        if call_answer == "YES":
            anim_print("""You chose to answer the phone.
He gives you a choice.
1. Play russain roulette with him to settle your debt.
2. Continue the chase.""")
            choice = int(input("What is your choice: "))
            if choice == 1:
                anim_print("You chose to play russian roulette.")
                player_death = russian_roulette()
                roulette_played = True
            elif choice == 2:
                anim_print("You declined his offer. The game continues")
        
        else:
            anim_print("You chose to not pick up.")
            
        event_list.remove("Loanshark")
    
    elif "Celebrity" == event_list[event_check]:
        anim_print("""You see a vaguely familiar looking celebrity.
All of a sudden he starts throwing cash around.
People rush in to gather as much as they can.

""")
    # end of random events
    else:
        event_check = r.randint(0,len(event_list)-1)
    return event_money, event_cp, kidney, player_death, roulette_played



