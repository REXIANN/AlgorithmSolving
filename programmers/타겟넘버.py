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


# 데카르트곱을 활용한 풀이
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    print(l)
    s = list(map(sum, product(*l)))
    return s.count(target)