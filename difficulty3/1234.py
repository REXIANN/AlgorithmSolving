# 1234.py 비밀번호
import sys
sys.stdin = open("1234input.txt", "r")

tc = 10 #int(input())

def check(str, val=1):
    for i in range(1, len(str)):
        if str[i - 1] == str[i]:
            str = str[:i - 1] + str[i + 1:]
            val = 0
            return str, val

    return str, val


for test_count in range(1, tc + 1):
    length, string_ = input().split()
    string, value = check(string_)
    while value:
        string, value = check(string)
        if value:
            print('#{} {}'.format(test_count, string))

