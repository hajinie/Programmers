def solution(n):
    answer = 0
    data=[]
    for i in range(1,n+1):
        if n%i==0:
            data.append(i)
    for i in data:            
        answer+=int(i)
    return answer
        