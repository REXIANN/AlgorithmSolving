# 3347.py 올림픽 종목 투표
import sys
sys.stdin = open("3347input.txt", "r")

for tc in range(int(input())):
    map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    I = [0] * len(B)
    for i in B:
        for idx, j in enumerate(A):
            if i >= j: I[idx] += 1; break
    print('#{} {}'.format(tc+1, I.index(max(I)) + 1))