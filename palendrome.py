import re # regular expressions module 

def is_palindrome(str): 
    '''
    determines if the given string is a palindrome 
    - ignores any characters that are not part of the english alphabet 
    - ignores symbols (e.g. ["'", ",", "."])

    1.  convert input string to lower case using .lower()
    2.  use re.findAll to match the regular expressions reducing the str.lower() to 
        only include letters a-z 
    3.  join array returned by re.findAll back into a single string (forwards) 
    4.  use the slice operator to make a copy of the joined string (forwards) 
        in reverse the joined string (backwards)
    5.  return True if forwards matches reversed 

    '''
    forwards = ''.join(re.findall(r'[a-z]+', str.lower()))
    backwards = forwards[::-1]
    return forwards == backwards 




tests = [
    ['hello world', False],
    ['Go hang a salami - I\'m a lasagna hog.', True],
    ['race car', True],
    ['orange', False]
]


print('Starting tests...')
for t in tests: 
    err_prefix = str(t[0]) + ' returned '  
    result = is_palindrome(t[0])
    assert result == t[1], err_prefix + str(result)
print('All tests passed')