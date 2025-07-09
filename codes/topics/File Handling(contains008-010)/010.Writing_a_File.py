#basic file writing didn't do json files
txt_data="I love Python"
file_path="output.txt"
with open(file_path,"w") as file:  #here w means Write,there is also x works but file shouldn't exist
    file.write(txt_data)           #a is for append to append a file,r can be used to read
    print("file was created")
txt_data2="I love Python"
file_path2="test_directory/output2.txt"
with open(file_path2,"w") as file: #w also overwrites the file if it exists
    file.write(txt_data2)
#writing/adding from list
List=["I","love","Python"]
with open(file_path2,"w")as f:
    for item in List:
        f.write(item+"\n")
import csv
employees=[["name","age","job"],
           ["joe","27","Unemployed"],
           ["moe","20","learner"],
           ["doe","17","student"],
           ["roe","23","engineer"]]
file_path="output.csv"
with open(file_path,"w") as file:
    writer = csv.writer(file)
    for row in employees:
        writer.writerow(row)


