import random as r
import time
import os
# Animated print function
def anim_print(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.03)

# Clearing console function
def clear_window():
    os.system('cls' if os.name=='nt' else 'clear')

def casino(money):
    curr_money = money
    game_select = ""
    anim_print("MONEKNOMOEKEOMONKE")
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