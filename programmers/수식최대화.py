from itertools import permutations

def calc(experssion, operand):
    stack = []


def solution(expression):
    answer = []
    head, tail = 0, 0
    while head < len(expression):
        if expression[head] in "+-*":
            answer.append(int(expression[tail: head]))
            answer.append(expression[head])
            head, tail = head + 1, head + 1
        else:
            head += 1
    
    answer.append(int(expression[tail:head]))
    for permutation in permutations('+-*'):
        print(permutation)
    
    return answer


expression = "100-200*300-500+20"
print(solution(expression))