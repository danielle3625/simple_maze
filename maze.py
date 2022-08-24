#Initialize height, width, the start position, ,and initial orientation
#Create Maze
import random


def generate_maze_board():
    """
    This function generates  nested list of lists, to display the maze. All single variable
    """
    return [['.'] * 10 for pos in range(10)]


def random_maze(maze):
    """
    This function replaces some of the single variable board to add obstacles in the maze.
    """
     #this list acts as a setlist for the random variable
    maze_char = ['.', '*', '.', '.']

    for i in range(6):
        for x in range(8):
            maze[i][x] = random.choice(maze_char)


def start_end(maze):
    x = random.randint(1,8)
    y = random.randint(1,8)
    x_x = random.randint(1,8)
    y_y= random.randint(1,8)
    maze[x][y] = 'X'
    maze[y_y][x_x] = 'O'

def display_maze(maze):
    """
    This function displays the current maze board as rows and columns
    """
    #row1 =
    print(maze[0][0] + maze[1][0] + maze[2][0] + maze[3][0] + maze[4][0] + maze[5][0] + maze[6][0] + maze[7][0] + maze[8][0] + maze[9][0])
    #row2 = 
    print(maze[0][1] + maze[1][1] + maze[2][1] + maze[3][1] + maze[4][1] + maze[5][1] + maze[6][1] + maze[7][1] + maze[8][1] + maze[9][1])
    #row3 = 
    print(maze[0][2] + maze[1][2] + maze[2][2] + maze[3][2] + maze[4][2] + maze[5][2] + maze[6][2] + maze[7][2] + maze[8][2] + maze[9][2])
    #row4 = 
    print(maze[0][3] + maze[1][3] + maze[2][3] + maze[3][3] + maze[4][3] + maze[5][3] + maze[6][3] + maze[7][3] + maze[8][3] + maze[9][3])
    #row5 = 
    print(maze[0][4] + maze[1][4] + maze[2][4] + maze[3][4] + maze[4][4] + maze[5][4] + maze[6][4] + maze[7][4] + maze[8][4] + maze[9][4])
    #row 6 =
    print(maze[0][5] + maze[1][5] + maze[2][5] + maze[3][5] + maze[4][5] + maze[5][5] + maze[6][5] + maze[7][5] + maze[8][5] + maze[9][5])
    #row 7 =
    print(maze[0][6] + maze[1][6] + maze[2][6] + maze[3][6] + maze[4][6] + maze[5][6] + maze[6][6] + maze[7][6] + maze[8][6] + maze[9][6])
    #row 8 =
    print(maze[0][7] + maze[1][7] + maze[2][7] + maze[3][7] + maze[4][7] + maze[5][7] + maze[6][7] + maze[7][7] + maze[8][7] + maze[9][7])
    #row 9 =
    print(maze[0][8] + maze[1][8] + maze[2][8] + maze[3][8] + maze[4][8] + maze[5][8] + maze[6][8] + maze[7][8] + maze[8][8] + maze[9][8])
    #row 10 =
    print(maze[0][9] + maze[1][9] + maze[2][9] + maze[3][9] + maze[4][9] + maze[5][9] + maze[6][9] + maze[7][9] + maze[8][9] + maze[9][9])


def perimeter_set(maze):
    """
    This function secures the perimeter!
    """
    top = [maze[0][0], maze[1][0],  maze[2][0],  maze[3][0],  maze[4][0], maze[5][0], maze[6][0],  maze[7][0],  maze[8][0],  maze[9][0]]
    bottom = [maze[0][0], maze[0][1], maze[0][2], maze[0][3], maze[0][4], maze[0][5], maze[0][6], maze[0][7], maze[0][8], maze[0][9]]
    left_side = [maze[9][0], maze[9][1], maze[9][2], maze[9][3], maze[9][4], maze[9][5], maze[9][6], maze[9][7], maze[9][8], maze[9][9]]
    right_side = [maze[0][9] , maze[1][9] + maze[2][9], maze[3][9], maze[4][9], maze[5][9], maze[6][9], maze[7][9], maze[8][9], maze[9][9]]

    #top
    for i in range(10):
        maze[i][0] = '*'
    #bottom
    for i in range(10):
        maze[0][i] = '*'
    #left
    for i in range(10):
        maze[9][i] = '*'
    #right
    for i in range(10):
        maze[i][9] = '*'



def perimeter_check(maze):
    """
    This function does a perimeter check. Will be used for move selector to check for available space.
    """
    top = [maze[0][0], maze[1][0],  maze[2][0],  maze[3][0],  maze[4][0], maze[5][0], maze[6][0],  maze[7][0],  maze[8][0],  maze[9][0]]
    bottom = [maze[0][0], maze[0][1], maze[0][2], maze[0][3], maze[0][4], maze[0][5], maze[0][6], maze[0][7], maze[0][8], maze[0][9]]
    left_side = [maze[9][0], maze[9][1], maze[9][2], maze[9][3], maze[9][4], maze[9][5], maze[9][6], maze[9][7], maze[9][8], maze[9][9]]
    right_side = [maze[0][9] , maze[1][9] + maze[2][9], maze[3][9], maze[4][9], maze[5][9], maze[6][9], maze[7][9], maze[8][9], maze[9][9]]

    for pos in top:
        if pos == '*':
            return True

    for pos in bottom:
        if pos == '*':
            return True

    for pos in left_side:
        if pos == '*':
            return True

    for pos in right_side:
        if pos == '*':
            return True

def replay():
    choice = input("Do you want to play again? Y or N: ").upper()
    if choice == 'Y':
        return True
    else:
        return False



def game_play():

    game_on = True

    maze_board = generate_maze_board()
    random_maze(maze_board)
    perimeter_set(maze_board)
    start_end(maze_board)
    display_maze(maze_board)

    while game_on:
        print('You have found THE MAZE')
        print('Each game will generate a new maze to solve')
        print('You are starting on position X. Your goal is to get to position O in as few moves as possible.')
        print('You may only step on places marked with a . You may not step on places marked *')
        
        play_now = 'a'

        while play_now not in ['y','n']:
            play_now = input('Are you Ready to play? Y or N: ')

        while play_now == 'y':
        
            

            play_x = 0
            play_y = 0

            count_moves = []

            while maze_board[play_x][play_y] not in ['O']:
                
                print('Choose your move in the form of (x,y), for (column, row) starting with count 0')
                play_x = int(input('Choose x value:  '))
                play_y = int(input('Choose y value:  '))

                count_moves.append(play_x)

                if maze_board[play_x][play_y] == '*':
                    print('You cannot move to * spaces!')
                    continue
                elif maze_board[play_x][play_y] == '.':
                    maze_board[play_x][play_y] = 'X'
                    display_maze(maze_board)
                    break
                elif maze_board[play_x][play_y] == 'O':
                    print('You win! It took you ' + str(len(count_moves)) + 'moves.')
                    break

            if not replay():
                play_now = 'a'
                game_on = False
                break
            else:
                game_play()
                break

game_play()

            


    
  
#for item in maze:
        #print (' '.join(str(x) for x in item))
    



#An infinite loop that breaks when either (1) our current location is the 
#same as the exit location, or (2) we've visited a coordinate we've already seen. 


    #Add current position/orientation to list of seen (position, orientation) pairs 
    

    
    #For each orientation, check if the character can move right, if not, then forward, 
   # if not, then left, and if not, then backward. Adjust the position according to 
    #which step you took. A step just consists of incrementing either the x or y coordinate. 
  

#After exiting the loop, check why you exited the loop, either you 
#(1) found the exit or (2) visited every coordinate (i.e. no exit was found). 


