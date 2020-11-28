# 5658.py 보물상자 비밀번호
import math
import sys
sys.stdin = open("testinput.txt", "r")

for tc in range(int(input())):
    N, K = map(int, input().split())
    X = input()
    X += X[0:N//4]
    L = sorted([int(i,16) for i in list(set(X[i:i+N//4] for i in range(N+1)))])
    print('#{} {}'.format(tc+1,L[len(L)-K]))