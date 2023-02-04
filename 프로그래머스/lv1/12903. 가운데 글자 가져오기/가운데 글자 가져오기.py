def solution(s):
    for i in s:
        if len(s)%2==0:
            half=len(s)//2
            return s[half-1:half+1]
        else:
            half=(len(s)+1)//2
            return s[half-1]
            