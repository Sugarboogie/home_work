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




class SidebarButton:
    def __init__(self, text):
        self.text = text
        self.type = "Кнопка"
        self.locator = ""

    def click(self):
        return f "Клик по кнопке {self.text}"



button_texts = [
    "Text Box",
    "Check Box",
    "Radio Button",
    "Web Tables",
    "Buttons",
    "Links",
    "Broken Links - Images",
    "Upload and Download",
    "Dynamic Properties"
]


buttons = [SidebarButton(text) for text in button_texts]

for btn in buttons:
    print(f"Текст кнопки: {btn.text}")


for btn in buttons:
    print(btn.click())


# file: car.py

class Car:
    def __init__(self, color: str = None, type_: str = None, year: int = None):
        self.color = color
        self.type = type_
        self.year = year

    # i
    def start(self):
        print("Автомобиль заведен")

    # ii
    def stop(self):
        print("Автомобиль заглушен")

    # iii — присвоение года выпуска
    def set_year(self, year: int):
        self.year = year

    # iv — присвоение типа
    def set_type(self, type_: str):
        self.type = type_

    # v — присвоение цвета
    def set_color(self, color: str):
        self.color = color


if, year: in== "__main__":
    car = Car()
    car.start()
    car.set_year(2020)
    car.set_type("седан")
    car.set_color("синий")
    car.stop()
    print(f"Итог: {car.year=}, {car.type=}, {car.color=}")




class Checks:
    def __init__(self, loc: str):
        self.loc = loc

    def check_text(self):
        return self.loc


# file: python_trening/task_9_oop_1.py

from task_9_checks import Checks



class TextBoxButton(Checks):
    def __init__(self):
        super().__init__(loc="Text Box")
        self.type = "Кнопка"
        self.locator = ""

    def click(self):
        return f"Клик по кнопке {self.loc}"

class CheckBoxButton(Checks):
    def __init__(self):
        super().__init__(loc="Check Box")
        self.type = "Кнопка"
        self.locator = ""

    def click(self):
        return f"Клик по кнопке {self.loc}"

class RadioButton(Checks):
    def __init__(self):
        super().__init__(loc="Radio Button")
        self.type = "Кнопка"
        self.locator = ""

    def click(self):
        return f"Клик по кнопке {self.loc}"

class WebTablesButton(Checks):
    def __init__(self):
        super().__init__(loc="Web Tables")
        self.type = "Кнопка"
        self.locator = ""

