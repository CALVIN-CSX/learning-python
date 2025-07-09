with open("test_file.txt") as file: #with is used to close the file automatically
    print(file.read())              #otherwise need to use file.close() in code
print(file.closed)

