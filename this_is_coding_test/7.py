# 7. 럭기 스크레이트
# https://www.acmicpc.net/problem/18406 
import sys
sys.stdin = open('7input.txt', 'r')
N = [int(x) for x in input()]
# left, right = sum(N[:len(N) // 2]), sum(N[len(N) // 2:])
print(sum(N[:len(N) // 2]) == sum(N[len(N) // 2:]) and 'LUCKY' or 'READY')