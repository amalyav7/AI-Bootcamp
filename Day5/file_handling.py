import os
from pathlib import Path
import csv

print("CWD", os.getcwd())

with open("notes.txt", "r") as file:
    contents = file.read()
    
print(contents)

with open("notes.txt", "r") as file:
    for line in file:
        print("Line:", line.strip())
with open("output.txt", "w") as file:
    file.write("This file was created \n")
    file.write("by my program \n")
with open("output.txt", "a") as file:
    file.write("Adding one more line.\n")
    
students = [
    ["Name", "Grade", "Score"],
    ["Priya", 9, 97],
    ["Marcus", 9, 84],
]

with open("new_students.csv", "w",
            newline="") as file:
    writer = csv.writer(file)

    writer.writerows(students)

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({
            "Name": row["Name"],
            "Score": int(row["Score"])
            })
total = sum(s["Score"] for s in students)
average = total / len(students)


with open("above_average.txt", "w") as file:
    file.write(f"Class average: {average:.1f}\n")

    for s in students:
    
        if s["Score"] > average:
        
            file.write(f"- {s['Name']} ({s['Score']})\n")
