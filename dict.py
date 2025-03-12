#to create a student info easier with dict
student = {
"name": "Irvin",
"course": "BSIT",
"age": 21
}       

student2 = {
"name": "Kristel",
"course": "BSSW",
"age": 19
}
#Age only or specify anything u want
print(student["age"])

#Changing the value using Assignment operator "="
student["name"] = "Imbing"

#Len you can check how many key pair inside the dictionary
len(student)

#Add item on a dictionary non-existent key
student2["super"] = "Beautiful"

#pop deletes an item based on their key value
student.pop("age")

#popitem deletes the last inserted item on the dictionary
student.popitem()

#copying a dictionary
student3 = student.copy()

#printing keys without the values
student.keys()

#printing values without the keys
student.values()

#creating a dictionary inside a list
students = [student,student2]
print(students[1].get("age"))

#Dictionary inside a dictionary
physicalAttributes1 = {
"Height": 164,
"Weight": 60,
"Skin": "Brown"
}
student = {
"name": "Irvin",
"course": "BSIT",
"age": 21,
"physical": physicalAttributes1
}   

physicalAttributes2 = {
"Height": 154,
"Weight": 50,
"Skin": "White"  
}
student2 = {
"name": "Kristel",
"course": "BSSW",
"age": 19,
"physical": physicalAttributes2
}
print(student[1].get("physical").get("Weight"))
print(student[0].get("physical").get("Height"))

