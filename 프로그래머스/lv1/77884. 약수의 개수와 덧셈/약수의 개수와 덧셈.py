def solution(left, right):
    a=[]
    re_=0
    for i in range(left,right+1):
        for j in range(1,i+1):
            if i%j==0:
                a.append(j)
                answer=len(a)
        if answer%2==0:
            re_+=i
            answer=0
            a.clear()
        else:
            re_-=i
            answer=0
            a.clear()
    return re_