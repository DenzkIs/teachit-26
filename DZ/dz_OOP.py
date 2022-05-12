class Animals:
    def __init__(self, sound, name):
        self.sound = sound
        self.name = name
        self.__color = 'Black'  # private encapsulation for example

    def __str__(self):
        return f'Name: {self.name}, sound: {self.sound}, color: {self.__color}  |  Class {self.__class__.__name__}'

    def info(self):
        print(f'{self.__color} {self.name} says {self.sound}.')


class Cats(Animals):  # наследуется
    pass


class Dogs(Animals):  # наследуется
    pass


class Birds(Animals): # наследуется
    # полиморфизм, переопределяю метод __init__
    def __init__(self, sound, name, flight_altitude):
        super().__init__(sound, name)
        self.flight_altitude = flight_altitude

    def fly(self):
        print(f'{self.name} can fly high {self.flight_altitude} km.')


cat = Cats('Myaw', 'Tom')
dog = Dogs('Woow', 'Reks')
bird = Birds('Karrr', 'Gosha', 2)

print(f'{cat._Animals__color} {cat.name} says {cat.sound}.')  # вариант доступа к приватному свойству
print(f'{dog._Animals__color} {dog.name} says {dog.sound}.')
print(f'{bird._Animals__color} {bird.name} says {bird.sound}.')
print('----------------------')
print(cat)
print(dog)
print(bird)
print('----------------------')
cat.info()
dog.info()
bird.info()
bird.fly()
