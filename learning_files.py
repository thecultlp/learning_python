with open("students.txt","w") as file:
    file.writelines(["Ravi\n","Rahul\n","Amit\n"])
with open("students.txt", "r") as file:
    print(file.read())
with open("students.txt","r") as file:
    for line in file:
        print(line)

