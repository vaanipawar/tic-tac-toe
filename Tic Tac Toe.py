import numpy as np
def initialize_board():
    return np.zeros((3, 3), dtype = int)

def display_board(board):
    symbols = {1: 'X', -1: 'O', 0 : ''}
    for row in board:
        print('|'.join([symbols[cell] for cell in row]))
        print('-'*7)

def check_winner(board):
    for player in [1,-1]:
        if any(np.all(row == player) for row in board) or\
           any(np.all(col == player) for col in board.T) or\
           np.all(np.diag(board) == player) or \
           np.all(np.diag(np.fliplr(board)) == player):
           return player  
    return 0

def is_draw(board):
    return np.all(board != 0) and check_winner(board) == 0

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner != 0:
        return (10 - depth) if winner == -1 else (depth - 10)
    if is_draw(board):
        return 0
    if is_maximizing:
        best_score = -np.inf
        for i in range(3):
            for j in range(3):
                if board[i,j] == 0:
                    board[i,j] = -1
                    score = minimax(board, depth +1, False)
                    board[i,j] = 0
                    best_score = max(best_score, score)
        return best_score
    else:
        
        best_score = np.inf
        for i in range(3):
            for j in range(3):
                if board[i, j] == 0:
                    board[i, j] = 1  
                    score = minimax(board, depth + 1, True)
                    board[i, j] = 0 
                    best_score = min(best_score, score)
        return best_score
    
def find_best_move(board):
    best_score = -np.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i, j] == 0:
               board[i, j] = -1  
               score = minimax(board, 0, False)
               board[i, j] = 0  
               if score > best_score:
                   best_score = score
                   best_move = (i, j) 
    return best_move
   
                

def play_game():
    board = initialize_board()
    print("Welcome to Tic-Tac-Toe!")
    display_board(board)

    while True:
        
        while True:
            try:
                row, col = map(int, input("Enter your move (row and column: 0, 1, 2): ").split())
                if board[row, col] == 0:
                    board[row, col] = 1
                    break
                else:
                    print("Cell is already occupied. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Enter row and column as 0, 1, or 2.")

        display_board(board)

        
        if check_winner(board) == 1:
            print("Congratulations! You win!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

    
        print("AI is making a move...")
        ai_move = find_best_move(board)
        if ai_move:
            board[ai_move[0],ai_move[1]] = -1

        display_board(board)

        
        if check_winner(board) == -1:
            print("AI wins! Better luck next time.")
            break
        if is_draw(board):
            print("It's a draw!")
            break
if __name__ == "__main__":
    play_game()
