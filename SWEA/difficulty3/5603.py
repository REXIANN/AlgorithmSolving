# 5603.py 건초더미

import sys
sys.stdin = open("5603input.txt", "r")

tc = int(input())

for test_count in range(1, tc + 1):
    num_block = int(input())
    blocks = []
    sum_ = 0

    for _ in range(num_block):
        blocks.append(int(input()))

    average = sum(blocks) // len(blocks)

    for block in blocks:
        sum_ += abs(average - block)
    print('#{} {}'.format(test_count, sum_//2))