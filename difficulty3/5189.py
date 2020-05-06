# 5189.py 전자카트
from pprint import pprint
from itertools import permutations
import sys
sys.stdin = open("5189input.txt", "r")

for tc in range(int(input())):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    minV = 100 * 10
    for permutation in permutations(range(1, N)):
        result = matrix[0][permutation[0]]
        for i in range(1, len(permutation)):
            result += matrix[permutation[i - 1]][permutation[i]]
        result += matrix[permutation[-1]][0]
        minV = result if result < minV else minV
    print('#{} {}'.format(tc + 1, minV))
