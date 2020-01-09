class Dog:
    def __init__(self, name, legCount, pattern):
        self.name = name
        self.legs = legCount
        self.fur = pattern

    def bark(self):
         print(f"Woof, my name is {self.name}")


beagel = Dog( "Bagel", 4, "Stripped")

boxer = Dog("Tyson", 3, "Black")
boxer.bark()
print(beagel.bark())
print(boxer.fur)