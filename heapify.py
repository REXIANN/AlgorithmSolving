import heapq

h1 = [1, 2, 3, 4, 5]
heapq.heapify(h1)
print('h1', h1)

h2 = [5, 4, 3, 2, 1]
heapq.heapify(h2)
print('h2', h2)

h3 = [1, 9, 4, 7, 2, 6, 4, 8, 5, 3]
heapq.heapify(h3)
print('h3', h3)

h4 = h3[::-1]
heapq.heapify(h4)
print('h4', h4)