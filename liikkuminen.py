import pyautogui as pa
import math
import random
def moving(x,y,moveamount=random.randint(30,60)):
    boolean_value = True
    d = False

    while boolean_value:
        position = pa.position()

        small_amount = 10
        xlength = (position[0] - x) * -1
        ylength = (position[1] - y) * -1
        legitlength = math.sqrt(xlength*xlength + ylength*ylength)
        if (d):
            moveamount=int(moveamount/10) + 1
        for i in range(moveamount):

            pa.moveRel(xlength/moveamount,ylength/moveamount)
            #print(i," siirrolla hiiri on paikassa : ",pa.position())
            d = True
            if(position[0] == x and position[1] == y):
                boolean_value=False
                break

moving(800,600)
print(pa.position())
