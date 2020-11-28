# 1945. 간단한 소인수분해

import sys
sys.stdin = open("1945input.txt", "r")

# 숫자 N은 다음과 같다
# N = 2^a x 3^b x 5^c x 7^d x 11^e
# N이 주어질 때 abcde를 출력해라
# N은 2이상 10,000,000 이하이다.


tc = int(input())

for test_count in range(1, tc + 1):
    N_ = int(input())
    dictionary = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0,}
    
    while N_ > 1:
        if N_ % 2 == 0:
            N_ //= 2
            dictionary['a'] += 1

        if N_ % 3 == 0:
            N_ //= 3
            dictionary['b'] += 1

        if N_ % 5 == 0:
            N_ //= 5
            dictionary['c'] += 1

        if N_ % 7 == 0:
            N_ //= 7
            dictionary['d'] += 1

        if N_ % 11 == 0:
            N_ //= 11
            dictionary['e'] += 1

    print('#{}'.format(test_count), end=" ")
    for value in dictionary.values():
        print(value, end=" ")
    print()