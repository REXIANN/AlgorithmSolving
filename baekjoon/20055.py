# 20055.py 컨베이어 벨트 위의 로봇
from collections import deque

N, K = map(int, input().split())
belt = deque([i for i in map(int, input().split())])
robots = deque([False for _ in range(N)])
stage = 1

while True:
    # 1. rotate the belt (and robots)  
    bt = belt.pop()
    belt.appendleft(bt)
    rt = robots.pop()
    robots.appendleft(rt)
    if robots[N - 1]:
        robots[N - 1] = False

    if belt.count(0) >= K:
        break
    
    # 2. move robots if possible
    for i in range(N - 2, 0, -1):
        if robots[i]:
            idx = i + 1
            if not robots[idx] and belt[idx] > 0:
                robots[idx] = True
                robots[i] = False
                belt[idx] -= 1
    
    if robots[N - 1]:
        robots[N - 1] = False

    if belt.count(0) >= K:
        break

    # 3. append a robot
    if belt[0] > 0 and not robots[0]:
        robots[0] = True
        belt[0] -= 1 
    
    if belt.count(0) >= K:
        break
    stage += 1

print(stage)