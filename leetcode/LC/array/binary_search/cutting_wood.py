https://bytebytego.com/exercises/coding-patterns/binary-search/cutting-wood


from typing import List

def cutting_wood(heights: List[int], k: int) -> int:
    left, right = 0, max(heights)

    while left < right:
        mid = (left + right) // 2 + 1
        if can_cut(mid, heights, k):
            left = mid
        else:
            right = mid - 1
    return right

def can_cut(mid, heights, k):
    sum = 0

    for h in heights:
        if h > mid:
            sum += h - mid
    return sum >= k
