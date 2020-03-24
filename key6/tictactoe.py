import numpy as np

n = 3
board_state = ["E" for i in range(n**2)]
points = {"X": +1, "E": 0, "O": -1}

def print_board(board_state):
    for i in range(n):
        print(" ".join(board_state[i*n:(i+1)*n]))

def computer_move(board_state):
    proposed_move = (n**2)//2 # center
    while board_state[proposed_move] != "E":
        proposed_move = np.random.randint(n**2)
    return proposed_move

# returns X if X has won, O if O has won, TIE if it is a tie, and NONE if the
# game is still in progress
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

