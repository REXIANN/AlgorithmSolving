# 2806.py N-Queen
import sys
sys.stdin = open("2806input.txt", "r")
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

def queen(arr, N):
    if len(arr) == N:
        global count
        count += 1
    else:
        for char in arr:
            
  

for tc in range(int(input())):
    N = int(input())
    visited = [[False] * N for _ in range(N)]
    count = 0
    for i in range(N):
        queen([i], N)
    print(count)