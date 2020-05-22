# 5207.py 이진탐색
import sys
sys.stdin = open("5207input.txt", "r")

for tc in range(int(input())):
    N, M = map(int, input().split())
    n_list = list(sorted(list(map(int, input().split()))))
    m_list = list(map(int, input().split()))
    count = 0
    for m in m_list:
        head = 0
        left_flag = 0
        right_flag = 0
        tail = len(n_list) - 1
        while True:
            middle =  (head + tail) // 2
            if m == n_list[middle]:
                count += 1
                break
            elif m > n_list[middle]:
                head = middle + 1
                right_flag += 1
                if right_flag == 2:
                    break
                else:
                    left_flag = 0        
            elif m < n_list[middle]:
                tail = middle - 1
                left_flag += 1
                if left_flag == 2:
                    break
                else:
                    right_flag = 0

    print('#{} {}'.format(tc + 1, count))
