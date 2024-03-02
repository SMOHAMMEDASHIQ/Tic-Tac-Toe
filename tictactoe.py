
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")


def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))


def dfs(board, player):
    if check_winner(board, 'X'):
        return 1
    elif check_winner(board, 'O'):
        return -1
    elif is_board_full(board):
        return 0

    scores = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = player
                if player == 'X':
                    scores.append(dfs(board, 'O'))
                else:
                    scores.append(dfs(board, 'X'))
                board[i][j] = ' '

    if player == 'X':
        return max(scores)
    else:
        return min(scores)


def find_best_move(board):
    best_score = float('-inf')
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                score = dfs(board, 'O')
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move    


def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    while True:
        print_board(board)
        if current_player == 'X':
            row, col = find_best_move(board)
            board[row][col] = 'X'
        else:
            while True:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
                    break
                else:
                    print("Invalid move. Try again.")
            board[row][col] = 'O'

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = 'X' if current_player == 'O' else 'O'

# Start the game
play_game()