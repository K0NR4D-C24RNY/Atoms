#!/usr/bin/python3
import random
import numpy
import matplotlib.pyplot as map

directions = ['N','NE','E','SE','S','SW','W','NW']

plansza_y = 10
plansza_x = 10
plansza = numpy.zeros((plansza_x,plansza_y),dtype=int)

class Ludzik:
    #zaczyna na srodku mapy
    def __init__(self,kolor,ksztalt) -> None:
        self.pos_y = int(plansza_y/2)
        self.pos_x = int(plansza_x/2)
        self.color = str(kolor)
        self.marker = str(ksztalt)
        pass

    def ruch(self) -> None:
        dir = numpy.random.choice(directions,p=[0.15,0.1,0.15,0.1,0.15,0.1,0.15,0.1]) #p to rozklad prawd.
        plansza[self.pos_x][self.pos_y] = 0 #skoro schodzi z pola, usufa flage, ze pole jest zajete

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

        if self.pos_y > plansza_y-1:
            self.pos_y = 1
        
        if self.pos_y < 0:
            self.pos_y = plansza_y-2
        
        if self.pos_x > plansza_x-1:
            self.pos_x = 1
        
        if self.pos_x < 0:
            self.pos_x = plansza_x-2

        if plansza[self.pos_x][self.pos_y] == 0:
            plansza[self.pos_x][self.pos_y] = 1 #ustawia flage, ze pole jest zajete
        
            
            print("pozycja y:",str(self.pos_y),"\npozycja x:",self.pos_x,"\nflaga pola:",plansza[self.pos_y][self.pos_x],"\n\n")
            map.plot(self.pos_x,self.pos_y,markerfacecolor=self.color,marker=self.marker)
            return

        print("pozycja y:",str(self.pos_y),"\npozycja x:",self.pos_x,"\nflaga pola:",plansza[self.pos_y][self.pos_x],"\n\n")
        map.plot(self.pos_x,self.pos_y,markerfacecolor=self.color,marker=self.marker)

        


ludzik1 = Ludzik(kolor='pink',ksztalt='x')
ludzik2 = Ludzik(kolor='pink',ksztalt='o')

i = 0
while i < 100:
    print("\nludzik1:\n")
    ludzik1.ruch()
    print("\nludzik2:\n")
    ludzik2.ruch()
    i += 1

map.show()