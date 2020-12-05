# 19236.py 청소년상어
import copy
import sys
sys.stdin = open('19236input.txt', 'r')

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]

fishes = [0] * 16
fish_dir = [0] * 16
