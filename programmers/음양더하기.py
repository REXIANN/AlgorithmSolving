def solution(a, s):
    return sum([a[i] if s[i] else -a[i] for i in range(len(a))])


solution = lambda x, y : sum([x[i] if y[i] else -x[i] for i in range(len(x))])