# 6190.py 정곤이의 단조증가

import sys
sys.stdin = open("6190input.txt", "r")

tc = int(input())

for test_count in range(1, tc + 1):
    print('#{} '.format(test_count), end="")
    N_ = int(input())
    num_list = list(map(int, input().split()))
    multiple_list = []
    final_list = []
    target = 0

    for i in range(len(num_list) - 1):
        for j in range(i+1, len(num_list)):
            target = num_list[i] * num_list[j]
            if target > 9:
                multiple_list.append(str(target))

    for string in multiple_list:
        for i in range(1, len(string)):
            if string[i] < string[i - 1]:
                break
        else:
            final_list.append(string)

    if final_list == []:
        print(-1)
    else:
        print(max(list(map(int, final_list))))

