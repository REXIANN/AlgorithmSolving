# 1221.py GNS

import sys
sys.stdin = open("1221input.txt", "r")

# 숫자 체계가 우리와 다른 어느 행성이 있다. 아래는 이 행성에서 사용하는 0 ~ 9의 값을 순서대로 나타낸 것이다.
# "ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"
# 0 ~ 9 의 값을 나타내는 단어가 섞여 있는 문자열을 받아 작은 수부터 차례로 정렬하여 출력하는 프로그램을 작성하라.

tc = int(input())

for test_count in range(1, tc + 1):
    print('#' + str(test_count))
    number, length = input().split()
    input_string = list(input().split())
    word_dict = {"ZRO": 0, "ONE": 0, "TWO": 0, "THR": 0, "FOR": 0, "FIV": 0, "SIX": 0, "SVN": 0, "EGT": 0, "NIN": 0}
    for word in input_string:
        word_dict[word] += 1

    for word, value in word_dict.items():
        print((word + ' ') * value, end=" ")
        print()

