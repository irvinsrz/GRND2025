#to create a student info easier with dict

physicalAttributes1 = {
"Height": 164,
"Weight": 60,
"Skin": "Brown"
}
physicalAttributes2 = {
"Height": 154,
"Weight": 50,
"Skin": "White"  
}

student = {
"name": "Irvin",
"course": "BSIT",
"age": 21,
"physical": physicalAttributes1
}       

student2 = {
"name": "Kristel",
"course": "BSSW",
"age": 19,
"physical": physicalAttributes2
}

students = [student,student2]
print(student.get("physical").get("Weight"))