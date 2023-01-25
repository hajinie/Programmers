def solution(x):
    x_list=list(str(x))
    n=0
    for i in x_list:
        n+=int(i)
    if x%n==0:
            return True
    else:
            return False


