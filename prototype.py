import mysql.connector
import random as r

# Connector does not work straight up, needs your own user and password
con = mysql.connector.connect(
                host='localhost',
                database='flight_game',
                user='kasper',
                password='Monkey',
                autocommit=True,
                collation="utf8mb4_general_ci"
                )

balance = 500




def current_airport(code):
    sql = f"select name from airport where ident = '{code}'"
    cursor = con.cursor()
    cursor.execute(sql)
    name = cursor.fetchall()
    return name[0][0]

# General gambling script
def gambling(money):
    curr_money = money
    game_select = ""
    while game_select != "return":
        game_select = input("Choose a game to play(dice,hilo) or go back(return): ")
        if game_select != "return":
            bet = int(input("How much do you want to bet: "))
        
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
                print(f"Second card is {second_card}.\n You win {bet} Dollars")
                curr_money += bet
            elif first_card == second_card:
                print(f"Second card is {second_card}.\n You tied")
            else:
                print(f"Second card is {second_card}.\n You lose {bet} Dollars")
                curr_money -= bet
    return curr_money

command = ""
# Command loop, end command stops loop
while command != "end":
    command = input("Select command (move,gamble,balance,end): ")
    if command == "move":
        next_airport = input("What airport do you want to go to now(ICAO): ").upper()
        airport = current_airport(next_airport)
        print(f"You are at {airport} ")
    elif command == "gamble":
        new_balance = gambling(balance)
        balance = new_balance
    elif command == "balance":
        print(f"You have {balance} Dollars")