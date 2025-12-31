# Syntax :

# While < condition >:
# Statement 1
# Statement 2
# Statement 3

# start_value = 1
# end_value = 10

# while start_value <= end_value:
#     print(start_value)
#     start_value += 1


is_logged_in = False
count = 0
while count < 3:
    password = input("Enter password: ")
    count += 1
    if password != "secret":
        print("Wrong password, try again!")
    else:
        print("Access Granted")
        is_logged_in = True
        break

if is_logged_in:
    print("Welcome Home")
