class Car:
    def __init__(self, model, speed):
        self._model = model
        self._speed = speed

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if value < 0:
            raise ValueError("Скорость не может быть отрицательной!")
        self._speed = value


car = Car("Romka", 120)
print(car.speed)

car.speed = 150
print(car.speed)
