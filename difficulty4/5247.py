# 5247.py 연산
import sys
sys.stdin = open("5247input.txt", "r")

from collections import deque

for tc in range(int(input())):
    N, M = map(int, input().split())
    array = [0] * 1000001
    array[N] = 1
    dq = deque([N])
    dq_append = dq.append
    while dq:
        target = dq.popleft() 
        value = array[target]
        
        if target == M: break

        if target + 1 < len(array) and not array[target + 1]:
            array[target + 1] = value + 1 
            dq_append(target + 1)
        if target - 1 > 0 and not array[target - 1]:
            array[target - 1] = value + 1
            dq_append(target - 1)
        if target * 2 < len(array) and not array[target * 2]:
            array[target * 2] = value + 1
            dq_append(target * 2)
        if target - 10 > 0 and not array[target - 10]:
            array[target - 10] = value + 1
            dq_append(target - 10)
    print('#{} {}'.format(tc + 1, value - 1))
