
import random
board = ["-" for _ in range(9)]
def play_game():
    game_on=True
    def display_board():
            print(board[0] + " | " + board[1] + " | " + board[2] + "      " + "1 | 2 | 3")
            print(board[3] + " | " + board[4] + " | " + board[5] + "      " + "4 | 5 | 6")
            print(board[6] + " | " + board[7] + " | " + board[8] + "      " + "7 | 8 | 9")
    def players():
            print("select the player 'X' or 'O' ")
            p1=input('player1:').upper()
            if p1=='X':
                    p2='O'
            elif p1=='O':
                    p2='X'
            else:
                print("sorry invalid input please input 'X' or 'O' :")
                return players()
            print('player2:'+p2)
            return p1,p2
    def current_state(current_player):
            print("current player:"+current_player)
            position=input("choose the current position from 1-9: ")
            while position not in ('1','2','3','4','5','6','7','8','9'):
                    position=input("choose the current position from 1-9: ")
            position=int(position)-1

            if board[position]=='-':
                board[position]=current_player
            else:
                print('position already selected, choose another position.!!')
                current_state()#calling function again
    def check_winner():
        winning_chances=[
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # represent winning in Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # represents winning in Columns
            [0, 4, 8], [2, 4, 6] ] #represents winning in diagonals
        for chances in winning_chances:
              if board[chances[0]]==board[chances[1]]==board[chances[2]]!='-':
                    return True
        return False
    def flip_player(current_player):
          if current_player=='X':
                return 'O'
          else:
                return 'X'
    print("WELCOME TO MY TIK-TAK-TOE-GAME")
    display_board()
    player1,player2=players()
    current_player=player1
    while game_on:
            current_state(current_player)
            display_board()
            if check_winner():
                    if '-' not in board:
                        print("oohh...it is a draw..!!")
                        break
                    else:
                        print('yahoo...!! "',current_player,'" wins..!!!!')
                        break
            current_player=flip_player(current_player)
play_game()

