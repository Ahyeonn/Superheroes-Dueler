# dog.py
class Dog:
  def __init__(self, name, breed):
    self.name = name
    self.breed = breed
    print("dog initialized!")

  def bark(self):
    print("Woof!")
  
  def sit(self):
    print(f"{self.name} sits")
  
  def roll_over(self):
    print(f"{self.name} rolls over")


# # my_dogs.py
# import dog
# ...

# my_other_dog = dog.Dog("Annie", "SuperDog")
# print(my_other_dog.name)

