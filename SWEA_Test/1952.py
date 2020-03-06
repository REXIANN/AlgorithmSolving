# 1952.py 수영장

import sys
sys.stdin = open("1952input.txt", "r")

def swim(k, s, d, m, m3):
    global minV
    if k >= 13:
        minV = s if minV > s else minV
    elif minV < s:
        return
    else:
        swim(k+1, s + min(d*months[k], m), d, m, m3)
        swim(k+3, s + m3, d, m, m3)


for tc in range(int(input())):
    d, m, m3, y = map(int, input().split())
    months = [0] + list(map(int, input().split()))
    minV = y
    swim(1, 0, d, m, m3)
    print('#{} {}'.format(tc+1, minV))