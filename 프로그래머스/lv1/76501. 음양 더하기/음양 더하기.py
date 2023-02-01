def solution(absolutes, signs):
    new=[]
    result=0
    for i,j in zip(absolutes,signs):
        if j==True:
            j=1
            new.append(j)
        else:
            j=-1
            new.append(j)
    for i,j in zip(absolutes,new):
        result+=i*j
    return result