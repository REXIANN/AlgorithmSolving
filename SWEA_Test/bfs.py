# 가장 기본적인 형태의  BFS
def bfs(G, v, n):
    queue = []
    visited = [0] * n # n: 모든 노드의 개수
    queue.append(v)

    if not visited[v]:
        visited[v] = 1

    while queue:
        t = queue.pop(o)
        for i in G[t]:
            if not visited[i]: 
                visited[i] = 1
                queue.append(i)

 # 내가 생각한 단계별 개수를 저장하는 BFS
def bfs_me(G, v):
    queue = []
    count_list = []
    visited = [0] * n
    queue.append(v)

    if not visited[v]:
        visited[v] = 1

    while queue: 
        t = queue.pop(0)
        count = 0

        for i in G[t]:
            if not visited[i]:
                visited[i] = 1
                count += 1
                queue.append(i)
        count_list.append(count)
        count = 0

# 