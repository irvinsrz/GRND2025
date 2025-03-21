def sayHello():
    print("Hello")

sayHello()

#Arguments
def sayHello(name):
    print("Hello",name)

sayHello("irvin")

#---------------------------------
def sayHello(name):
    print("Hello",name)

name = input("Enter name: ")
sayHello(name)

#Return Values
def add(numOne,numTwo):
    return numOne + numTwo

sum = add(5,3)

print(sum)

#-------------------------------------
def LegalAge(age):
    if age >= 18:
        return True
    else:
        return False

print(LegalAge(18))


#Activity

