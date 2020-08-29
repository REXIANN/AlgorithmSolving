# 01. 모험가 길드
import sys
sys.stdin = open("1input.txt", "r")
N = int(input())
L = [0]  * (N + 1)
esc = 0
count = 0
for i in input().split():
    L[int(i)] += 1
for i in range(1, N + 1):
    e, v = L[i] // i, L[i] % i
    if i != N:
        L[i + 1] += v
    count += e
print(count)