# 1486.py 장훈이의 높은 선반
import sys
sys.stdin = open("1486input.txt", "r")

def backtrack(a, k, N, s):
    c = [0] * N
    if s > B and maxnums[0] > s:
        maxnums[0] = s
        return 

    if k == N:
        return 
    else:
        in_perm = [False] * N
        for i in range(k):
            in_perm[a[i]] = True
        
        n_candid = 0
        for i in range(N):
            if in_perm[i] == False:
                c[n_candid] = i
                n_candid += 1

        for i in range(n_candid):
            a[k] = c[i]
            backtrack(a, k+1, N, s+H[a[k]])
            # if maxnums: 
            #     if s + H[a[k]] < maxnums[0]:
            #         backtrack(a, k+1, N, s + H[a[k]])
            #     elif s >= B and maxnums[0] >= s:
            #         maxnums[0] = s
            # else:
            #     backtrack(a, k+1, N, s + H[a[k]])    

for tc in range(int(input())):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    # print(N, B, H)
    
    maxnums = [sum(H)]
    backtrack([0] * len(H), 0, len(H), 0)
    print('#{} {}'.format(tc+1, maxnums[0] - B))

