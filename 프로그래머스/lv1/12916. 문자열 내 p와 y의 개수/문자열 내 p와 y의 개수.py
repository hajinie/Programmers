def solution(s):
    s_list=list(str(s))
    p_list= s_list.count('p')+s_list.count('P')
    y_list= s_list.count('y')+s_list.count('Y')
    for i in s_list:
        if p_list==y_list:
            return True
        else:
            return False
    if p_list and y_list==0:
        return True