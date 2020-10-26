def solution(n):
    answer = []
    while n > 0:
        x, y = n // 3, n % 3
        if y == 1:
            answer.append(str(y))
        elif y == 2:
            answer.append(str(y))
        elif y == 0:
            x = x - 1
            y = 3
            answer.append('4')
        n = x
    answer.reverse()
    result = ''.join(answer)
    return result


n = 4
print(solution(n))