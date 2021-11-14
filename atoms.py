#!/usr/bin/python3
import random
import numpy
import matplotlib.pyplot as map

directions = ['N','NE','E','SE','S','SW','W','NW']

plansza_y = 10
plansza_x = 10
plansza = numpy.zeros((plansza_x,plansza_y),dtype = int)    #inicjalizacja pol zerami dwuwymiarowej planszy plansza_x X plansza_y

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

        #print("pozycja y:",str(self.pos_y),"\npozycja x:",self.pos_x,"\nflaga pola:",plansza[self.pos_y][self.pos_x],"\n\n") #do logow
        self.posHistory.append([(self.pos_x),(self.pos_y)])

        
hydrogen = Atom()
neon = Atom()
prawd = [0.15,0.1,0.15,0.1,0.15,0.1,0.15,0.1]
dir1 = numpy.random.choice(directions,p = prawd)
dir2 = numpy.random.choice(directions,p = prawd)
i = 0

hydrogen.moveOnBoard(dir1)
neon.moveOnBoard(dir2)
#jest to po to, aby ominac bug zwiazany z tym, ze punkt startowy jest zawsze ten sam

while i < 100:
    dir1 = numpy.random.choice(directions,p = prawd)
    dir2 = numpy.random.choice(directions,p = prawd)

    if plansza[hydrogen.pos_x][hydrogen.pos_y] == 2:
        dir1 = dir2

    #print("\nhydrogen:\n")   #do logow
    hydrogen.moveOnBoard(dir1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    #print("\nneon:\n")   #do logow
    neon.moveOnBoard(dir2)
    i += 1

neonBlue = '#099FFF'
neonYellow = '#FF00CC'
neonGreen = '#00FF66'
hydrogenColor = str(neonBlue)
neonColor = str(neonYellow)
togetherColor = str(neonGreen)

#########################################################################
#Short version without different color in together case
# map.plot(hydrogen.history_x,hydrogen.history_y,color = hydrogenColor)
# map.plot(neon.history_x,neon.history_y, color = neonColor)
#########################################################################

map.ion()
fig = map.figure()
i = 0

for idx,hydroPosHist in enumerate(hydrogen.posHistory):
    neonPosHist = neon.posHistory[idx]
    
    if hydroPosHist == neonPosHist:
        map.plot(hydroPosHist,marker = 'x',color = togetherColor,markeredgecolor = "red")
        map.plot(neonPosHist,marker = 'x', color = togetherColor,markeredgecolor = "red")

    else:
        map.plot(hydroPosHist,marker = '*',color = hydrogenColor,markeredgecolor = "black")
        map.plot(neonPosHist,marker = 'o', color = neonColor, markeredgecolor = "black")


map.show()