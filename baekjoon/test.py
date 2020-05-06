# from itertools import combinations
# import sys
# sys.stdin = open("testinput.txt", "r")
# able_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for ables in list(combinations(able_list, 6)):
#     for able in list(combinations(ables, 3)):
#         print(able)

def dfs(M, a, k):
    if k == len(M):
        print()
    else:
        for i in range(3):
            num = M[k][i]
            M[k][i] = 0
            if k == 2: print(M)
            dfs(M, a, k + 1)
            M[k][i] = num

M = [
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
]

s = [0, 0, 0]
dfs(M, s, 0)