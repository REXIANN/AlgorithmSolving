import math

def solution(w,h):
    if w == h:
        return w * h - h    
    count = 0
    w, h = min(w, h), max(w, h)
    for i in range(1, min(w, h) + 1):
        count += (math.ceil(h * i / w) - math.floor(h * (i - 1) / w))    
    return w * h - count