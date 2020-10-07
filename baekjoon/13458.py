# 13458.py 시험감독

import sys
sys.stdin = open("13458input.txt", "r")

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
count = len(A)
people = [x - B for x in A]

for person in people:
    if person <= 0: continue
    x, y = person // C, person % C
    count += x + 1 if y != 0 else x
print(count)
