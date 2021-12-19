"""class Pet:
    def __init__(self, name, age=0):    # NAME OF THE CONSTRUCTOR METHOD
        self.name = name    # SELF = POINTER TO THE CURRENT INSTANCE
        self.age = age

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def celebrate_birthday(self):
        self.age += 1

"""


class Animal:
    def __init__(self, weight_kg,num_legs):
        self._weight_kg = weight_kg
        self.num_legs = num_legs

    def __get_weight_kg_per_leg(self):
        print(self.weight_kg/self.num_legs)

    def set_weight_kg(self, weight):
        self._weight_kg = weight

    def get_weight_kg(self):
        return self._weight_kg

    def get_weight_grams_per_leg(self):
        print(self._weight_kg/self.num_legs/0.001)


dog_caesar = Animal(10, 4)
parrot_barney = Animal(1, 2)

dog_caesar.get_weight_grams_per_leg()
parrot_barney.get_weight_grams_per_leg()






"""pet = Pet("Lilo")
print(pet.get_age())
pet.celebrate_birthday()
print(pet.get_age())
"""






