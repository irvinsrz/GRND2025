age = 12

while age < 18:
    print("Still Young:" , str(age))
    age = age + 1

#Else is added to the bottom of a while loop
age = 12

while age < 18:
    print("Still Young:" , str(age))
    age = age + 1
else: 
    print("Legal Age:", str(age))

#While loop can be used to acces item in collection(List & Tuples)
studentID = [2001,2002,2003,2004]

i = 0 

while i <= 3:
    print(studentID[i])
    i = i + 1

#--------------------------------------------------------------------#
studentID = [2001,2002,2003,2004,2005,2006]

i = 0 

while i < len(studentID):
    print(studentID[i])
    i = i + 1

#Break keyword
while True:
    print("Hello World")
    break

#Conditional Statement inside a WHILE loop
print("Enter a missing Letter(Big Letter Only!)")
print("\tGa_l_")

while True:
    answer = input("Answer: ")
    
    if answer == "GAILE":
        print("You're Correct!")
        print("The Answer is", ans)
        break
    else:
        print("Please Try Again!")
#----------------------------------------------------
numbers = [1,2,3,4,5,6,7,8,9,10]

i = 0

while i < len(numbers):
    if (numbers[i] % 2 == 0):
        print("Even number", str(numbers[i]))
    else:
        print("Odd number", str(numbers[i]))
    i = i + 1

#ACTIVITY
#MY ANSWER
lives = 2
print("MATH QUESTION")


while True:
    question = input("100 + 120 = ")
    
    if question == "220":
        print("You Won!")
        break
    elif lives == 0:
        print("You Lose!")
        break
    else:
        print("Try Again")
    
        lives = lives - 1

#SDPT ANSWER
lives = 3
print("MATH QUESTION")

answer = 150

while lives > 0:
    question = int(input("100 + 50: "))
    if question == answer:
        print("You Won!")
        break
    else:
        print("Try Again")
        lives = lives - 1
else:
    print("You Lose!")
    