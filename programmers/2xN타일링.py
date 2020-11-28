def solution(n):
    memo = [1, 2, 3]
    if n - 1 < 3:
        return memo[n - 1]
    
    x, y = memo[1], memo[2]
    for i in range(3, n):
         z = x + y
         x, y = y, z
        
    return z % 1000000007