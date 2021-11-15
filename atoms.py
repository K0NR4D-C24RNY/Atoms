#!/usr/bin/python3
import numpy
import matplotlib.pyplot as map

directions = ['N','NE','E','SE','S','SW','W','NW']      # list of possible directions
board_y = 35        # board hight
board_x = 35        # board width
board = numpy.zeros((board_x,board_y),dtype = int)  # initialize board as 2d array filled 0 - a flag which mean a field is free
prawd = [0.15,0.1,0.15,0.1,0.15,0.1,0.15,0.1]       # probability distribution
dir1 = numpy.random.choice(directions,p = prawd)    # direction to move first atom. It's randomly generated direction from directions list
dir2 = numpy.random.choice(directions,p = prawd)    # direction to move second atom. It's randomly generated direction from directions list
neonBlue = '#099FFF'    # color used in plot
neonPink = '#FF00CC'    # color used in plot
neonGreen = '#00FF66'   # color used in plot
hydrogenColor = str(neonBlue)   # define which color is dedicated to hydrogen on plot
neonColor = str(neonPink)       # define which color is dedicated to neon on plot
togetherColor = str(neonGreen)  # define which color is dedicated to situation, when atoms is contiguous

class Atom:
    
    def __init__(self) -> None:        
        self.pos_y = numpy.random.randint(board_y/2 - 3,board_y/2 + 3)     # atom is spawned randomly in area board center +- 3 fields in hight
        self.pos_x = numpy.random.randint(board_x/2 - 3,board_x/2 + 3)     # atom is spawned randomly in area board center +- 3 fields in width
        self.posHistory = [[self.pos_x,self.pos_y]]                        # list to store all atom positions history. Stored by pair of x and y coordinates
        self.posHistory.append([(self.pos_x),(self.pos_y)])                # add start position to history
    
    def moveToDirection(self,dir) -> None:      # function to store instructions to move atom
        if dir == 'N':      # move up
            self.pos_y += 1
            self.pos_x += 0
        
        elif dir == 'NE':   # move up-right
            self.pos_y += 1
            self.pos_x += 1

        elif dir == 'E':    # move right
            self.pos_y += 0
            self.pos_x += 1
        
        elif dir == 'SE':   # move down-right
            self.pos_y += -1
            self.pos_x += 1
        
        elif dir == 'S':    # move down
            self.pos_y += -1
            self.pos_x += 0
        
        elif dir == 'SW':   # move down-left
            self.pos_y += -1
            self.pos_x += -1
        
        elif dir == 'W':    # move left
            self.pos_y += 0
            self.pos_x += -1
        
        elif dir == 'NW':   # move up-left
            self.pos_y += 1
            self.pos_x += -1

    def moveOnBoard(self,dir) -> None:      # function to store all necessary steps to move atom
        board[self.pos_x][self.pos_y] = 0   # first delete a flag that field is occupied
        self.moveToDirection(dir)           # move our atom in inputed direction
        
        ########################################################################################################################
        # Here we looking at corner cases
        # When Atom cross borders or even occupie a border field, move atom 1 field away
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
            board[self.pos_x][self.pos_y] = 1       # set a flag, which mean a field is occupied
        
        elif board[self.pos_x][self.pos_y] == 1:    # if field is occupied, it means that our atoms meet
            board[self.pos_x][self.pos_y] = 2       # set alarm flag

        self.posHistory.append([(self.pos_x),(self.pos_y)])     # add newest position to history

        
hydrogen = Atom()
neon = Atom() 
contiguousAtoms = [] # it's for different coloring plot in contiguous case

map.ion()       # matplotlib plot is saved as map object. Ion() function is to clear plot ... ( in a nutshell)

while input("q - exit, enter - start simulation: ") != 'q':  # when user hit q key, program will exit
    map.clf()                       # clear old plot
    hydrogen.posHistory.clear()     # clear previous history
    neon.posHistory.clear()         # clear previous history
    contiguousAtoms.clear()         # clear previous history
    
    i = 0
    while i < 512:
        dir1 = numpy.random.choice(directions,p = prawd)        # randomly generated direction to move hydrogen
        dir2 = numpy.random.choice(directions,p = prawd)        # randomly generated direction to move neon

        if board[hydrogen.pos_x][hydrogen.pos_y] == 2:          # If atoms met they will go in the same dir
            hydrogen.moveOnBoard(dir1)
            neon.moveOnBoard(dir1)
            contiguousAtoms.append(neon.posHistory.pop())      #save position of atoms in special list and remove from neon history
            hydrogen.posHistory.pop()                          #remove last object from history  

        else:
            hydrogen.moveOnBoard(dir1)
            neon.moveOnBoard(dir2)
        
        i += 1

    # zip function separate x position and y position to different lists ... (in a nutshell)
    map.plot(*zip(*hydrogen.posHistory),marker = '*', color = hydrogenColor)    # plot hydrogen position history
    map.plot(*zip(*neon.posHistory),marker = 'o',color = neonColor)             # plot neon position history
    if contiguousAtoms.__len__ != 0:                                            # if there were contiguous case
        map.plot(*zip(*contiguousAtoms), marker = 'x', color = togetherColor)   # plot contiguous history
    
    map.show()
