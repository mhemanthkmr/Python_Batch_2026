def greet():
    # Sample One
    # Sample Two
    print("Hello World")


def multiply(x=0, y=1):
    print("Multiple of X and Y is :", x * y)
    # return x * y


def addition(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


# x = int(input("Enter a Number X :"))
# y = int(input("Enter a Number Y :"))

# a^2 + b^2 + 2ab
# output = multiply(x,x) + multiply(y,y) + multiply(2,multiply(x,y))
# print(multiply(x,x))
print(addition(1, 2, 3, 4, 5, 6))
