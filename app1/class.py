class Things:
    pass
class Inanimate(Things):
    pass
class Animate(Things):
    pass
class Sidewalks(Inanimate):
    passs
class Animals(Animate):
    pass
class Mammals(Animals):
    pass
class Giraffes(Mammals):
    pass
reginald = Giraffes()
class Animal:
    def __init__(self,species,number_of_legs,color):
        self.species = species
        self.number_of_legs = number_of_legs
        self.color = color
harry = Animal('hippogriff', 6, 'pink')
print(harry.species)
import copy
harry = Animal('hippogriff',6,'pink')
harriet = copy.copy(harry)
print('harriet.species is',harriet.species)
carrie = Animal('chimera',4,'green polka dots')
billy = Animal('bogill',0,'paisley')
my_animals = [harry,carrie,billy]
more_animals = copy.copy(my_animals)
print('more_animals[0].species is',more_animals[0].species)
print('more_animals[1].species is',more_animals[1].species)
more_animals[0].species = 'ghoul'
print('more_animals[0].species is',more_animals[0].species)
