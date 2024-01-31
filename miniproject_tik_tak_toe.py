
board = ["-" for _ in range(9)]  # Use list comprehension for board initialization

# Initialize the game_on flag within the play_game function
def play_game():
    game_on = True


    def display_board():#CREATING A BOARD IN A MANNER WHERE PLAYER CAN EASILY IDENTIFY THE POSITION THE CELLS FROM 1-9
        print(board[0] + " | " + board[1] + " | " + board[2] + "      " + "1 | 2 | 3")
        print(board[3] + " | " + board[4] + " | " + board[5] + "      " + "4 | 5 | 6")
        print(board[6] + " | " + board[7] + " | " + board[8] + "      " + "7 | 8 | 9")

    # Function to define players
    def players():
        print("Select Player - X or O")
        p1 = input("Player 1: ").upper() #CONVERTING INTO UPPER EVEN WE ARE ENTERING LOWER CASE SO THAT WE COULD EASILY COMPARE
        if p1 == "X":
            p2 = "O"
        elif p1 == "O":
            p2 = "X"
        else:
            print("Sorry, invalid input. Type X or O")
            return players()  # Use return to exit function if input is invalid
        print("Player 2: " + p2)
        return p1, p2  # Return players to use later

    # Define the player position
    def player_position(current_player):
        print("Current Player: " + current_player)
        position = input("Choose position from 1 - 9: ")

        # Loop until there is a valid position
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose position from 1 - 9: ")
        position = int(position) - 1 #HERE WE NEED TO CONVERT THE NUMBERS AS THE INDEXES REQUIRED FOR THE BOARD , SINCE IT STARTS WITH 0 AND ENDS WITH 8

        if board[position] == "-":
            board[position] = current_player
        else:
            print("Position already selected, choose another position!")
            player_position(current_player) #calling function again

    # Check for a winner
    def check_winner():
        # Define winning combinations
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # represent winning in Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],   # represents winning in Columns
            [0, 4, 8], [2, 4, 6]  #represents winning in diagonals
        ]
        for combination in winning_combinations:
            if board[combination[0]] == board[combination[1]] == board[combination[2]] != "-":
                return True
        return False

    # Function to flip player
    def flip_player(current_player):#TO FLIP THE PLAYER AFTER EACH TURN
        if current_player == "X":
            return "O"
        else:
            return "X"

    print("My Tic Tac Toe Game")
    display_board()
    player1, player2 = players()#SINCE PLAYER FUNCTION RETURNS TWO VALUES WE WILL ASSIGN IT IN PLAYER1 AND PLAYER2
    current_player = "X"  # Set initial player to X

    # Loop to switch players and check for winner
    while game_on:
        player_position(current_player)
        display_board()
        if check_winner():
            game_on = False
            if "-" not in board: #WHEN THE BOARD COMPLETELY FILLED WITH THE 'X's AND 'O's
                print("It's a Tie")
            else:
                print('yahoo...!! "',current_player,'" wins..!!!!')#PRINTING THE NAME OF THE WINNER WHO RECENTLY MATCHES THE WINNING CHANCE
        current_player = flip_player(current_player)#GAME WILL CONTINUE UNTIL DRAW OR FINDING THE WINNER

play_game()
