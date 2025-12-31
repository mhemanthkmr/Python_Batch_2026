
class NumberNotAcceptError(Exception):
    pass


try:
    number1 = int(input("Enter the number 1:"))
    number2 = int(input("Enter the number 2:"))
    if number2 == 15:
        raise NumberNotAcceptError("Number not accept error")
    print("Division of Two Numbers is :", number1 / number2)
except Exception as err:
    print("Something went wrong!!")
    print(str(err))
finally:
    print("Finally!")

print("Hello")