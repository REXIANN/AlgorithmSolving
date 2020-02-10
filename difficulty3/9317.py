# 9317.py 석찬이의 받아쓰기

import sys 
sys.stdin = open("9317input.txt", "r")

tc= int(input())

for test_count in range(1, tc + 1):
    len_string = int(input())
    original_string = input()
    users_string = input()
    count = 0

    for idx, users in enumerate(users_string):
        if users == original_string[idx]:
            count += 1

    print('#{} {}'.format(test_count, count))