# 1976. 시각 덧셈

import sys
sys.stdin = open("1976input.txt", "r")

# 첫번째 
# 4개의 수가 주어진다. 1,3번째 수는 시, 2,4번째 수는 분을 나타낸다.
# 시각은 12시간제로 시는 1~12, 분은 0~59이하의 값을 가진다.
tc = int(input())

for test_count in range(1, tc+1):
    times = tuple(map(int, input().split()))
    hour, minute = 0, times[1] + times[3]
    hour += 1 if minute > 60 else 0
    minute %= 60
    hour += times[0] + times[2]
    hour %= 12
    if hour == 0:
        hour = 12

    print('#{} {} {}'.format(test_count, hour, minute))