# 4613.py 러시아 국기 같은 깃발
import sys
sys.stdin = open("4613input.txt", "r")

for tc in range(int(input())):
    R, C = map(int, input().split())
    flag = [input() for _ in range(R)]
    points = [(i, j) for i in range(1, R -1) for j in range(1, R - i)]
    maxV = 0
    for i, j in points:
        count = 0
        for w in range(j): count += flag[w].count('W')
        for b in range(j, j + i): count += flag[b].count('B')
        for r in range(j + i, R): count += flag[r].count('R')
        maxV = count if count > maxV else maxV
    print('#{} {}'.format(tc+1, R * C - maxV))  