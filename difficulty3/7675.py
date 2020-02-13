# 7675.py 통역사 성경이

import sys
sys.stdin = open("7675input.txt", "r")
# 각 문장의 마지막 단어는 '.','?','!' 중 하나가 된다.
# 문장은 대소문자 알파벳과 숫자로 이루어진 단어들이 공백을 두고 구성되어있음
# 이름은 대문자첫글자+나머지는소문자알파벳인 단어
# 대문자 한글자도 이름이다.

tc = int(input())
upper_ = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_ = 'abcdefghijklmnopqrstuvwxyz'
end_ = '.!?'


for test_count in range(1, tc + 1):
    print('#{}'.format(test_count), end=" ")
    number = int(input())
    phrases = input().split()
    count = 0
    print(phrases)
    for phrase in phrases:
        if phrase[0] not in upper_:
            if phrase[-1] in end_:
                print(count, end=" ")
                count = 0
            continue

        if len(phrase) == 1:
            count += 1
            continue

        if phrase[-1] in end_:
            for i in range(1, len(phrase) - 1):
                if phrase[i] not in lower_:
                    print(count, end=" ")
                    count = 0
                    break
            else:
                count += 1
                print(count, end=" ")
                count = 0
        else:
            for i in range(1, len(phrase)):
                if phrase[i] not in lower_:
                    break
            else:
                count += 1

    print()