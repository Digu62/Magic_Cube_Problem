#python 3.5.2

# COMP 3710
# Robert Spanell
# T00597013
# April, 2018

# This Python program finds a solution to the Rubik's Cube using the
#   A* algorithm.

# Contents:
#
# Functions:    hCalc(cube)
#               getBestNode(expandedQ)
#               inQ(cube,Q)
#               extractPath(visitedQ)

# Due to the nature of the algorithm and the problem space, any solution path
#   more than 8 rotations away takes an excessive amount of time to complete.
#   1 to 6 is almost instantaneous, 7 to 8 can be anywhere from a minute to
#   several hours, and 9 can take hours to days. Anything 10 or over has not
#   yet been tested for long enough to finish, so is unknown.
#
#   Some improvement may be possible by changing the heuristic, something I am
#   working on, but it looks like it will require considerable re-writing of the
#   existing code.
#
################################################################################
#
#   I have used a non-standard representation of a cube. Most Rubik's Cube
#   "experts" use the notation of U for top, D for bottom, L for left, R for
#   right, B for back and F for front. I thought this would be both difficult
#   to implement and unnecessary, so I invented my own representation. I have
#   no idea if this method of implementation has been used by others.
#
#   A cube is represented as a 3D array (six 2D faces). When instantiated, it
#   is initialized to its unscrambled state. Cubes of each face are indexed by
#   row and column [0, 1 or 2] and are oriented as follows:
#       -corner where yellow, white and orange meet are all row[0],column[0]
#       -corner where red, blue and green meet are all row[0],column[0]
#       -looking directly at any face (row[0],column[0]) is the top left square
#
#   +-----------+                   +-----------+
#   |\ y \ y \ y \                 /|0,2|1,2|2,2|
#   |o\-----------\               /r|-----------|
#   |\|\ y \ Y \ y \             /|/|0,1| B |2,1|
#   |o|o\-----------\           /r|r|-----------|
#   |\|\|\ y \ y \ y \         /|/|/|0,0|1,0|2,0|
#   |o|O|o+-----------+       |r|R|r+-----------+
#    \|\|\| w | w | w |       |/|/|/0,0/0,1/0,2/
#     \o|o|-----------|       |r|r/-----------/
#      \|\| w | W | w |       |/|/1,0/ G /1,2/
#       \o|-----------|       |r/-----------/
#        \| w | w | w |       |/2,0/2,1/2,2/
#         +-----------+       +-----------+
#
################################################################################
#
# A* parameters:
#
#   gValue is the cost of the path to the current cube from the STARTCUBE.
#       It is the number of rotations multiplied by GMULTIPLIER to approximate
#       the cost of a rotation.
#   hValue is a heuristic equal to the total number of incorrect squares on all
#       faces. It is an underestimate of how far away the current cube is from
#       the GOALCUBE. 
#   fValue is a path-based evaluation function:
#       fValue = gValue + hValue
#
#   A* algorithm expands paths from nodes that have the lowest fValue until
#   the algorithm visits the goal node.
#
################################################################################

import math
import Rcube    # my custom Rubik's Cube module
from datetime import datetime

# GLOBAL CONSTANTS

# SCRAMBLES is an integer representing how many times a random side will be
#   rotated a quarter turn.
#   ***USER INPUT***

# create goal cube
GOALCUBE = [[[z.name for x in range(3)] for y in range(3)] for z in Rcube.Side]

# GMULTIPLIER estimates ratio between # of rotations and # of changed squares.
#   In theory it is a ratio but in application it is just the gValue since it is
#       always multiplied by only 1 rotation. It is related to the heuristic but
#       is applied to the gValue. Best guess is it's somewhere between 8 and 20.
GMULTIPLIER = 8     # Let's set to 8. Testing seems to indicate it's best

scramble_list = []  # scramble_list is a list to keep a record of the random
                    #   scramble for later comparison to the solution the
                    #   algorithm finds.
expandedQ = []      # aka openSet - list of discovered nodes
                    #   stored as [cube, gValue, hValue, previous rotation]
visitedQ = []       # aka closedSet - list of visited nodes
                    #   stored as [cube, gValue, hValue, previous rotation]

# Procedure:    hCalc(cube)
# Inputs:       cube list
# Returns:      integer
# Description:  Sums the total number of incorrect squares on all faces.
#               Used as the heuristic.
def hCalc(cube):
    incorrect = 0
    for z in range(6):
        for y in range(3):
            for x in range(3):
                if cube[z][y][x] != Rcube.Side(z+1).name:
                    incorrect += 1
    return incorrect

# Procedure:    hCalc2(cube)
# Inputs:       cube list
# Returns:      integer
# Description:  Experimental heuristic. NOT FINISHED, JUST A STUB COPY OF hCalc
#               Sums the total number of rotations required to bring each square
#               on a face to its proper location (independent of what happens to
#               the other squares). An examination of a cube will show that any
#               square is either 1, 2 or 3 rotations away from where it belongs.
def hCalc2(cube):
    moves = 0
    for z in range(6):
        for y in range(3):
            for x in range(3):
                if cube[z][y][x] != Rcube.Side(z+1).name:
                    moves += 1
    return moves

# Procedure:    getBestNode(expandedQ)
# Inputs:       queue list
# Returns:      integer
# Description:  Finds the index of the node that has the smallest fValue
def getBestNode(expandedQ):
    Qlength = len(expandedQ)
    fValues = [0] * Qlength     # create empty list
    for i in range(Qlength):    # populate list with gValue + hValue
        fValues[i] = expandedQ[i][1] + expandedQ[i][2]
    return fValues.index(min(fValues))

# Procedure:    inQ(cube,Q)
# Inputs:       cube list, queue list
# Returns:      boolean
# Description:  Returns True if cube is in Q.
def inQ(cube,Q):
    return [cube] in [i[0:1] for i in Q]

# Procedure:    extractPath(visitedQ)
# Inputs:       queue list
# Returns:      list
# Description:  Extracts the solution path from the visitedQ.
def extractPath(visitedQ):
    path = []
    currentNode = visitedQ.pop()
    while (len(visitedQ) > 0):
        previousNode = visitedQ.pop()
        path.append(currentNode[4:6])
        while (currentNode[3] != previousNode[0]):
            previousNode = visitedQ.pop()
        currentNode = previousNode
    path.reverse()
    return path
            
def main():
    # User input:
    print('\nTo input an existing cube or create your own type the word CUBE '+
          'and hit enter.')
    print('Keep in mind that creating a solvable puzzle is tricky!')
    print('One mistake will probably make it unsolvable!')
    selection = input('\nOr simply hit enter for a random cube.')

    if selection.upper() != "CUBE":
        while True:
            try:
                n = int(input('\nEnter number of random rotations: '))
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
            else:
                break
        if n > 7:
            print(
                '\nAnything over 7 will take a really long time (days to '+
                'weeks). Are you sure?')
            while True:
                try:
                    n = int(input('Enter new value or re-enter previous value'
                                  +' if certain: '))
                except ValueError:
                    print("\nSorry, I didn't understand that.")
                    continue
                else:
                    break
        SCRAMBLES = n
        # get a scrambled initial cube
        STARTCUBE = Rcube.scramble(GOALCUBE, SCRAMBLES, scramble_list)
    else:
        # cube from user (must be legal and fit my datatype)
        print('\nYou may need to reference the following cube graphic.')
        print('The oyw and rbg corner cubes represent the top-left 0,0 ' +
              'coordinate of each face.')
        Rcube.displayASCII(GOALCUBE)
        print('\nA graphic will be displayed after that you can compare a')
        print('physical cube to to confirm that you entered it correctly.')
        print('\nOr here is a sample 7-rotation scramble you can input.')
        print('On my system it took about 9 minutes to solve.')
        print('y face = wwrrybbgy')
        print('w face = owogwogrg')
        print('o face = yoryowbyg')
        print('r face = rbbgrywwy')
        print('b face = ybrrbywrg')
        print('g face = bboogoogw\n')
        STARTCUBE = Rcube.get_cube()
        
        #STARTCUBE = Rcube.test_cube()   # instant testing cube
        
    starttime = datetime.now()  # start timer
    gValue = 0                  # actual cost from STARTCUBE to currentCube
    hValue = hCalc(STARTCUBE)   # calculated h(node) heuristic value

    currentNode = [STARTCUBE, gValue, hValue, 0, 0, 0]
    
    # currentNode = [cube, gValue, hValue, parent cube,
    #               previously rotated face, rotation direction]

    print('\nScrambled CUBE:')
    Rcube.displayASCII(STARTCUBE)               # display scrambled cube

    # convert scramble path to face names ('y','w','o','r','b','g') and display
    scramblePath = []
    for i in range(0,len(scramble_list)):
        scramblePath.append([Rcube.Side(scramble_list[i][0]).name,
                             90*scramble_list[i][1]])
        #scramblePath.append(scramble_list)
        
    # display list of rotations
    if scramblePath != []:
        print('Random clockwise rotations as [\'side colour\', degrees]:\n', scramblePath)

    expandedQ.append(currentNode) # at start only first node has been discovered

    print('\nStart time was '+str(starttime))

    while len(expandedQ) != 0:
        currentNode = expandedQ[getBestNode(expandedQ)]
        if currentNode[0] == GOALCUBE:  # currentNode[0] is the currentCube
            visitedQ.append(currentNode)
            break   # DONE: currentNode is the last node of the solution path

        expandedQ.remove(currentNode)
        visitedQ.append(currentNode)
        
        for x in Rcube.Side:    # outer loop checks next nodes for all sides
            for direction in range(1,4): # this loop checks all rotations (90,180,270)
                nextCube = Rcube.copy_cube(currentNode[0])
                for i in range(direction):
                    Rcube.rotate(nextCube, x)
                    if inQ(nextCube, visitedQ):
                        continue
                    if not inQ(nextCube, expandedQ):
                        # currentNode[0] is currentCube and x.value is the
                        #   value of the current face being rotated:
                        #       1 = yellow, 2 = white, etc
                        #   direction: 1=90°, 2=180° and 3=270°
                        nextNode = [nextCube, currentNode[1]+GMULTIPLIER,
                            hCalc(nextCube), currentNode[0], x.value, direction]
                        expandedQ.append(nextNode)        

    print('\nSolved CUBE:')
    Rcube.displayASCII(currentNode[0])

    #print(visitedQ)

    # convert solution path to face names ('y','w','o','r','b','g') and display
    solutionPath = extractPath(visitedQ)
    for i in range(0,len(solutionPath)):
        solutionPath[i][0] = Rcube.Side(solutionPath[i][0]).name
        solutionPath[i][1] = 90 * solutionPath[i][1]
    print('Solution path as [\'side colour\', degrees]:\n', solutionPath)

    print('\nTime to complete was '+str(datetime.now()-starttime))

    input('Hit enter to exit!')
        
main()
