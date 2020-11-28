# 1859.py 백만장자 프로젝트

import sys
sys.stdin = open("1859input.txt", "r")

# 다음과 같은 조건 하에서 사재기를 하여 최대한의 이득을 얻도록 도와주자.
# 1. 원재는 연속된 N일 동안의 물건의 매매가를 예측하여 알고 있다.
# 2. 당국의 감시망에 걸리지 않기 위해 하루에 최대 1만큼 구입할 수 있다.
# 3. 판매는 얼마든지 할 수 있다.

# 예를 들어 3일 동안의 매매가가 1, 2, 3 이라면
# 처음 두 날에 원료를 구매하여 마지막 날에 팔면 3의 이익을 얻을 수 있다.

# N(2 ≤ N ≤ 1,000,000)이 주어지고,
# 둘째 줄에는 각 날의 매매가를 나타내는 N개의 자연수들이 
# 공백으로 구분되어 순서대로 주어진다.
# 각 날의 매매가는 10,000이하이다

tc = int(input())

for test_count in range(1, tc + 1):
    count = int(input())
    prices = list(map(int, input().split()))
    revenue = 0
    last_value = prices[-1]

    for idx in range(len(prices) -2, -1 ,-1):
        if prices[idx] <= last_value:
            revenue += last_value - prices[idx]
        else:
            last_value = prices[idx]

    print('#{} {}'.format(test_count, revenue))