def solution(price, money, count):
    answer=0
    for i in range(0,count+1):
        answer+=price*i
    if answer<money:
        return 0
    else:
        return answer-money
    