game_matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9]
victory = [[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8],
           [0, 3, 6],
           [1, 4, 7],
           [2, 5, 8],
           [0, 4, 8],
           [2, 4, 6]]


def playing_field(matrix):
    print(matrix[0], end=" ")
    print(matrix[1], end=" ")
    print(matrix[2])
    print(matrix[3], end=" ")
    print(matrix[4], end=" ")
    print(matrix[5])
    print(matrix[6], end=" ")
    print(matrix[7], end=" ")
    print(matrix[8])


def player_move(num, sign, my_matrix):
    position = my_matrix.index(num)
    my_matrix[position] = sign


def get_result():
    winner = ""
    for i in victory:
        if game_matrix[i[0]] == "X" and game_matrix[i[1]] == "X" and game_matrix[i[2]] == "X":
            winner = f"Player X won!!!!"
        if game_matrix[i[0]] == "O" and game_matrix[i[1]] == "O" and game_matrix[i[2]] == "O":
            winner = f"Player O won!!!!"
    return winner


print(f"Choose which of the players will go first")
print(f"First Player - X")
print(f"Second player - O")
step = 1
player_1 = True
winning = ''
while step <= 9:
    playing_field(game_matrix)
    if player_1 is True:
        symbol = 'X'
        move = int(input("The first player's (X) move: "))
    else:
        symbol = 'O'
        move = int(input("The second  player's (O) move: "))
    player_move(move, symbol, game_matrix)
    winning = get_result()
    if winning == "":
        step += 1
        player_1 = not player_1
        continue
    else:
        break
playing_field(game_matrix)
if winning != "":
    print(f"{winning}")
else:
    print(f"Friendship won")
