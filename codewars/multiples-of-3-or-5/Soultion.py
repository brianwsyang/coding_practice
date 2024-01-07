def solution(number):
    # sum multiples of 3 or 5 below the given number
    # if number < 0, return 0

    if number < 0: 
        return 0
    
    multiple_sum = 0
    for n in range(number):
        if (n % 3 == 0) or (n % 5 == 0):
            multiple_sum += n
    
    return multiple_sum