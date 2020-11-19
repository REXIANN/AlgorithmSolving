def solution(n):
    memo = [0, 1]
    if n <= 1:
        return memo[n]
    else:
        for i in range(2, n + 1):
            val = memo[i - 1] + memo[i - 2]
            memo.append(val)
    return memo[n] % 1234567