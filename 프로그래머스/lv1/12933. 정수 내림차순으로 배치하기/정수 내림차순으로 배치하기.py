def solution(n):
    n_int=int(n)
    n_list=str(n_int)
    return int(''.join(sorted(n_list,reverse=True)))