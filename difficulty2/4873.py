# 4873.py 반복문자 지우기
import sys
sys.stdin = open("4873input.txt", "r")

tc = int(input())

for test_count in range(1, tc + 1):
    string = input()
    stack = [string[0]]

    for i in range(1, len(string)):
        if not stack:
            stack.append(string[i])
            continue

        char = stack.pop(-1)

        if string[i] != char:
            stack.append(char)
            stack.append(string[i])

    print('#{} {}'.format(test_count, len(stack)))