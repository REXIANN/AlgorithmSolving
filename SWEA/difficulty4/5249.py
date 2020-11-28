# 5249.py 최소 신장 트리
import sys
sys.stdin = open("5249input.txt", "r")

for tc in range(int(input())):
    V, E = map(int, input().split())
    adj = [[0] * (V + 1) for _ in range(V + 1)]
    INF = float('inf')
    key = [INF] * (V + 1)
    p = [-1] * (V + 1)
    mst = [False] * (V + 1)
    for i in range(E):
        s, e, c = map(int, input().split())
        adj[s][e] = c
        adj[e][s] = c
    # 시작
    key[0] = 0
    cnt = 0
    result = 0
    while cnt < (V + 1):
        min_ = INF
        u = -1
        for i in range(V + 1):
            if not mst[i] and key[i] < min_:
                min_ = key[i]
                u = i
            mst[u] = True
            result += min_
            # u 에 인접하고 아직 mst가 아닌 정점 w에서 key[w] > u - w 가중치이면 갱신
            cnt += 1
            for w in range(V + 1):
                if adj[u][w] > 0 and not mst[w] and key[w] > adj[u][w]:
                    key[w] = adj[u][w]
                    p[w] = u
        
    print(result)
