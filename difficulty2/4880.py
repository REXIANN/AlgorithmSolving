# 4880.py 토너먼트 카드게임
import sys
sys.stdin = open("4880input.txt", "r")

def T(begin, end):
    if begin == end:
        return people[begin]
    elif begin + 1 == end:
        return who_win(begin, end)
    else:
        center = (begin + end) // 2
        return who_win(T(begin, center), T(center+1, end))


def who_win(begin, end):
    if people[begin] == people[end]:
        return begin
    elif people[begin] == 1 and people[end] == 3:
        return begin
    elif people[begin] == 3 and people[end] == 1:
        return end
    else:
        return begin if people[begin] > people[end] else end


tc = int(input())
for test_count in range(1, tc + 1):
    N = int(input())
    people = list(map(int, input().split()))
    print('#{} {}'.format(test_count, T(0, len(people) - 1) + 1))
