def solution(nums):
    length = len(nums) // 2
    
    answer = len(set(nums))
    return length if answer > length else answer