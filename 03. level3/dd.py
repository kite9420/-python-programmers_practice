#2026/06/13
#연습문제 올바른 괄호의 갯수
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12929



def solution(n):
    def count(open,close):
        if open == n and close == n:
            return 1
        total = 0
        if open < n:
            total += count(open+1,close)
        if close < open:
            total+= count(open,close+1)
        return total
    return count(0,0)

#백트래킹 재귀는 while 이 아닌 if로 두갈래로 짬
#아래는 같은 코드를 스택 방식으로
'''
def solution(n):
    def count(open,close):
        total = 0
        stack = [(0,0)]
        while stack:
            open,close = stack.pop()
            if open == n and close == n:
                total += 1
            else:
                if open < n:
                    stack.append(count(open+1,close))
                if close < open:
                    stack.append(count(open,close+1))
        return total
    return count(0,0)
'''
        
#처음 -> (0,0,2)
    #다음 -> (1,0,2) -> total =2
        #다음 - >(2,0,2) total = 1
            #다음 - >(2,1,2) total = 1
                #다음 - >(2,2,2) -> return 1
        #다음 -> (1,1,2) total = 1
            #다음 -> (2,1,2) total = 1
                #다음 -> (2,2,2) return 1 
