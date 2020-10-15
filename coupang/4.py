from collections import deque

def solution(depar, hub, dest, roads):
    routes = {}
    for road in roads:
        x, y = road[0], road[1]
        if routes.get(x):
            routes[x].append(y)
        else:
            routes[x] = [y]
    # print(routes)
    
    first_count = 0
    dq = deque()
    dq.append(depar)
    while dq:
        start = dq.popleft()

        if not routes.get(start):
            continue
        else:
            for route in routes[start]:
                if route == hub:
                    first_count += 1
                else:
                    dq.append(route)

    second_count = 0
    dq = deque()
    dq.append(hub)
    while dq:
        start = dq.popleft()

        if not routes.get(start):
            continue
        else:
            for route in routes[start]:
                if route == dest:
                    second_count += 1
                else:
                    dq.append(route)

    
    
    answer = first_count * second_count
    answer = answer % 10007
    return answer


depar = 'ULSAN'
hub = 'SEOUL'
dest = 'BUSAN'
roads = [["SEOUL","DAEJEON"],["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","ULSAN"],["DAEJEON","BUSAN"],["GWANGJU","BUSAN"]]
print(solution(depar, hub, dest, roads))