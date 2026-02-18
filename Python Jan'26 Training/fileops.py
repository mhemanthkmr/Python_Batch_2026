# file = open(r"C:\Users\mhema\OneDrive\Desktop\Python_Batch_2026\Python Jan'26 Training\test.txt", mode="a")

# data = file.write(r"\n\tBesant")

# # Some error occured


# file.close()

# print(data)


# With Context Manager

def read_file(file_path, mode="r"):
    try:
        with open(file_path, mode=mode) as file:
            data = file.read()
            return data
    except Exception as err:
        print("Error Occured", str(err))


data = read_file("f_string.py")
print(data)