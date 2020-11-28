# -*- coding: utf-8 -*-

# 패턴 마디의 길이

# 각 문자열의 길이는 30, 마디의 최대 길이는 10
# 첫줄에는 테스트케이스의 개수 T, 그 아래로 각 테스트케이스

total_num = int(input())
strings = []
length_list = []

for _ in range(total_num):
    strings.append(input())
# 각 문자열은 스트링으로 리스트에 순차적으로 들어감

for string in strings:
    for i in range(2, 11):
        if string[:i] == string[i:2*i]:
            length_list.append(i)
            break

for i in range(total_num):
    print(f'#{i+1} {length_list[i]}')
