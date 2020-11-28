# 9700.py USB꽂기의 미스터리
import sys
sys.stdin = open("9700input.txt", "r")
for tc in range(int(input())):
    p, q = map(float, input().split())
    s1, s2 = (1 - p) * q, p * (1 - q) * q
    print('YES' if s1 < s2 else 'NO')
