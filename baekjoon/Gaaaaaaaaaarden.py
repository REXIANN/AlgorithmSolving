# Gaaaaaaaaaarden.py 백준 모의고사
from itertools import combinations
import copy
import time
import sys
sys.stdin = open("gardeninput.txt", "r")

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
start_time = time.time()
R, C, green, red = map(int, input().split())
M = [list(map(int, input().split())) for _ in range(R)]
# print(R, C, green, red)
# for _ in range(R): print(M[_])
able_list = [(i, j) for i in range(R) for j in range(C) if M[i][j] == 2]
# print(able)
for i in range(R):
    for j in range(C):
        if M[i][j] == 2:
            M[i][j] = 1
count_max = -1
# print(able_list[1])
# print()

for ables in list(combinations(able_list, green + red)):
    for able in list(combinations(ables, green)):
        MM = copy.deepcopy(M)
        MMM = [[0]* C for _ in range(R)]
        for i in range(green):
            MM[able[i][0]][able[i][1]] = 3
        for i in range(len(ables)):
            if ables[i] not in able:
                MM[ables[i][0]][ables[i][1]] = 4        
        # for _ in range(R): print(MM[_])
        # print()
        one_count = 0
        for r in range(R):
            for c in range(C):
                if MM[r][c] == 1:
                    one_count += 1

        flag, count = 1, 0
        while flag != 0:
            flag = 0
            if one_count + count < count_max: 
                break

            for r in range(R):
                for c in range(C):
                    if MM[r][c] > 1:
                        for i in range(4):
                            if 0 <= r + dr[i] < R and 0 <= c + dc[i] < C and MM[r + dr[i]][c + dc[i]] == 1:
                                MMM[r + dr[i]][c + dc[i]] += MM[r][c]
                                flag += 1

            for r in range(R):
                for c in range(C):
                    if MMM[r][c] != 0:
                        one_count = one_count - 1
                        if MMM[r][c] % 3 == 0:
                            MMM[r][c] = 0
                            MM[r][c] = 3
                        elif MMM[r][c] % 4 == 0:
                            MMM[r][c] = 0
                            MM[r][c] = 4
                        else:
                            MMM[r][c] = 0
                            MM[r][c] = 0
                            count += 1
        # print('count', count) 
        # print()     
        count_max = count if count > count_max else count_max
        
print(count_max, time.time() - start_time)



    