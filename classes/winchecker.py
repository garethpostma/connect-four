class WinChecker:
    #this class is used to see if a player has connected four pieces
    def __init__(self, game, board):
        self.game = game
        self.board = board

    def check_for_win(self):    #function is used to call the functions that check for different ways of winning
        results = []
        results.append(self.check_win_horizontally()) #append true if there is a win or append false if there is not
        results.append(self.check_win_vertically())
        results.append(self.check_win_diagonally_1())
        results.append(self.check_win_diagonally_2())
        try:
            results.index(True)
            # if the above statement does not generate a ValueError, then a win exists with except ValueError
            return True
        except ValueError:
            return False

    def check_win_horizontally(self):   #this functions checks to see if 4 are connected in any of the rows
        win = False

        for i in range(self.board.rows):    #we must loop through each of the rows
            row = i
            cols = [0, 1, 2, 3]
            while not win:      #keep looping until win is changed to true
                try:
                    # seq will represent the current 4 squares being examined
                    seq = []
                    for i in range(len(cols)):
                        # append current 4 squares to seq list
                        seq.append(self.board.board[row][cols[i]])
                    if self.check_equal(seq):   #check to see if all 4 pieces are the same
                        return True     #if they are then we have a winner
                    else:
                        # increment each value in cols, this is how the horizontal
                        # win checking progresses from left to right
                        for i in range(len(cols)):
                            cols[i] += 1
                        continue
                except IndexError:
                    # we've hit the end of this row, break the loop and move to the next row
                    break
        return win

    def check_win_vertically(self):
        win = False

        for i in range(self.board.cols):#we must check all the columns
            col = i
            rows = [0, 1, 2, 3]
            while not win:
                try:
                    # seq will represent the current 4 squares being examined
                    seq = []
                    for i in range(len(rows)):
                        # append current 4 squares to seq list
                        seq.append(self.board.board[rows[i]][col])
                    if self.check_equal(seq):   #if all 4 are the same then we have a winner
                        return True
                    else:
                        # increment each value in rows, this is how the horizontal
                        # win checking progresses from top to bottom
                        for i in range(len(rows)):
                            rows[i] += 1
                        continue
                except IndexError:
                    # we've hit the end of this col, break the loop and move to the next col
                    break

        return win

    def check_win_diagonally_1(self):#this function checks for diagonals from top left toward bottom right
        win = False

        for i in range(self.board.cols):    
            col = i
            cols = [col, col+1, col+2, col+3]
            rows = [0, 1, 2, 3]
            while not win:
                try:
                    # seq will represent the current 4 squares being examined
                    seq = []
                    for i in range(len(rows)):
                        # append current 4 squares to seq list
                        seq.append(self.board.board[rows[i]][cols[i]])
                    if self.check_equal(seq):   #check to see if all the squares match
                        return True
                    else:
                        # increment each value in rows, this is how the diagonal
                        # win checking progresses from top to bottom
                        for i in range(len(rows)):
                            rows[i] += 1 #we must increment all the row values as we move our diagonal toward the bottom of the board
                        continue
                except IndexError:
                    # we've hit the end of this col, break the loop and move to the next col
                    break

        return win

    def check_win_diagonally_2(self): #this function checks for diagonals from bottom left toward top right
        win = False

        for i in range(self.board.cols):
            col = i
            cols = [col, col+1, col+2, col+3]
            rows = [5, 4, 3, 2]
            while not win:
                try:
                    # seq will represent the current 4 squares being examined
                    seq = []
                    for i in range(len(rows)):
                        # append current 4 squares to seq list
                        seq.append(self.board.board[rows[i]][cols[i]])
                    if self.check_equal(seq): #check to see if all the squares match
                        return True
                    else:
                        # increment each value in rows, this is how the diagonal
                        # win checking progresses from top to bottom
                        for i in range(len(rows)):
                            rows[i] -= 1 #we must decrement all the row values as we move our diagonal toward the top of the board
                        continue
                except IndexError:
                    # we've hit the end of this col, break the loop and move to the next col
                    break

        return win

    def check_equal(self, lst): #this function checks to see if all the pieces in the array are equal and not None
        return lst[1:] == lst[:-1] if lst[0] != self.board.NONE else False
