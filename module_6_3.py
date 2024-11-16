from random import randint


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    _cords = [0, 0, 0]
    speed = 0

    def move(self, dx, dy, dz):
        self._cords[0] = dx * self.speed
        self._cords[1] = dy * self.speed
        if dz * self.speed < 0:
            print("It’s too deep, i can’t dive :(")
        else:
            self._cords[2] = dz * self.speed

    def get_cords(self):
        print(f"X:{self._cords[0]}, Y:{self._cords[1]}, Z:{self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        print(f"Here are(is) {randint(1, 4)} eggs for you")


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def div_in(self, dz):
        self._cords[2] = int(abs(dz / (2 * self.speed)))


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    sound = "Click-click-click"

    def __init__(self, speed):
        self.speed = speed

    def dive_in(self, dz):
        super().div_in(dz)


db = Duckbill(10)
print(db.live)
print(db.beak)

db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()

# Вывод на консоль:

# True
# True
# Click-click-click
# Be careful, i'm attacking you 0_0
# X:10, Y:20, Z:30
# X:10, Y:20, Z:0
# Here are(is) 3 eggs for you  # Число может быть другим (1-4)
