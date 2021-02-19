from queue import PriorityQueue

pq = PriorityQueue()

# 쓰레기인 이유 1
pq.put(4)
print(pq)

h = [4, 1, 5, 3, 2, 6, 2, 3, 9, 7]
pqq = PriorityQueue(h) 
print(pqq)
