from collections import namedtuple

Dog = namedtuple('Dog',['age','breed','name'])
sammy = Dog(age = 5,breed = 'Husky', name = 'sam')
print(sammy)
print(type(sammy))
print(sammy.breed)
print(sammy.name)
print(sammy[0])