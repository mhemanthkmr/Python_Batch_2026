
# Without Parameter Function
def hello():
    print("Hello World!")

# With Parameter Function
def add(a , b):
    print(a + b)

# Default Function
def sub(a = 0, b = 0):
    print(a - b) 

def multiply(a, b):
    return a * b
# arbitary argument
def sum_of_all_numbers(*args):
    sum = 0
    for i in args:
        sum += i

    return sum


def test_keyword_arguments(*args, **kwargs):
    print(kwargs)
    print(type(kwargs))
    print(args)
    print(type(args))
    pass

A = 5
B = 7

a_square = multiply(A, A)
b_square = multiply(B, B)
two_A_B = multiply(multiply(A, B), 2)

def divide(a,b):
    pass


answer = sum_of_all_numbers(a_square, b_square, two_A_B)


test_keyword_arguments(8,7,8,9,5,6, khasdkjhsa="Raj", age=18, location="Chennai")