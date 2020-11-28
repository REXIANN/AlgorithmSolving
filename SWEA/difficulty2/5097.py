for tc in range(int(input())):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    print('#{} {}'.format(tc + 1, A[M%N]))