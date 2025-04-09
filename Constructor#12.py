#1
class Character:
    def __init__(self):
        print("Character Created!")

charOne = Character()
charTwo = Character()

#Self Parameter
class Character:
    def __init__(self,name,hp,mp,atk,lvl):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.atk = atk
        self.lvl = lvl

        print("Created " + self.name)

charOne = Character("irvin",100,50,12,2)
charTwo = Character("Kristel",101,51,13,3)


