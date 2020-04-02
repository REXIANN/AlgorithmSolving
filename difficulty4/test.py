def f(i):
    return int(i)//2 + 1 if int(i)%2 else int(i)//2


N, M = map(f, input().split())
print(N, M)
print(f('5'))