# -*- encoding: utf-8 -*-

def solution(A):
    comp = [i for i in range(1, len(A) + 1)]
    A.sort()
    result = [abs(A[i] - comp[i]) for i in range(len(comp))]
    return sum(result) if sum(result) <= 1000000000 else -1

a = [1] * 200000
print(solution(a))

