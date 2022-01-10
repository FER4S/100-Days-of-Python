from art import welcome

scores = {
    'X': 1,
    'O': -1,
    'Tie': 0
}
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


def print_board(bo):
    print('     1   2   3')
    for i in range(len(bo)):
        if i != 0:
            print('   -------------')
        print(i + 1, end='   ')
        for j in range(len(bo[0])):
            if j != 0:
                print('|', end='')
            if j == 2:
                print(f' {bo[i][j]} ')
            else:
                print(f' {bo[i][j]} ', end='')


def is_free(i, j):
    return board[i][j] == ' '


def insert(symbol, i, j):
    board[i][j] = symbol


def three(q, w, e):
    return q == w and w == e and q != ' '


def check_winner():
    winner = None

    # horizontal
    for i in range(3):
        if three(board[i][0], board[i][1], board[i][2]):
            winner = board[i][0]

    # vertical
    for i in range(3):
        if three(board[0][i], board[1][i], board[2][i]):
            winner = board[0][i]

    # diagonal
    if three(board[0][0], board[1][1], board[2][2]):
        winner = board[0][0]
    if three(board[0][2], board[1][1], board[2][0]):
        winner = board[1][1]

    # free spots
    free_spots = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                free_spots += 1

    if winner is None and free_spots == 0:
        return 'Tie'
    else:
        return winner


def change_turn(player):
    if player == x:
        return o
    else:
        return x


def human_move(player):
    global current_player
    while True:
        move = input(f"It's {player}'s turn! choose the free spot from the board! (row then column eg. 32)\n")
        a, b = int(move[0]) - 1, int(move[1]) - 1
        if is_free(a, b):
            insert(player, a, b)
            current_player = change_turn(player)
            break
        else:
            print('Invalid input! try again!')


def ai_move():
    best_score = float('-inf')
    best_move = None
    global current_player
    for i in range(3):
        for j in range(3):
            if is_free(i, j):
                insert(x, i, j)
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    insert(x, best_move[0], best_move[1])
    current_player = change_turn(current_player)


def minimax(bo, depth, is_maximizing):
    res = check_winner()
    if res is not None and res != ' ':
        return scores[res]

    if is_maximizing:
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = x
                    score = minimax(bo, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = o
                    score = minimax(bo, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score


x = 'X'
o = 'O'
current_player = x

print(welcome)
mode = input('Do you want to play against an AI or a Human? type AI or Human\n').lower()

if mode == 'human':
    while True:
        print_board(board)
        human_move(current_player)

        result = check_winner()
        if result is not None:
            print_board(board)
            if result == 'Tie':
                print('Tie!')
            else:
                print(f'The winner is: {result}!')
            break

elif mode == 'ai':
    while True:
        ai_move()
        print_board(board)
        result = check_winner()
        if result is not None and result != ' ':
            if result == 'Tie':
                print('Tie!')
            else:
                print(f'The winner is: {result}!')
            break
        human_move(current_player)
        result = check_winner()
        if result is not None and result != ' ':
            if result == 'Tie':
                print('Tie!')
            else:
                print(f'The winner is: {result}!')
            break

