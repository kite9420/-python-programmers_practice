#2026/04/27
#가운데_글자_가져오기
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    return s[(len(s)-1)//2 : len(s)//2 + 1]

'''
def solution(s):
    leng = len(s)
    if leng % 2:
        return s[leng // 2]
    else:
        return s[leng //2 -1 : leng //2+1]
'''