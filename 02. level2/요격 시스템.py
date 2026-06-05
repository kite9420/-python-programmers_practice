#2026/06/06
#요격 시스템 연습문제
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181188

def solution(targets):
    shot = 0
    last_shot = -1
    #last_shot은 편의상 4일때 4가 아닌 직전(3.9999)으로 생각
    targets.sort(key = lambda x : x[1])
    for s,e in targets:
        if s >= last_shot:
            shot += 1
            last_shot = e
    
    return shot


'''
targets 정렬하면
[1,4]
[4,5]
[3,7]
[4,8]
[5,12]
[11,13]
[10,14]

4(3.999)에서 발사 -> last_shot=4 (3.999)  shot 1
4 >= 4 (last_shot) -> 5(4.999)발사, last_shot = 5 shot 2
3,4 < 5 넘어감
5>= 5, last_shot = 12 shot = 3
11,10 < 12 넘어감
'''