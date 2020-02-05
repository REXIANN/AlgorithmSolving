# 1284.py 수도 요금 경쟁

import sys
sys.stdin = open("1284input.txt", "r")

# 종민이는 두 수도회사 중 하나를 선택하여 수도를 사용할 수 있다
# A사 : 1리터당 P원의 돈을 내야 한다.
# B사 : 기본 요금이 Q원이고, 월간 사용량이 R리터 이하인 경우 요금은 기본 요금만 청구된다. 
# 하지만 R 리터보다 많은 양을 사용한 경우 초과량에 대해 1리터당 S원의 요금을 더 내야 한다.
# 종민이가 한달에 사용하는 양은 W라고 가정한다
# 각 테스트 케이스마다 첫 번째 줄에 위 본문에서 설명한 대로 
# P, Q, R, S, W  (1 ≤ P, Q, R, S, W ≤ 10000, 자연수)가 순서대로 공백 하나로 구분되어 주어진다.

tc = int(input())

for test_count in range(1, tc + 1):
    print('#{}'.format(test_count), end=" ")
    P, Q, R, S, W = tuple(map(int, input().split()))
    #print(P, Q, R, S, W)

    # A회사 수도요금 고지서
    bill_a = P * W

    # B회사 수도요금 고지서
    bill_b = Q if (W - R) < 0 else Q + (W - R) * S

    print(bill_a if bill_a < bill_b else bill_b)
