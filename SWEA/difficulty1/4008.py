# 4008.py [모의 SW 역량테스트] 숫자 만들기

import sys
sys.stdin = open("4008input.txt", "r")

oper = '+-*/'
for tc in range(int(input())):
    N = int(input())
    op = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    numbers.reverse()
    
    operands = oper[0] * op[0] + oper[1] * op[1] + oper[2] * op[2] + oper[3] * op[3]
    print(operands, numbers)
