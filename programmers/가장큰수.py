def solution(numbers):
    numbers = sorted(list(map(str, numbers)), reverse=True)
    return numbers


numbers = [3, 30, 34, 5, 9]
print(solution(numbers))
