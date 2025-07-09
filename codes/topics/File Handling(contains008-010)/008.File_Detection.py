import os #first time using os module
file_path="test_file.txt"
if os.path.exists(file_path):
    print("file exists")
else:
    print("file does not exist")
file_path2="test_directory/test.txt"#forward slash and double stash can also be used
if os.path.exists(file_path2) and os.path.isfile(file_path2):
    print("file exists and is a file")
elif os.path.isdir(file_path2):
    print(" is a directory")
else:
    print("file does not exist or wrong path")