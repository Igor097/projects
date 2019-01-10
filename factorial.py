
def factorial(value):
    
    check_number = value == 0 or value == 1

    if (check_number):
        result = 1
        return result

    else:
        fact = 1
        for count in range(1, value + 1):
            
            fact *= count
        
        return fact


value = int(input('Enter a value : '))
result = factorial(value)

print('The result : {}! is {}'.format(value, result))
