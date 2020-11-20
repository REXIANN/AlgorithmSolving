from math import ceil
def solution(n,a,b):
    count = 0
    while True:
        aa, bb = ceil(a / 2), ceil(b / 2)
        count += 1
        if aa == bb:
            return count
        a, b = aa, bb