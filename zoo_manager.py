class Animal:
    def __init__(self,
            name:str,
            species:str,
            sound:str):
        self._name = name
        self._species = species
        self._sound = sound
    
    def speak(self):
        return self._sound

class Mammal(Animal):
    def __init__(self, 
            name, 
            species, 
            sound):
        super().__init__(name, species, sound)
    
    def give_birth(self):
        print(f"Mammal: {self._name} has given birth")

class Bird(Animal):
    def __init__(self,
            name:str,
            species:str,
            sound:str,
            wingspan:int):
        super().__init__(name, species, sound)
        self._wingspan = wingspan

class Reptile(Animal):
    def __init__(self,
            name:str,
            species:str,
            sound:str):
        super().__init__(name, species, sound)
    
    def bask_in_sun(self):
        print(f"{self._name} is basking in the sun")

class Primate(Mammal):
    def __init__(self, 
            name, 
            species, 
            sound):
        super().__init__(name, species, sound)
    
    def climb_trees(self):
        print(f"{self._name} is climbing trees")

class Marsupial(Mammal):
    def __init__(self, 
        name, 
        species, 
        sound):
        super().__init__(name, species, sound)

    def carry_babies(self):
        print(f"{self._name} is carrying its baby")


class 
        


goat = Mammal("goat", "mammal", "bahhh")
eagle = Bird("Eagle", "bird", "KAAW", 20)
print(goat._name)
print(goat._species)
print(f"\n{eagle._wingspan}")

gator = Reptile("gator", "reptile", "croak")

gator.bask_in_sun()

monkey = Primate("Monkey", "Primate", "ooh")

monkey.climb_trees()

opossum = Marsupial("Opossum", "Marsupial", "hisss")

opossum.carry_babies()