#1
class Character:
    name = "Name"
    hp = 100
    mp = 50 
    atk = 12
    lvl = 1

CharacterOne = Character()
CharacterTwo = Character()

CharacterOne.name = "Kristel"
CharacterOne.hp = 200

print(CharacterOne.name)
print(CharacterTwo.name)

#2

class Product:
    ID = 1000
    name = "Name"
    qty = 0

ProductOne = Product()
ProductOne.ID = 1001
ProductOne.name = "Milk"
ProductOne.qty = 10

print(ProductOne.ID)
print(ProductOne.name)
print(ProductOne.qty)
