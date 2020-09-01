from pprint import pprint
import sys
sys.stdin = open("testinput.txt", "r")

answers = [list(map(int, input().split())) for _ in range(20)]
pprint(answers)
result = []
for i in range(0, 20, 2):
    for j in range(10):
        result.append((answers[i][j], answers[i + 1][j]))
print(result)
result.sort(key=lambda x: x[0] )
print()
print(result)

for val in result:
    print(val[0], val[1])
