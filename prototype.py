import mysql.connector
import random as r

# Connector does not work straight up, needs your own user and password
con = mysql.connector.connect(
                host='localhost',
                database='flight_game',
                user='root',
                password='K1rahV1!',
                autocommit=True,
                collation="utf8mb4_general_ci"
                )

# All variables
command = ""
balance = 500
airport_name = "Helsinki Vantaa Airport"
airport_country = "FI"
airport_icao = "EFHK"
airport_casino = ["LEBL"]

# Airport moving
def current_airport(code):
    sql = f"select name, iso_country, ident from airport where ident = '{code}'"
    cursor = con.cursor()
    cursor.execute(sql)
    name = cursor.fetchall()
    if cursor.rowcount > 0:
        return name[0][0] , name[0][1], name[0][2]
    else:
        return "","",""

# General gambling script
def gambling(money):
    curr_money = money
    game_select = ""
    while game_select != "return":
        game_select = input("Choose a game to play(dice,hilo) or go back(return): ")
        if game_select != "return":
            bet = int(input("How much do you want to bet: "))
            if bet > curr_money:
                print("You dont have enough money")
                continue
            else:
                # Dice game, win if higher than dealer
                if game_select == "dice":
                    dealer_dice1 = r.randint(1,6)
                    dealer_dice2 = r.randint(1,6)
                    player_dice1 = r.randint(1,6)
                    player_dice2 = r.randint(1,6)
                    dealer_dice_total = dealer_dice1 + dealer_dice2
                    player_dice_total = player_dice1 + player_dice2
                    if dealer_dice_total > player_dice_total:
                        print(f"The dealer got {dealer_dice1,dealer_dice2}.\nYou got {player_dice1,player_dice2}.\n"
                            f"You lost {bet} Dollars")
                        curr_money -= bet
                    elif dealer_dice_total < player_dice_total:
                        print(f"The dealer got {dealer_dice1,dealer_dice2}.\nYou got {player_dice1,player_dice2}.\n"
                            f"You won {bet} Dollars")
                        curr_money += bet
                    else:
                        print(f"The dealer got {dealer_dice1,dealer_dice2}.\nYou got {player_dice1,player_dice2}.\n"
                            f"You tied")
                
                # HiLo game, Win if correct quess
                elif game_select == "hilo":
                    first_card = r.randint(1,13)
                    print(f"First card is {first_card}.")
                    player_quess = input("Will the next one be higher or lower (HI/LO):").upper()
                    second_card = r.randint(1,13)
                    if (first_card < second_card and player_quess == "HI") or (first_card > second_card and player_quess == "LO"):
                        print(f"Second card is {second_card}.\nYou win {bet} Dollars")
                        curr_money += bet
                    elif first_card == second_card:
                        print(f"Second card is {second_card}.\nYou tied")
                    else:
                        print(f"Second card is {second_card}.\nYou lose {bet} Dollars")
                        curr_money -= bet
    return curr_money


# Command loop, end command stops loop
while command != "end":
    command = input("Select command (help): ")
    if command == "help":
        print("List of commands\n"
              "move - Move to a new airport\n"
              "gamble - Go to gambling\n"
              "balance - Check current balance\n"
              "end - Ends game\n"
              "airport - See what airport you are at currently"
              
              )
    elif command == "move":
        next_airport = input("What airport do you want to go to now(ICAO): ").upper()
        airtemp1,airtemp2,airtemp3 = current_airport(next_airport)
        if airtemp1 == "":
            print("This icao code is incorrect")
        else:
            airport_name, airport_country,airport_icao = airtemp1,airtemp2,airtemp3
            print(f"You are at {airport_name}, {airport_country} ")
            
    elif command == "gamble":
        if airport_icao in airport_casino:
            new_balance = gambling(balance)
            balance = new_balance
        else:
            print("This airport doesnt have a casino")
    elif command == "balance":
        print(f"You have {balance} Dollars")
    elif command == "airport":
        print(f"Your current airport is {airport_name}, {airport_country}")
    elif command == "end":
        print("Goodbye")
        break

#a random comment to test shit out
#another one