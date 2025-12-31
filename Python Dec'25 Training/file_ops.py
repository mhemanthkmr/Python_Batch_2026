def read_file(file_path, encoding = "UTF-8"):
    try:
        with open(file_path, mode="r", encoding=encoding) as file:
            data = file.read()
            return data
    except Exception as err:
        print(str(err))

def write_file(file_path, content, encoding = "UTF-8"):
    try:
        with open(file_path, mode="w", encoding=encoding) as file:
            data = file.write(content)
            return data
    except Exception as err:
        print(str(err))

def append_file(file_path, content, encoding = "UTF-8"):
    try:
        with open(file_path, mode="a", encoding=encoding) as file:
            data = file.write(content)
            return data
    except Exception as err:
        print(str(err))

