#2026/06/25
#숫자 블록
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12923

def solution(begin, end):
    '''Brute
    -> 블록의 총수를 고려안함
    tiles = [0] * (end +1)
    for i in range(1,end+1):
        idx =2
        while i * idx <= end:
            tiles[i*idx] = i
            idx += 1
    return tiles[begin:end+1]
    ''' 
    
    #블럭의 값은 가장 큰 약수
    #제한사항 -> 블록의 총 수는 10,000,000까지
    def find_num(x):
        if x == 1:
            return 0
        root = int(x ** 0.5)+1
        best_small = 1
        for i in range(2,root +1):
            if x % i == 0:
                if x//i <= 10000000:
                    return x // i
                best_small = i
        return best_small
    idx = 0
    answer = [0] * (end - begin + 1)
    cur = begin
    while cur <= end:
        answer[idx] = find_num(cur)
        cur += 1
        idx += 1
    return answer