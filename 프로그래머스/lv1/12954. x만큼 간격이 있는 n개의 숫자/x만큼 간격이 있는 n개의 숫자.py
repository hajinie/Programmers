def solution(x, n):
    answer = []
    plus=0
    for i in range (0,n):
        plus+=x
        answer.append(plus)
    return answer