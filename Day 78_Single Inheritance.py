# single inheritance
class animal:
    def __init__(self,name,species):
        self.name = name 
        self.species = species
        
    def make_sound(self):
        print("Sound made by animal")
        
class dog(animal):
    def __init__(self, name, breed):
        animal.__init__(self, name, species = "dog")
        self.breed = breed 
        
    def make_sound(self):
        print("Bark!")
        
d = dog("Dog", "Bulldog")
d.make_sound

a = animal("Dog", "German shferd")
a.make_sound

# Implement  a cat class by using animal class
class cat(animal):
    def __init__(self, name, breed):
        animal.__init__(self, name, species = "dog")
        self.breed = breed 
        
    def make_sound(self):
        print("meow")
        
c = animal("cat", "German shferd")
c.make_sound