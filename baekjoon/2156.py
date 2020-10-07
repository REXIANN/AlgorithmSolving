# 2156.py 포도주 시식
import sys
sys.stdin = open('2156input.txt', 'r')

N = int(input())
vins = [int(input()) for _ in range(N)]
vins.extend([0 for _ in range(3 - (N % 3)) if N % 3])
answer = [0, vins[0], vins[0] + vins[1]]

for i in range(2, len(vins)):
    answer.append(
        max(
            answer[-1], 
            answer[-2] + vins[i],
            answer[-3] + vins[i] + vins[i - 1]
        )
    )
print(max(answer[-3:]))
