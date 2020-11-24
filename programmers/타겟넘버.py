from collections import deque

def solution(numbers, target):
    dq = deque([0])
    if sum(numbers) == target:
        return 1
    
    outer_count = 1
    for number in numbers:
        
        inner_count = 0
        while outer_count > 0:
            value = dq.popleft()
            dq.append(value + number)
            dq.append(value - number)
            inner_count += 2
            outer_count -= 1
            #print(dq)
        outer_count = inner_count
    
    
    return dq.count(target)