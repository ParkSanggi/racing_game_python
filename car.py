from random import randint
from output_view import OutputView


class Car:

    __GO_CONDITION = 4

    def __init__(self, name):
        self.__name = name
        self.__position = 0

    def get_position(self):
        return self.__position

    def try_to_go_ahead(self):
        if randint(0, 9) > self.__GO_CONDITION:
            self.__position += 1

    def inform_position(self):
        OutputView.output_car_position(self.__name, self.__position)

    def is_win(self, car):
        return self.__position > car.get_position()

    def is_draw(self, car):
        return self.__position == car.get_position()

    def get_name(self):
        return self.__name

