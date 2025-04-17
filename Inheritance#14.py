#1
#Parent Class
class person:
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
        
    def introduce(self):
        print("Hi I'am " + self.firstName + " " + self.lastName)



#Child Class

class Student(person):
    pass

pOne = person("Irvin","Suarez")
pOne.introduce()

sOne = Student("Kristel","Maranan")
sOne.introduce()

#2 Adding Attributes
#Parent Class
class person:
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
        
    def introduce(self):
        print("Hi I'am " + self.firstName + " " + self.lastName)
    


#Child Class

class Student(person):
    def __init__(self, firstName, lastName,sectionYear):
        super().__init__(firstName, lastName)
        self.sectionYear = sectionYear


pOne = person("Irvin","Suarez")
pOne.introduce()

sOne = Student("Kristel","Maranan","2A")
sOne.introduce() 
sOne.sectionYear()

#3
#Parent Class
class person:
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
        
    def introduce(self):
        print("Hi I'am " + self.firstName + " " + self.lastName)
    


#Child Class

class Student(person):
    def __init__(self, firstName, lastName,sectionYear):
        super().__init__(firstName, lastName)
        self.sectionYear = sectionYear


    def introduce(self):
        print("Hi I'am " + self.firstName + " " + self.lastName + " From " + self.sectionYear)

pOne = person("Irvin","Suarez")
pOne.introduce()

sOne = Student("Kristel","Maranan","2-B")
sOne.introduce()

#4
#Parent Class
class person:
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
        
    def introduce(self):
        print("Hi I'am " + self.firstName + " " + self.lastName)
    


#Child Class

class Student(person):
    def __init__(self, firstName, lastName,sectionYear):
        super().__init__(firstName, lastName)
        self.sectionYear = sectionYear


    def introduce(self):
        super().introduce()

pOne = person("Irvin","Suarez")
pOne.introduce()

sOne = Student("Kristel","Maranan","2-B")
sOne.introduce()

    
class Employee(person):
    def __init__(self,firstName,lastName,salary):
        super().__init__(firstName,lastName)
        self.salary = salary

    def introduce(self):
        super().introduce()
        print("My Salary is " + str(self.salary))

eOne = Employee("Irvin","Kristel",200000)
eOne.introduce()

#5
#Parent Class
class person:
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
        
    def introduce(self):
        print("Hi I'am " + self.firstName + " " + self.lastName)
    


#Child Class

class Student(person):
    def __init__(self, firstName, lastName,sectionYear):
        super().__init__(firstName, lastName)
        self.sectionYear = sectionYear


    def introduce(self):
        super().introduce()

    def saySection(self):
        print(self.sectionYear)    

    
class Employee(person):
    def __init__(self,firstName,lastName,salary):
        super().__init__(firstName,lastName)
        self.salary = salary

    def introduce(self):
        super().introduce()
        print("My Salary is " + str(self.salary))

    def saySalary(self):
        print("Salary: " + str(self.salary))
pOne = person("Irvin","Suarez")
pOne.introduce()

sOne = Student("Kristel","Maranan","2-B")
sOne.introduce()
sOne.saySection()

eOne = Employee("Irvin","Kristel",200000)
eOne.introduce()
eOne.saySalary()
