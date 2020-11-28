# 3499.py 퍼펙트 셔플
import sys
sys.stdin = open("3499input.txt", "r")

for tc in range(int(input())):
    N = int(input())
    L = input().split()
    M = N//2 if not N%2 else N//2 + 1
    X, Y = L[:M], L[M:]
    print('#{} '.format(tc+1), end='')
    for i in range(N):
        print(X.pop(0), end=' ') if not i%2 else print(Y.pop(0), end=' ')
    print()
        