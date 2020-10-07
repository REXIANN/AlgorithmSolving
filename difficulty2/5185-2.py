# 5185.py 이진수 
# 파이썬 내장함수를 사용하지 않은 풀이
import sys
sys.stdin = open("5185input.txt", "r")

def dec_to_bin(dec_num): return ''.join(['1' if dec_num & (1 << i) else '0' for i in range(3, -1, -1)])
for tc in range(int(input())): print('#{} {}'.format(tc + 1, ''.join([dec_to_bin(arg) for arg in [int(char) if char.isdigit() else ord(char) - 55 for char in input().split()[1]]])))
