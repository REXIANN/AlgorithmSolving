# -*- encoding: utf-8 -*-

def solution(S):
    # variables
    a_count = 0
    count = 0
    flag = False
    # check the string
    for s in S:
        if s == 'a':
            a_count += 1
        else:
            count += 2 - a_count
            a_count = 0

        if a_count > 2:
            count = -1
            break

    count += 2 - a_count
    
    return count

print(solution('aba'))
