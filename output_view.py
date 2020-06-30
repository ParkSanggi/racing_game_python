
class OutputView:

    @staticmethod
    def output_car_position(name, position):
        position_mark = '-' * position
        print("{}의 {}".format(name, position_mark))

    @staticmethod
    def output_empty_line():
        print('')

    @staticmethod
    def output_race_start_message():
        print("실행결과\n")

    @staticmethod
    def output_announce_winner(winners):
        print("최종 우승자는 ", end='')
        for i in range(len(winners)):
            print(winners[i].get_name(), end='')
            if i < len(winners) - 1:
                print(", ", end='')
            else:
                print(" ", end='')
        print("입니다.")
