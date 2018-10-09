class Pet:
    pass

class Cat(Pet):
    pass

print(issubclass(Pet, Cat))
print(issubclass(Cat, object))
print(isinstance(Cat(), Cat))
print(issubclass(Cat, Pet))
print(isinstance(Cat(), Pet))


print(dict.fromkeys((1,2)))
a = dict()
print(a.fromkeys((1,2)))