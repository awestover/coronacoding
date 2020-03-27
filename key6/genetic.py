
"""
conventions:
    - X goes first
note:
    if num(X) = num(O) then it is Xs turn
    else it is Os turn
"""

import numpy as np
n = 3

"""
What is a genetic algorithm?

We have
- a population of `players` / bots
- each player has some "DNA" that determines how they are going to act in any given situtation
- natural selection survival of the fitest
- we play the bots against each other
- and the bots that win matches survive and reproduce (asexually)
- and the losing bots die
"""

"""
tic tac toe bot's DNA:

EEE EEE EEE -> 4
EEE EXE EOE -> 1
...

number of possible tic tac toe boards: 
    num(X) = num(O) or num(X) = num(O) + 1

"""

points = {"X": +1, "E": 0, "O": -1}

def print_board(board_state):
    for i in range(n):
        print(" ".join(board_state[i*n:(i+1)*n]))
    print("-"*10)


# returns X if X has won, O if O has won, TIE if it is a tie, and NONE if the game is still in progress
# returns [X, O, TIE, or NONE]
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
    for i in range(n):
        diagonal_down += points[board_state[i*n+i]]
        diagonal_up += points[board_state[(n-i-1)*n+i]]

    for i in range(n**2):
        if board_state[i] == "E":
            return "NONE"
    return "TIE"

# returns winner ("X" or "O")
# note: cheaters never win
def play_game(strategyX, strategyO):
    board_state = "E"*n**2
    while board_value(board_state) == "NONE":
        for player, strategy in (("X", strategyX), ("O", strategyO)):
            other_player = "O" if player == "X" else "X"
            #  print_board(board_state)
            move = strategy(board_state, player)
            board_state = modify_val(board_state, move, player)
            if board_value(board_state) != "NONE":
                #  print_board(board_state)
                return board_value(board_state)

def modify_val(string, idx, val):
    return string[:idx] + val + string[idx+1:]

def get_other_player(player):
    if player == "X":
        return "O"
    else:
        return "X"

# generate all possible tic tac toe game states
all_notover_tictactoe_boards = [{"E"*n**2}]

player = "X"
for game_round in range(n**2):
    next_level = set()
    for board in all_notover_tictactoe_boards[-1]:
        for spot in range(n**2):
            if board[spot] == "E" and board_value(board) == "NONE":
                modified_board = modify_val(board, spot, player)
                if board_value(modified_board) == "NONE":
                    next_level.add(modified_board)
    all_notover_tictactoe_boards.append(next_level)
    player = get_other_player(player)

flat_all_ttt_boards = []
for game_round_boards in all_notover_tictactoe_boards:
    for x in game_round_boards:
        flat_all_ttt_boards.append(x)

num_boards = len(flat_all_ttt_boards)
print(num_boards)

ttt_board_idx = {} # "EEE EEE EEE" -> 1
for i in range(num_boards):
    ttt_board_idx[flat_all_ttt_boards[i]] = i

def random_bot():
    moves = []
    for board in flat_all_ttt_boards:
        proposed_move = n**2//2
        while board[proposed_move] != "E":
            proposed_move = np.random.randint(0, n**2)
        moves.append(proposed_move)
    return moves

def bot_strategy(bot_dna):
    def strategy(board_state, player):
        return bot_dna[ttt_board_idx[board_state]]
    return strategy

def mutate(bot_dna):
    new_random_dna = random_bot()
    for i in range(num_boards):
        if np.random.rand() > 0.01:
            new_random_dna[i] = bot_dna[i]
    return new_random_dna

pop_size = 100
population = [random_bot() for i in range(pop_size)]

num_matches = 20
best_bot = 0
num_generations = 5

for generation in range(num_generations):
    # play the bots against each other, 
    # decide which bots are the best

    bot_scores = [0 for i in range(pop_size)]
    for j in range(pop_size):
        cur_bot_strategy = bot_strategy(population[j])
        for i in range(num_matches//2):
            other_bot = np.random.randint(0,pop_size)
            other_bot_strategy = bot_strategy(population[other_bot])
            winner = play_game(other_bot_strategy, cur_bot_strategy)
            if winner == "X":
                bot_scores[j] -= 1
                bot_scores[other_bot] += 1
            elif winner == "O":
                bot_scores[j] += 1
                bot_scores[other_bot] -= 1
        for i in range(num_matches//2):
            other_bot = np.random.randint(0,pop_size)
            other_bot_strategy = bot_strategy(population[other_bot])
            winner = play_game(cur_bot_strategy, other_bot_strategy)
            if winner == "X":
                bot_scores[j] += 1
                bot_scores[other_bot] -= 1
            elif winner == "O":
                bot_scores[j] -= 1
                bot_scores[other_bot] += 1

    # keep those bots for next generation
    # mutate those bots to use as "children" in next generation

    next_population = []

    if generation == num_generations-1:
        best_bot = population[np.argmax(bot_scores)]

    for j in range(pop_size):
        if bot_scores[j] > 1:
            next_population.append(population[j])

    while len(next_population) < pop_size:
        next_population.append(mutate(population[np.random.randint(0,pop_size)]))

    population = next_population
    print(bot_scores)


board_state = "E"*n**2
computer_strategy = bot_strategy(best_bot)
while board_value(board_state) == "NONE":
    board_state = modify_val(board_state, computer_strategy(board_state, "X"), "X")
    print_board(board_state)
    if board_value(board_state) != "NONE":
        break
    user_move = int(input("O move? :\t"))
    board_state = modify_val(board_state, user_move, "O")
    print_board(board_state)
        

