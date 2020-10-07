# 4864.py 문자열 비교
import sys
sys.stdin = open("4864input.txt", "r")


tc = int(input())
for test_count in range(1, tc + 1):
    first_str = input()
    second_str = input()
    print(1) if first_str in second_str else print(0)