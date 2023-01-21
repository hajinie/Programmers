
#1
def solution(n):
    n_list=list(map(int,str(n)))
    n_reverse=n_list.reverse()
    return n_list
#2
def solution(n):
    return list(map(int, reversed(str(n))))
