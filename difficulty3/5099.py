# 5099.py 피자굽기
import sys
sys.stdin = open("5099input.txt", "r")

for tc in range(int(input())):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    idx, front = 0, N
    fire = [i for i in range(N)]

    while True:
        C[fire[idx]] //= 2 
        if C[fire[idx]] == 0 and front != len(C):
            fire[idx] = front
            front += 1
            
        if C.count(0) == M - 1: break
        idx = (idx + 1) % N

    for c in C:
        if c != 0:
            print('#{} {}'.format(tc + 1, C.index(c) + 1))

        
