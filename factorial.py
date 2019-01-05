value = int(input('Enter a value : '))

check_number = value == 0 or value == 1

if (check_number):
    result = 1
    print('The result : {}! is {}'.format(value, result))

else:
    factorial = 1
    for count in range(1, value + 1):

        factorial *= count
        
    print('The result : {}! is {}'.format(value, factorial))