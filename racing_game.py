from cars import Cars
from output_view import OutputView
from input_view import InputView


class RacingGame:

    @staticmethod
    def start():
        try_count = RacingGame.get_try_count()
        cars = Cars()
        OutputView.output_race_start_message()
        for _ in range(try_count):
            cars.try_to_go_ahead()
            cars.inform_position()
        OutputView.output_announce_winner(cars.get_winners())

    @staticmethod
    def get_try_count():
        try_count = InputView.input_try_count()
        while not try_count.isdigit():
            try_count = InputView.input_try_count()
        return int(try_count)


if __name__ == "__main__":
    RacingGame().start()



