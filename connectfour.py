from classes import board, game, exceptions
play_again = "yes"
#This file initiates the first game and board
#once the game is done, it will see if the player would like to continue playing

while play_again == "yes":
    b = board.Board()
    #initiate a game with board b
    g = game.Game(board=b)
    #check to see if the player would like to play again and store answer to play_again
    play_again = input("Would you like to play again? Enter yes to replay: ").lower().strip()
