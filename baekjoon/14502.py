# 14502.py 연구소
from pprint import pprint
import sys
sys.stdin = open("14502input.txt", "r")
# 정답은 1번: 27, 2번: 9, 3번: 3
tc = int(input())
for _ in range(tc):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    print(N, M)
    pprint(matrix)