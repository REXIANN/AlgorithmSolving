import time
from itertools import permutations
a = [0, 1, 2, 3, 4, 5, 6, 7, 8]
b = [0] * len(a)
def dfs(k, N):
    if k == N:
        return
    else:
        for i in range(k):
            visited[b[i]] = True
        
        for i in range(N):
            if not visited[i]:
                b[k] = i
                dfs(k + 1, N)
                visited[b[k]] = False
                


visited  = [False] * len(a)

start_time = time.time()
for i in permutations(a):
    pass
print(time.time() - start_time)

start_time = time.time()
dfs(0, len(a))
print(time.time() - start_time)



