from collections import deque

def bfs(depart, airports):
    visited = set()
    trips = [(depart, city) for city in airports[depart]]
    print(trips)

    dq = deque([trips])
    print(dq)

    # while dq:
    #     trip = dq.popleft()
    #     depart = trip[1]
    #     arrives = airports[depart]

    #     for arr in arrives:
    #         if (depart, arr) in visited:
    #             continue
    #         dq.append((depart, arr))



def solution(tickets):
    answer = []
    cities = set([bill for ticket in tickets for bill in ticket])
    airports = dict()
    
    for ticket in tickets:
        if airports.get(ticket[0]):
            airports[ticket[0]].append(ticket[1])
        else:
            airports[ticket[0]] = [ticket[1]]

    for city in cities:
        bfs(city, airports)
    
    
    return answer


tickets = [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]
print(solution(tickets))