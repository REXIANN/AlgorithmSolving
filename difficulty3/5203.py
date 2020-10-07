# 5203.py 베이비진
import sys
sys.stdin = open("5203input.txt", "r")
def win(L):
    L.sort()
    for l in L:
        if L.count(l) == 3:
            return 1
    
    L = list(set(L))
    if len(L) >= 3:
        for i in range(len(L) - 2):
            a, b, c = L[i], L[i + 1], L[i + 2]
            if b - a == 1 and c - b == 1:
                return 1
        else:
            return 0
    return 0

for tc in range(int(input())):
    L = list(map(int, input().split()))
    print('#{}'.format(tc + 1), end=' ')
    p1 = []
    p2 = []
    p1.append(L.pop(0))
    p2.append(L.pop(0))
    p1.append(L.pop(0))
    p2.append(L.pop(0))

    while L:
        p1.append(L.pop(0))
        p2.append(L.pop(0))
        result1 = win(p1)
        if result1: break
        result2 = win(p2)
        if result2: break
    
    if result1 ^ result2:
        print('1' if result1 else '2')
    else:
        print('0')

