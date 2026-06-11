#2026/06/12
#2023 KAKAO 표현 가능한 이진트리
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/150367

def solution(numbers):
    def padding(b):
        L = len(b)
        k = 1
        while 2**k-1 < L:
            k += 1
        while L < 2**k -1:
            b = "0" + b
            L = len(b)
        return b
                
    def check(b):
        lo = 0
        hi = len(b)
        if lo >= hi:
            return True
        mid = (lo + hi) //2
        
        if b[mid] == '0':
            if '1' in b[lo:mid] or '1' in b[mid:hi]:
                return False
            else:
                return True
        else:
            return check(b[lo:mid]) and check(b[mid+1:hi])
    
    result = []
    for dec in numbers:
        b = padding(bin(dec)[2:])
        if check(b):
            result.append(1)
        else:
            result.append(0)
    return result
        
'''간략화
def solution(numbers):
    def padding(b):
        k = 1
        while 2** k-1 < len(b):
            k += 1
        return "0" * (2 **k -1 - len(b)) + b

    def check(lo, hi):
        if lo >= hi:   #(이 문제에서는 자식이 없는 리프 노드를 검사할 필요가 없으므로 해당 노드는 방문하지 않게 처리하였음)
            return True
        mid = (lo + hi) //2
        if b[mid] == '0':
            return '1' not in b[lo:hi]
        return check(lo,mid) and check(mid+1,hi)

    result = [] 
    for dec in numbers:
        b = padding(bin(dec)[2:])
        result.append(1 if check(0,len(b)) else 0)
    return result
'''