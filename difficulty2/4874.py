# 4874.py Forth
import sys
sys.stdin = open("4874input.txt", "r")

numbers = '0123456789'
operands = '+-*/'
def my_pop(num1, num2, op):
    if op == '+':
        return int(num1) + int(num2)
    elif op == '-':
        return int(num1) - int(num2)
    elif op == '*':
        return int(num1) * int(num2)
    elif op == '/':
        return int(int(num1) / int(num2))

tc = int(input())

for test_count in range(1, tc + 1):
    equation = input().split()
    print(equation)

    flag = 0
    idx = 0
    char = 'x'

    while char != '.':
        char = equation[idx]
        if char in operands:
            if idx - 2 < 0:
                flag = 1
                break

            operand = equation.pop(idx)
            num2 = equation.pop(idx - 1)
            num1 = equation.pop(idx - 2)
            if operand not in operands:
                flag = 1
                break
            if not num2.isdecimal():
                flag = 1
                break
            if not num1.isdecimal():
                flag = 1
                break

            result = my_pop(num1, num2, operand)
            equation.insert(idx - 2, str(result))
            idx = idx - 2
            print(equation)

        idx += 1
    final = equation[0] if flag == 0 and len(equation) == 2 and equation[-1] == '.' else 'error'
    print(final)