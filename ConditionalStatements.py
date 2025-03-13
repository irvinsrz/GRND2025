#indentation 
age = eval(input("Enter your age: "))

if age >= 18:
    print("Legal Age")
print("Under Age")

#Two Conditions
age = eval(input("Enter your age: "))

if age >= 18:
    print("Legal Age")
else:
    print("Too Young")

#Three or More Conditions
age = eval(input("Enter your age: "))

if age >= 18:
    print("Legal Age")
elif age >= 13:
    print("Teenager")
else:
    print("Too Young")

#Condition Inside a Condition
age = eval(input("Enter your age: "))

if age >= 18:
    height = eval(input("Enter your Height: "))
    
    if height >= 170:
        print("Legal Age and Tall")
    elif height >= 156:
        print("Legal Age and Average")
    else:
        print("Legal Age and Short")
else:
    print("Too Young")

#Invert the condition value
if not age >= 18:
    print("Too Young")
else:
    print("Legal Age")

#Logical Operators
age = eval(input("Enter your age: "))
height = eval(input("Enter your Height: "))   

if age >= 18 and height >= 170:
    print("Legal Age and Tall")
elif age >= 18 and height >= 156:
    print("Legal Age and Average")
elif age >= 18:
    print("Legal Age and Short")
else:
    print("Too Young")

#Logical Operators #2
if username == "irvin" and password == "suarez":
    print("Welcome Irvin")
elif username == "kristel" and password =="maranan":
    print("Welcome Kristel")
else:
    print("Please Try Again")

#Logical Operators #3
hasMeterStick = False
hasRuler = True

if hasMeterStick or hasRuler == True:
    print("Come in")
else:
    print("Go Out")

#Used to check an item
bag = ["Wallet","Gun","Money"]

if "Gun" in bag:
    print("HULI!")
else:
    print("Welcome")

#Activity
GradeOne = float(input("Enter Your Grade: "))
GradeTwo = float(input("Enter Your Grade: "))
GradeThree = float(input("Enter Your Grade: "))
Avg = (GradeOne + GradeTwo + GradeThree) / 3
print(Avg)

if Avg > 100 or Avg <= 50:
    print("Invalid Grade")
elif Avg >= 98 or Avg == 100:
    print("With Highest Honor")
elif Avg >= 95 or Avg >= 97:
    print("With High Honors")
elif Avg >= 90 or Avg >= 94:
    print("With Honors")
elif Avg >= 75 or Avg >= 89:
    print("Passed")
elif Avg >= 74 or Avg <=51:
    print("Failed")
else:
    print("okay!")

