import time
def fibo(n):
    if n <= 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

memo = [1, 1]
def fibo_m(n):
    if n >= len(memo):
        for i in range(2, n):
            memo.append(memo[i - 1] + memo[i - 2])
    return memo[n - 1]

start = time.time()
print(fibo_m(60))
print(time.time() - start)

start = time.time()
print(fibo(60))
print(time.time() - start)
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 ...
