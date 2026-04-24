#2025 카카오 하반기 1차 levl1 노란불 신호등
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/468371

#유클리드 호제법을 이용한 최대공약수(gcd)와 최소공배수(lcm) 구하기
#재귀문을 이용하여 리스트의 최대 공약수를 구하는 함수를 구현하였다
def gcd(lst):
    if len(lst) == 1:
        return lst[0]
    a = lst[0]
    b = gcd(lst[1:])
    while b:
        a, b = b, a % b
    return a

#최소공배수는 두 수의 곱을 최대공약수로 나눈 값과 같다. 이를 이용하여 리스트의 최소공배수를 구할 수 있다.
# lcm(a,b) = a*b // gcd(a,b)
# 재귀문을 이용하여 리스트의 최소 공배수를 구하는 함수를 구현하였다    

def lcm(lst):
    if len(lst) == 1:
        return lst[0]
    a = lst[0]
    b = lcm(lst[1:])
    return a * b //gcd([a,b])

def solution(signals):
    T = [sum(signal) for signal in signals]
    period = lcm(T)
    for t in range(1,period+1):
        if all(
            (t-1)%T[i] >= signals[i][0] and \
            (t-1)%T[i] < signals[i][0]+signals[i][1] \
            for i in range(len(signals))
        ):
            return t
    return -1

'''
#all을 사용하지 않았을 경우 함수는 다음과 같이 작성될 수 있다.
def solution(signals):
    T = [sum(signal) for signal in signals]
    period = lcm(T)
    for t in range(1,period+1):
        all_True = True
        for i in range(len(signals)):
            if (t-1)%T[i] >= signals[i][0] and \
            (t-1)%T[i] < signals[i][0]+signals[i][1]:
                pass
            else:
                all_True = False
                break
        if all_True:
            return t
    return -1
'''
