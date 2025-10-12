class Dog:
    def __init__ (self,color,breed):
        self.color = color
        self.breed = breed

Milo = Dog("Brown","German Shepherd")
Scooby = Dog("Beige","Pomerainian")

print("Milo is a {} colored {}".format(Milo.color,Milo.breed))
print("Scooby is a {} colored {}".format(Scooby.color,Scooby.breed))