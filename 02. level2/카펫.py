#2026/06/24
#카펫
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42842

#총 배열의 수를 찾는 문제
#두 수의 합 = 두수의 곱으로 표현됨
#단 두 수의 곱 -> a,b가 있을 때 (a*b) = brown + yellow, (a-c)*(b-d) = yellow -> brown =  ad + cb - cd (테두리가 한줄이므로 c,d=2)
#a*b = brown + yellow, brown = 2a+2b - 4
#-> 두수의 합과 곱을 앎으으로 이차방정식으로 표현가능  2(a+b) -4 = brown ->> a+b = (brown +4)/2
# (x-a)(x-b) = x^2 -(a+b)+ab => x^2 - ((brown +4)/2)x + brown + yellow 를 푸는 x값
#a = 1, b = -(brown +4)/2), c= brown + yellow인 근의 공식 사용


def solution(brown, yellow):
    b = -(brown +4)//2
    c = brown + yellow
    w = (-b + (b*b - 4*c)**0.5)//2  #가로가 더 길므로 더해줌
    h = -b - w
    return [w,h]



'''
def solution(brown, yellow):
    candidate =[]
    for i in range(1,(brown+yellow)//2 +1):
        if (brown+yellow)%i == 0 :
            candidate.append((max((brown+yellow)//i,i),min((brown+yellow)//i,i)))
    for a,b in candidate:
        if 2*a+2*b -4 == brown:
            return[a,b]
        
            
-> 간략화
def solution(brown, yellow):
    total = brown + yellow
    for i in range(1, int(total**0.5)+1):
        if total % i == 0:
            j = total //i
            if 2*i + 2*j == brown:
                return[i,j]
'''
 
#완전 탐색 버전
def solution(brown, yellow):
    for h in range(3, brown + yellow + 1):
        for w in range(h, brown + yellow + 1):  
            if w * h == brown + yellow:          
                if (w - 2) * (h - 2) == yellow:  
                    return [w, h]