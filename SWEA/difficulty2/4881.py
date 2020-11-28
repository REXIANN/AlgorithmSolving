# 4881.py 최소합
import sys
sys.stdin = open("4881input.txt", "r")

result = []
def back_track(a, k, N, s):
    c = [0] * N
    global asdfk
    if k == N:
        result.append(s)
        print('final', a, s)

    else:
        in_perm = [False] * N
        for i in range(k):
            in_perm[a[i]] = True

        n_candidate = 0
        for i in range(N):
            if not in_perm[i]:
                c[n_candidate] = i
                n_candidate += 1

        for i in range(n_candidate):
            a[k] = c[i]
            if len(result) == 0:
                back_track(a, k + 1, N, s + matrix[k][a[k]])
                print(a, s + matrix[k][a[k]])
            elif s + matrix[k][a[k]] < min(result):
                back_track(a, k + 1, N, s + matrix[k][a[k]])
                print(a, s + matrix[k][a[k]])


tc = int(input())
for test_count in range(1, tc + 1):
    N = int(input())  # 행렬의 행,렬 의 길이
    matrix = [list(map(int, input().split())) for _ in range(N)]
    arr = [0] * N
    back_track(arr, 0, N, 0)
    print('#{} {}'.format(test_count, min(result)))
    result.clear()
