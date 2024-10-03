from operator import truediv
from utilities import anim_print
import time
import random

#Tappelu funktio
def start_fighting(salvia_mode=False):
    player = {
        "name": "Player",
        "health": 100,
        "attacks": {
            "Punch": (10, 20),
            "Kick": (15, 25),
            "Nut cracker": (20, 35)
        }
    }

    enemy = {
        "name": "Enemy",
        "health": 100,
        "attacks": {
            "Bite": (8, 18),
            "Claw": (12, 22),
            "Crotch grab": (18, 30)
        }
    }

    if salvia_mode:
        anim_print("You're in a violent, drug-induced state!\n")
        player["attacks"] = {
            "Frenzied punch": (15, 30),
            "Hallucination kick": (20, 40),
            "Salvia rage": (25, 50)
        }
        enemy["name"] = "Single mother"
        enemy["health"] = 80
    # Hyökkäys
    def attack(attacker, defender, attack_type):
        damage = random.randint(*attacker["attacks"][attack_type])
        defender["health"] -= damage
        print(f"{attacker['name']} uses {attack_type} and deals {damage} damage!")
        print(f"{defender['name']} has {defender['health']} health left.\n")
        time.sleep(1)


    # Liikkeen valinta
    def player_turn():
        print("It's your turn! Choose your attack:")
        for attack in player["attacks"]:
            print(f"- {attack}")

        choice = input("Enter your attack: ").capitalize()
        while choice not in player["attacks"]:
            print("Invalid choice. Please select a valid attack.")
            choice = input("Enter your attack: ").capitalize()

        return choice


    # Vihu valitsee satunnaisen liikkeen
    def enemy_turn():
        choice = random.choice(list(enemy["attacks"].keys()))
        return choice


    # Main game loop
    print("The fight begins!\n")
    while player["health"] > 0 and enemy["health"] > 0:

        player_attack = player_turn()
        attack(player, enemy, player_attack)
        if salvia_mode==True and enemy["health"] <= 0:
            anim_print("You murdered a single mother in cold blood!\n")
        elif enemy["health"] <= 0:
            anim_print("Enemy has been killed!\n")
            break


        print("Enemy's turn...\n")
        time.sleep(1)
        enemy_attack = enemy_turn()
        attack(enemy, player, enemy_attack)
        if player["health"] <= 0:
            anim_print("You have been killed!\n")
            player_death=True
            return player_death

    print("The fight is over!")

cigarette_brands = [
        "MARLBORO RED", "MARLBORO GOLD", "WEST BLUE", "JOHN PLAYER SPECIAL",
        "SALVIA JOINT", "AMERICAN BLACK"]
def smoking_action():
    money = 0
    for brand in cigarette_brands:
     anim_print(brand + "\n")
    cig=input(anim_print("You are at 7eleven, choose your delicacy: \n")).upper()
    if cig==cigarette_brands[3]:
        anim_print("You start enjoying your pack of cigarettes\n")
        time.sleep(2)
        bum=input(anim_print("A random strangers appears and is desperate for a cigarette, do you give her one or not? (Yes or No): \n")).upper()
        if bum=="YES":
            anim_print("She is extremely thankful and offers you a handjob\n")
            handjob=input("Do you accept: \n").upper()
            if handjob=="YES":
                anim_print("You accepted and received a rough treatment in a back alley\n")
                time.sleep(3)
                anim_print("While you're getting treated, a mysterious guy comes up behind you and stabs you\n")
                player_death=True
                return player_death


            elif handjob=="NO":
                anim_print("You denied the strangers offer and continued smoking\n")

        elif bum=="NO":
            anim_print("You denied the cigarette and the stranger\n")

    elif cig==cigarette_brands[0]:
        anim_print("You chose Marlboro Red, a classic choice\n")
        time.sleep(2)
        anim_print("While smoking you start talking to a Japanese businessman\n")
        businessman=input(anim_print("The businessman offers you 1000€. Do you accept: \n")).upper()
        if businessman=="YES":
         money+=1000
         anim_print(f"Your balance now is {money}€\n")
        elif businessman=="NO":
            return

    elif cig==cigarette_brands[1]:
        anim_print("You chose Marlboro Gold\n")
        time.sleep(1)
        anim_print("You start smoking indoors and people around you start getting agitated\n")
        angry_person=input(anim_print("An angry person asks you to stop and threatens to attack you, do you stop smoking (Yes or No): \n")).upper()
        if angry_person=="NO":
            player_death=start_fighting()
            return player_death
        if angry_person=="YES":
            anim_print("You stop smoking and the situation cools down\n")

    elif cig==cigarette_brands[2]:
        anim_print("You chose West Blue, broke choice\n")
        time.sleep(1)
        anim_print("Due to your low money choice a group of guys come up to you and mock you for choosing West Blue.\n")
        time.sleep(1)
        anim_print("They feel so bad for you that they give you money")
        random_money=random.randint(100, 300)
        time.sleep(0.5)
        anim_print(f"You got {random_money}")
        money+=random_money


    elif cig==cigarette_brands[4]:
        anim_print("You chose the Salvia Joint.\n")
        time.sleep(1)
        anim_print("You experience a whole other lifetime in your drug trip\n")
        time.sleep(1)
        anim_print("You wake up and feel extremely violent and confused \n")
        time.sleep(1)
        anim_print("You attack a single mother while still being under the influence \n")
        start_fighting(salvia_mode=True)

    elif cig==cigarette_brands[5]:
        anim_print("You chose American Black, strong choice\n")
        time.sleep(1)
        anim_print("You start smoking \n")

    return money
