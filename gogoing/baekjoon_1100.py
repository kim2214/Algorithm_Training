# A = input()
# B = input()
# C = input()
# D = input()
#
# E = input()
# F = input()
# G = input()
# H = input()
#
board = []
board.append([])

test = "this"

count_1 = 0
count_2 = 1

for i in range(len(test)):
    for y in range(len(test)):
        board[0].append(test[count_1:count_2])
        count_1 += 1
        count_2 += 1

for i in range(len(test)):
    print(test[0][0])

# print(board[0][0])