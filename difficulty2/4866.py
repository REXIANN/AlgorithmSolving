# 4866.py 괄호검사
import sys
sys.stdin = open("4866input.txt", "r")

tc = int(input())

for test_count in range(1, tc + 1):
    string = input()
    stack = []
    flag1, flag2 = 0, 0

    for char in string:
        if char == '\'':
            flag1 += 1

        elif (char == '{' or char == '(') and flag1 % 2 == 0:
            stack.append(char)

        elif char == '}' and flag1 % 2 == 0:
            if len(stack) == 0 or stack.pop(-1) != '{':
                flag2 = 1
                break;

        elif char == ')' and flag1 % 2 == 0:
            if len(stack) == 0 or stack.pop(-1) != '(':
                flag2 = 1
                break;

    print('#{} {}'.format(test_count, 0)) if flag2 or len(stack)!= 0 else print('#{} {}'.format(test_count, 1))



