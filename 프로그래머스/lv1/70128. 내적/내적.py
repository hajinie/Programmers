def solution(a, b):
    new=len(a)
    answer=0
    for i in range(0,new):
        answer+=a[i]*b[i]
    return answer