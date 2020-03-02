def backtrack(a, k, N, s):
    if s > 10: return 

    if k == N:
        if s == 10:
            for i in range(N):
                if a[i]:print(S[i], end=' ')
            print()
    else:
        a[k] = 0
        backtrack(a, k+1, N, s)
        if s+S[k] <= 10:
            backtrack(a, k+1, N, s+S[k])

a = [0] * 10
S = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
backtrack(a, 0, 10, 0)

