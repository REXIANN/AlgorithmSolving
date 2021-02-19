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
hq.heappush(h, (1, 'hello'))
print('Put 1 ')
print(h)
print()

# pop a value from h
hq.heappop(h)
print('Pop')
print(h)
print()


# nlargest from h
result = hq.nlargest(3, h)
print('result', result)
print('h', h)
print()

# nsmallest from h
result = hq.nsmallest(5, h)
print('result', result)
print('h', h)
print()
