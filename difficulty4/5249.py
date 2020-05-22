# 5249.py 최소 신장 트리
import sys
sys.stdin = open("5249input.txt", "r")

INF = float('inf')
for tc in range(int(input())):
    V, E = map(int, input().split())
    adj = [[0] * (V + 1) for _ in range(V + 1)]
    key = [INF] * V
    p = [-1] * V
    mst = [False] * V
    for i in range(E):
        s, e, c = map(int, input().split())
        adj[s][e] = c
        adj[e][s] = c
    # 시작
    key[0] = 0
    cnt = 0
    while cnt < V:
        min_ = INF
        u = -1
        result = 0
        for i in range(V):
            if not mst[i] and key[i] < min_:
                min_ = key[i]
                u = i
                mst[u] = True
            result += key[i]
            # u 에 인접하고 아직 mst가 아닌 정점 w에서 key[w] > u - w 가중치이면 갱신
            for w in range(V):
                if adj[u][w] > 0 and not mst[w] and key[w] > adj[u][w]:
                    key[w] = adj[u][w]
                    p[w] = u
        
        cnt += 1
    
    print(result)
