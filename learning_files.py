"""Without looking at the notes, write a program that:

Creates student.txt
Writes:
Ravi
Rahul
Amit

Reads the file
Prints all names line by line using a for loop
Uses with open() instead of close()"""

with open("students.txt","w") as file:
    file.writelines(["Ravi\n","Rahul\n","Amit\n"])
with open("students.txt", "r") as file:
    print(file.read())
with open("students.txt","r") as file:
    for line in file:
        print(line)

