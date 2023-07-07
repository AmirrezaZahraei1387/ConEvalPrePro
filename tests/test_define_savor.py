import unittest
from ceval.defines_saver import check_type, MacroSaver


class test(unittest.TestCase):

    @check_type(int)
    def check_type_test(self, number):
        return number*2

    def test_check_type_error_raising(self):

        try:
            self.check_type_test("kkk")
        except TypeError:
            a = True
        else:
            a = False

        self.assertEqual(a, True)

    def test_check_type_error_raising_2(self):

        try:
            self.check_type_test(5)
        except TypeError:
            a = False
        else:
            a = True

        self.assertEqual(a, True)





