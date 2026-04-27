# 2026/04/27
# 연습문제 해시 폰켓몬
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    k = len(nums)//2
    unique = len(set(nums))
    return min(k,unique)

'''

def solution(nums):
    k = len(nums)//2
    set_nums = set()
    for num in nums:
        set_nums.add(num)
    if len(set_nums) > k:
        return k
    else:
        return len(set_nums)

'''