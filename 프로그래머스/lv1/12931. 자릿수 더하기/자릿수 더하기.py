def solution(n):
    answer = 0
    M=list(str(n))
    for i in M:
        answer+=int(i)
    return answer
