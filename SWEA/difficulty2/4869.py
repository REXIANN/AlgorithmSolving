import sys
sys.stdin = open("4869input.txt", "r")

def confetti(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return confetti(n - 1) + 2 * confetti(n - 2)


tc = int(input())

for test_count in range(1, tc + 1):
    number = int(input())
    conf = confetti(number//10)
    print('#{} {}'.format(test_count, conf))
