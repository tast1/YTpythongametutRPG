# YTPythontut
# Sondre Nordtun

import cmd
import textwrap
import sys
import os
import time
import random

screen_with = 100

#####-Player Setup-#####

class player:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        slef.location = 'start'
myPlayer = player()

#####-Title Screen-#####
def Title_Screen_Selections():
    option = input("> ")
    if option.lower() == ("play"):
        Start_Game() #Place holder until Start_Game function is made
    elif option.lower() == ("help"):
        help_menu() # Place holder untull help_menu is made
    elif option().lower == ("quit"): #Quits the game, uses sys functions
        sys.exit()
    while option.lower() not in ['play',  'help',  'quit']:
        print("Please enter a valid command")
        option = input("> ")
        if option.lower() == ("play"):
            Start_Game() #Place holder until Start_Game function is made
        elif option.lower() == ("help"):
            help_menu() # Place holder untull help_menu is made
        elif option.lower() == ("quit"):
            sys.exit()

def Title_screen():
    os.system('clear')
    print('######################################')
    print('#### Welcome to my text based RPG ####')
    print('              -Play-                  ')
    print('              -Help-                  ')
    print('              -Quit-                  ')
    print('       -made by sondre 2018-          ')
    Title_Screen_Selections()

def help_menu():
    print('######################################')
    print('####  -This is the help menu-     ####')
    print('-Use up, down, left, right to move    ')
    print('-Type commands to use them            ')
    print('-Use "look" to inspect something      ')
    print('-Good luck have fun                   ')
    Title_Screen_Selections()


##### GAME FUNCTIONALITY #####
def start_game():




############# -MAP- ############

#################################
# a1 a2 .. player starts at b2  #
#-------------                  #
#|  |  |  |  | 1,2,3,4          #
#-------------                  #
#|  |  |  |  | 1,2,3,4          #
#-------------                  #
#|  |  |  |  | 1,2,3,4          #
#-------------                  #
#|  |  |  |  | 1,2,3,4          #
#-------------                  #
#################################

    ZONENAME = ''
    DESCRIPTION = 'description'
    EXAMINTAION = 'examine'
    SOLVED = False
    UP = 'up', 'north'
    DOWN = 'down', 'south'
    LEFT = 'left', 'west'
    RIGHT = 'right','east'

    ### IN PYTHON { } is seen as dictonary ####The main operations on a dictionary are storing a value with some key and extracting the value given the key. It is also possible to delete a key:value pair with del. If you store using a key that is already in use, the old value associated with that key is forgotten. It is an error to extract a value using a non-existent key.####

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                 'b1': False, 'b2': False, 'b3': False, 'b4': False,
                 'c1': False, 'c2': False, 'c3': False, 'c4': False,
                 'd1': False, 'd2': False, 'd3': False, 'd4': False,}

####-Map navigation has to be filled in manually, each zonemap a1 etc has neighbouring tiles, that needs to be connected to it. Depending on the current#
##### Tiles locations. Example.. b2 have a2 up, b1 to left, b3 to right and c2 down. If we are on a tile that dont have a neighbour on a side. ###
### The direction that dont have a tile is left with '' Example a1 dont have anything to the left or up, so we sat left = ''

ZoneMap = {
    'a1': {
        ZONENAME: ''
        DESCRIPTION = 'description'
        EXAMINTAION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right','east'
    },
    'a2': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMINTAION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right','east'
    },
    'a3': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMINTAION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right','east'
    },
    'a4': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMINTAION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right','east'
    },
    'b1': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMINTAION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right','east'
    },
    'b2': {
        ZONENAME = 'Home'
        DESCRIPTION = 'This is your home.'
        EXAMINTAION = 'It apperas to be just like you left it.'
        SOLVED = False
        UP = 'a2',
        DOWN = 'c2'.
        LEFT = 'b1',
        RIGHT = 'b3',
    },

    'b3': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMINTAION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right','east'
    },
    'b4': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMINTAION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right','east'
    },
    'c1': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMINTAION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right','east'
    },
    'c2': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMINTAION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right','east'
    },
    'c3': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMINTAION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right','east'
    },
    'c4': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMINTAION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right','east'
    },
    'd1': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMINTAION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right','east'
    },
    'd2': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMINTAION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right','east'
    },
    'd3': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMINTAION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right','east'
    },
    'd4': {
        ZONENAME = ''
        DESCRIPTION = 'description'
        EXAMINTAION = 'examine'
        SOLVED = False
        UP = 'up', 'north'
        DOWN = 'down', 'south'
        LEFT = 'left', 'west'
        RIGHT = 'right','east'
    },
}

#### -GAMEINTEGRETY- ####

def print_location():
    print('\n' + ('#' * (4 + len(myPlayer.location))))

Title_screen()
