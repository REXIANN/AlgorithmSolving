# -*- coding: utf-8 -*-

# 초심자의 회문 검사

# 각 단어의 길이는 3글자 이상 10글자 이하이다.

count = int(input())
strings = []

for _ in range(count):
    strings.append(input())
# strings have inserted successfully.
# ['level', 'samsung', 'eye']

for idx, string in enumerate(strings):
    # input뒤에 가끔 공백이 붙음. 뒤쪽 공백제거 실행
    string = string.rstrip(' ') 
    for id, char in enumerate(string):
        if char == string[-(id+1)]:
            result = 1
        else:
            result = 0
    print(f'#{idx+1} {result}')