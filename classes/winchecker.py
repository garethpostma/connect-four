class WinChecker:

    def __init__(self, game, board):
        self.game = game
        self.board = board

    def check_for_win(self):
        return self.check_win_horizontally()

    def check_win_horizontally(self):
        win = False

        for i in range(6):
            row = i
            cols = [0, 1, 2, 3]
            while not win:
                try:
                    # seq will represent the current 4 squares being examined
                    seq = []
                    for i in range(len(cols)):
                        # append current 4 squares to seq list
                        seq.append(self.board.board[row][cols[i]])
                    if self.check_equal(seq):
                        return True
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
        pass

    def check_win_diagonally(self):
        pass

    def check_equal(self, lst):
        return lst[1:] == lst[:-1] if lst[0] != self.board.NONE else False