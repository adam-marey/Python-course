
# Creating and Manipulating a Person Class

# Steps to the assignment:

# Create a Person Class.  Include the following attributes
# Height
# Weight
# Hair color
# Date of Birth
# Shoe Size
# Glove Size
# Skin color

# Create an Animal Class.  Include the following attributes
# Type of animal
# Weight
# Good as a Pet
# LifeSpan
# Can fly Yes/No
# Can Swim Yes/No

class Person:
  def details(self,height,weight,hairColor,DOB,shoeSize,gloveSize,skinColor):
    self.height = height
    self.weight = weight
    self.hairColor = hairColor
    self.DOB = DOB
    self.shoeSize = shoeSize
    self.gloveSize = gloveSize
    self.skinColor = skinColor

class Animal:
  def characteristics(self,typeOfAnimal,weight,goodAsApet,lifeSpan,canFly,canSwim):
    self.typeOfAnimal = typeOfAnimal
    self.weight = weight
    self.goodAsApet = goodAsApet
    self.lifeSpan = lifeSpan
    self.canFly = canFly
    self.canSwim = canSwim
    print("\n\tType of animal: ",self.typeOfAnimal)
    print("\tWeight: ",self.weight)
    print("\tGood as a Pet: ",self.goodAsApet)
    print("\tLife Span: ",self.lifeSpan,"Years")
    print("\tCan Fly: ",self.canFly)
    print("\tCan Swim: ",self.canSwim)
class ExtraDetails(Person):
  def allDetails(self,height,weight,hairColor,DOB,shoeSize,gloveSize,skinColor,hatSize):
    Person.details(self,height,weight,hairColor,DOB,shoeSize,gloveSize,skinColor)
    self.hatSize = hatSize
    print("\n\tHeight:",self.height)
    print("\tWeight:",self.weight)
    print("\tHair Color:",self.hairColor)
    print("\tDate of Birth:",self.DOB,"(DayMonthYear)")
    print("\tShoe Size:",self.shoeSize)
    print("\tGlove Size:",self.gloveSize)
    print("\tSkin Color:",self.skinColor)
    print("\tHat Size:",self.hatSize)

peter = ExtraDetails()
print("... Details of Peter ...")
peter.allDetails(6.3, 150, "Black", 16081995, 9, 5, "White", 22)
print("\n")
dog = Animal()
print('... Characteristics of Dog ...')
dog.characteristics("Dog", 48, "Yes", 30, "No", "Yes")
