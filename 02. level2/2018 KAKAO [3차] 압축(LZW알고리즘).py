#2026/06/01
#2018 KAKAO [3차] 압축(LZW알고리즘)
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/17684


'''
LZW 핵심
1. 단어 사전 초기화 : A-Z까지의 알파벳을 사전에 등록
2. 입력 문자열 탐색 -> 현재 단어(w) + 다음 문자(c)가 사전에 존재하는지 확인(다음 단어 탐욕적 최장 일치)
3. 분기 기준 = w+c가 사전에 존재하는지 여부
- 존재하는 경우 : w를 w+c로 확장하여 탐색 계속
- 존재하지 않는 경우 : w의 사전 번호를 결과에 추가, w+c를 사전에 등록, w를 c로 초기화하여 탐색 계속
4. 입력 문자열 끝까지 탐색 후 마지막 w의 사전 번호를 결과에 추가
'''

def solution(msg):
    #ord : 문자를 ASCII 정수로 바꿈 -> ord('A')=65, ord('Z')=90
    word_dict = {}
    answer = []
    for i in range(ord('A'), ord('Z')+1):
        word_dict[chr(i)] = i - ord('A') +1
    
    w = msg[0]
    i = 1
    while i < len(msg):
        c = msg[i]
        if w + c  in word_dict:
            w = w + c
        else : 
            answer.append(word_dict[w])
            word_dict[w+c] = len(word_dict) + 1
            w = c
        i += 1
    answer.append(word_dict[w])
    return answer