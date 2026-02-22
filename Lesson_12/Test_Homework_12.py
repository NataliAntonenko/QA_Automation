
import unittest
from Lesson_12.Homework_12 import sum_two, average, sum_even_numbers

class TestSum(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(sum_two(1, 2), 3)

    def test_negative_numbers(self):
        self.assertEqual(sum_two(-2, 2), 0)

    def test_mixed_signs(self):
        self.assertEqual(sum_two(1, -12), -11)

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            sum_two(5, "abc")

    def test_missing_argument(self):
        with self.assertRaises(TypeError, msg="Очікувався TypeError при відсутності аргумента"):
            sum_two(5)



class TestAverage(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(
            average([1, 2, 3, 4]),
            2.5,
            msg="Середнє [1,2,3,4] має бути 2.5"
        )

    def test_single_element(self):
        self.assertEqual(
            average([10]),
            10,
            msg="Середнє з одного елемента має дорівнювати самому елементу"
        )

    def test_empty_list(self):
        with self.assertRaises(ZeroDivisionError):
            average([])

    def test_invalid_values(self):
        with self.assertRaises(TypeError):
            average([1, 2, "3"])

class TestSumEvenNumbers(unittest.TestCase):

    def test_mixed_numbers(self):
        self.assertEqual(
            sum_even_numbers([1, 2, 3, 4, 5, 6]),
            12,
            msg="Сумма парних чисел [1,2,3,4,5,6] має бути 12"
        )

    def test_only_even(self):
        self.assertEqual(
            sum_even_numbers([2, 4, 6]),
            12)

    def test_empty_list(self):
        self.assertEqual(
            sum_even_numbers([]),
            0,
            msg="Порожній список має повертати 0"
        )

    def test_invalid_type(self):
        with self.assertRaises(TypeError, msg="Строки у списку мають повертати TypeError"):
            sum_even_numbers([2, "4", 6])

if __name__ == "__main__":
    unittest.main(verbosity=2)