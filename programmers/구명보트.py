def solution(people, limit):
    if len(people) == 1:
        return 1

    tail, count = 0, 0
    while tail < len(people):
        total = people[tail]
        head = tail
        while head + 1 < len(people) and total + people[head + 1] <= limit:
            total += people[head]
            head += 1
            
        count += 1
        tail = head + 1 
    return count


people = [70, 50, 80, 50]
limit = 100
print(solution(people, limit))