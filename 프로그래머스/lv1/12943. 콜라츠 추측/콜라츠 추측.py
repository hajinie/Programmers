def solution(num):
    a=int(num)
    i=1
    while i<=500:
        if a%2==0:
            a=a/2
            i+=1 
            if a==2:
                return i
        elif a==1:
            return 0
        else:
            a=a*3+1
            i+=1
    return -1
    