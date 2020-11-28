# 5102.py 노드의 거리
from pprint import pprint
import sys
sys.stdin = open("5102input.txt", "r")

def bfs(M, V, S):
    queue = []
    visited = [0] * (V + 1)
    visited[S] = 1
    queue.append(S)

    while queue:
        t = queue.pop(0)
        
        for value in M[t]: 
            if visited[value] == 0:
                visited[value] = visited[t] + 1
                queue.append(value)
    return visited


for tc in range(int(input())):
    V, E = map(int, input().split())
    M = [[] for _ in range(V + 1)]
    for _ in range(E):
        i, j = map(int, input().split())
        M[i].append(j)
        M[j].append(i)

    S, G = map(int, input().split())
    result = bfs(M, V, S)
    print('#{} {}'.format(tc + 1, result[G] - result[S]))
    