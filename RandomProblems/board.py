def is_valid_board(n, board):
    x_count = 0
    o_count = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'X':
                x_count += 1
            elif board[i][j] == 'O':
                o_count += 1
            elif board[i][j] != '~':
                return False
    
    if abs(x_count - o_count) > 1:
        return False
    
    if check_winner(n, board, 'X') and check_winner(n, board, 'O'):
        return False
    
    if check_winner(n, board, 'X') and x_count <= o_count:
        return False
    
    if check_winner(n, board, 'O') and x_count > o_count:
        return False
    
    return True

def check_winner(n, board, player):
    for i in range(n):
        if all(board[i][j] == player for j in range(n)):
            return True
    
    for j in range(n):
        if all(board[i][j] == player for i in range(n)):
            return True
    
    if all(board[i][i] == player for i in range(n)):
        return True
    
    if all(board[i][n-i-1] == player for i in range(n)):
        return True
    
    return False

print(is_valid_board(3, [["X", "~", "~"], ["~", "~", "~"], ["~", "~", "~"]]))