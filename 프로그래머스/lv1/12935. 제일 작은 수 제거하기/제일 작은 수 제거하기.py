def solution(arr):
    if len(arr)>1:
        remove_=min(arr)
        arr.remove(remove_)
        return arr
    else:
        remove=arr.pop()
        arr.append(-1)
        return arr