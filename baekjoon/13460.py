from pprint import pprint
import sys
sys.stdin = open("13460input.txt", "r")

N, M = map(int, input().split())
matrix = [[char for char in input()] for _ in range(N)]
pprint(matrix)
red_position = [(r, c) for r in range(N) for c in range(M) if matrix[r][c] == 'B']
blue_position = [(r, c) for r in range(N) for c in range(M) if matrix[r][c] == 'R']

