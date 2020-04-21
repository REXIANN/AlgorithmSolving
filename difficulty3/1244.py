# 1244.py 최대 상금
import sys
sys.stdin = open("1244input.txt", "r")

def backtrack(k, N, a):
    if k == N:
        num = int(''.join(map(str, a)))
        global result
        result = num if num > result else result
    else:
        for i in range(0, len(a) - 2, 1):
            for j in range(i + 1, len(a) - 1, 1):
                a[i], a[j] = a[j], a[i]
                backtrack(k + 1, N, a)
                a[j], a[i] = a[i], a[j] 


for tc in range(int(input())):
    N, T = input().split()
    N = [int(i) for i in N]
    result = 0
    backtrack(0, T, N)
    print('#{} {}'.format(tc + 1, result))
    