#2026/06/27
#2020 카카오 괄호 변환
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/60058

def solution(p):
    def check(p):
        stack = 0
        for c in p:
            if stack < 0:
                return False
            elif c == "(":
                stack += 1
            elif c == ")":
                stack -= 1
        if stack == 0:
            return True
        return False
    
    def divide(w):
        u = ""
        v = ""
        stack = 0
        for c in w:
            if c == "(":
                stack += 1
                u = u + c
            if c == ")":
                stack -= 1
                u = u+c
            if stack == 0:
                break
        return u, w[len(u):]
    
    def reverse(u):
        u = u[1:-1]
        nu = ""
        for c in u:
            if c == "(":
                nu += ")"
            if c == ")":
                nu += "("
        return nu
    
    def fix(p):
        if len(p) == 0:
            return ""
        u, v = divide(p)
        if check(u):           #재귀문 핵심. v는 어차피 fix(v)로 재검사하므로 따로 체크할 필요없음.
            return u + fix(v)
        else:
            return "(" + fix(v) + ")" + reverse(u)
    
    return fix(p)

'''
u를 자른 시점에서 u가 올바른지 알 수 있으므로 check를 divde와 분리할 필요가 없다.
위에서 사용한 모든 함수를 합칠 수 있음
'''
def solution(p):                         
    if not p:
        return ""
    cnt = 0
    for i, c in enumerate(p):   
        cnt += 1 if c == "(" else -1
        if cnt == 0:
            break

    u, v = p[:i+1], p[i+1:]

    if u[0] == "(":
        return u + solution(v)
    
    answer = '(' + solution(v) + ')'
    for c in u[1:-1]:
        answer += ')' if c == '(' else '('
    return answer