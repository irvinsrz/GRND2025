class Animal:
    def __init__(self,type,voice):
        self.type = type
        self.voice = voice
    
    def speak(self):
        print(self.voice)

    def introduceSelf(self):
        print("i am a " + self.type)
    
aOne = Animal("Dog","Arf")
aOne.speak()
aOne.introduceSelf()

aTwo = Animal("Cat","Meow")
aTwo.speak()
aTwo.introduceSelf()

#Activity
class User:
    def __init__(self,firstname,lastname,likesCount,friendsName):
        self.firstname = firstname
        self.lastname = lastname
        self.likesCount = likesCount
        self.friendsName = friendsName
        print("User Created ", self.firstname)

    def introduceSelf(self):
        print("Hi i'am " + self.firstname , "" , self.lastname)

    def fullProfile(self):
        print("Full Name: ", self.firstname,"", self.lastname)
        print("Likes    : ", self.likesCount)
        print("Friends")
        for fname in self.friendsName:
            print("-",fname)

userOne = User("Irvin","Suarez",100,["Reneil","Justin","Keith","Cyrus"])

userOne.fullProfile()