#2026/06/02
#124나라의 숫자
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12899

'''
%해서 끝자리 결정 
다음 자릿수는 n // 3 -> 나누어 떨어질 때는 몫에서 1을 빼야 정상 동작
경험적으로 풀이 가능 -> 수학적으로는??
6 => 3진법 => 20 = 3*2+0
6 => 124나라 => 14 = 3*1 +3  -> 몫에서 하나 빠짐
7 => 21 = 3*2+1
7 =? 21 = 3*2+1
즉 나머지가 0인 경우에 nuber의 몫은 1 작아야함
'''

#원본 코드
def solution(n):
    answer = ''
    number = n
    
    while number:
        write = number % 3
        if write == 0:
            answer = f'4{answer}'
            number = (number // 3) -1
        else:
            answer = f'{write}{answer}'
            number = (number //3)
    return answer

# 리팩토링
        # ex = n =3 이면 n-1 = 2 -> '124'[2] = '4' -> answer = '4' + '' -> answer = '4'
        # ex = n = 4 이면 n-1 = 3 -> '124'[0] = '1' -> n = 3 // 3 = 1 -> 1 - 1 = 0 -> '124'[0] = '1' -> answer = '1' + '4' -> answer = '14'

def solution(n):
    answer = ''
    while n:
        n -= 1
        answer = '124'[n % 3] + answer

        n //= 3
    return answer