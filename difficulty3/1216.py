# 1216.py 회문2

import pprint
import sys
sys.stdin = open("1216input.txt", "r")
# 가장 긴 회문을 찾기

tc= 10 # int(input())

def is_palin(string):
    length = len(string)
    for i in range(length//2):
        if string[i] != string[-1-i]:
            return False
    return True


def first_palindrome(matrix, palindrome):
    palindrome_string = palindrome
    for length_str in range(2, 101):
        for i in range(100 - length_str): # 리스트의 0부터 끝까지
            sample_string = matrix[0][i:i+length_str]
            if is_palin(sample_string) and len(sample_string) >= len(palindrome):
                palindrome_string = sample_string
    return palindrome_string


def second_palindrome(matrix, palindrome):
    
    for i in range(2,100): # 두번째 행부터 시작
        length_palin = len(palindrome)
        for j in range(101 - length_palin): #회문의 시작위치
            for length in range(length_palin, 101):
                sample_string2 = matrix[i][j : j + length]
                if is_palin(sample_string2) and len(sample_string2) >= len(palindrome):
                    palindrome = sample_string2
    return palindrome


for test_count in range(1, tc + 1):
    number = int(input())
    matrix = []
    
    for _ in range(100):
        matrix.append(input())
    #pprint.pprint(matrix)

    zip_matrix = list(map(''.join, zip(*matrix)))

    palind = ''

    palindrome = first_palindrome(matrix, palind)
    palindrome2 = second_palindrome(matrix, palindrome)
    #print(palindrome2, len(palindrome2))
    palindrome3 = first_palindrome(zip_matrix, palindrome2)
    #print(palindrome3, len(palindrome3))
    palindrome4 = second_palindrome(zip_matrix, palindrome3)
    print(palindrome4, len(palindrome4))
    

       # for i in range(2,100): # 두번째 행부터 시작
    #     length_palin = len(palindrome)
    #     for j in range(101 - length_palin): #회문의 시작위치
    #         for length in range(length_palin, 101):
    #             sample_string2 = matrix[i][j : j + length]
    #             if is_palin(sample_string2) and len(sample_string2) >= len(palindrome):
    #                 palindrome = sample_string2
    