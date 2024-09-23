import mysql.connector
import random as r
import time
import os
import trivia
from gambling import casino
# Connector does not work straight up, needs your own user and password
con = mysql.connector.connect(
                host='localhost',
                database='flight_game',
                user='root',
                password='K1rahV1!',
                autocommit=True,
                collation="utf8mb4_general_ci"
                )

# Animated print function
def anim_print(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.0)

# Clearing console function
def clear_window():
    os.system('cls' if os.name=='nt' else 'clear')

# Variables
game_end = False
command = ""
balance = 500
airport_name = "Helsinki Vantaa Airport"
airport_country = "FI"
airport_type = "large_airport"
cp = 1500
airport_cp_cost = [100,200,500]
actions_per_airport = 2
# What if when you go to a small airport the event counter goes down by 1, medium goes by 2, and large goes by 3. and events are some good some bad, more bad
event_counter = 6
loan_shark = 2
task_active = True


# Airport moving
def airport_options(type):
    sql = f"select name, iso_country, type from airport where type = '{type}' and name not like 'CLICK%' order by rand() limit 1;"
    cursor = con.cursor()
    cursor.execute(sql)
    list = cursor.fetchall()
    return list[0]

# Function for next airport
def airport_chooser():
    anim_print (f"""\nYou are at {airport_name},{airport_country}.
Your next airport options are:
1. {small_airport[0]}, {small_airport[1]}: 100CP
2. {medium_airport[0]}, {medium_airport[1]}: 200CP
3. {large_airport[0]}, {large_airport[1]}: 500CP""")
    next_airport = int(input("\nSelect airport number: "))
    return next_airport
# General gambling script


# Function for dumpster diving at small airports, returns gained currencies
def dumpster_dive():
    money = 0
    cp = 0
    
    find = r.randint(1,10)
    if find == 1:
        trash_money = r.randint(50, 200)
        anim_print(f"\nYou found {trash_money} € from the trash!")
        money += trash_money
    elif find == 2:
        trash_money = r.randint(50, 200)
        anim_print(f"\nYou found {trash_money} € from the trash!")
        money += trash_money
    elif find == 3:
        trash_money = r.randint(50, 200)
        anim_print(f"\nYou found {trash_money} € from the trash!")
        money += trash_money
    elif find == 4:
        trash_money = r.randint(50, 200)
        anim_print(f"\nYou found {trash_money} € from the trash!")
        money += trash_money
    elif find == 5:
        trash_money = r.randint(50, 200)
        anim_print(f"\nYou found {trash_money} € from the trash!")
        money += trash_money
    elif find == 6:
        trash_money = r.randint(50, 200)
        anim_print(f"\nYou found {trash_money} € from the trash!")
        money += trash_money
    elif find == 7:
        trash_money = r.randint(50, 200)
        anim_print(f"\nYou found {trash_money} € from the trash!")
        money += trash_money
    elif find == 8:
        trash_money = r.randint(50, 200)
        anim_print(f"\nYou found {trash_money} € from the trash!")
        money += trash_money
    elif find == 9:
        trash_money = r.randint(50, 200)
        anim_print(f"\nYou found {trash_money} € from the trash!")
        money += trash_money
    elif find == 10:
        trash_money = r.randint(50, 200)
        anim_print(f"\nYou found {trash_money} € from the trash!")
        money += trash_money
    return money, cp


# Under here should be the last part of code
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
    next_airport = airport_chooser()
    
    # Check what airport was chosen
    if next_airport == 1:
        if cp < airport_cp_cost[0]:
            anim_print("You dont have enough CP.")
            continue
        else:
            airport_name, airport_country, airport_type= small_airport[0], small_airport[1], small_airport[2]
            cp -= airport_cp_cost[0]
    elif next_airport == 2:
        if cp < airport_cp_cost[1]:
            anim_print("You dont have enough CP.")
            continue
        else:
            airport_name, airport_country, airport_type= medium_airport[0], medium_airport[1], medium_airport[2]
            cp -= airport_cp_cost[1]
    elif next_airport == 3:
        if cp < airport_cp_cost[2]:
            anim_print("You dont have enough CP.")
            continue
        else:
            airport_name, airport_country, airport_type = large_airport[0], large_airport[1], large_airport[2]
            cp -= airport_cp_cost[2]
    # For testing, at selection input 4 to stop game
    elif next_airport == 4:
        game_end = True
        break
    anim_print(f"You have {cp}CP left.")
    loan_shark += 1
    # Task loop
    while actions_per_airport !=0 or task_active == True:


        # Insert task system here
        anim_print(f"\nYou are at {airport_name}, {airport_country}")
        # So far we have only 1 task, to gamble
        if airport_type == "small_airport":
            anim_print(f"""\nThings to do at this airport:
1. Dumpster dive
2. Go to the next airport
""")
            task_choice = int(input("What do you want to do: "))
            if task_choice == 1:
                temp_money, temp_cp = dumpster_dive()
                loan_shark -= 1
            elif task_choice == 2:
                clear_window()
                task_active = False
        elif airport_type == "medium_airport":
            anim_print(f"""\nThings to do at this airport:
1. Trivia
2. Go to the next airport
""")
            task_choice = int(input("What do you want to do: "))
            if task_choice == 1:
                trivia_score = trivia.trivia_game()
                print(trivia_score)
            elif task_choice == 2:
                clear_window()
                task_active = False
        elif airport_type == "large_airport":
            anim_print(f"""\nThings to do at this airport:
1. Gamble
2. Go to the next airport
""")
            task_choice = int(input("What do you want to do: "))
            if task_choice == 1:
                gambling_balance = casino(balance)
                balance = gambling_balance
                loan_shark -= 1
            elif task_choice == 2:
                clear_window()
                task_active = False
        # Shits fucked if it goes here
        else: 
            print("how the fuck you get here")
        actions_per_airport -= 1
        anim_print(f"\nthe loan shark is {loan_shark} airports behind...")
        if actions_per_airport == 0:
            task_active = False





    if cp < airport_cp_cost[0]:
        clear_window()
        anim_print(f"""\nYou dont have enough CP for any flights anymore.
Lets see how your journey has gone: 
#list shit here#""")
        input()
        game_end = True
    if loan_shark <1:
        if balance > 10000:
            anim_print("\nYou've been caught by the loan shark but you had enough money on you to pay them back.")
        else:
            anim_print("\nYou've been caught by the loan shark and got beaten to death...")

        game_end = True
    actions_per_airport = 2
    task_active = True






# Credits at the end of the game
anim_print(f"""\nCredits:  
Elias Eide
Munttu
Kasper Paredes Aalto
Alexander Wolff
Special thanks to:
Googling shit
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
""")
input()

# List of shit to do:
# Make more tasks
# Rewrite gambling(See alex) 
# See what else can be done with SQL(See munttu)
# Make Loanshark chasing 
# 
#
# List of problems: 
# Will crash if input is not number
# anim_print works but you can still use the next input before it finishes, kind of a non-issue but if can be looked at  
# If player doesnt have enough CP to a airport the code will randomize the choises again, maybe problem, maybe not
#
#
#
#

