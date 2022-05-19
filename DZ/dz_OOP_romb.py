# Демонстрация работы с классами при ромбовидном наследовании.

class Duck:
    def can(self):
        print(f'{self.__class__.__name__} can fly, swim, run, jump.')

class Dolphin(Duck):
    def can(self):
        print(f'{self.__class__.__name__} can swim, jump out of the water.')

class Crow(Duck):
    def can(self):
        print(f'{self.__class__.__name__} can fly, run, jump.')

# Имеет значение порядок записи классов-родителей при множественном наследовании
class Pigeon(Crow, Dolphin):
    pass

class Shark(Dolphin, Crow):
    pass

a = Duck()
b = Dolphin()
c = Crow()
d = Pigeon()
e = Shark()

a.can()
b.can()
c.can()

print()
print('Порядок поиска функции can, при ее вызове из класса Shark:')
for i in range(len(Shark.__mro__)):
    print(f'{i + 1}) {Shark.__mro__[i]} ')
e.can()

print()
print('Порядок поиска функции can, при ее вызове из класса Pigeon:')
for i in range(len(Pigeon.__mro__)):
    print(f'{i + 1}) {Pigeon.__mro__[i]} ')
d.can()

