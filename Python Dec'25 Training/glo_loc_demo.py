name1 = "Raj"  # Global
name2 = "Vijay"


def hello():
    global name2
    name2 = "Surya"  # Local Scope
    # print("Hello World")
    # print(name1, name2)


hello()
print(name1)  # Raj
print(name2)  # Vijay
