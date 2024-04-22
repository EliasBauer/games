# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with fewer than two live neighbors dies, as if by underpopulation.
# Any live cell with more than three live neighbors dies, as if by overpopulation.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

from time import sleep

WIDTH = 6
HEIGHT = 6

game_board = [
    ["O", "O", "O", "O", "O", "O"],
    ["O", "O", "X", "O", "O", "O"],
    ["O", "O", "X", "O", "O", "O"],
    ["O", "O", "X", "O", "O", "O"],
    ["O", "O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O", "O"],
]


def count_neighbors(y, x):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if y + i >= 0 and x + j >= 0 and y + i < HEIGHT and x + j < WIDTH:
                if game_board[y + i][x + j] == "X":
                    count += 1
    return count


def conway_game_of_life(cell: str, neighbors: int):
    if cell == "O" and neighbors == 3:
        return True
    elif cell == "X" and (neighbors == 2 or neighbors == 3):
        return True
    # elif cell == "X" and neighbors < 2:
    #     return False
    # elif cell == "X" and neighbors > 3:
    #     return False
    else:
        return False


def print_board(board):
    for row in board:
        # print(WIDTH * "--")
        for cell in row:
            print(cell + " ", end="")
            # print("|", end="")
        print()
    print(WIDTH * "--")


while True:
    print_board(game_board)
    new_board = [[0 for x in range(WIDTH)] for y in range(HEIGHT)]
    for y in range(HEIGHT):
        for x in range(WIDTH):
            neighbors = count_neighbors(y, x)
            if conway_game_of_life(game_board[y][x], neighbors):
                new_board[y][x] = "X"
            else:
                new_board[y][x] = "O"

    game_board = new_board
    sleep(5)
