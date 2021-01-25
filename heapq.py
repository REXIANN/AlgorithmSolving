import heapq as hq

h = [1, 2, 5, 17, 49, 25, 37, 19, 99]
print('Init ')
print(h)
print()

# make list h heap!
hq.heapify(h)
print('Heapify! ')
print(h)
print()

# put a value 48 into h
hq.heappush(h, 48)
print('Put 48 ')
print(h)
print()

# put another value 1 into h
hq.heappush(h, 1)
print('Put 1 ')
print(h)
print()
