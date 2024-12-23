from math import pi, sqrt


class Figure:
    sides_count = 0

    def __init__(self, rgb=(0, 0, 0), *sides):
        if self.__is_valid_color(*rgb) is True:  # На всякий случай "защитил" от некорректного ввода значений.
            self.__color = list(rgb)
            self.filled = True  # filled реализовал так
        else:
            self.__color = [0, 0, 0]
            self.filled = False
        if self.__is_valid_sides(*sides) is True:
            self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        for i in (r, g, b):
            if 255 > i > 0 and isinstance(i, int):
                return True
            else:
                return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b) is True:
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        bool_sides = []
        for side in sides:
            if isinstance(side, int) and side > 0:
                side = True
                bool_sides.append(side)
        if len(sides) == self.sides_count and [True] * len(sides) == bool_sides:
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, rgb=(0, 0, 0), *sides):
        super().__init__(rgb, *sides)
        self.__radius = sum(sides) / (2 * pi)

    def get_square(self):
        return pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        a, b, c = self.get_sides()
        p = sum(self.get_sides()) / 2
        return sqrt(p * (p - a) * (p - b) * (p - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, rgb=(0, 0, 0), *sides):
        super().__init__(rgb, *sides)
        if self.__is_valid_sides(*sides) is True:
            self.__sides = list(sides) * self.sides_count
        else:
            self.__sides = [1] * self.sides_count

    def __is_valid_sides(self, *sides):
        if len(sides) == 1 and sum(sides) > 0 and isinstance(sum(sides), int):
            return True
        else:
            return False

    def __len__(self):
        return sum(self.__sides)

    def get_sides(self):
        return self.__sides

    def get_volume(self):
        return int((sum(self.__sides) / self.sides_count) ** 3)


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())
cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())
print(len(circle1))
print(cube1.get_volume())

# Консоль

# [55, 66, 77]
# [222, 35, 130]
# [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
# [15]
# 15
# 216


# print('------- Tests ------')
#
# circle = Circle((200, 200, 100), 10, 15, 6)  # [1]
# triangle1 = Triangle((200, 200, 100), 10, 6)  # [1, 1, 1]
# cube = Cube((200, 200, 100), 9)  # [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
# cube2 = Cube((200, 200, 100), 9, 12)  # [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#
# print(circle.get_sides())
# print(triangle1.get_sides())
# print(cube.get_sides())
# print(cube2.get_sides())
#
# print('-------------')
#
# print(circle1.get_square())  # 7.9577471545947684
# print(triangle1.get_square())  # 0.4330127018922193
#
# print(len(cube1))  # 72
# print(len(triangle1))  # 3