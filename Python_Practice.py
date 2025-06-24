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
     