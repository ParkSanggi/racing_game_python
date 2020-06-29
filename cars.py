from input_view import InputView
from car import Car
from names import Names


class Cars:

    def __init__(self, names):
        self.cars = []
        name = names.next()
        while name:
            self.cars.append(Car(name))
            name = names.next()


if __name__ == "__main__":
    names = Names()
    cars = Cars(names)
    print(cars.cars)



