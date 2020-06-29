from input_view import InputView


class Names:

    def __init__(self):
        temp_names = []
        while not self.is_valid(temp_names):
            temp_names = InputView.input_car_names().split(',')
        self.__names = iter(temp_names)

    @staticmethod
    def is_valid(temp_names):
        if not temp_names:
            return False
        for name in temp_names:
            if len(name) > 5 or len(name) < 1:
                return False
        return True

    def next(self):
        try:
            return self.__names.__next__()
        except StopIteration:
            return ""


if __name__ == "__main__":
    names = Names()
    print(names.next())
    print(names.next())
    print(names.next())

