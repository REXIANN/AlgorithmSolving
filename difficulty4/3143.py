# 3143.py 세상에서 가장 빠른 문자열 타이핑
import sys
sys.stdin = open("3143input.txt", "r")

for tc in range(int(input())):
    A, B = input().split()
    C = A.count(B)
    print('#{} {}'.format(tc + 1, len(A) - len(B) * C + C))
    # count = 0
    # idx = 0
    # b = B[0]
    # while idx < len(A):
    #     if A[idx] == b:
    #         if A[idx : idx + len(B)] == B:
    #             count += 1
    #             idx += len(B)
    #     else:
    #         count += 1
    #         idx += 1
    # print('#{} {}'.format(tc + 1, count))