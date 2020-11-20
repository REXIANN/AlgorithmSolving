from collections import deque

def solution(s):
    answer = 0
    dq = deque([ss for ss in s])
    stack = []
    while dq:
        now = dq.popleft()
        if not stack:
            stack.append(now)
        else:
            prev = stack[-1]
            if prev == now:
                stack.pop()       
            else:
                stack.append(now)

    return 1 if not stack else 0