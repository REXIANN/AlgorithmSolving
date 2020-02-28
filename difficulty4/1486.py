# 1486.py 장훈이의 높은 선반
import sys
sys.stdin = open("1486input.txt", "r")

flag = 0
def backtrack(H, a, k, N, maxnum, s):

    if k == N:
        
        if s > B and maxnum > s: 
            maxnum = s 
        print(a, 'sum=', sum(a))
    
    else:
        c = [0] * N
        
        in_perm = [False] * N
        for i in range(k):
            in_perm[i] = True
        
        n_candid = 0
        for i in range(N):
            if in_perm[i] == False:
                c[n_candid] = i
                n_candid += 1

        for i in range(n_candid):
            a[k] = c[i]
            if s + H[a[k]] < maxnum:
                backtrack(H, a, k+1, N, maxnum, s + H[a[k]])
            else:
                print(s + H[a[k]])
        

for tc in range(int(input())):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    print(N, B, H)
    a = [0] * len(H)
    backtrack(H, a, 0, sum(H), len(H), 0)

