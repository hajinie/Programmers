def solution(s):
    for i in s:
        if len(s)==4:
            return s.isnumeric()
        elif len(s)==6:
            return s.isnumeric()
        else:
            return False