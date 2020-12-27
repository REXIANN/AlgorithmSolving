def solution(tickets):
    answer = []
    airports = dict()
    for ticket in tickets:
        if airports.get(ticket):
            airports[ticket].append(ticket)
        else:
            airports[ticket] = [ticket]
    return answer