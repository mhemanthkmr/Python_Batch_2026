# temperature = 35

# if temperature > 30:
#     print("It's hot outside")
# else:
#     print("It's not too hot")

# print("Program Completed")


# color = input("Enter a color: ")

# if color.lower() == "green":
#     print("Go ...")
# elif color.lower() == "yellow":
#     print("Get Ready ...")
# elif color.lower() == "red":
#     print("Stop ...")
# else:
#     print("Invalid Color")

# Nested If Example

voter_id = False
country = "India"

if voter_id:
    if country == "India":
        print("You're eligible to Vote")
    else:
        print("Not Eligible to Vote you're from different country")
else:
    print("Not Eligible to Vote you didn't have your Voter ID")
    age = int(input("Enter your age: "))
    if age >= 18:
        print("Please apply voter ID in the website : ")
    else:
        print(f"Please wait {18 - age} years")    
