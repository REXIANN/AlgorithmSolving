import heapq

def solution(scoville, K):
    h = []
    count = 0
    
    for scov in scoville:
        heapq.heappush(h, scov)
    
    head = heapq.heappop(h)
    while head < K:
        
        if not len(h):
            count = -1
            break
        tail = heapq.heappop(h)

        result = head + (tail * 2)
        heapq.heappush(h, result)
        count += 1
        head = heapq.heappop(h)
        
    
    return count