"""
Author: FaDr_YL (_YL_)
"""


class Animal:
    type = "Animal"
    age = 0

    def get_animal_class(self):
        return "Animal"

    def get_class_pos(self):
        return 0

    def __len__(self):
        # override __len__() to return the age which is the "length" of animals.
        return self.age

    def __str__(self):
        return "type: " + self.type + ", age: " + str(self.age)


class Mammal(Animal):
    def get_class_pos(self):
        return 1


class Panda(Mammal):
    type = "Panda"

    def get_animal_class(self):
        # super().<function name>
        return super().get_animal_class() + " Panda"


if __name__ == "__main__":
    a_panda = Panda()
    print(a_panda.type)
    print(a_panda.get_animal_class())
    print("len:", len(a_panda))
    print("str: " + str(a_panda))

