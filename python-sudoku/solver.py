board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7],
]


def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for num in range(1, 10):
        if valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0

    return False


def valid(board, num, pos):
    # pos is a tuple (row, column)
    pos_x = pos[1]
    pos_y = pos[0]

    # Check row
    for column in range(len(board[0])):
        if board[pos_y][column] == num:
            return False

    # Check column
    for row in range(len(board)):
        if board[row][pos_x] == num:
            return False

    # Check box
    box_x = pos_x // 3
    box_y = pos_y // 3

    for y in range(box_y * 3, box_y * 3 + 3):
        for x in range(box_x * 3, box_x * 3 + 3):
            if board[y][x] == num and (y, x) != pos:
                return False

    return True


def print_board(bo):
    for y in range(len(bo)):
        if y % 3 == 0 and y != 0:
            print("-----------------------")

        for x in range(len(bo[0])):
            if x % 3 == 0 and x != 0:
                print("|", end="")

            if x == 8:
                print(bo[y][x])
            else:
                print(str(bo[y][x]) + " ", end="")


def find_empty(board):
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == 0:
                return (y, x)  # row, column
    return None


print_board(board)
solve(board)
print("\n\n")
print_board(board)
