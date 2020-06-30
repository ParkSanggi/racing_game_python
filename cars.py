from car import Car
from names import Names
from output_view import OutputView


class Cars:

    def __init__(self):
        self.__cars = list()
        car_names = Names()
        name = car_names.get_next_name()
        while name:
            self.__cars.append(Car(name))
            name = car_names.get_next_name()

    def try_to_go_ahead(self):
        for car in self.__cars:
            car.try_to_go_ahead()

    def inform_position(self):
        for car in self.__cars:
            car.inform_position()
        OutputView.output_empty_line()

    def get_winners(self):
        winners = list()
        winners.append(self.__cars[0])
        for car in self.__cars[1:]:
            if car.is_win(winners[0]):
                winners = [car]
            elif car.is_draw(winners[0]):
                winners.append(car)
        return winners





