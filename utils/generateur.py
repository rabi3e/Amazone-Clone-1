import random

def generate_code(n=9):
    numbers = '123456789'
    code = ''.join(random.choice(numbers)  for x in range(n))
    return code
    