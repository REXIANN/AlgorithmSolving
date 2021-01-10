def solution(a, b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    index = 5
    answer = sum(months[:a - 1]) + b
    answer = answer + 4
    answer = answer % 7
    return days[answer]