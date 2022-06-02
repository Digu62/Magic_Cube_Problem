#python 3.5.2

# COMP 3710
# Robert Spanell
# T00597013
# April, 2018

# This Python module defines the data represention of a Rubik's Cube for use
#    with AstarRubiks.py.

# Contents:
#
# Classes:      Side(Enum)
#
# Functions:    display(cube)
#               displayASCII(cube)
#               cube3Dto1D(cube)
#               rotate(cube, side)
#               scramble(cube, rotations, slist)
#               unscramble(cube, sequence)
#               copy_cube(cube)
#               get_cube()

import random
import math
from enum import Enum

###############################################################################
#
# CUBE is reperesented as a 3D array (six 2D faces), initialized to its
#   unscrambled state. Cubes of each face are indexed by row and column
#   [0, 1 or 2] and are oriented as follows:
#       corner where yellow, white and orange meet are all row[0],column[0]
#       corner where red, blue and green meet are all row[0],column[0]
#       looking directly at face, row[0],column[0] acts as top left
#
# +-----------+                   +-----------+
# |\ y \ y \ y \                 /|0,2|1,2|2,2|
# |o\-----------\               /r|-----------|
# |\|\ y \ y \ y \             /|/|0,1| b |2,1|
# |o|o\-----------\           /r|r|-----------|
# |\|\|\ y \ y \ y \         /|/|/|0,0|1,0|2,0|
# |o|o|o+-----------+       |r|r|r+-----------+
#  \|\|\| w | w | w |       |/|/|/0,0/0,1/0,2/
#   \o|o|-----------|       |r|r/-----------/
#    \|\| w | w | w |       |/|/1,0/ g /1,2/
#     \o|-----------|       |r/-----------/
#      \| w | w | w |       |/2,0/2,1/2,2/
#       +-----------+       +-----------+
#
###############################################################################

# Enum for Rubik's Cube sides oriented with same relation to one another as
#  on a standard die.
# NOTE: when using as a list index values start at 1 not 0 so use the 'index'
#   function.
# Use examples: Side.y.value returns 1, Side.y.index() returns 0
class Side(Enum):
    y = 1   # yellow
    w = 2   # white
    o = 3   # orange
    r = 4   # red
    b = 5   # blue
    g = 6   # green

    def index(self):    # use for indexing into CUBE row, column or face
        return self.value - 1

# NOT CURRENTLY USED IN AstarRubiks.py
# Procedure:    display(cube)
# Inputs:       list
# Returns:      void
# Description:  Displays configuration of cube as a simple printout of the list
def display(cube):
    for x in range(0,6):
        print(Side(x+1).name, 'face')
        for y in range(0,3):
            print(cube[x][y])
        print()

# Procedure:    displayASCII(cube)
# Inputs:       list
# Returns:      void
# Description:  Displays configuration of a cube as pseudo-3D ASCII graphic
def displayASCII(cube):
    y = cube[Side.y.index()]
    w = cube[Side.w.index()]
    o = cube[Side.o.index()]
    r = cube[Side.r.index()]
    b = cube[Side.b.index()]
    g = cube[Side.g.index()]
    print('\n +-----------+                 +-----------+')
    print(' |\\',y[0][2],'\\',y[1][2],'\\',y[2][2],'\\               /|',b[0][2],'|',b[1][2],'|',b[2][2],'|')
    print(' |'+o[2][0]+'\-----------\\             /'+r[2][0]+'|-----------|')
    print(' |\|\\',y[0][1],'\\ Y \\',y[2][1],'\\           /|/|',b[0][1],'| B |',b[2][1],'|')
    print(' |'+o[2][1]+'|'+o[1][0]+'\-----------\\         /'+r[2][1]+'|'+r[1][0]+'|-----------|')
    print(' |\|\|\\',y[0][0],'\\',y[1][0],'\\',y[2][0],'\\       /|/|/|',b[0][0],'|',b[1][0],'|',b[2][0],'|')
    print(' |'+o[2][2]+'|O|'+o[0][0]+'+-----------+     |'+r[2][2]+'|R|'+r[0][0]+'+-----------+')
    print('  \|\|\|',w[0][0],'|',w[0][1],'|',w[0][2],'|     |/|/|/',g[0][0],'/',g[0][1],'/',g[0][2],'/')
    print('   \\'+o[1][2]+'|'+o[0][1]+'|-----------|     |'+r[1][2]+'|'+r[0][1]+'/-----------/')
    print('    \|\|',w[1][0],'| W |',w[1][2],'|     |/|/',g[1][0],'/ G /',g[1][2],'/')
    print('     \\'+o[0][2]+'|-----------|     |'+r[0][2]+'/-----------/')
    print('      \|',w[2][0],'|',w[2][1],'|',w[2][2],'|     |/',g[2][0],'/',g[2][1],'/',g[2][2],'/')
    print('       +-----------+     +-----------+\n')

# Procedure:    rotate(cube, side)
# Inputs:       list, Side(Enum)
# Returns:      cube (by reference)
# Description:  Rotates a side of a cube 90 degrees clock-wise
def rotate(cube, side):
    #print('Rotating', side.name, 'side')
    face = [[0 for x in range(3)] for y in range(3)]
    for x in range(0,3):
        for y in range(0,3):
            face[x][y] = cube[side.index()][abs(y-2)][x]
    cube[side.index()] = face

    # Rotation mappings
    # Variable 'fi' (a.k.a. 'faceindex') represents the indices of the affected faces
    if side.name == 'y':
        fi = [1,3,4,2]
    elif side.name == 'w':
        fi = [2,5,3,0]
    elif side.name == 'o':
        fi = [0,4,5,1]
    elif side.name == 'g':
        fi = [3,1,2,4]
    elif side.name == 'b':
        fi = [5,2,0,3]
    elif side.name == 'r':
        fi = [4,0,1,5]
    else:
        print('error in choosing side')
    
    rotation = [cube[fi[0]][0][0],cube[fi[0]][0][1],cube[fi[0]][0][2],
                cube[fi[1]][2][2],cube[fi[1]][2][1],cube[fi[1]][2][0],
                cube[fi[2]][0][2],cube[fi[2]][1][2],cube[fi[2]][2][2],
                cube[fi[3]][2][0],cube[fi[3]][1][0],cube[fi[3]][0][0]]

    # rotate map by 3 values
    for x in range(3): rotation.append(rotation.pop(0))
    
    # copy values back to cube
    cube[fi[0]][0][0] = rotation[0]
    cube[fi[0]][0][1] = rotation[1]
    cube[fi[0]][0][2] = rotation[2]
    cube[fi[1]][2][2] = rotation[3]
    cube[fi[1]][2][1] = rotation[4]
    cube[fi[1]][2][0] = rotation[5]
    cube[fi[2]][0][2] = rotation[6]
    cube[fi[2]][1][2] = rotation[7]
    cube[fi[2]][2][2] = rotation[8]
    cube[fi[3]][2][0] = rotation[9]
    cube[fi[3]][1][0] = rotation[10]
    cube[fi[3]][0][0] = rotation[11]

# Procedure:    scramble(cube, rotations, slist)
# Inputs:       list, integer, list
# Description:  Returns a scrambled copy of a cube by applying the specified
#               number of clockwise 1/4 rotations to a sequence of randomly
#               selected faces.
def scramble(input_cube, rotations, slist):
    random.seed()
    output_cube = copy_cube(input_cube)
    if len(slist) == 0: print(slist)
    for x in range(0, rotations):
        face = random.randint(1,6)
        for rotation in range(random.randint(1,3)):
            rotate(output_cube, Side(face))
        slist.append([face, rotation+1])
    return output_cube
        
# NOT CURRENTLY USED IN AstarRubiks.py
# Procedure:    unscramble(cube, sequence)
# Inputs:       list, list
# Description:  Returns an unscrambled copy of a cube by applying a specified
#               sequence of clockwise one-quarter rotations in reverse order.
def unscramble(input_cube, sequence):
    sequence.reverse()      # reverse list
    output_cube = copy_cube(input_cube)
    for x in sequence:
        rotate(output_cube, Side(x))
    return output_cube

# Procedure:    copy_cube(cube)
# Inputs:       list
# Returns:      list
# Description:  Returns a deep copy of a cube (doesn't change the original).
def copy_cube(cube):
    return [[[cube[z][y][x] for x in range(3)] for y in range(3)]
                for z in range(6)]

# Procedure:    get_cube()
# Inputs:       user input
# Returns:      list
# Description:  Gets a cube from a user interactively inputted as 6 strings.
def get_cube():
    cube = [[[z.name for x in range(3)] for y in range(3)] for z in Side]
    for x in range(0,6):
        inString = input('Enter 9 characters for '+Side(x+1).name+' face: ')
        for i in range(9):
            cube[x][math.floor(i/3)][i%3] = inString[i]
    return cube

# Procedure:    test_cube()
# Inputs:       none
# Returns:      list
# Description:  Returns a test cube.
def test_cube():
    #input_list = ['wwwryogyo','owwgwrggb','yoryowyor',
    #              'yroyrbyro','bbbgbbgyr','rbbggogww']

    # current mystery scramble
    input_list = ['yyybyboww','bgyrwrwwr','rworoyryg',
                  'wgbgrbggb','orrobyoow','ybbogwgog']

    cube = [[[z.name for x in range(3)] for y in range(3)] for z in Side]
    for x in range(0,6):
        inString = input_list[x]
        for i in range(9):
            cube[x][math.floor(i/3)][i%3] = inString[i]
    return cube
