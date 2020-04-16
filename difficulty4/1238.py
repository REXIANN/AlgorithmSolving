# 1238.py contact
from pprint import pprint
import sys
sys.stdin = open("1238input.txt", "r")

def bfs(M, S):
    queue = []
    queue.append(S)
    visited = [0] * 101 
    visited[S] = 1

    while queue:
        t = queue.pop(0)
        for i in M[t]:
            if visited[i] == 0:
                visited[i] = visited[t] + 1
                queue.append(i)

    return visited


for tc in range(1, 11):
    N, S = map(int, input().split())
    M = [[] for _ in range(101)]
    I = list(map(int, input().split()))
    for i in range(0, N, 2):
        r, c = I[i], I[i + 1]
        M[r].append(c)
    results = bfs(M, S)
    
    maxV, maxI = 0, -1
    for index, result in enumerate(results):
        if result >= maxV:
            maxV = result
            maxI = index
    print('#{} {}'.format(tc, maxI))

    

