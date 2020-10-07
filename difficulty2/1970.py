# 1970. 쉬운 거스름돈

import sys
sys.stdin = open("1970input.txt", "r")

# 손님에게 거슬러주어야할 금액 N이 입력되면
# 돈의 최소 개수로 거슬러주기 위해 필요한 각 종류의 돈의 개수
# 금액 N은 10이상 1000000이하의 정수
# N의 마지막 자릿수는 항상 0이다. 10원이하는 버린다.

# N이 32850일 경우,
# 50,000 원 : 0개
# 10,000 원 : 3개
# 5,000 원 : 0개
# 1,000 원 : 2개
# 500 원 : 1개
# 100 원 : 3개
# 50 원 : 1개
# 10 원 : 0개

tc = int(input())

for test_count in range(1, tc+1):
    b_50000, b_10000, b_5000, b_1000,  = 0, 0, 0, 0
    b_500, b_100, b_50, b_10 = 0, 0, 0, 0

    money = int(input())

    if money >= 50000:
        b_50000 = money // 50000    
        money %= 50000

    if money >= 10000:
        b_10000 = money // 10000    
        money %= 10000
    
    if money >= 5000:
        b_5000 = money // 5000    
        money %= 5000

    if money >= 1000:
        b_1000 = money // 1000    
        money %= 1000

    if money >= 500:
        b_500 = money // 500    
        money %= 500

    if money >= 100:
        b_100 = money // 100    
        money %= 100

    if money >= 50:
        b_50 = money // 50    
        money %= 50

    if money >= 10:
        b_10 = money // 10    
        money %= 10
    
    print('#',test_count)
    print(b_50000, b_10000, b_5000, b_1000,b_500, b_100, b_50, b_10)

    