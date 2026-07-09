class Animal:
    def __init__(self,
            name:str,
            species:str,
            sound:str):
        self._name = name
        self._species = species
        self._sound = sound
    
    def speak(self):
        print(self._sound) 
    
    def __repr__(self):
        return f"Name: {self._name}"

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




class Enclosure:
    def __init__(self,
                 animals:list[Animal]=[]):
        self._animals = animals
    
    def add_animals(self, *new_animals):
        self._animals.extend(new_animals)

    @property
    def animals(self):
        return f"{self._animals}"


class Aviary(Enclosure):
    def sqwuak(self):
        for animal in self._animals:
            animal.speak()

    

class ReptileEnclosure(Enclosure):
    pass




eagle = Bird("Eagle", "bird", "KAAW", 20)
gator = Reptile("Gator", "reptile", "croak")

enclosure1 = Aviary([eagle])

print(enclosure1.animals)

enclosure1.sqwuak()

enclosure2 = ReptileEnclosure([gator])

print(enclosure2.animals)

























# print(f"enclosure one has: {enclosure1.birds}")



# goat = Mammal("goat", "mammal", "bahhh")

# print(goat._name)
# print(goat._species)
# print(f"\n{eagle._wingspan}")


# gator.bask_in_sun()

# monkey = Primate("Monkey", "Primate", "ooh")

# monkey.climb_trees()

# opossum = Marsupial("Opossum", "Marsupial", "hisss")

# opossum.carry_babies()