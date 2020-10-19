# https://programmers.co.kr/learn/courses/30/lessons/42839?language=python3
# 소수찾기 와는 다른 소수찾기 문제로 그냥 뒤에 2 를 붙임
from itertools import permutations

def solution(numbers):
    numbers = [int(i) for i in numbers]
    count = 0
    values = list(set(int(''.join(map(str, permutation))) for i in range(1, len(numbers) + 1) for permutation in permutations(numbers, i)))

    for value in values:
        if value == 1 or value == 0:
            continue
        for i in range(2, value // 2 + 1):
            if value % i == 0:
                break
        else:
            count += 1
    return count


numbers = '17'
print(solution(numbers))
