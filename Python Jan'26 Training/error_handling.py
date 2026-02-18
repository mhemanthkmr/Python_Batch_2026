try : 
    number_1 = int(input("Enter a Number: "))
    number_2 = int(input("Enter a Number: "))
    print(number_1 / number_2)    
except Exception as err:
    print("Can't Calculate the Numbers", str(err))
finally:
    print("This is Finally Block")

print("Hello World !")