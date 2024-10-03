from utilities import anim_print
import random as r
# Function for dumpster diving at small airports, returns gained currencies
def dumpster_dive():
    money = 0
    cp = 0
    phallic_object = 0
    #r.randint(1,10)
    find = 10 
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
        trash_money = r.randint(300, 500)
        anim_print(f"\nHUGE!! You found {trash_money} € from the trash!")
        money += trash_money
    elif find == 10:
        anim_print(f"\nYou found a voucher for CP from the trash! You got 200 CP")
        cp += 500
        anim_print(f"\nYou found 1 phallic object from the trash!")
        phallic_object += 1
    return money, cp, phallic_object