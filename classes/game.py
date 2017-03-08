from sys import exit
from . import winchecker
#in this class we are defining all the general movement functions for the game
class Game:
    P1 = 'P1'
    P2 = 'P2'
    
    def __init__(self, board):  #function used to initially setup the game
        
        self.current_player = self.P1   #set the first player to move as P1
        self.board = board      #set local board to equal the input board
        self.winchecker = winchecker.WinChecker(game=self, board=self.board)  #initiate the winchecker class and pass in the current game and board
        print("Welcome to connect four! ")
        self.make_move()        #start game by calling for the first move

    def make_move(self):    #this function will be used to get user input and make the necessary changes to the board
        print("{}\n{}, you're up! ".format(self.board, self.current_player))  # ask current player to make a move
        column_choice = self.get_column_choice()    #get players move from function get_column_choice and store it
        valid_column = self.place_checker(column=column_choice) #place the piece using place_checker function with the selected column
        if not valid_column:       #make sure it is legal
            print("That column is full. Please enter a non-full column. ")  #if column is not legal, tell the user
            self.make_move()  #call make_move again in order to make the user make a legal move
            return False
        win = True if self.check_for_win() else False   #check if a player has won the game using check_for_win function
        if not win:      #if they did not win then change players and begin their turn 
            self.toggle_players()
            self.make_move()
        if win:            #if a player has won then print the board and congratulate the winner
            print(self.board)
            print("\ncongratulations {}, you win!\n".format(self.current_player))
            
    def get_column_choice(self):    #function used to get the users move
        print("What column what you like to place your piece?\n")
        column_choice = input("Valid choices are columns 0 through 6: ")
        try:
            if column_choice == "exit": exit()   #if player hits exit then quit 
            column_choice = int(column_choice)  #otherwise store the column they chose
            return column_choice if 0 <= column_choice <= 6 else self.get_column_choice()   #if the user chose a location outside the board then get new input
        except ValueError:  #if player entered incorrect character then restart function
            return self.get_column_choice()
        
    def place_checker(self, column):    #this function will find the location for the piece the user has placed and put a piece there
        print("You've selected column {}".format(column))      #tell the player what column they selected
        if(self.board.board[0][column] != ' . '):   #check to see if that column is full
            # column is full, force player to re-choose
            return False
        lowest_available_row = self.find_lowest_row_in_column(column=column)    #find the lowest position in the chosen column
        try:
            self.board.board[lowest_available_row][column] = self.players_piece()   #place the players piece in that position
            return True
        except IndexError:   #just in case there is a array error we can catch it
            # this should never happen
            print("Array out of bounds error! Exiting...")
            exit()
            
    def find_lowest_row_in_column(self, column):    #this function actually finds the next location in the selected column
        column_as_list = []
        for row in self.board.board:    #loop through all the rows in the board
            column_as_list.append(row[column])  #add all these values to the array
        try:
            first_red = column_as_list.index(self.board.RED) - 1 #find location above first red piece in the column
        except ValueError:
            first_red = None    #set it to none if there are no red pieces
        try:
            first_blue = column_as_list.index(self.board.BLUE) - 1  #find the location above first blue piece in the column
        except ValueError:
            first_blue = None   #set it to none if there are no blue pieces

        if first_blue == None and first_red == None:
            return 5       #if there are no pieces in the column then our row value is 5
        elif first_blue == None or first_red == None:   
            return first_blue if first_blue != None else first_red   # if there is only one colour then send the location above the highest one
        else:
            return min(first_blue, first_red)   #if there are two colours then send the location above the highest piece

    def check_for_win(self):    #this function simply checks to see if there is a winner using the winchecker class
        return self.winchecker.check_for_win()

    def toggle_players(self):   #this function changes which player's turn it is
        self.current_player = self.P2 if self.current_player == self.P1 else self.P1

    def players_piece(self):    #this function returns the colour of the current players pieces
        return self.board.RED if self.current_player == self.P1 else self.board.BLUE
