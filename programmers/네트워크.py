from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        if visited[i]:
            continue
        else:
            visited[i] = True
            
        dq = deque([j for j in range(len(computers[i])) if computers[i][j]])
        # print(dq)
        while dq:
            v = dq.popleft()
            if v == 0 or v == i:
                continue
            
            if not visited[v]:
                visited[v] = True
                for u in range(len(computers[v])):
                    if computers[v][u] and not visited[u]:
                        dq.append(u)
        
        answer += 1
            
    return answer
