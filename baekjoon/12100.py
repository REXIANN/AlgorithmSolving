# 12100.py 2048(Easy)
import sys
sys.stdin = open("12100input.txt", "r")

N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
print(mat)
