# 3190.py 뱀
from pprint import pprint
import sys
sys.stdin = open("3190input.txt", "r")

global dir
dir = 1
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def head(x1, y1, N):
    x2, y2 = x1 + dr[dir], y1 + dc[dir]
    if 0 <= x2 < N and 0 <= y2 < N: 
        snake.append((x2, y2))
        if M[x2][y2] == 1: 
            return -1, -1
        elif M[x2][y2] == 2:    
            M[x2][y2] = 1
        else:
            M[x2][y2] = 1
            x1, y1 = snake.pop(0)
            M[x1][y1] = 0
        return x2, y2
    else:
        return -1, -1


N = int(input())
M = [[0] * N for _ in range(N)]
for i in range(int(input())):
    x, y = map(int, input().split())
    M[x - 1][y - 1] = 2
L = []
for _ in range(int(input())):
    x, y = input().split()
    L.append(int(x))
    L.append(y)

for i in range(len(L) - 2, 0, -2):
    L[i] = L[i] - L[i - 2]
L.append(N)
# print(N, L)
# pprint(M)

x1, y1 = 0, 0
M[x1][y1] = 1
snake = [(x1, y1)]
count = 0

for l in L:
    if l == 'D' or l == 'L':
        dir = dir + 1 if l == 'D' else dir - 1
        dir %= 4
    else:
        for i in range(l):
            x1, y1 = head(x1, y1, N)
            count += 1
    
            if x1 == -1 and y1 == -1:
                break    
    if x1 == -1 and y1 == -1:
        break    
    
print(count)