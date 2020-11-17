from collections import deque

def solution(priorities, location):
    dq = deque(priorities)
    count = 0
    while dq:
        target = dq.popleft()
        if target < max(dq):
            dq.append(target)            
        else:
            count += 1
            if location == 0:
                return count
        location -= 1
        if location < 0:
             location = len(dq) - 1
        print(dq, location, count)

priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))