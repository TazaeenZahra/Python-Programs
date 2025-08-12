records = [
    "Ali,Math,88",
    "Sara,English,92",
    "Ali,English,76",
    "Sara,Math,85",
    "Bilal,Math,70",
    "Bilal,English,82"
]

students={}
for i in records:
    name,subject,marks=i.split(",")
    marks=int(marks)
    # add info into dict
    if name not in students:
    # create student name key dict
        students[name]={}
    students[name][subject]=marks

# print(students.items())

# calculate average marks of each student
for name,subjects_marks in students.items():
    total=sum(subjects_marks.values())
    avg=total/len(subjects_marks)

    print(f"Name: {name}\nMarks gained in Subjects: {subjects_marks}\nAverage Marks: {avg:.2f}\n")