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