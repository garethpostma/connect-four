class Board:

    NONE = ' . '
    RED = ' A '
    BLUE = ' O '

    def __init__(self, cols = 6, rows = 7, required_to_win = 4):
        self.cols = cols
        self.rows = rows
        self.win = required_to_win
        #set all the squares to none symbol
        self.board = [[self.NONE] * rows for col in range(cols)]

    def __str__(self):
        b = '\n'
        for row in self.board: #we add all the rows from the board to b
            b += ''.join(row) + '\n'
        b += " 0  1  2  3  4  5  6  \n" #add labels to each of the columns
        return b
