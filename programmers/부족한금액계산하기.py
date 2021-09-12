def solution(price, money, count):
    total = sum([price * c for c in range(1, count + 1)])
    return total - money if money < total else 0