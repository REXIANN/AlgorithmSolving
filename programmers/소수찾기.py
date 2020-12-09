def solution(n):
    answer = 0
    memo = [True] * (n + 1)
    p_num = []
    for i in range(2, n + 1):
        if memo[i]:
            answer += 1
            max_v = (n // i) + 1
            for j in range(2, max_v):
                k = i * j
                if memo[k]: 
                    memo[k] = False
    return answer

n = 5
print(solution(n))
