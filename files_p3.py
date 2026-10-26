with open("students.txt","w") as file:
    file.writelines(["Ravi,90\n"
"Rahul,85\n"
"Amit,78\n"
"John,92\n"])
with open("students.txt","r") as file:
    content = file.readlines()
# print(content)
students = {}
for line in content:
    name, marks = line.strip().split(",")
    students[name] = int(marks)
print(students)