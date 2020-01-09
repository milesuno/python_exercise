class Dog:
    def __init__(self, name, leg_count, pattern):
        self.name = name
        self.legs = leg_count
        self.fur = pattern

    def bark(self):
        print(f"Woof, my name is {self.name}")


beagel = Dog("Bagel", 4, "Stripped")
boxer = Dog("Tyson", 3, "Black")
beagel.bark()
boxer.bark()

print(beagel.legs)
print(boxer.fur)