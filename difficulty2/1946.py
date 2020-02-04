# 1946. 간단한 압축풀기

import sys
sys.stdin = open("1946input.txt", "r")

# 원본문서는 너비가 10인 여러줄의 문자열로 이루어져 있다.
# 문자열은 마지막줄을 제외하고 빈공간없이 알파벳으로 채워져있다
# 마지막줄은 왼쪽부터 채워져 있다
# 이 문서를 압축한 문서는 알파벳과 그 알파벳의 연속된 개수로 이루어진 쌍들이 나열되어 있다.
# 압축된 문서를 입력받아 원본문서를 만드는 프로그램을 작성하시오

tc = int(input())

for test_count in range(1, tc + 1):
    char_count = int(input())
    result = ''
    
    for _ in range(char_count):
        char, count = tuple(input().split())
        result += char * int(count)

    print('#{} {:<10}'.format(test_count, result))

    