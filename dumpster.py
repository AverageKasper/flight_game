from utilities import anim_print
import random as r

# Function for dumpster diving at small airports, returns gained currencies
def dumpster_dive():
    money = 0
    cp = 0
    phallic_object = 0
    
    find =  r.randint(1,100)
    if find < 40:
        trash_money = r.randint(50, 150)
        anim_print(f"\nYou found a portable dvd player from the trash, you got {trash_money}€ for it at the pawn shop!")
        money += trash_money
    elif find >= 40 and find <=60:
        trash_money = r.randint(200, 400)
        anim_print(f"\nYou found a pair of earbuds from the trash, you got {trash_money} for it at the pawn shop!")
    elif find > 60 and find <= 80:
        trash_money = r.randint(500, 700)
        anim_print(f"\nYou found an IPhone XS in the trash, you got {trash_money}€ for it at the pawn shop!")
        money += trash_money
    elif find > 80 and find <=95:
        anim_print(f"\nYou found a voucher for CP from the trash! You got 500 CP")
        cp += 500
    elif find>95 and find <= 100:
        anim_print(f"\nYou found 1 phallic object from the trash! It smells wierd.")
        phallic_object += 1
    return money, cp, phallic_object