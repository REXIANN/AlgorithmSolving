def solution(name):
    moves = [ord(i) - 65 if ord(i) - 65 <= 90 - ord(i) else 91 - ord(i) for i in name]

    answer = moves[0]
    moves[0] = 0

    start = 0
    while sum(moves):
        distance = 0
        for i in range(1, len(moves)):
            if moves[start + i] != 0 or moves[start - i] != 0:
                distance = i
                break
            
        if moves[start + distance] != 0:
            answer += moves[start + distance]
            moves[start + distance] = 0
            answer += distance
            start = start + distance
        elif moves[start - distance] != 0:
            answer += moves[start - distance]
            moves[start - distance] = 0
            answer += distance
            start = start - distance
        
    
    return answer


name = 'ABABAAAAAAB'
print(solution(name))