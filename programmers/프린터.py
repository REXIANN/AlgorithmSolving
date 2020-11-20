from collections import deque

def solution(priorities, location):
    dq = deque(priorities)
    count = 0
    while True:
        target = dq.popleft()
        if dq and target < max(dq):
            dq.append(target)            
        else:
            count += 1
            if location == 0:
                return count
        location -= 1
        if location < 0:
             location = len(dq) - 1

priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))