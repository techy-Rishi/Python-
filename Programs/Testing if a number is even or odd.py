a = int(input('Enter a number: '))

def check_evod(num):
    if num % 2 == 0:
        return f'{num} is an even number'
    else:
        return f'{num} is an odd number'

result = check_evod(a)
print(result)
