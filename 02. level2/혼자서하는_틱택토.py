
#2026/07/03
#혼자서하는_틱택토
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/160585
#문제 자체의 구조를 짜는 것보다는 조건을 머리속으로 분리하는 것이 어려웠던 문제

def solution(board):
    countO = 0
    countX = 0
    X_win = 0
    O_win = 0
    lines = []
    for i in range(3):
        row = ""
        col = ""
        for j in range(3):
            row += board[i][j]
            col += board[j][i]
            if board[i][j] == "O":
                countO += 1
            if board[i][j] == "X":
                countX += 1
        lines.append(row)
        lines.append(col)
    lines.append(board[0][0] + board[1][1] + board[2][2])
    lines.append(board[0][2] + board[1][1] + board[2][0]) 
    
    for line in lines:
        if line == "OOO":
            O_win += 1
        elif line == "XXX":
            X_win += 1
            
    if countX > countO:
        return 0
    if countO > countX +1:
        return 0
    if O_win and X_win:
        return 0
    if O_win >= 1:
        if countO != countX + 1:
            return 0
    if X_win >= 1:
        if countO != countX:
            return 0
    return 1

'''AI를 이용한 리팩토링
반복문 제거 (count 이용), if countX > countO및 if countO > countX + 1 합치기, 
def solution(board):
    flat = board[0] + board[1] + board[2]
    diff = flat.count("O") - flat.count("X")
    
    lines = []
    for i in range(3):
        lines.append(board[i][0] + board[i][1] + board[i][2])
        lines.append(board[0][i] + board[1][i] + board[2][i])
    lines.append(board[0][0] + board[1][1] + board[2][2])
    lines.append(board[0][2] + board[1][1] + board[2][0])
    
    O_win = "OOO" in lines
    X_win = "XXX" in lines
    
    if diff not in (0, 1): return 0
    if O_win and X_win: return 0
    if O_win and diff == 0: return 0
    if X_win and diff == 1: return 0
    return 1


'''