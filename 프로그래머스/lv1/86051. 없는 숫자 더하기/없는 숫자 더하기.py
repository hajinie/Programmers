def solution(numbers):
    new=[]
    for i in range(0,10):
        new.append(i)
        if i in numbers:
            new.remove(i)
            
    return sum(new)