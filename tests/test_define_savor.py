import unittest
from ceval.defines_saver import check_type, MacroSaver, Macro


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

    def test_search_class_MacroSaver(self):

        obj = MacroSaver()

        macro_1 = Macro("AH", "5")
        macro_2 = Macro("AI", "5")
        macro_3 = Macro("AL", "5")

        obj += macro_1
        obj += macro_2
        obj += macro_3

        result = obj.search("AH")
        result_1 = obj.search("hh")

        result_all = [result, result_1]
        self.assertEqual(result_all, [("AH", 0), None])
