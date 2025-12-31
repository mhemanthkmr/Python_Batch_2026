age = int(input("Enter your Age :"))
citizen = input("Enter your Country :")

if age >= 18:
    if citizen.lower() == "india":
        print("Elible to Vote")
    else:
        print("Not a Citizen")
else:
    print("Underage")
