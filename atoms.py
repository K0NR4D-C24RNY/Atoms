#!/usr/bin/python3
import random
import numpy
import matplotlib.pyplot as map

directions = ['N','NE','E','SE','S','SW','W','NW']

plansza_y = 100
plansza_x = 100
plansza = numpy.zeros((plansza_x,plansza_y),dtype = int)    #inicjalizacja pol zerami dwuwymiarowej planszy plansza_x X plansza_y
prawd = [0.15,0.1,0.15,0.1,0.15,0.1,0.15,0.1]
dir1 = numpy.random.choice(directions,p = prawd)
dir2 = numpy.random.choice(directions,p = prawd)
neonBlue = '#099FFF'
neonPink = '#FF00CC'
neonGreen = '#00FF66'
hydrogenColor = str(neonBlue)
neonColor = str(neonPink)
togetherColor = str(neonGreen)


class Atom:

    def __init__(self) -> None:        
        self.pos_y = int(plansza_y/2)     #spawnuje sie ma srodku mapy
        self.pos_x = int(plansza_x/2)     #spawnuje sie na srodku mapy
        self.posHistory = [[self.pos_x,self.pos_y]]
        self.posHistory.append([(self.pos_x),(self.pos_y)])
    
    def moveToDirection(self,dir) -> None:
        if dir == 'N':
            self.pos_y += 1
            self.pos_x += 0
        
        elif dir == 'NE':
            self.pos_y += 1
            self.pos_x += 1

        elif dir == 'E':
            self.pos_y += 0
            self.pos_x += 1
        
        elif dir == 'SE':
            self.pos_y += -1
            self.pos_x += 1
        
        elif dir == 'S':
            self.pos_y += -1
            self.pos_x += 0
        
        elif dir == 'SW':
            self.pos_y += -1
            self.pos_x += -1
        
        elif dir == 'W':
            self.pos_y += 0
            self.pos_x += -1
        
        elif dir == 'NW':
            self.pos_y += 1
            self.pos_x += -1

    def moveOnBoard(self,dir) -> None:
        plansza[self.pos_x][self.pos_y] = 0     #skoro schodzi z pola, usuwa flage, ze pole jest zajete
        self.moveToDirection(dir)

        if self.pos_y > plansza_y-1:
            self.pos_y = 1
        
        if self.pos_y < 0:
            self.pos_y = plansza_y-2
        
        if self.pos_x > plansza_x-1:
            self.pos_x = 1
        
        if self.pos_x < 0:
            self.pos_x = plansza_x-2

        if plansza[self.pos_x][self.pos_y] == 0:
            plansza[self.pos_x][self.pos_y] = 1     #ustawia flage, ze pole jest zajete
        
        elif plansza[self.pos_x][self.pos_y] == 1:    #jezeli flaga juz jest ustawiona, to oznacza, ze byl ktos inny
            plansza[self.pos_x][self.pos_y] = 2     #ustawia flage awaryjna, ktora informuje o incydencie (xD)

        # print("pos x:",str(self.pos_x),"\npozycja y:",self.pos_y,"\nflaga pola:",plansza[self.pos_x][self.pos_y],"\n\n") #do logow
        self.posHistory.append([(self.pos_x),(self.pos_y)])

        
hydrogen = Atom()
neon = Atom()
hydrogen.moveOnBoard(dir1)
neon.moveOnBoard(dir2)
#jest to po to, aby ominac bug zwiazany z tym, ze punkt startowy jest zawsze ten sam

contiguousAtoms = []
i = 0
while i < 512:
    dir1 = numpy.random.choice(directions,p = prawd)
    dir2 = numpy.random.choice(directions,p = prawd)

    # if hydrogen.posHistory[i-1] == neon.posHistory[i-1]:
    if plansza[hydrogen.pos_x][hydrogen.pos_y] == 2:
        dir1 = dir2
        # print("\nhydrogen:\n")   #do logow
        hydrogen.moveOnBoard(dir1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
        # print("\nneon:\n")   #do logow
        neon.moveOnBoard(dir2)
        contiguousAtoms.append(neon.posHistory.pop())

    # print("\nhydrogen:\n")   #do logow
    hydrogen.moveOnBoard(dir1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    # print("\nneon:\n")   #do logow
    neon.moveOnBoard(dir2)
    
    i += 1

map.plot(*zip(*hydrogen.posHistory),marker = '*', color = hydrogenColor)
map.plot(*zip(*neon.posHistory),marker = 'o',color = neonColor)
if array.__len__ != 0:
    map.plot(*zip(*contiguousAtoms), marker = 'x', color = togetherColor)

map.show()