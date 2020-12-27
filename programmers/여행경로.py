def solution(tickets):
    answer = []
    airports = dict()
    for ticket in tickets:
        if airports.get(ticket[0]):
            airports[ticket[0]].append(ticket[1])
        else:
            airports[ticket[0]] = [ticket[1]]

    print(airports)

    return answer


tickets = [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]
print(solution(tickets))