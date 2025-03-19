#NestedForLoop
for x in range(5):
    for y in range(5):
        print("*")
#-------------------------------------
for x in range(5):
    for y in range(10):
        print("*", end="")
    print("NEW LINE")

#Collection
students = ["irvin","kristel","giji","imbing","keigi"]

for student in students:
    print(students)

#------------------------------------------------------------
courseStudents = [
    ["BSIT", "irvin"],
    ["BSSW", "kristel"],
    ["CRIM", "reneil"],
    ["BSAA", "bien"]
]

print(courseStudents[0][1])

#------------------------------------------------------------
courseStudents = [
    ["BSIT", "irvin"],
    ["BSSW", "kristel"],
    ["CRIM", "reneil"],
    ["BSAA", "bien"]
]

for cs in courseStudents:
    print(cs[1])

#------------------------------------------------------------
courseStudents = [
    ["BSIT", "irvin"],
    ["BSSW", "kristel"],
    ["CRIM", "reneil"],
    ["BSAA", "bien"]
]

for cs in courseStudents:
    for i in cs:
        print(i)

#Activity - my answer
students = [
    ["BSIT", ["irvin","paul"]],
    ["BSSW", ["kristel","keigi","gi"]]
]

for course in students:
    print(course[0])
    for student in course[1]:
        print(student)
    print()