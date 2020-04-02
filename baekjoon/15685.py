# 15685.py 드래곤 커브
from pprint import pprint
import sys
sys.stdin = open("15685input.txt", "r")

#direction  = 0:Left, 1:Up, 2:Right, 3:Down
r, c, count =[0, -1, 0, 1], [1, 0, -1, 0], 0
M = [[0] * 101 for _ in range(101)]

for i in range(int(input())): #N번 반복하면서 L에 있는거 꺼내다가 드래곤커브 그려야됨
    C, R, D, G = map(int, input().split())
    path = [D]
    M[R][C] = 1

    for j in range(1, G + 1):
        for k in list(reversed(path)):
            path.append((k+1)%4)
        # print(f'{j}th : {path}')
    
    for p in path:
        R, C = R + r[p], C + c[p]
        M[R][C] = 1
    # print(M) # 볼려면 M의 크기를 20으로 줄여야함
    path.clear()

for j in range(100):
    for k in range(100):
        if M[j][k] and M[j+1][k] and M[j][k+1] and M[j+1][k+1]:
            count += 1
print(count)