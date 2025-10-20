class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)



rect1 = Rectangle(5, 10)
rect2 = Rectangle(3, 7)
rect3 = Rectangle(8, 12)


for i, rect in enumerate([rect1, rect2, rect3], start=1):
    print(f"Прямоугольник {i}:")
    print(f"  Площадь: {rect.area()}")
    print(f"  Периметр: {rect.perimeter()}")



class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        result = self.a + self.b
        print(f"Сложение: {self.a} + {self.b} = {result}")

    def multiplication(self):
        result = self.a * self.b
        print(f"Умножение: {self.a} * {self.b} = {result}")

    def division(self):
        if self.b != 0:
            result = self.a / self.b
            print(f"Деление: {self.a} / {self.b} = {result}")
        else:
            print("Ошибка: Деление на ноль!")

    def subtraction(self):
        result = self.a - self.b
        print(f"Вычитание: {self.a} - {self.b} = {result}")


