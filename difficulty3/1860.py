# 1860.py 진기의 최고급 붕어빵
import sys
sys.stdin = open("1860input.txt", "r")

for tc in range(int(input())):
    N, M, K = map(int, input().split())
    plist = [0] * 11112
    for person in list(map(int, input().split())):
        plist[person] += 1
    print('#{} '.format(tc + 1), end='')

    fish, client = 0, 0
    for idx, value in enumerate(plist):
        if idx <= 1:
            if value == 0:
                continue
            else:
                print("Impossible")
                break
            
        if idx % M == 0:
            fish += K
        fish -= value

        if fish < 0:
            print("Impossible")
            break
    else:
        print('Possible')