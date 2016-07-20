from random import randint
import numpy as np


def board_setup(width, height):
    h, w = height, width
    iboard = np.zeros((h,w), dtype=np.int16)
    for x in range(h):
        for y in range(w):
            if (x == 20) or (y == 0 or y == 21):
                iboard[x][y] = 1
    return iboard


def new_piece(iboard, ipieces):
    board_width = len(iboard[0]) # 22
    #random_position = randint(1,board_width)
    random_piece = randint(1,5)
    if random_piece == 1:
        random_positiony = randint(1, board_width - 5 - 1)
    elif random_piece in [2,3,4,5]:
        random_positiony = randint(1, board_width - 1 - 1)
    print(random_positiony)
    ipiece_position = [0,random_positiony]
    # random_position = 1
    ipiece = ipieces[random_piece]
    print(ipiece)
    for i, value1 in enumerate(ipiece):
        for j, value2 in enumerate(value1):
            if value2 == 1:
                if iboard[0+i][random_positiony+j-1] == 1:
                    print("Game Over!!!")
                    return 0
                else:
                    iboard[0+i][random_positiony+j-1] = 1
                print(value2)
    ipiece = ipieces[1]
    ipiece_position = [0, 4]
    return iboard, ipiece, ipiece_position

6562 6879 0060zz
def next_move(iboard, ipiece, ipiece_position):
    value = input("Input your next move (wasd): ")
    # value = "a"
    if value in ["w", "a", "s", "d"]:
        if value == "a":  # move left
            if ipiece_position[1] == 1:
                ipiece_position = [ipiece_position[0] + 1, ipiece_position[1]]
                print("position 1")
            else:
                ipiece_position = [ipiece_position[0] + 1, ipiece_position[1] - 1]
                print("position 2")
            # ipiece_position = [ipiece_position[0] + 1, ipiece_position[1] - 1]
            print("==="+str(ipiece_position))
            iboard = board_update(iboard, ipiece, ipiece_position)
            pass
        elif value == "d":  # move right
            pass
    else:
        print("Invalid input! Please re-input other value")

    return iboard, ipiece, ipiece_position


def board_update(iboard, ipiece, ipiece_position):
    pass
    for i, value1 in enumerate(ipiece):
        for j, value2 in enumerate(value1):
            if value2 == 1:
                iboard[ipiece_position[0] + i - 1][ipiece_position[1] + j] = 0  # clear previous position
                if iboard[ipiece_position[0] + i][ipiece_position[1] + j - 1] == 1:
                    print(ipiece_position)
                    print("Game Over2!!!")
                    return 0
                else:
                    iboard[ipiece_position[0] + i][ipiece_position[1] + j - 1] = 1
    print(iboard)
    return iboard

if __name__ == "__main__":
    pieces = {1: np.array([[1,1,1,1],
                           [0,0,0,0]]),
              2: np.array([[1,0],
                          [1,0],
                          [1,1]]),
              3: np.array([[0,1],
                          [0,1],
                          [1,1]]),
              4: np.array([[0,1],
                          [1,1],
                          [1,0]]),
              5: np.array([[1,1],
                          [1,1]])
              }
    board = board_setup(22, 21)
    board[0][1] = 3
    # print(board)
    board, piece, piece_position = new_piece(board, pieces)
    print(board)
    while 1:
        board, piece, piece_position = next_move(board, piece, piece_position)