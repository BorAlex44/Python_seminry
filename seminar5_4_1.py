import random


def player_move(player_name):
    move = int(input(f"{player_name} enter the number of candies you will take (from 1 to 28): "))
    while move < 1 or move > 28:
        move = int(input(f"{player_name} you have entered the wrong number of candies!!! Enter again."))
    return move


def print_result(name, num, count, rem):
    print(f"Player's move {name}.{name} took {num} candies.Now he has {count} candy.There are some sweets left - {rem}")


name_1 = input("Enter the name of the first player: ")
name_2 = input("Enter the name of the second player: ")
candies = int(input("Enter the number of candies: "))
player = random.randrange(0, 2)
if player:
    print(f"The player with the name {name_1} goes first")
else:
    print(f"The player with the name {name_2} goes first")
score_1 = 0
score_2 = 0

while candies > 28:
    if player:
        number = player_move(name_1)
        score_1 += number
        candies -= number
        player = not player
        print_result(name_1, number, score_1, candies)
    else:
        number = player_move(name_2)
        score_2 += number
        candies -= number
        player = not player
        print_result(name_2, number, score_2, candies)
if player:
    print(f"The player {name_1} won")
else:
    print(f"The player {name_2} won")

