# 1493.py 수의 새로운 연산
import sys
sys.stdin = open("1493input.txt", "r")

def point(val):
    x, idx = 0, 0
    while val > idx:
        x += 1
        idx += x
    diff = abs(idx - val)
    return x - diff, 1 + diff

def location(x, y):
    return sum(range(x + y)) - abs(1 - y)

for tc in range(int(input())):
    p, q = map(int, input().split())
    x1, y1 = point(p)
    x2, y2 = point(q)
    result = location((x1 + x2), (y1 + y2))
    print(result)