def solution(n):
    n_sqrt=n**(1/2)
    if int(n_sqrt)==n_sqrt:
        n_sqrt1=(n_sqrt+1)**2
        return n_sqrt1
    else:
        return -1
    