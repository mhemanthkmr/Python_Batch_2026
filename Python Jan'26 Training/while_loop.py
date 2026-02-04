count = 2

while count <= 30:
    if count % 3 == 0:
        print(count)
    count += 1

print("End")


password = ""
while password != "secret":
    password = input("Enter password: ")
    if password != "secret":
        print("Wrong password, try again!")
print("Access granted!")

