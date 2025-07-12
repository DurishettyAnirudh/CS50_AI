"""
Tic Tac Toe Player
"""

import math
import copy


X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    flat = [cell for row in board for cell in row]
    
    x_count = flat.count(X)
    o_count = flat.count(O)

    return X if x_count == o_count else O
    """
    Returns player who has the next turn on a board.
    """
    raise NotImplementedError


def actions(board):
    list_of_actions = []
    
    for i, row in enumerate(board):
        for j, element in enumerate(row):
            if element is None:
                list_of_actions.append((i, j))
    return set(list_of_actions)
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    raise NotImplementedError


def result(board, action):
    i, j = action
    if i<0 or i>=3 or j<0 or j>=3:
        raise Exception("Action out of bounds")
    
    if board[i][j] is not EMPTY:
        raise Exception('Invalid move')
    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)

    return new_board

    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    for row in board:
        if row[0] is not None and row.count(row[0]) == 3:
            return row[0]
    for col in range(3):
        if board[0][col] is not None and all(board[row][col] == board[0][col] for row in range(3)):
            return board[0][col]
        
    if board[0][0] is not None and all(board[i][i] == board[0][0] for i in range(3)):
        return board[0][0]
    
    if board[0][2] is not None and all(board[i][2-i] == board[0][2] for i in range(3)):
        return board[0][2]
    
    return None
        

    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


class user_defined:
    
    def row_wise(self, board):
        for row in board:
            if len(set(row)) == 1:
                return True
        return False
    
    def column_wise(self, board):
        prev = None
        buffer = 1
        
        row_len = len(board)
        col_len = len(board[0])
        for i in range(col_len):
            for j in range(row_len):
                if prev == board[j][i]:
                    buffer+=1
                if buffer == row_len:
                    return True
                prev = board[j][i]
            buffer = 0 
        return False
    
    
    def diagonal_wise(self, board):
        vertical = len(board)
        horizontal = len(board[0])
        prev = None
        left = 1
        right = 1
        for i in range(vertical):
            if board[i][i] == prev:
                left += 1
            if left == vertical:
                return True
            
        prev = None
        for i in range(3):
            j = vertical - i -1
            if board[i][j] == prev:
                right += 1
            if right == vertical:
                return True  
            prev = board[i][j]
        return False
            
    def is_full(self, board):
        for row in board:
            if EMPTY in row:
                return False
        return True


def terminal(board):
    return winner(board) is not None or all(cell is not None for row in board for cell in row)
                
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    champ = winner(board)
    if champ == X:
        return 1
    elif champ == O:
        return -1
    else: return 0
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):

    if terminal(board):
        return None
    turn = player(board)

    def min_value(board):
        if terminal(board):
            return utility(board)
        
        v = math.inf
        actions_list = list(actions(board))
        for action in actions_list:
            v = min(v, max_value(result(board, action)))
        
        return v
    
    def max_value(board):
        if terminal(board):
            return utility(board)
        
        v = -math.inf
        actions_list = list(actions(board))
        for action in actions_list:
            v = max(v, min_value(result(board,action)))
        
        return v

    if turn == X:
        best_score = -math.inf
        best_action = None
        actions_list = list(actions(board))
        for action in actions_list:
            score = min_value(result(board, action))
            if score > best_score:
                best_score = score
                best_action = action
        return best_action
    
    else:
        best_score = math.inf
        best_action = None
        actions_list = list(actions(board))
        for action in actions_list:
            score = max_value(result(board, action))
            if score < best_score:
                best_score = score
                best_action = action
        return best_action


# def debug():
#     board = [[X,    O,  None], 
#              [None, None,  X], 
#              [O,    X,  None]]
#     actionae = actions(board)
#     print(actionae)

# # debug()