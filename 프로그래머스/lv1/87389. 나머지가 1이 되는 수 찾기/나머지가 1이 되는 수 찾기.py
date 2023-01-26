def solution(n):
    x_list=[]
    for i in range(1,n):
        if n%(i)==1:
            x_list=str(i)
            return int(x_list)