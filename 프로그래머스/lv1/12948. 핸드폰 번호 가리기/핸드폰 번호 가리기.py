def solution(phone_number):
    list_len=len(phone_number)
    str_='*'
    new=(str_*(list_len-4)+phone_number[list_len-4:])
    return new
        