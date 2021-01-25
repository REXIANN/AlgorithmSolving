from queue import PriorityQueue

pq = PriorityQueue(maxsize=2) 

h = [4, 1, 5, 3, 2, 6, 2, 3, 9, 7]

pq.put(4)
pq.put(8)  


print(pq)