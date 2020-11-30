from collections import deque

def solution(bridge_length, weight, truck_weights):
    count = 0
    total_weight = 0
    length = len(truck_weights)
    arrival = 0
    bridge_weight = 0
    bridge = deque()
    truck_weights = deque(truck_weights)
    
    first_truck = truck_weights.popleft()
    bridge.append(first_truck)
    total_weight += first_truck
    count += 1
    
    while total_weight != 0 or len(bridge) != 0:

        if len(truck_weights) == 0:
            bridge.append(0)
        elif total_weight + truck_weights[0] > weight:
            bridge.append(0)
        
        if len(bridge) > bridge_length:
            out = bridge.popleft()
            if out != 0:
                total_weight -= out
                arrival += 1
            
        if truck_weights and total_weight + truck_weights[0] <= weight:
            truck = truck_weights.popleft()
            bridge.append(truck)
            total_weight += truck
        
        if len(bridge) > bridge_length:
            out = bridge.popleft()
            if out != 0:
                total_weight -= out
                arrival += 1
        
        count += 1
        print(count, bridge, total_weight, truck_weights)
        if arrival == length:
            break

    return count


bridge_length, weight = 2, 10
truck_weights = [7, 4, 5, 6]
print(solution(bridge_length, weight, truck_weights))