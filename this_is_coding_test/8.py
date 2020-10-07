# 8. 문자열 재정렬
import sys
sys.stdin = open('8input.txt', 'r')
total = 0
lettres = []
for value in input():
    if value.isdecimal():
        total += int(value)
    else:
        lettres.append(value) 

    print(lettres, total)
c = sorted(lettres, key = lambda x : ord(x))
result = ''.join(c) + str(total)
print(result)
