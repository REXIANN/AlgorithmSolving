import time
x, y = 2, 5
N = [1, 2, 3, 4, 5]
def su(N):
    result = 0
    for i in range(len(N)):
        result += N[i] * 10 ** (len(N) - (i + 1))
    return result

a = '12345'
print(list(a))  
# start = time.time()
# for _ in range(1000000):
#     result = min(x, y)
# print(time.time() - start)

# start = time.time()
# for _ in range(1000000):
#     result = x if x > y else y
# print(time.time() - start)

# start = time.time()
# for _ in range(1000000):
#     num = int(''.join(map(str, N)))
# print(time.time() - start)

# start = time.time()
# for _ in range(1000000):
#     num = su(N)
# print(time.time() - start)

print(su(N))
