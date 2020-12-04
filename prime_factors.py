

def get_prime_factors(num):
    """
    gets all the prime factors that 
    can be multiplied to produce the provided 
    number 
    """
    factors =[]
    divisor = 2
    while (divisor <= num):
        if int(num % divisor) == 0: 
            factors.append(int(divisor))
            num = int(num / divisor) 
        else: 
            divisor += 1 
    return factors 


tests = [
    [7,  [7]],
    [10, [2, 5]],
    [11, [11]], 
    [12, [2,2,3]], 
    [13, [13]], 
    [14, [2,7]],
    [60, [2,2,3,5]],
    [90, [2,3,3,5]],
    [630, [2,3,3,5,7]],
]

print('Starting Tests')
for test in tests: 
    err_start = str(test[0]) + ' returned '
    factors = get_prime_factors(test[0])
    err_message =  err_start + str(len(factors)) + ', expected ' + str(len(test[1]))
    assert len(factors) == len(test[1]), err_message
    i = 0 
    while i < len(test[1]): 
        err_message += err_start + str(factors[i]) 
        err_message += ', expected' + str(test[1][i])
        assert int(factors[i]) == int(test[1][i]), err_message
        i += 1 
print('All tests passed successfully')