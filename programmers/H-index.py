def solution(citations):
    citations.sort(reverse=True)
    max_value = citations[0]

    while max_value >= 0:
        count = 0
        for i in citations:
            if i >= max_value:
                count += 1
            
        if count >= max_value and len(citations) - count <= max_value:
            count = 0
            return max_value
                
        max_value -= 1


citations = [5, 5, 5, 5]
print(solution(citations))
