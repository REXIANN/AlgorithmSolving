koko = int(input())
 
for qwer in range(koko):
    cc = int(input())
    putter = list(map(int, input().split()))
    ekek = 0
    zxcv = putter[-1]
    for x in range(len(putter) - 1, -1, -1):
        if putter[x] <= zxcv:
            ekek += zxcv - putter[x]
        else:
            zxcv = putter[x]
    print('#{} {}'.format(qwer + 1, ekek))