class Animals:
    def __init__(self, category, name):
        self.category = category
        self.name = name


class Wilds(Animals):
    def __init__(self, category, name, dangerous):
        super().__init__(category, name)
        self.dangerous = True


wild_1 = Wilds('wild', 'elephant', False)


def n_awful(self):
    return "I'm not dangerous"


wild_2 = Wilds('wild', 'lion', True)


def awful(self):
    return "I am dangerous"


class Pets(Animals):
    def __init__(self, category, name, friendly):
        super().__init__(category, name)
        self.friendly = True


pet_1 = Pets('pet', 'dog', True)

pet_2 = Pets('pet', 'cat', False)


class Farm(Animals):
    def __init__(self, category, name, spending):
        super().__init__(category, name)
        self.__spending = spending

    def get_spending(self):
        return f'My cost is {self.__spending}'


farm_1 = Farm('farm', 'cow', '20 000')

farm_1.name = 'duck'
print(farm_1.name)
print(wild_2.category)
print(pet_1.name)
# print(farm_1.spending)

farm_1.__spending = '90'
print(farm_1.__spending)

# farm_1.set_spending = '333'
# print(farm_1.get__spending)

# class ZooAnimal:
#     def __init__(self, category, name, color):
#         self.category = category
#         self._name = name
#         self.__color = color
#
#     # getter method
#     def get_name(self):
#         return self._name
#
#     # setter method
#     def set_name(self, x):
#         self._name = x

# rhino = ZooAnimal('herbivorous', 'rhino', 'gray')
#
# rhino.category = 'predator'
# rhino._name = 'hippo'
# rhino.__color = 'red'
#
# print(rhino.category, rhino._name, rhino.__color)

# # setting the age using setter
# raj.set_age(21)
#
# # retrieving age using gettergi
# print(raj.get_age())
#
# print(raj._age)

