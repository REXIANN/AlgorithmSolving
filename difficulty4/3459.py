# 3459.py 승자 예측하기
import sys
sys.stdin = open("3459input.txt", "r")

def winning( N, x=1, T=0):
    if x > N:
        print(names[T % 2])
    else:
        winning(N, x * 2, T + 1)
        winning(N, x * 2 + 1, T + 1)

def gazua(N):
    if N == 1: return 'Bob'
    elif N == 2: return 'Alice'
    count = N
    while N > 2:
        count = N 
        N = N - 1 if N % 2 else N // 2
    return 'Bob' if count%2 else 'Alice'
        
for tc in range(int(input())):
    N = int(input()) # 1 <= N <= 10^18
    name = gazua(N)
    print('#{} {}'.format(tc+1, name))