import math 
from random import Random, randint, random, randrange, uniform

from time import time,sleep
class Ruleta():
    gravity = 9.8
    def Premios(numero:float,times):
        Ruleta.result += 1
        while Ruleta.result <= times:
            if numero < 0.5:
                Ruleta.cl += 1
                break     
            elif numero < 5.5 and numero > 0.5:
                Ruleta.ce += 1
                break
            elif numero < 30.5 and numero > 5.5:
                Ruleta.cr += 1
                break
            elif numero < 99.99 and numero > 30.5:
                Ruleta.cc += 1
                break
        if Ruleta.result == times:
            print(f"You have gotten {Ruleta.cc} comunes")
            print(f"You have gotten {Ruleta.cr} raras")
            print(f"You have gotten {Ruleta.ce} epicas")
            print(f"You have gotten {Ruleta.cl} !!legendarios!!")
            if input("Quieres jugar de nuevo???\n") is not "no":
                Ruleta.ruleta_epica(10)

    def __init__(self):
        pass
    
    def inicio():
        print("How many times you wanna play?")
        times = int(input())
        Ruleta.ruleta_epica(times)

    def truncate(number: float, max_decimals: int):
        int_part, dec_part = str(number).split(".")
        return float(".".join((int_part, dec_part[:max_decimals])))
    
    def ruleta_epica(times):
        Ruleta.cc,Ruleta.cr,Ruleta.ce,Ruleta.cl = 0,0,0,0
        Ruleta.result = 0
        for i in range(times):
            a = (uniform(0,99.99))
            a = Ruleta.truncate(a,2)
            sleep(0.1)
            Ruleta.Premios(a,times)

        



Goku_MUI_Banner = Ruleta()
Ruleta.inicio()
