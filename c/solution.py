import sys


def parse_input(raw_input):
    if len(raw_input) < 2:
        print(f'Your input: {raw_input}. Please input more numbers to predict.')
        return None
    try:
        return list(map(int, raw_input))

    except ValueError:
        print(f'Your input: {raw_input}. Input string contains invalid value.')
        return None


def predict(input_numbers, n=10):
    arith_series = ArithmeticSeries(input_numbers)
    if len(input_numbers) == 2:
        prediction_result = arith_series.predict_next_series(n)
    elif arith_series.is_follow_pattern():
        prediction_result = arith_series.predict_next_series(n)
    elif input_numbers[0] != 0 and GeometricSeries(input_numbers).is_follow_pattern():
        prediction_result = GeometricSeries(input_numbers).predict_next_series(n)
    elif input_numbers[1] - input_numbers[0] != 0 and QuadraticSeries(input_numbers).is_follow_pattern():
        prediction_result = QuadraticSeries(input_numbers).predict_next_series(n)
    elif SquareSeries(input_numbers).is_follow_pattern():
        prediction_result = SquareSeries(input_numbers).predict_next_series(n)
    elif FibonacciSeries(input_numbers).is_follow_pattern():
        prediction_result = FibonacciSeries(input_numbers).predict_next_series(n)
    else:
        print("Can't predict.")
        prediction_result = None

    return prediction_result


def check_integer_output(number: float):
    if number.is_integer():
        return int(number)
    else:
        return number


class BasicPattern():

    def __init__(self, numbers):
        self.numbers = numbers
        self.next_series = []

    def is_follow_pattern():
        pass

    def predict_next_series():
        pass


class ArithmeticSeries(BasicPattern):

    def __init__(self, numbers):
        super().__init__(numbers)
        self.difference = self.numbers[1] - self.numbers[0]

    def is_follow_pattern(self) -> bool:
        return all(self.numbers[i] + self.difference == self.numbers[i+1]for i in range(1, len(self.numbers)-1))

    def predict_next_series(self, n=10) -> list:
        next_value = self.numbers[-1]
        for _ in range(n):
            next_value += self.difference
            self.next_series.append(next_value)
        return self.next_series


class GeometricSeries(BasicPattern):
    def __init__(self, numbers):
        super().__init__(numbers)
        self.ratio = self.numbers[1] / self.numbers[0]

    def is_follow_pattern(self) -> bool:
        return all(self.numbers[i] * self.ratio == self.numbers[i+1] for i in range(1, len(self.numbers)-1))

    def predict_next_series(self, n=10) -> list:
        next_value = self.numbers[-1]
        for _ in range(n):
            next_value *= self.ratio
            self.next_series.append((check_integer_output(next_value)))
        return self.next_series


class QuadraticSeries(BasicPattern):
    def __init__(self, numbers):
        super().__init__(numbers)
        self.slope = (numbers[2]-numbers[1]) / (numbers[1] - numbers[0])
        self.intercept = numbers[1] - numbers[0] * self.slope

    def is_follow_pattern(self) -> bool:
        return all(self.numbers[i] * self.slope + self.intercept == self.numbers[i+1] for i in range(1, len(self.numbers)-1))

    def predict_next_series(self, n=10) -> list:
        next_value = self.numbers[-1]
        for _ in range(n):
            next_value = next_value * self.slope + self.intercept
            self.next_series.append(check_integer_output(round(next_value, 2)))
        return self.next_series


class SquareSeries(BasicPattern):
    def __init__(self, numbers):
        super().__init__(numbers)
        self.power = 2
        self.difference = pow(
            numbers[1], 1 / self.power) - pow(numbers[0], 1 / self.power)

    def is_follow_pattern(self) -> bool:

        return all(pow(self.numbers[i], 1/self.power) + self.difference == pow(self.numbers[i+1], 1/self.power) for i in range(1, len(self.numbers)-1))

    def predict_next_series(self, n=10) -> list:
        next_value = self.numbers[-1]
        for _ in range(n):
            root = pow(next_value, 1 / self.power)
            next_root = root + self.difference
            next_value = pow(next_root, self.power)
            self.next_series.append(check_integer_output(next_value))
        return self.next_series


class FibonacciSeries(BasicPattern):
    def __init__(self, numbers):
        super().__init__(numbers)

    def is_follow_pattern(self) -> bool:
        return all(self.numbers[i-1] + self.numbers[i] == self.numbers[i+1] for i in range(1, len(self.numbers)-1))

    def predict_next_series(self, n=10) -> list:
        last_value = self.numbers[-1]
        last_second_value = self.numbers[-2]
        for _ in range(n):
            next_value = last_value + last_second_value
            last_value, last_second_value = next_value, last_value
            self.next_series.append(next_value)
        return self.next_series


def main():
    raw_input = sys.argv[1:]
    while True:

        if not raw_input:
            raw_input = input(
                "Please enter at least two numbers and split by space:").strip().split()

        input_numbers = parse_input(raw_input)
        if input_numbers is None:
            raw_input = []
            continue
        predict_numbers = predict(input_numbers)
        if predict_numbers:
            output_string = ' '.join([str(i) for i in predict_numbers])
            print(output_string)
        raw_input = []


if __name__ == '__main__':
    main()
