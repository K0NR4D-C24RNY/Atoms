#!/usr/bin/python3
import numpy
import matplotlib.pyplot as map

directions = ['N','NE','E','SE','S','SW','W','NW']
board_y = 60
board_x = 60
board = numpy.zeros((board_x,board_y),dtype = int)    #inicjalizacja pol zerami dwuwymiarowej planszy board_x X board_y
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
        self.pos_y = numpy.random.randint(board_y/2 - 3,board_y/2 + 3)     #spawnuje sie w losowym miejscu środek +- 3
        self.pos_x = numpy.random.randint(board_x/2 - 3,board_x/2 + 3)     #spawnuje sie w losowym miejscu środek +- 3
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
        board[self.pos_x][self.pos_y] = 0     #skoro schodzi z pola, usuwa flage, ze pole jest zajete
        self.moveToDirection(dir)
        
        ########################################################################################################################
        # tutaj sprawdzamy tzw. corner case'y, czyli przypadki szczególne.
        # W naszej sytuacji są to przypadki, gdy atom wyjdzie poza granice mapy
        # rozwiązaniem jest przetransportowanie go na drugi koniec (przesuwam o 1 jednostkęm aby uniknąć sytuacji na krawędzi)
        #######################################################################################################################
        if self.pos_y >= board_y:
            self.pos_y = board_y - 1
        
        if self.pos_y <= 0:
            self.pos_y = 1
        
        if self.pos_x >= board_x:
            self.pos_x = board_x - 1
        
        if self.pos_x <= 0:
            self.pos_x = 1

        if board[self.pos_x][self.pos_y] == 0:
            board[self.pos_x][self.pos_y] = 1     #ustawia flage, ze pole jest zajete
        
        elif board[self.pos_x][self.pos_y] == 1:    #jezeli flaga juz jest ustawiona, to oznacza, ze byl ktos inny
            board[self.pos_x][self.pos_y] = 2     #ustawia flage awaryjna, ktora informuje o incydencie (xD)

        # print("pos x:",str(self.pos_x),"\npozycja y:",self.pos_y,"\nflaga pola:",board[self.pos_x][self.pos_y],"\n\n") #do logow
        self.posHistory.append([(self.pos_x),(self.pos_y)])

        
hydrogen = Atom()
neon = Atom()
contiguousAtoms = [] #tablica przechowujaca pozycje, gdy atomy sa na tej samej pozycji
#inp = input("q - exit, else - start simulation: ")

map.ion()

while True:
    map.clf()
    hydrogen.posHistory.clear()
    neon.posHistory.clear()
    contiguousAtoms.clear()
    
    i = 0
    while i < 512:
        dir1 = numpy.random.choice(directions,p = prawd)
        dir2 = numpy.random.choice(directions,p = prawd)

        if board[hydrogen.pos_x][hydrogen.pos_y] == 2:
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
    if contiguousAtoms.__len__ != 0:
        map.plot(*zip(*contiguousAtoms), marker = 'x', color = togetherColor)

    
    inp = input("q - exit, enter - start simulation: ")
    if inp == 'q':
        break