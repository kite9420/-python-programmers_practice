#2026/04/27
#2016년
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12901

#datetime 모듈을 사용한 개선된 코드
import datetime

def solution(a, b):
    week = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    day = datetime.date(2016, a, b)
    return week[day.weekday()]
'''
def solution(a,b):
    day = datetime.date(2016, a, b)
    return day.strftime("%a").upper()
#요일 약자가 다를 수 있으므로 오답이 발생할 수 있음
'''


'''
def solution(a, b):
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    day = sum(days[:a-1]) + b - 1
    return week[day%7]
'''