def dfs(depart, airports, ticket_count):
    stack = [[depart, city] for city in airports[depart]]
    result = []
    print()
    print('stack', stack)
    print()
    
    while stack:
        visited = set()
        trip = stack.pop()
        flag = True
        print()
        print('first trip', trip)
        print()
        visited.add((trip[0], trip[1]))
        
        while flag:
            depart = trip[-1]
            if airports.get(depart):
                arrives = airports[depart]
            else:
                break
            print('visit', visited)
            print('trip', trip)
            for arrive in arrives:
                if (depart, arrive) not in visited:
                    visited.add((depart, arrive))
                    trip.append(arrive)
                    break
            else: 
                break

            if len(trip) == ticket_count + 1:
                result.append(trip)         
    
    return result
                       

def solution(tickets):
    answer = []
    cities = set([bill for ticket in tickets for bill in ticket])
    ticket_count = len(tickets)
    airports = dict()
    results = []
    for ticket in tickets:
        if airports.get(ticket[0]):
            airports[ticket[0]].append(ticket[1])
        else:
            airports[ticket[0]] = [ticket[1]]

    result = dfs('ICN', airports, ticket_count)
    results.extend(result)
    print('result', result)

    print(results)
    results = [result for result in results if result]
    results.sort()
    print(results)

    return results[0]


tickets = [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]
tickets = [['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]
tickets = [["ICN", 'A'], ['ICN', 'B'], ['B', 'ICN']]
print(solution(tickets))