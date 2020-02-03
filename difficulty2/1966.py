# 1966.py 숫자를 정렬하자

import sys 
sys.stdin = open("1966input.txt", "r")


tc = int(input())

for test_count in range(tc):
    length = int(input())
    num_list = list(map(int, input().split()))
    print('#{} '.format(test_count+1), end="")
    num_list.sort()
    for num in num_list:
        print(num, end=' ')
    print()