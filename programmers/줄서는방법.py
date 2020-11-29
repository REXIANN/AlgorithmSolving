from itertools import product

def solution(n, k):
    answer = []
    s = [(i for i in range(1, n + 1)) for _ in range(n)]
    p = list(product(*s))
    return p


n, k = 3, 5
print(solution(n, k))