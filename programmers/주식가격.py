def solution(prices):
    answer = []
    for i in range(len(prices)):
        price = prices[i]
        count = 0
        idx = i + 1
        while idx < len(prices):
            count += 1
            next_price = prices[idx]
            if next_price < price:
                break
            idx += 1
        answer.append(count)
        count = 0
    return answer