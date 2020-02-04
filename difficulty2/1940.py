# 1940. 가랏! RC카!

import sys
sys.stdin = open("1940input.txt", "r")

# RC카의 이동거리를 계산하려고 한다
# #입력으로 매 초마다 아래와같은 command가 정수로 주어진다.
# 0 : 현재 속도 유지 // 1 : 가속 // 2 : 감속
# 이 중 가속(1) 또는 감속(2)의 경우 가속도의 값이 추가로 주어진다.
# 가속도의 단위는 m/s2이며 모두 양의 정수로 주어진다
# 입력으로 주어진 N개의 command를 모두 수행했을 때, 
# N초동안 디옿나 거리를 계산하는 프로그램을 작성하시오

# N은 2이상 30이하의 정수이다.
# 가속도의 값은 1m/s2 또는 2m/s2이다.
# 현재속도보다 감속할 속도가 더 클경우 속도는 0이 된다.

tc = int(input())

for test_count in range(1, tc + 1):
    # 명령받을 횟수. N이 된다.
    num_command = int(input())
    #print('num_command',num_command)
    velocity_list = []

    def command_input(command_list):
        if len(command_list) == 2:
            if command_list[0] == '1':
               velocity_list.append(int(command_list[1]))
            elif command_list[0] == '2':
               velocity_list.append(int(command_list[1]) * -1)
        else: 
            velocity_list.append(0)
               

    for index in range(num_command):
        command_input(list(input().split()))
    #print('속도', velocity_list)

    # 누적배열 만들기
    sum_ = 0
    velocity_list_acc = []
    for velocity in velocity_list:
        sum_ += velocity
        if sum_ < 0:
            sum_ = 0
        velocity_list_acc.append(sum_)
    #print('누적속도', velocity_list_acc)

    # 최소속도가 0밑으로 내려가지 않게 하면서 누적배열을 더함
    sum_acc = 0
    for velocity_acc in velocity_list_acc:
        sum_acc += velocity_acc
        if sum_acc < 0:
            sum_acc = 0


    print('#{} {}'.format(test_count, sum_acc))
