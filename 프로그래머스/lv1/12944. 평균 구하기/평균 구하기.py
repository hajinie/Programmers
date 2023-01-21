def solution(arr):
    M=list(arr)
    answer=0
    for i in M:
        answer+=float(i)/len(M)
    return answer
