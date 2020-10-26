# 20056.py 마법사 상어와 파이어볼
import copy

dr = [-1, -1, 0, 1, 1,  1,  0, -1]
dc = [ 0,  1, 1, 1, 0, -1, -1, -1]

N, M ,K = map(int, input().split())
matrix = [[[] for _ in range(N)] for __ in range(N)]
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    matrix[r - 1][c - 1].append([m, s, d])

# for i in range(N):
#     print(matrix[i])
# print('---------')

while K > 0:
    new_mat = [[[] for _ in range(N)] for __ in range(N)]
    for r in range(N):
        for c in range(N):
            point = matrix[r][c]
            while point:
                arg = point.pop()
                m, s, d = arg[0], arg[1], arg[2]
                rr, cc = r + dr[d] * s, c + dc[d] * s
                if rr >= N:
                    rr = rr % N
                elif rr < 0:
                    rr = (rr + N) % N
                
                if cc >= N:
                    cc = cc % N
                elif cc < 0:
                    cc = (cc + N) % N
                
                new_mat[rr][cc].append([m, s, d])
    
    matrix = copy.deepcopy(new_mat)
    
    # for i in range(N):
    #     print(matrix[i])     
    # print()

    for r in range(N):
        for c in range(N): 
            fireballs = matrix[r][c]
            if len(fireballs) >= 2:
                # print(fireballs)
                M, S, D = 0, 0, []
                for fireball in fireballs:
                    mm, ss, dd = fireball[0], fireball[1], fireball[2]
                    M, S = M + mm, S + ss
                    D.append(True if dd % 2 else False) 
                flag = D[0]
                for d in D:
                    if flag != d:
                        D = [1, 3, 5, 7]
                        break
                else:
                    D = [0, 2, 4, 6]
                
                
                M = M // 5
                S = S // len(fireballs)
                # print(M, S, D)
                matrix[r][c]  = [[M, S, i] for i in D]
    
    # for i in range(N):
    #     print(matrix[i])  
    # print()

    for r in range(N):
        for c in range(N): 
            if matrix[r][c]:
                matrix[r][c] = list(filter(lambda x : x[0] != 0, matrix[r][c]))
                
    # for i in range(N):
    #     print(matrix[i])  
    # print()
                        
    K -= 1

total = 0
for r in range(N):
    for c in range(N):
        if matrix[r][c]:
            args = matrix[r][c]
            for arg in args:
                total += arg[0]
print(total)