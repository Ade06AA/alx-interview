#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner


print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
print("Winner: {}".format(isWinner(4, [4, 5, 4, 5])))
print("Winner: {}".format(isWinner(1, [5])))
print("Winner: {}".format(isWinner(1, [4])))
print("Winner: {}".format(isWinner(1, [])))
