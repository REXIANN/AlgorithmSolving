# -*- coding: utf-8 -*-

# 중간 평균값 구하기

# 10개의 수를 입력받아 최대수와 최소수를 제외한 나머지의 평균값을 출력
# 각 수는 0이상 10000이하의 정수이다


count = int(input())

strings = []
for i in range(count):
    strings.append(input().rstrip(' ').split(' '))
    for idx, char in enumerate(strings[i]):
        strings[i][idx] = int(char)

# variables have inserted successfully
# [['3', '17', '1', '39', '8', '41', '2', '32', '99', '2'],
#  ['22', '8', '5', '123', '7', '2', '63', '7', '3', '46'],
#  ['6', '63', '2', '3', '58', '76', '21', '33', '8', '1']]

for idx, string in enumerate(strings):
    string.remove(max(string))
    string.remove(min(string))
   
    print('#{0} {1}'.format(idx+1, round(sum(string)/len(string))))