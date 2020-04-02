from itertools import combinations
import sys
sys.stdin = open("testinput.txt", "r")
able_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for ables in list(combinations(able_list, 6)):
    for able in list(combinations(ables, 3)):
        print(able)