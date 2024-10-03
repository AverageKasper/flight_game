import random as r
import time

import mysql.connector
#Task Scripts
from triviasql import trivia_game
from gambling import casino
from random_events import random_event
from pickpocket import pickpocket
from rules import rule_print
from dumpster import dumpster_dive

# Utilities 
from utilities import anim_print
from utilities import clear_window
from utilities import int_check
from utilities import loading
# Remember to change your own credentials in the connector
from utilities import conn
from smoking import smoking_action




# Variables
game_end = False
command = ""
balance = 1000
airport_name = "Helsinki Vantaa Airport"
airport_country = "FI"
airport_type = "large_airport"
cp = 7000
phallic_object = 0
airport_cp_cost = [100,200,500]
actions_per_airport = 2
# What if when you go to a small airport the event counter goes down by 1, medium goes by 2, and large goes by 3. and events are some good some bad, more bad
kidney = 2
event_counter = 6
loan_shark = 2
airports_travelled = 0

# Airport moving
def airport_options(type):
    sql = f"select name, iso_country, type from airport where type = '{type}' and name not like 'CLICK%' order by rand() limit 1;"
    cursor = conn.cursor()
    cursor.execute(sql)
    list = cursor.fetchall()
    return list[0]

# Function for next airport
def airport_chooser(cod_points, euro,shark):
    anim_print (f"""\nYou are at {airport_name},{airport_country}.
You have {cod_points}CP left and {euro}€ in the bank.
The Shark is {shark} airports behind...
Your next airport options are:
1. {small_airport[0]}, {small_airport[1]}: 100CP
2. {medium_airport[0]}, {medium_airport[1]}: 200CP
3. {large_airport[0]}, {large_airport[1]}: 500CP""")
    next_airport = input(anim_print("\nSelect airport number: "))
    next_airport= int_check(next_airport)
    return next_airport

# Small airport tasks
def s_airport_task(shark):
    small_money = 0
    small_cp = 0
    small_phallic_object = 0
    actions_left = 2
    while actions_left > 0:
        anim_print(f"""\nThe Shark is {shark} airports behind...
Things to do at this airport:
1. Dumpster dive
2. Pickpocket
3. Go to the next airport
""")
        task_choice = input(anim_print("What do you want to do: "))
        task_choice = int_check(task_choice)
        # Checks if task_choice is  valid
        while task_choice not in range(1,4):
            task_choice = input("Invalid option, try again: ")
            task_choice = int_check(task_choice)
            
        if task_choice == 1:
            temp_money, temp_cp, small_phallic_object   = dumpster_dive()
            small_money += temp_money
            small_cp += temp_cp
            shark -= 1
            actions_left -= 1
        elif task_choice == 2:
            temp_money = pickpocket()
            small_money += temp_money 
            shark -= 1
            actions_left -= 1
        elif task_choice == 3:
            clear_window()
            break
    return small_money, small_cp, small_phallic_object, shark

# Medium airport tasks
def m_airport_task(shark):
    medium_money = 0
    medium_cp = 0
    total_money = 0
    total_cp = 0
    actions_left = 2
    while actions_left >0:
        anim_print(f"""\nThe Shark is {shark} airports behind...
Things to do at this airport:
1. Trivia
2. Go to the next airport
""")
        task_choice = input(anim_print("What do you want to do: "))
        task_choice = int_check(task_choice)
        # Checks if task_choice is  valid
        while task_choice != 1 and task_choice != 2:
            task_choice = input("Invalid option, try again: ")
            task_choice = int_check(task_choice)
        
        if task_choice == 1:
            trivia_score = trivia_game()
            if trivia_score == 1:
                medium_money = 300
                anim_print(f"You got {medium_money}€")
            elif trivia_score == 2:
                medium_money = 600
                anim_print(f"You got {medium_money}€")
            elif trivia_score == 3:
                medium_money = 1000
                medium_cp = 500
                anim_print(f"You got {medium_money}€ and a Voucher for {medium_cp}CP!")

            shark -= 1
            total_money += medium_money
            total_cp += medium_cp
            actions_left -= 1
        elif task_choice == 2:
            clear_window()
            break
    return medium_money, medium_cp, shark


# Large airport tasks
def l_airport_task(current_money,shark):
    
    large_money = 0
    large_cp = 0
    total_money = current_money
    total_cp = 0
    actions_left = 2
    while actions_left >0:
        anim_print(f"""\nThe Shark is {shark} airports behind...
Things to do at this airport:
1. Gamble
2. Smoking break
3. Go to the next airport
""")
        task_choice = input(anim_print("What do you want to do: "))
        task_choice = int_check(task_choice)

        # Checks if task_choice is  valid
        while task_choice != 1 and task_choice != 2:
            task_choice = input("Invalid option, try again: ")
            task_choice = int_check(task_choice)
        if task_choice == 1:
            large_money = casino(total_money)
            total_money = large_money
            shark -= 1
            actions_left -= 1
        elif task_choice == 2:
            temp_money=smoking_action()
            total_money+=temp_money
            shark-=1
            actions_left -= 1
        elif task_choice == 3:
            clear_window()
            break
    return total_money, total_cp, shark



clear_window()
# Under here starts the game

## TODO:   MAIN MENU
##          Change pickpocket penalty    
anim_print("""Welcome to Dept & Deceit.
Would you like to play the game or read the rules?
""")
game_choice = input(anim_print("Type play or rules: ")).upper()
while game_choice != "PLAY" and game_choice != "RULES":
    game_choice = input(anim_print("Incorrect command. Type play or rules: ")).upper()
if game_choice == "RULES":
    clear_window()
    rule_print()





clear_window()
# Small beginning lore
anim_print(f"""You are 10000€ in debt with only 500€ left.
You have to escape the loanshark by flying away using your Carbon Points(CP).
""")
# Main game loop
while game_end == False:
    # Change airport part
    small_airport = airport_options("small_airport")
    medium_airport = airport_options("medium_airport")
    large_airport = airport_options("large_airport")
    
    # Go to airport choosing function 
    next_airport = airport_chooser(cp,balance,loan_shark)
    
    # Check what airport was chosen
    if next_airport == 1:
        if cp < airport_cp_cost[0]:
            anim_print("You dont have enough CP.")
            continue
        else:
            airport_name, airport_country, airport_type= small_airport[0], small_airport[1], small_airport[2]
            cp -= airport_cp_cost[0]
            event_counter -= 1
            airports_travelled += 1
    elif next_airport == 2:
        if cp < airport_cp_cost[1]:
            anim_print("You dont have enough CP.")
            continue
        else:
            airport_name, airport_country, airport_type= medium_airport[0], medium_airport[1], medium_airport[2]
            cp -= airport_cp_cost[1]
            event_counter -= 2
            airports_travelled += 1
    elif next_airport == 3:
        if cp < airport_cp_cost[2]:
            anim_print("You dont have enough CP.")
            continue
        else:
            airport_name, airport_country, airport_type = large_airport[0], large_airport[1], large_airport[2]
            cp -= airport_cp_cost[2]
            event_counter -= 3
            airports_travelled += 1

    # For testing, at selection input 4 to stop game
    elif next_airport == 4:
        game_end = True
        break
    else:
        cp -= airport_cp_cost[2]
        event_counter -= 3
    clear_window()
    
    loan_shark += 1

    # Task loop
    while actions_per_airport !=0:

        anim_print(f"\nYou are at {airport_name}, {airport_country}")
        anim_print(f"\nYou have {cp}CP left.\n")
        anim_print(f"You have {balance}€.")
        # Goes to small airport task function
        if airport_type == "small_airport":
            temp_money,temp_cp, small_phallic_object, loan_shark = s_airport_task(loan_shark)
            balance += temp_money
            cp += temp_cp
            phallic_object += small_phallic_object
            break
        elif airport_type == "medium_airport":
            temp_money,temp_cp,loan_shark = m_airport_task(loan_shark)
            balance += temp_money
            cp += temp_cp
            break
        elif airport_type == "large_airport":
            temp_money,temp_cp,loan_shark = l_airport_task(balance, loan_shark)
            balance = temp_money
            cp += temp_cp
            break

        # Shit is fucked
        else: 
            print("how the fuck you get here")
        actions_per_airport -= 1

        if actions_per_airport == 0:
            break
    
    if cp < airport_cp_cost[0]:
        clear_window()
        anim_print(f"""\nYou have run out of CP to continue flying.
                   """)
        
        input()
        game_end = True
        if balance > 10000:
            pass
    if loan_shark <1:
        if balance > 10000:
            anim_print("""\nYou've been caught by the Shark.
Throughout your journey you have managed to gather enough money to pay him back.
GOOD ENDING
""")
        elif balance < 10000 and phallic_object > 0:
            anim_print("""\nYou've been cought by the Shark...
You did not manage to gather enouth money on time but you feel 
the wormth of a phallical object in your pocket. You decide to try your luck
and smack the poor guy right in the testies. He never stood a chance...
you manage to get away this time and get another chance to gather the money!
""")        
            phallic_object -= 1
            loan_shark += 2
            continue

        else:
            anim_print("""\nYou've been caught by the Shark.
You did not manage to gather enough money on time.
You got beaten up by the Shark and put in jail for life.
BAD ENDING
""")

        game_end = True
    actions_per_airport = 2
    task_active = True

    # Random event. If counter reaches 0 or under, executes random event script
    if event_counter <= 0:
        event_money, event_cp, kidney, player_death, roulette_played, shark = random_event()
        balance += event_money
        cp += event_cp
        loan_shark += shark

        # Results of russian roulette if played
        if roulette_played == True:

            # Ending lore for the russian roulette, if the player dies
            if player_death == True:
                anim_print("""You died during your game of russian roulette.
Your body was never found. 
BRUTAL ENDING
""")
                time.sleep(3)
                break

            # Ending lore for the russian roulette, if the player surrvives
            elif player_death == False:
                anim_print("""The Shark died during the game of russian roulette.
You got free of your debt and inherited the sharks loan business.
You found a list of names in the office.
Time to go hunting.
VILLAIN ENDING
""")
                time.sleep(3)
                break
        event_counter = 6


anim_print(f"""Stats:
Your money: {balance}€
Your Carbon points: {cp}CP
Total airports travelled: {airports_travelled}
Your kidneys: {kidney}
Phallic objects collected: {phallic_object}
""")
loading()
clear_window()

# Credits at the end of the game
anim_print(f"""Credits:  
Elias Eide
Munttu
Kasper Paredes Aalto
Alexander Wolff
Special thanks to:
Googling shit""")
anim_print("""
———————————No bitches?———————————
⠀⣞⢽⢪⢣⢣⢣⢫⡺⡵⣝⡮⣗⢷⢽⢽⢽⣮⡷⡽⣜⣜⢮⢺⣜⢷⢽⢝⡽⣝
⠸⡸⠜⠕⠕⠁⢁⢇⢏⢽⢺⣪⡳⡝⣎⣏⢯⢞⡿⣟⣷⣳⢯⡷⣽⢽⢯⣳⣫⠇
⠀⠀⢀⢀⢄⢬⢪⡪⡎⣆⡈⠚⠜⠕⠇⠗⠝⢕⢯⢫⣞⣯⣿⣻⡽⣏⢗⣗⠏⠀
⠀⠪⡪⡪⣪⢪⢺⢸⢢⢓⢆⢤⢀⠀⠀⠀⠀⠈⢊⢞⡾⣿⡯⣏⢮⠷⠁⠀⠀
⠀⠀⠀⠈⠊⠆⡃⠕⢕⢇⢇⢇⢇⢇⢏⢎⢎⢆⢄⠀⢑⣽⣿⢝⠲⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡿⠂⠠⠀⡇⢇⠕⢈⣀⠀⠁⠡⠣⡣⡫⣂⣿⠯⢪⠰⠂⠀⠀⠀⠀
⠀⠀⠀⠀⡦⡙⡂⢀⢤⢣⠣⡈⣾⡃⠠⠄⠀⡄⢱⣌⣶⢏⢊⠂⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢝⡲⣜⡮⡏⢎⢌⢂⠙⠢⠐⢀⢘⢵⣽⣿⡿⠁⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠨⣺⡺⡕⡕⡱⡑⡆⡕⡅⡕⡜⡼⢽⡻⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⣳⣫⣾⣵⣗⡵⡱⡡⢣⢑⢕⢜⢕⡝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣴⣿⣾⣿⣿⣿⡿⡽⡑⢌⠪⡢⡣⣣⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡟⡾⣿⢿⢿⢵⣽⣾⣼⣘⢸⢸⣞⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠁⠇⠡⠩⡫⢿⣝⡻⡮⣒⢽⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
—————————————————————————————
""", 0.0001)
input()

# List of shit to do:
# Make more tasks
# 
#monk
# List of problems: 
#
# ENDINGS to make
#KIDNEY ENDING
#



#___________________________________________________________
# Check duplicate lines = cntr + f > .* > ^(.*)(\n\1)+$ 