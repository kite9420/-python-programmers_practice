#2026/07/06
#월간 코드 챌린지 시즌2
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/76502

#문제 분석 - 두가지 기능 혼합
#기능 1. 문자열 회전 
    # 어떻게 할 것인가? 슬라이싱 이용하면 간단해보암
    # rotate 함수는 solution 안에 작성하면 됨으로 따로 필요하지는 않지만, 설계를 위해 사전에 작성
def rotate(s : str):
    n = len(s)
    for i in range(n):
        rotated = s[i:] + s[:i]
        
#기능 2. 올바른 괄호 문자열인지 확인
    # 어떻게 할 것인가? 단순 스택으로 만들기에는 괄호 입력이 다수
    # 괄호 입력이 다수 일 때 각각의 괄호들을 검사하려면?
        # 아이디어 -> 스택 구조로 스택의 가장 위와 일치할 때만 빼내고 아니면 False. 딕셔너리로 쌍을 만들어서 관리
def check(s : str):
    word_dict  = {    ')': '(',
                      '}': '{',
                      ']': '['
                }
    stack = []
    for c in s:
        if c in word_dict:
            if not stack:
                return False
            else:
                top = stack.pop()
                if word_dict[c] == top:
                    continue
                else:
                    return False
        else:
            stack.append(c)
    if stack:
        return False
    return True


def solution(s):
    n = len(s)
    answer = 0
    for i in range(n):
        rotated = s[i:] + s[:i]
        if check(rotated):
            answer += 1
    return answer