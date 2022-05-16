class Fract:
    """
    Принимает числитель и знаменатель в виде целых положительных чисел. Умеет совершать
    стандартные арифметические и логические операции с обыкновенными дробями.
    """
    numer: int
    denom: int
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __str__(self):
        if self.numer == self.denom:
            return '1'
        if self.numer == 0:
            return '0'
        return f'{self.numer}/{self.denom}'

    @staticmethod
    def nod(x, y):  # находим наибольший общий делитель
        x = abs(x)
        y = abs(y)
        while x != 0 and y != 0:
            if x > y:
                x %= y
            else:
                y %= x
        return x + y

    def __add__(self, other):
        a = self.numer * other.denom + self.denom * other.numer
        b = self.denom * other.denom
        gcd = self.nod(a, b)  # gcd - greatest common divisor (наибольший общий делитель)
        return Fract(a // gcd, b // gcd)

    def __iadd__(self, other):
        a = self.numer * other.denom + self.denom * other.numer
        b = self.denom * other.denom
        gcd = self.nod(a, b)
        return Fract(a // gcd, b // gcd)

    def __sub__(self, other):
        if self.numer * other.denom - self.denom * other.numer == 0:
            return Fract(0, 1)
        a = self.numer * other.denom - self.denom * other.numer
        b = self.denom * other.denom
        gcd = self.nod(a, b)
        return Fract(a // gcd, b // gcd)

    def __isub__(self, other):
        if self.numer * other.denom - self.denom * other.numer == 0:
            return Fract(0, 1)
        a = self.numer * other.denom - self.denom * other.numer
        b = self.denom * other.denom
        gcd = self.nod(a, b)
        return Fract(a // gcd, b // gcd)

    def __mul__(self, other):
        a = self.numer * other.numer
        b = self.denom * other.denom
        gcd = self.nod(a, b)
        return Fract(a // gcd, b // gcd)

    def __imul__(self, other):
        a = self.numer * other.numer
        b = self.denom * other.denom
        gcd = self.nod(a, b)
        return Fract(a // gcd, b // gcd)

    def __truediv__(self, other):
        a = self.numer * other.denom
        b = self.denom * other.numer
        gcd = self.nod(a, b)
        return Fract(a // gcd, b // gcd)

    def __itruediv__(self, other):
        a = self.numer * other.denom
        b = self.denom * other.numer
        gcd = self.nod(a, b)
        return Fract(a // gcd, b // gcd)

    def __eq__(self, other):
        a = self.numer * other.denom
        b = self.denom * other.numer
        return a == b

    def __ne__(self, other):
        a = self.numer * other.denom
        b = self.denom * other.numer
        return a != b

    def __gt__(self, other):
        a = self.numer * other.denom
        b = self.denom * other.numer
        return a > b

    def __ge__(self, other):
        a = self.numer * other.denom
        b = self.denom * other.numer
        return a >= b

    def __lt__(self, other):
        a = self.numer * other.denom
        b = self.denom * other.numer
        return a < b

    def __le__(self, other):
        a = self.numer * other.denom
        b = self.denom * other.numer
        return a <= b

print(Fract.__doc__)
a = Fract(1, 2)
b = Fract(2, 4)

c = a + b
print(a, '+', b, '=', c)
c = a - b
print(a, '-', b, '=', c)
c = a * b
print(a, '*', b, '=', c)
c = a / b
print(a, ':', b, '=', c)
print(f'{a} == {b} ---> {a == b}')
print(f'{a} != {b} ---> {a != b}')
print(f'{a} > {b} ---> {a > b}')
print(f'{a} >= {b} ---> {a >= b}')
print(f'{a} < {b} ---> {a < b}')
print(f'{a} <= {b} ---> {a <= b}')
print('-----------------------------------')
a = Fract(4, 7)
b = Fract(2, 5)

c = a + b
print(a, '+', b, '=', c)
c = a - b
print(a, '-', b, '=', c)
c = a * b
print(a, '*', b, '=', c)
c = a / b
print(a, ':', b, '=', c)
print(f'{a} == {b} ---> {a == b}')
print(f'{a} != {b} ---> {a != b}')
print(f'{a} > {b} ---> {a > b}')
print(f'{a} >= {b} ---> {a >= b}')
print(f'{a} < {b} ---> {a < b}')
print(f'{a} <= {b} ---> {a <= b}')

