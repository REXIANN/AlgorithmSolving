# 6485.py 삼성시의 버스 노선
import sys
sys.stdin = open("6485input.txt", "r")

for i in range(int(input())):
    a = [0]*5001
    b = [tuple(map(int,input().split())) for _ in range(int(input()))]
    # c = [int(input()) for _ in range(int(input()))]
    for j in range(len(b)):
        for k in range(b[j][0],b[j][1]+1):
            a[k] += 1
    print('#{} {}'.format(i+1,' '.join([str(a[l]) for l in [int(input()) for _ in range(int(input()))]])))

