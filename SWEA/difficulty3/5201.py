# 5201.py 컨테이너 운반
import sys
sys.stdin = open("5201input.txt", "r")

for tc in range(int(input())):
    N, M = map(int, input().split())
    W = list(map(int, input().split()))
    T = list(map(int, input().split()))
    W.sort(reverse=True)
    T.sort(reverse=True)
    load = 0
    idx = 0
    for w in W:
        if idx == len(T):
            break
        if w <= T[idx]:
            load += w
            idx += 1

    print('#{} {}'.format(tc + 1, load))

    
