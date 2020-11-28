# 1217.py 거듭제곱

import sys
sys.stdin = open("1217input.txt", "r")

tc = 10
def multiple(x, y):
    if y == 1:
        return x
    else:
        y -= 1
        return x * multiple(x, y) 


for test_count in range(1, tc + 1):
    count = int(input())
    x_, y_ = tuple(map(int, input().split()))
    print('#{} {}'.format(test_count,multiple(x_, y_)))