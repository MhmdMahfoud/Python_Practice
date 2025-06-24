records = [
["Layla", 89], ["Tariq", 77], ["Layla", 91], ["Jana", 100], ["Tariq", 84],
["Ziad", 62], ["Jana", 97], ["Tariq", 73], ["Ziad", 71], ["Layla", 86],
["Jana", 94], ["Ziad", 75]
]

class_journal = {
}
for name,grade in records:
    if name in class_journal:
        class_journal[name].append(grade)
    else:
            class_journal[name] = [grade]

for name in class_journal:
     grade=class_journal[name]
     avg =sum(grade)/len(grade)
     print("Name: " + name)
     print("Grades: " + str(grade))
     print("Average: " + str(round(avg, 2)))

highest_avg = 0
top_student = ""
most_consistent = ""
smallest_range = float('inf')
students_below_70 = []
for name in class_journal:
     grades = class_journal[name]
     avg = sum(grades) / len(grades)
     max_grade = max(grades)
     min_grade = min(grades)
     grade_range = max_grade - min_grade
if avg > highest_avg:
        highest_avg = avg
        top_student = name
if grade_range < smallest_range:
    smallest_range = grade_range
    most_consistent = name
if any(g < 70 for g in grades):
        students_below_70.append(name)

with open("report.txt", "w") as file:
      file.write(" CLASS REPORT \n\n")
      file.write("1. Highest Average:\n")
      file.write("   " + top_student + " with " + str(highest_avg) + "\n\n")
      file.write("2. Most Consistent Performance:\n")
      file.write("   " + most_consistent + " with a grade range of " + str(smallest_range) + "\n\n")
      file.write("3. Students with at least one grade below 70:\n")
      if students_below_70:
        file.write("   " + ", ".join(students_below_70) + "\n\n")
      else:
        file.write("   None\n\n")