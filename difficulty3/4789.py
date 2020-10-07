# 4789.py 성공적인 공연 기획
import sys
sys.stdin = open("4789input.txt", "r")

for tc in range(int(input())):
    people = input()
    idx = 1
    applause, support = int(people[0]), 0
    while idx < len(people):
        if applause < idx:
            support += idx - applause
            applause = idx
        applause += int(people[idx])
        idx += 1
    print('#{} {}'.format(tc + 1, support))