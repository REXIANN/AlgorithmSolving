def solution(numbers):
    return sorted(list(set([numbers[i] + numbers[j] for i in range(len(numbers) - 1) for j in range(i + 1, len(numbers))])))