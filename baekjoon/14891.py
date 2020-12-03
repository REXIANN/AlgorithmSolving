from collections import deque
import sys

sys.stdin = open('14891input.txt', 'r')
first = deque(list(map(int, input().split())))
second = deque(list(map(int, input().split())))
third = deque(list(map(int, input().split())))
fourth = deque(list(map(int, input().split())))

print(first, second, third, fourth)
for i in range(int(input())):
    asdf = input()
    print(asdf)
