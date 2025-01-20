from copy import deepcopy

def is_winner(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def is_draw(board):
    return all(cell != 0 for cell in board)

def heuristic(board, player):
    opponent = 1 if player == 2 else 2
    if is_winner(board, player):
        return 10  
    elif is_winner(board, opponent):
        return -10  
    else:
        return 0  

def get_neighbors(board, player):
    neighbors = []
    for i in range(len(board)):
        if board[i] == 0: 
            new_board = deepcopy(board)
            new_board[i] = player
            neighbors.append((new_board, i)) 
    return neighbors

def a_star_tic_tac_toe(board, current_player):
    open_set = [(board, None)] 
    came_from = {}
    g_score = {tuple(board): 0}
    f_score = {tuple(board): heuristic(board, current_player)}

    while open_set:
        current, move = min(open_set, key=lambda x: f_score.get(tuple(x[0]), float('inf')))
        open_set.remove((current, move))

        if is_winner(current, current_player) or is_draw(current):
            return move  

        for neighbor, move_index in get_neighbors(current, current_player):
            tentative_g_score = g_score[tuple(current)] + 1

            if tuple(neighbor) not in g_score or tentative_g_score < g_score[tuple(neighbor)]:
                came_from[tuple(neighbor)] = (current, move_index)
                g_score[tuple(neighbor)] = tentative_g_score
                f_score[tuple(neighbor)] = tentative_g_score + heuristic(neighbor, current_player)
                open_set.append((neighbor, move_index))

    return None 

# Example usage
board = [
    1, 2, 0,
    0, 1, 0,
    0, 1, 0
]
current_player = 1  # X's turn
best_move = a_star_tic_tac_toe(board, current_player)
print("Best next move index:", best_move)
