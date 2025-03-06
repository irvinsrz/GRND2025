# + INDEX     0      1      2     3       4
# - INDEX   -5      -4     -3    -2      -1
courses = ["BSIT","BSCS","BLIS","BSSW","BSE"]
courses2 = ["ENTREP","DHRS"]
#Append or Adding a new course
courses[0] = "GG"
courses.append("awaw")

#Insert or Insert anywhere
courses.insert(1,"BSPA")

#Remove or Deleting
courses.remove("BSIT")

#Pop or not specified delete last item
courses.pop("BSCS")

#Del or not specified delete whole list
del courses[0]

#Clear or deletes all value in a list
courses.clear()

#Copy the whole list
courses2 = courses.copy()

#Combining List
courses3 = courses + courses2

#Extend like Combining List
courses.extend(courses2)

#Reverse
courses.reverse()

#Sort List item by Alphabet
courses.sort()

#sublist List inside a List
#Index   0   1   2       3  [][]
List = ["A","B","C"["D","E","F"]]

#Tuples Read only using ()
courses = ("BSIT","BSSW","BSA")

#Convert Tuple to List 
#Convert List to Tuple

courses = list(courses)
courses = tuple(courses)


print(courses2)