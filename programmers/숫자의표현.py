def solution(n):
    head, tail = 1, 1
    numbers = [i for i in range(n + 1)]
    total = 1
    count = 0
    while head != n and tail != n:
        if total < n:
            head += 1
            if head == n:
                head = n
            total += numbers[head]
        else:
            if total == n:
                count += 1
            total -= numbers[tail]
            tail += 1
            if tail == n:
                tail = n
  
    return count + 1