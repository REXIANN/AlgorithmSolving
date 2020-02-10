# 4865.py 글자수
import sys
sys.stdin = open("4865input.txt", "r")
tc = int(input())

for test_count in range(1, tc + 1):
    first_str = input()
    second_str = input()
    string_dict = {}
    for char in first_str:
        string_dict[char] = 0
    
    for char in second_str:
        if string_dict.get(char) != None:
            string_dict[char] += 1

    print('#{} {}'.format(test_count, max(string_dict.values())))