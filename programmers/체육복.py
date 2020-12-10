def solution(n, lost, reserve):
    students = [1] * (n + 1)
    
    for los in lost:
        students[los] -= 1
    
    for res in reserve:
        students[res] += 1

    first_students = students[:]
    for i in range(1, n + 1):
        if first_students[i] == 2:
            if i - 1 >= 0 and first_students[i - 1] == 0:
                first_students[i - 1] = 1
                first_students[i] = 1
            elif i + 1 < n and first_students[i + 1] == 0:
                first_students[i + 1] = 1
                first_students[i] = 1
    first_value = sum([1 for student in first_students[1:] if student])
    
    second_students = students[:]
    for i in range(1, n + 1):
        if second_students[i] == 2:
            if i + 1 < n and second_students[i + 1] == 0:
                second_students[i + 1] = 1
                second_students[i] = 1
            elif i - 1 >= 0 and second_students[i - 1] == 0:
                second_students[i - 1] = 1
                second_students[i] = 1
            
    second_value = sum([1 for student in second_students[1:] if student])

    return max(first_value, second_value)