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
    os.system('cls' if os.name == 'nt' else 'clear')

#Horse racing
def horse_race(money):
    horses = ["Diddy", "Kolovastaava", "Sakke", "Rinne", "Vuoristo"]
    odds = {horse: r.uniform(1.5, 5.0) for horse in horses}  # Generate random odds for each horse

    # Show available horses and odds
    anim_print("Welcome to the Horse Racing track!\n")
    anim_print("Here are the competing horses and their odds:\n")
    for horse in horses:
        anim_print(f"{horse} (Odds: {odds[horse]:.2f})\n")

    # Player places a bet
    while True:
        bet_horse = input(f"Which horse do you want to bet on? ({', '.join(horses)}): ").capitalize()
        if bet_horse not in horses:
            anim_print("Invalid horse. Please choose from the list.\n")
            continue
        break

    bet_amount = int(input("How much do you want to bet? "))
    if bet_amount > money:
        anim_print("Broke ass!\n")
        return money

    anim_print(f"You placed {bet_amount} euros on {bet_horse}.\n")

    # Simulate the race with randomized speeds for each horse
    horse_speeds = {horse: r.randint(10, 20) for horse in horses}  # Random speeds between 10-20
    race_results = sorted(horse_speeds.items(), key=lambda x: x[1], reverse=True)

    # Announce race start
    anim_print("The race is starting!\n")
    time.sleep(2)
    for horse, speed in race_results:
        anim_print(f"{horse} finishes with a speed of {speed} km/h!\n")
        time.sleep(1)

    # Determine the winner
    winner = race_results[0][0]
    anim_print(f"\nThe winner is {winner}!\n")

    # Determine if the player won or lost
    if bet_horse == winner:
        winnings = bet_amount * odds[bet_horse]
        anim_print(f"Congratulations! You won {winnings:.0f} euros!\n")
        money += winnings
    else:
        anim_print(f"You lost {bet_amount} euros bozo.\n")
        money -= bet_amount

    anim_print(f"Your total balance is now {money} euros.\n")
    return money



# Blackjack game
def blackjack(money):
    def deal_card():
        """Deals a random card from the deck."""
        cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
        return r.choice(cards)

    def calculate_hand_value(hand):
        """Calculates the value of a hand of cards."""
        card_values = {
            '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
            'J': 10, 'Q': 10, 'K': 10, 'A': 11
        }
        value = 0
        ace_count = 0
        for card in hand:
            value += card_values[card]
            if card == 'A':
                ace_count += 1
        while value > 21 and ace_count:
            value -= 10  # Adjust Ace from 11 to 1
            ace_count -= 1
        return value

    def display_hand(player, hand, hide_dealer_card=False):
        """Displays the player's or dealer's hand. Optionally hides the dealer's second card."""
        if hide_dealer_card:
            hand_display = [hand[0], "Hidden"]
            anim_print(f"{player}'s hand: {', '.join(hand_display)}\n")
        else:
            anim_print(f"{player}'s hand: {', '.join(hand)} (Value: {calculate_hand_value(hand)})\n")

    print("Welcome to Blackjack!")

    bet = int(input("How much do you want to bet: "))
    if bet > money:
        anim_print("You don't have enough money!\n")
        return money

    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    display_hand("Dealer", dealer_hand, hide_dealer_card=True)  # Show the dealer's first card, hide the second
    display_hand("Player", player_hand)

    # Player's turn
    while calculate_hand_value(player_hand) < 21:
        choice = input("Do you want to 'hit' or 'stand'? ").lower()
        if choice == 'hit':
            player_hand.append(deal_card())
            display_hand("Player", player_hand)
            if calculate_hand_value(player_hand) > 21:
                anim_print("Player busted! You lose!\n")
                money -= bet
                anim_print(f"Your total balance is {money}\n")
                return money
        elif choice == 'stand':
            break

    # Dealer's turn
    display_hand("Dealer", dealer_hand)  # Now reveal the dealer's full hand
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card())
        display_hand("Dealer", dealer_hand)

    # Determine winner
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    if dealer_value > 21 or player_value > dealer_value:
        anim_print(f"Player wins! You won {bet} euros!\n")
        money += bet
    elif dealer_value > player_value:
        anim_print(f"Dealer wins! You lost {bet} euros!\n")
        money -= bet
    else:
        anim_print("It's a tie!\n")

    anim_print(f"Your total balance is {money} euros\n")
    return money



# Casino function with Blackjack
def casino(money):
    game_select = ""

    gameoptions = ["SNAKE EYES", "HILO", "DICE", "BLACKJACK", "HORSE RACING", "RETURN"]

    while game_select != gameoptions[5]:
        game_select = input("Choose a game to play (dice, hilo, snake eyes, blackjack, horse racing) or go back (return): ").upper()
        if game_select not in gameoptions:
            anim_print("Invalid selection\n")
            continue

        if game_select != gameoptions[5]:
            if game_select == gameoptions[2]:  # Dice game
                bet = int(input("How much do you want to bet: "))
                if bet > money:
                    anim_print("Broke ass\n")
                    continue
                dealer_dice1, dealer_dice2 = r.randint(1, 6), r.randint(1, 6)
                player_dice1, player_dice2 = r.randint(1, 6), r.randint(1, 6)
                dealer_total = dealer_dice1 + dealer_dice2
                player_total = player_dice1 + player_dice2
                anim_print(f"Dealer rolled: {dealer_dice1}, {dealer_dice2} (Total: {dealer_total})\n")
                anim_print(f"You rolled: {player_dice1}, {player_dice2} (Total: {player_total})\n")
                if dealer_total > player_total:
                    anim_print(f"You lost {bet} euros\n")
                    money -= bet
                elif dealer_total < player_total:
                    anim_print(f"You won {bet} euros\n")
                    money += bet
                else:
                    anim_print("It's a tie!\n")
                anim_print(f"Your total balance is {money} euros\n")
            elif game_select == gameoptions[1]:  # Hi-Lo
                bet = int(input("How much do you want to bet: "))
                if bet > money:
                    anim_print("You don't have enough money\n")
                    continue
                first_card = r.randint(1, 13)
                anim_print(f"First card: {first_card}\n")
                guess = input("Will the next card be higher or lower (HI/LO)? ").upper()
                second_card = r.randint(1, 13)
                anim_print(f"Second card: {second_card}\n")
                if (guess == 'HI' and second_card > first_card) or (guess == 'LO' and second_card < first_card):
                    anim_print(f"You won {bet} euros\n")
                    money += bet
                else:
                    anim_print(f"You lost {bet} euros\n")
                    money -= bet
                anim_print(f"Your total balance is {money} euros\n")
            elif game_select == gameoptions[0]:  # Snake Eyes
                bet = int(input("How much do you want to bet: "))
                if bet > money:
                    anim_print("You don't have enough money\n")
                    continue
                dice_1, dice_2 = r.randint(1, 6), r.randint(1, 6)
                anim_print(f"You rolled: {dice_1} and {dice_2}\n")
                if dice_1 == dice_2 == 1:
                    anim_print(f"BIG WIN BOZO! You won {bet * 10} euros!\n")
                    money += bet * 10
                elif dice_1 == dice_2:
                    anim_print(f"Small win bozo! You won {bet} euros!\n")
                    money += bet
                else:
                    anim_print(f"You lost {bet} euros bozo\n")
                    money -= bet
                anim_print(f"Your total balance is {money} euros\n")
            elif game_select == gameoptions[3]:  # Blackjack
                money = blackjack(money)

            elif game_select==gameoptions[4]:
                money=horse_race(money)

    return money

#monke
