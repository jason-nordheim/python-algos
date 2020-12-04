def is_prime(num): 
    """
    determines if the provided number is a prime number 
    """
    if num == 1 or num == 2 or num == 3: # basic prime numbers 
        return True 
    if not num and num < 1 or  num % 2 == 0: # edge cases 
        return False
    else: 
        i = 3
        while(i < num): 
            remainder = num % i 
            if remainder == 0: 
                return False  
            i += 1 
    return True 


tests = [
    [7, True], [13, True], [21, False], [2, True],
    [10, False], [42, False], [15, False], [20, False],
    [5, True], [11, True], [17, True], [19, True], 
    [23, True], [24, False], [25, False], [26, False], 
    [27, False], [28, False], [29, True]
]


print('Starting Tests')
for test in tests: 
    err_message = str(test[0]) + ' returned ' + str(bool(not test[1]))
    assert is_prime(test[0]) == test[1], err_message
print('All tests passed successfully')