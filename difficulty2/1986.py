# -*- coding: utf-8 -*-

# 지그재그 숫자

# 1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺄때 최종값 구하기

count = int(input())
numbers = []
for _ in range(count):
    numbers.append(int(input()))
# variables have inserted successfully
# [5, 6]

for idx, number in enumerate(numbers):
    string = list(range(1, number+1))
    final_sum = sum(string[::2]) - sum(string[1::2])
    print('#{0} {1}'.format(idx+1, final_sum))

    # 여기가 끝입니다.