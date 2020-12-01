from collections import deque

def solution(bridge_length, weight, truck_weights):
    count, time = 0, 0
    goal = len(truck_weights)
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    total_weight = 0
    # 빼고
    # 무게 확인해서 올라갈 수 있나 보고
    # 넣고 (0 또는 트럭)
    # 카운트 += 1
    while True:
        out = bridge.popleft()
        if out != 0:
            count += 1
            total_weight -= out
        
        if len(truck_weights) == 0:
            bridge.append(0)
        elif total_weight + truck_weights[0] <= weight:
            truck = truck_weights.popleft()
            bridge.append(truck)
            total_weight += truck
        elif total_weight + truck_weights[0] > weight:
            bridge.append(0)
        
        time += 1
        
        if count == goal:
            return time