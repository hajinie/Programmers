def solution(n):
    x_list=[]
    for i in range(2,n):
        if n%(i)==1:
            return i