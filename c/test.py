import unittest
from solution import parse_input, predict, ArithmeticSeries, GeometricSeries, QuadraticSeries, SquareSeries, FibonacciSeries


class TestSequenceFunctions(unittest.TestCase):

    def test_parse_input_success(self):

        self.assertEqual(parse_input(['1', '2', '3', '4']), [1, 2, 3, 4])

    def test_parse_input_empty_input(self):

        self.assertEqual(parse_input(['']), None)

    def test_parse_input_input_value_error(self):

        self.assertEqual(parse_input(['1', '2', 'hello']), None)

    def test_arithmetic_success(self):
        seq = [1, 3, 5, 7, 9]
        arith_series = ArithmeticSeries(seq)
        self.assertTrue(arith_series.is_follow_pattern())
        self.assertEqual(arith_series.predict_next_series(), [
                         11, 13, 15, 17, 19, 21, 23, 25, 27, 29])

    def test_input_two_elements_for_arithmetics(self):
        seq = [-1, 4]
        self.assertEqual(
            predict(seq),  [9, 14, 19, 24, 29, 34, 39, 44, 49, 54])

    def test_geometric_success(self):
        seq = [1, 2, 4]
        geo_series = GeometricSeries(seq)
        self.assertTrue(geo_series.is_follow_pattern())
        self.assertEqual(geo_series.predict_next_series(), [
                         8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096])

    def test_quadratics_success(self):
        seq = [1, 3, 7]
        quadratic_series = QuadraticSeries(seq)
        self.assertTrue(quadratic_series.is_follow_pattern())
        self.assertEqual(quadratic_series.predict_next_series(), [
                         15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191])

    def test_quadratic_fail(self):
        seq = [1, 4, 9, 16]
        quadratic_series = QuadraticSeries(seq)
        self.assertFalse(quadratic_series.is_follow_pattern())

    def test_square_success(self):
        seq = [1, 4, 9, 16]
        square_series = SquareSeries(seq)
        self.assertTrue(square_series.is_follow_pattern())
        self.assertEqual(square_series.predict_next_series(),
                         [25, 36, 49, 64, 81, 100, 121, 144, 169, 196])

    def test_square_fail(self):
        seq = [1, 4, 8, 16]
        quadratic_series = QuadraticSeries(seq)
        self.assertFalse(quadratic_series.is_follow_pattern())

    def test_fibonacci_success(self):
        seq = [1, 1, 2]
        fib_series = FibonacciSeries(seq)
        self.assertTrue(fib_series.is_follow_pattern())
        self.assertEqual(fib_series.predict_next_series(), [3, 5, 8, 13, 21, 34, 55, 89, 144, 233])


if __name__ == '__main__':
    unittest.main()
