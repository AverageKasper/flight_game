from utilities import anim_print
from utilities import clear_window
from utilities import int_check
import random as r

def pickpocket():
    steal_list = {"Homeless man" : 1,
                  "Monke" : 1,
                  


                  "Airport security" : 4,
                  "Store clerk" : 3,
                  
                  



                  "Sausage man" : 5,
                  "Juha" : 5,
                  }
    name,difficulty = r.choice(list(steal_list.items()))
    print(name,difficulty)

pickpocket()
print("★")