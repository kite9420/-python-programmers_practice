# 2026/04/25
# 2025 카카오 하반기 1차 levl1 중요한 단어를 스포 방지
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/468370
def solution(message, spoiler_ranges):
    words = []
    spoiler_words = []
    non_spoiler_words = set()
    answer = 0
    ws = 0
    for i in range(len(message)):
        if message[i] == ' ':
            words.append((ws,i-1,message[ws:i]))
            ws = i+1
    words.append((ws,len(message)-1,message[ws:len(message)]))
    
    for ws,we,word_str in words:
        for ss,se in spoiler_ranges:
            if se >= ws and ss <= we:
                if word_str not in spoiler_words:
                    spoiler_words.append(word_str)
                break
        else:
            non_spoiler_words.add(word_str)
    
    seen = set()
    for word in spoiler_words:
        if word not in non_spoiler_words and word not in seen:
            answer +=1
            seen.add(word)
    return answer