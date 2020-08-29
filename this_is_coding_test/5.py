# 5. 볼링공 고르기
N, M = map(int, input().split())
L = list(map(int, input().split()))
count = [1 for i in range(0, len(L) - 1) for j in range(i + 1, len(L)) if L[i] != L[j]]
print(count)