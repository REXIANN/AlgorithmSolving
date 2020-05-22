import time
z = (1, 2, 3, 6, 5, 9)

a = []
b = []
c = []
d = []
c_append = c.append

start_time = time.time()
for i in range(1000000):
    a.append(i)
print(time.time() - start_time)

start_time = time.time()
for i in range(1000000):
    b += [i]
print(time.time() - start_time)

start_time = time.time()
for i in range(1000000):
    c_append(i)
print(time.time() - start_time)

start_time = time.time()
d = [i for i in range(1000000)]
print(time.time() - start_time)

