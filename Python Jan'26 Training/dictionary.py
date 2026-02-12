my_dict = {
    "name" : "Raj",
    "age"  : 23,
    "phone_number" : "+91-9876543210",
    "location" : "Bengaluru"
}

# print(my_dict.get("location", "NA")) # Chennai
# print(my_dict['location']) # Chennai

my_dict.update(
    {
        "age": 12,
        "location" : "Chennai",
        "address" : "T Nagar"
    }
)

# my_dict.pop("address")
# my_dict.pop("age")

# => [(key, value), (key1, value1) .... (keyN, valueN)]



my_dict.clear()
items = list(my_dict.items())
print(list(my_dict.items()))



for key, value in items:
    print(f"{key} <====> {value}")