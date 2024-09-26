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
    game_select = ""
    gameoptions=["SNAKE EYES", "HILO", "DICE", "RETURN"]
    while game_select != gameoptions[3]:
        game_select = input("Choose a game to play(dice,hilo, snake eyes) or go back(return): ").upper()
        if game_select not in gameoptions:
            print("Invalid selection")
            continue
        if game_select !=gameoptions[3]:
            bet = int(input("How much do you want to bet: "))
            if bet > money:
                print("You dont have enough money")
                continue
            else:
                # Dice game, win if higher than dealer
                if game_select ==gameoptions[2]:
                    dealer_dice1 = r.randint(1,6)
                    dealer_dice2 = r.randint(1,6)
                    player_dice1 = r.randint(1,6)
                    player_dice2 = r.randint(1,6)
                    dealer_dice_total = dealer_dice1 + dealer_dice2
                    player_dice_total = player_dice1 + player_dice2
                    if dealer_dice_total > player_dice_total:
                        print(f"The dealer got {dealer_dice1,dealer_dice2}.\nYou got {player_dice1,player_dice2}.\n"
                            f"You lost {bet} Dollars")
                        money -= bet
                    elif dealer_dice_total < player_dice_total:
                        print(f"The dealer got {dealer_dice1,dealer_dice2}.\nYou got {player_dice1,player_dice2}.\n"
                            f"You won {bet} Dollars")
                        money += bet
                    else:
                        print(f"The dealer got {dealer_dice1,dealer_dice2}.\nYou got {player_dice1,player_dice2}.\n"
                            f"You tied")
                
                # HiLo game, Win if correct quess
                elif game_select ==gameoptions[1]:
                    first_card = r.randint(1,13)
                    print(f"First card is {first_card}.")
                    player_quess = input("Will the next one be higher or lower (HI/LO):").upper()
                    second_card = r.randint(1,13)
                    if (first_card < second_card and player_quess == "HI") or (first_card > second_card and player_quess == "LO"):
                        print(f"Second card is {second_card}.\nYou win {bet} Dollars")
                        money += bet
                    elif first_card == second_card:
                        print(f"Second card is {second_card}.\nYou tied")
                    else:
                        print(f"Second card is {second_card}.\nYou lose {bet} Dollars")
                        money -= bet
                #Snake eyes
                elif game_select== gameoptions[0]:
                    dice_1 = r.randint(1,6)
                    dice_2 = r.randint(1,6)
                    print(f"{dice_1} and {dice_2}.")
                    if dice_1==dice_2==1:
                        print("HUGE WIN BOZO")
                        print(f"You won {bet*10} euros")
                        money +=bet*10
                        print(f"Your total balance is {money}")
                    elif (dice_1>=2 and dice_2>=2) and dice_1==dice_2:
                        print("Small win bozo")
                        print(f"You won {bet} euros")
                        money +=bet
                        print(f"Your total balance is {money}")
                    else:
                        print(f"You lost {bet} euros bozo")
                        money -=bet
                        print(f"Your total balance is {money}")

    return money