#!/usr/bin/python3

import random
from random import randrange

class Guy:
    posX = 0 #X position of our guy. 
    posY = 0 #Y position of our guy.
    # controller = Controller() #controller of our guy, it tells where to go

    # def __init__(self):
    #     self.posX = 0
    #     self.posY = 0

#class Board:
    

class Controller:
    
    def __init__(self,targ1,targ2):
        self.target1 = targ1
        self.target2 = targ2
    
    def up(target):
        target.posX += 0
        target.posY += 1

    def down(target):
        target.posX += 0
        target.posY += -1

    def left(target):
        target.posX += 1
        target.posY += 0

    def right(target):
        target.posX += -1
        target.posY += 0

    def movement(self):
        #randomize a number from 0 to 3, where: 0=N 1=S 2=E 3=W
        dir = random.randrange(4)
        target = self.target1

        if dir == 0:
            self.up(target)
            return
        
        if dir == 1:
            self.down(target)
            return
        
        if dir == 2:
            self.left(target)
            return
        
        if dir == 3:
            self.right(target)
            return

        

gostek1 = Guy()
gostek2 = Guy()

test = Controller(gostek1,gostek2)
test.movement()
