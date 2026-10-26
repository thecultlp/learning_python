"""Create a file marks.txt containing:

Plain Text
90
85
78
92
88

Then write a program to:

Read all marks from the file.
Calculate the total.
Calculate the average.
Print:"""
with open("marks.txt","w") as file:
    file.writelines(["90\n","85\n","78\n","92\n","88"])
with open("marks.txt","r") as file:
        content = file.readlines()
        #print(content)
total = 0
subjects = 0
for mark in content:
      subjects += 1
      total += int(mark.strip())
average = total / subjects
print(f"Total: {total}")
print(f"Average: {average}")


