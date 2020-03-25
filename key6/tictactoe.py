import numpy as np

n = 3
points = {"X": +1, "E": 0, "O": -1}

def print_board(board_state):
    for i in range(n):
        print(" ".join(board_state[i*n:(i+1)*n]))
    print("-"*10)

# returns X if X has won, O if O has won, TIE if it is a tie, and NONE if the game is still in progress
def board_value(board_state):
    for i in range(n):
        horizontal_ct = 0
        vertical_ct = 0
        for j in range(n):
            horizontal_ct += points[board_state[i*n + j]]
            vertical_ct += points[board_state[j*n + i]]
        if horizontal_ct == n or vertical_ct == n:
            return "X"
        if horizontal_ct == -n or vertical_ct == -n:
            return "O"
    
    diagonal_down = 0 
    diagonal_up = 0
    for i in range(3):
        diagonal_down += points[board_state[i*n+i]]
        diagonal_up += points[board_state[(n-i-1)*n+i]]

    for i in range(9):
        if board_state[i] == "E":
            return "NONE"
    return "TIE"

# returns winner ("X" or "O")
# note: cheaters never win
def play_game(strategyX, strategyO):
    board_state = ["E" for i in range(n**2)]
    while board_value(board_state) == "NONE":
        for player, strategy in (("X", strategyX), ("O", strategyO)):
            other_player = "O" if player == "X" else "X"
            old_board_state = board_state[:]
            print_board(board_state)
            move = strategy(board_state, player)
            print(f"^(move = {player}({board_state}))", strategy)
            if board_state[move] != "E" or board_state != old_board_state or not (0 <= move < n**2): 
                print(f"{player} is a CHEATER, tried move={move}")
                return other_player
            board_state[move] = player
            if board_value(board_state) != "NONE":
                #  print_board(board_state)
                return board_value(board_state)


#### strategies:

def ziyong_computer_move(boardState, player):
    other_player = "O" if player == "X" else "X"
    # check for moves that can win the game
    for i in range(3):
        if (boardState[i] == boardState[i + 3] == player):
            if (boardState[i + 6] == "E"):
                return i + 6
        if (boardState[i + 3] == boardState[i + 6] == player):
            if (boardState[i] == "E"):
                return i
        if (boardState[i] == boardState[i + 6] == player):
            if (boardState[i + 3] == "E"):
                return i + 3
        if (boardState[i * 3] == boardState[i * 3 + 1] == player):
            if (boardState[i * 3 + 2] == "E"):
                return i * 3 + 2
        if (boardState[i * 3 + 1] == boardState[i * 3 + 2] == player):
            if (boardState[i * 3] == "E"):
                return i * 3 
        if (boardState[i * 3] == boardState[i * 3 + 2] == player):
            if (boardState[i * 3 + 1] == "E"):
                return i * 3 + 1
    if (boardState[0] == boardState[4] == player):
        if (boardState[8] == "E"):
            return 8
    if (boardState[0] == boardState[8] == player):
        if (boardState[4] == "E"):
            return 4
    if (boardState[4] == boardState[8] == player):
        if (boardState[0] == "E"):
            return 0
    if (boardState[2] == boardState[4] == player):
        if (boardState[6] == "E"):
            return 6
    if (boardState[2] == boardState[6] == player):
        if (boardState[4] == "E"):
            return 4
    if (boardState[6] == boardState[4] == player):
        if (boardState[2] == "E"):
            return 2

    # checking for moves that can lose the game
    for i in range(3):
        if (boardState[i] == boardState[i + 3] == other_player):
            if (boardState[i + 6] == "E"):
                return i + 6
        if (boardState[i + 3] == boardState[i + 6] == other_player):
            if (boardState[i] == "E"):
                return i
        if (boardState[i] == boardState[i + 6] == other_player):
            if (boardState[i + 3] == "E"):
                return i + 3
        if (boardState[i * 3] == boardState[i * 3 + 1] == other_player):
            if (boardState[i * 3 + 2] == "E"):
                return  i * 3 + 2
        if (boardState[i * 3 + 1] == boardState[i * 3 + 2] == other_player):
            if (boardState[i * 3] == "E"):
                return i * 3
        if (boardState[i * 3] == boardState[i * 3 + 2] == other_player):
            if (boardState[i * 3 + 1] == "E"):
                return i * 3 + 1

    if (boardState[0] == boardState[4] == other_player):
        if (boardState[8] == "E"):
            return 8
    if (boardState[0] == boardState[8] == other_player):
        if (boardState[4] == "E"):
            return 4
    if (boardState[4] == boardState[8] == other_player):
        if (boardState[0] == "E"):
            return 0
    if (boardState[2] == boardState[4] == other_player):
        if (boardState[6] == "E"):
            return 6
    if (boardState[2] == boardState[6] == other_player):
        if (boardState[4] == "E"):
            return 4
    if (boardState[6] == boardState[4] == other_player):
        if (boardState[2] == "E"):
            return 2
    #check corners: 0, 2, 6, 8
    for i in range(9):
        if (boardState[i] == "E" and i % 2 == 0 and i != 4):
            return i

    #check center
    if (boardState[4] == "E"):
        return 4

    #if all else fails, place it on the sides: 1, 3, 5, 7
    for i in range(9):
        if (boardState[i] == "E" and i % 2 == 1):
            return i



def alek_computer_move(board_state, computer_symbol):
    opponent_symbol = "O" if computer_symbol == "X" else "X"
    # if there is a win available take it, 
    # if the opponent has a win available block it
    for symbol in (computer_symbol, opponent_symbol):
        for i in range(n**2):
            if board_state[i] == "E":
                tmp_board_state = board_state[:] # make a copy of board_state
                tmp_board_state[i] = symbol
                if board_value(tmp_board_state) == symbol:
                    return i

    def random_computer_move(board_state):
        print("USING RANDOM MOVE")
        proposed_move = (n**2)//2 # center
        while board_state[proposed_move] != "E":
            proposed_move = np.random.randint(n**2)
        return proposed_move

    return random_computer_move(board_state)


# play games
#  X vs O
total_rounds = 1000
alek_wins = 0
ziyong_wins = 0
for i in range(total_rounds):
    if np.random.rand() < 0.5:
        winner = play_game(alek_computer_move, ziyong_computer_move)
        print(f"ALEK (X) VS ZIYONG (O), RESULT: {winner}\n\n\n")
        if winner=="X":
            alek_wins += 1
        if winner == "O":
            ziyong_wins+=1
    else:
        winner = play_game(ziyong_computer_move, alek_computer_move)
        print(f"ALEK (X) VS ZIYONG (O), RESULT: {winner}\n\n\n")
        if winner =="O":
            alek_wins += 1
        elif winner=="X":
            ziyong_wins+=1
        
print(f"ALEK WON {alek_wins} / {total_rounds}")
print(f"ZIYONG WON {ziyong_wins} / {total_rounds}")

